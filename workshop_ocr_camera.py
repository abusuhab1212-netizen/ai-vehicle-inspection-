# workshop_ocr_camera.py
# ==============================================================================
# ENTERPRISE OCR NODE - AUTOMATIC LICENSE PLATE RECOGNITION (ALPR)
# Entry Gate Camera: Detects Plate -> Extracts Text -> Sends to FastAPI Queue
# ==============================================================================

import cv2
import easyocr
import requests
import time
import re
import threading

# 1. Configuration
RENDER_API_URL = "https://ai-vehicle-inspection.onrender.com/api/v1/inspect/process"
CAMERA_SOURCE = 0  # Entry Gate Webcam (0 for laptop cam, or RTSP URL for CCTV)

print("[INFO] Initializing OCR AI Engine... (This may take a moment)")
# Load EasyOCR for English & Arabic numbers/text (Saudi Plates)
reader = easyocr.Reader(['en'], gpu=False)

# Thread-safe globals
detected_plates = []
last_sent_time = {}

def clean_plate_text(raw_text):
    """
    Cleans the OCR text to match standard KSA License Plate formats (e.g., KSA 1234)
    """
    cleaned = re.sub(r'[^A-Z0-9 ]', '', raw_text.upper())
    # Remove common OCR errors
    cleaned = cleaned.replace('O', '0').replace('l', '1')  # Letter to number confusion
    return cleaned.strip()

def send_to_dashboard_queue(plate_number):
    """
    Sends the automatically detected Plate Number to the Render API 
    so it appears in the Inspector's Dashboard Queue.
    Non-blocking (threaded) to prevent UI freezing.
    """
    def _send():
        print(f"\n[🚀 TRIGGER] Sending Plate '{plate_number}' to Cloud Queue...")
        
        # Check anti-spam: don't send same plate twice within 30 seconds
        current_time = time.time()
        if plate_number in last_sent_time and (current_time - last_sent_time[plate_number]) < 30:
            print(f"[⏱️ SPAM FILTER] Plate already sent recently. Waiting...")
            return
        
        # We send an initial payload. The inspector will add other details later.
        payload = {
            "vin": "AUTO-DETECTED-VIN",
            "plate_number": plate_number,
            "sequence_number": f"SCAN-{int(time.time())}",
            "make": "Unknown (Auto-Scanned)",
            "model_year": 2024,
            "vehicle_type": "car",
            "side_slip_val": 0.0,
            "brake_efficiency_val": 0.0,
            "brake_imbalance_val": 0.0,
            "front_barrier_height_val": 0.0,
            "rear_barrier_height_val": 0.0,
            "side_barrier_gap_val": 0.0,
            "side_barrier_height_val": 0.0,
            "tire_tread_depth_val": 0.0,
            "oil_leakage_detected": False
        }

        try:
            response = requests.post(RENDER_API_URL, json=payload, timeout=5)
            if response.status_code == 200:
                result = response.json()
                print(f"[✅ SUCCESS] Vehicle queued! Inspection ID: {result['inspection_id']}")
                last_sent_time[plate_number] = current_time
            else:
                print(f"[❌ ERROR] Cloud API rejected: {response.status_code}")
        except Exception as e:
            print(f"[⚠️ WARNING] Could not connect to Cloud API: {str(e)}")
    
    # Run in background thread
    thread = threading.Thread(target=_send, daemon=True)
    thread.start()

def run_ocr_entry_gate():
    """
    Entry Gate OCR Loop: Captures frames, detects plates, extracts text via EasyOCR
    """
    cap = cv2.VideoCapture(CAMERA_SOURCE)
    
    if not cap.isOpened():
        print("[ERROR] Could not open camera")
        return
    
    print("[INFO] Entry Gate OCR Camera Started")
    print("[INFO] Press 'r' to manually trigger OCR scan")
    print("[INFO] Press 'q' to quit\n")
    
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        height, width, _ = frame.shape
        
        # Define ROI (Region of Interest) where plate should be placed
        roi_height = 100
        roi_width = 300
        roi_y1 = int(height/2) - roi_height // 2
        roi_y2 = roi_y1 + roi_height
        roi_x1 = int(width/2) - roi_width // 2
        roi_x2 = roi_x1 + roi_width
        
        # Draw alignment guides
        cv2.rectangle(frame, (roi_x1, roi_y1), (roi_x2, roi_y2), (0, 255, 255), 2)
        cv2.putText(frame, "ALIGN PLATE HERE", (roi_x1, roi_y1 - 10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
        
        # Display info
        cv2.putText(frame, f"Frame: {frame_count}", (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.putText(frame, f"Detected Plates: {len(detected_plates)}", (10, 60), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.putText(frame, "Press 'r' to SCAN | 'q' to QUIT", (10, height - 20), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        # Display recently detected plates
        for i, plate in enumerate(detected_plates[-3:]):  # Show last 3
            cv2.putText(frame, f"Recent: {plate}", (10, 90 + i*25), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 200, 0), 1)

        cv2.imshow("SASO OCR Entry Gate Scanner (EasyOCR)", frame)
        key = cv2.waitKey(1) & 0xFF

        # Manual Trigger for testing (Press 'r' to read plate)
        if key == ord('r'):
            print("\n" + "="*60)
            print("[ACTION] 📸 Capturing Plate Image from ROI...")
            print("="*60)
            
            # Crop the region of interest
            plate_crop = frame[roi_y1:roi_y2, roi_x1:roi_x2]
            
            # Run EasyOCR on the cropped image
            try:
                result = reader.readtext(plate_crop)
                
                if result:
                    # Extract text with highest confidence
                    texts_with_conf = [(r[1], r[2]) for r in result]
                    texts_with_conf.sort(key=lambda x: x[1], reverse=True)
                    
                    raw_text = texts_with_conf[0][0]
                    confidence = texts_with_conf[0][1]
                    
                    plate_text = clean_plate_text(raw_text)
                    print(f"[🔍 OCR RESULT] Detected Plate: '{plate_text}'")
                    print(f"[📊 CONFIDENCE] {confidence:.2%}")
                    
                    if len(plate_text) >= 4:  # Basic validation
                        detected_plates.append(plate_text)
                        print(f"[✅ VALID] Sending to Cloud Queue...")
                        send_to_dashboard_queue(plate_text)
                    else:
                        print("[⚠️ VALIDATION] Plate too short. Ignored.")
                else:
                    print("[⚠️ OCR] No text detected. Please align the plate clearly.")
            except Exception as e:
                print(f"[❌ ERROR] OCR processing failed: {str(e)}")
            
            print("="*60 + "\n")
            time.sleep(1)  # Anti-spam delay

        elif key == ord('q'):
            print("[INFO] Exiting OCR Camera...")
            break

    cap.release()
    cv2.destroyAllWindows()
    print("[INFO] ✅ OCR Camera closed successfully")
    print(f"[SUMMARY] Total plates detected: {len(detected_plates)}")

if __name__ == "__main__":
    print("\n" + "="*60)
    print("SASO OCR ENTRY GATE - License Plate Recognition Engine")
    print("="*60 + "\n")
    run_ocr_entry_gate()
