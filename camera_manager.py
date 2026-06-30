# Camera Manager - 7-Camera Synchronization & Watchdog System
# Ensures zero-copy frame processing and heartbeat monitoring

import asyncio
import time
from typing import Dict, List
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CameraManager:
    """
    Manages 7 camera feeds with real-time status monitoring
    Cameras: Front, Rear, Left, Right, Undercarriage, Brake, Side-Slip
    """
    
    # Camera indices
    CAMERA_LABELS = {
        0: "FRONT",
        1: "REAR",
        2: "LEFT",
        3: "RIGHT",
        4: "UNDERCARRIAGE",
        5: "BRAKE_ASSEMBLY",
        6: "SIDE_SLIP"
    }
    
    def __init__(self, heartbeat_timeout: float = 0.5):
        """
        Initialize camera manager with heartbeat timeout
        heartbeat_timeout: seconds (0.5 = 500ms for real-time)
        """
        self.heartbeat_timeout = heartbeat_timeout
        self.camera_status = {i: "DISCONNECTED" for i in range(7)}
        self.last_heartbeat = {i: None for i in range(7)}
        self.frame_count = {i: 0 for i in range(7)}
        self.inspection_active = False
        self.alarm_triggered = False
        self.logs = []
    
    async def heartbeat_check(self, camera_id: int):
        """
        Continuous heartbeat monitoring for a single camera
        """
        while self.inspection_active:
            current_time = time.time()
            
            # Check if heartbeat is missing
            if self.last_heartbeat[camera_id] is not None:
                time_since_heartbeat = current_time - self.last_heartbeat[camera_id]
                
                if time_since_heartbeat > self.heartbeat_timeout:
                    self.camera_status[camera_id] = "DISCONNECTED"
                    self._log_alarm(
                        camera_id,
                        f"CAMERA {self.CAMERA_LABELS[camera_id]} - HEARTBEAT TIMEOUT ({time_since_heartbeat:.2f}s)"
                    )
                    self.alarm_triggered = True
                elif self.camera_status[camera_id] != "CONNECTED":
                    self.camera_status[camera_id] = "CONNECTED"
                    self._log_info(
                        camera_id,
                        f"CAMERA {self.CAMERA_LABELS[camera_id]} - RECONNECTED"
                    )
            
            await asyncio.sleep(0.1)  # Check every 100ms
    
    def receive_frame(self, camera_id: int, frame_timestamp: float):
        """
        Receive heartbeat from camera (called when frame arrives)
        """
        if not (0 <= camera_id < 7):
            logger.error(f"Invalid camera ID: {camera_id}")
            return False
        
        self.last_heartbeat[camera_id] = frame_timestamp
        self.frame_count[camera_id] += 1
        
        if self.camera_status[camera_id] != "CONNECTED":
            self.camera_status[camera_id] = "CONNECTED"
            self._log_info(camera_id, f"CAMERA {self.CAMERA_LABELS[camera_id]} - CONNECTED")
        
        return True
    
    def check_all_cameras(self) -> Dict:
        """
        Check if all cameras are connected and ready
        Returns: status dict with alarm if any camera missing
        """
        status = {
            "all_connected": True,
            "connected_count": 0,
            "disconnected_count": 0,
            "cameras": {},
            "alarm": False,
            "timestamp": datetime.now().isoformat()
        }
        
        for cam_id, cam_status in self.camera_status.items():
            status["cameras"][self.CAMERA_LABELS[cam_id]] = cam_status
            
            if cam_status == "CONNECTED":
                status["connected_count"] += 1
            else:
                status["disconnected_count"] += 1
                status["all_connected"] = False
        
        # Trigger alarm if any camera is disconnected
        if not status["all_connected"]:
            status["alarm"] = True
            status["error"] = "🚨 ALARM: ONE OR MORE CAMERAS MISSING"
            self._log_alarm(-1, "INSPECTION CANNOT START - MISSING CAMERAS")
        
        return status
    
    def start_inspection(self) -> Dict:
        """
        Start inspection - requires all 7 cameras connected
        """
        camera_check = self.check_all_cameras()
        
        if not camera_check["all_connected"]:
            return {
                "status": "FAILED",
                "error": "Cannot start inspection - not all cameras connected",
                "camera_status": camera_check
            }
        
        self.inspection_active = True
        self.alarm_triggered = False
        self._log_info(-1, "INSPECTION STARTED - ALL 7 CAMERAS CONNECTED")
        
        return {
            "status": "STARTED",
            "message": "Inspection started with 7 cameras synchronized",
            "camera_status": camera_check
        }
    
    def pause_inspection(self, reason: str = "Camera disconnect detected"):
        """
        Pause inspection immediately if camera issue detected
        """
        if self.inspection_active:
            self.inspection_active = False
            self._log_alarm(-1, f"INSPECTION PAUSED - {reason}")
            
            return {
                "status": "PAUSED",
                "reason": reason,
                "camera_status": self.check_all_cameras()
            }
        return {"status": "NOT_ACTIVE"}
    
    def stop_inspection(self) -> Dict:
        """
        Stop inspection and generate report
        """
        self.inspection_active = False
        
        return {
            "status": "STOPPED",
            "total_frames_captured": sum(self.frame_count.values()),
            "frames_per_camera": self.frame_count,
            "alarm_triggered": self.alarm_triggered,
            "camera_status": self.check_all_cameras()
        }
    
    def get_status(self) -> Dict:
        """
        Get current system status
        """
        return {
            "inspection_active": self.inspection_active,
            "alarm_triggered": self.alarm_triggered,
            "camera_status": self.check_all_cameras(),
            "frame_count": self.frame_count,
            "logs_count": len(self.logs)
        }
    
    def _log_alarm(self, camera_id: int, message: str):
        """
        Log alarm message
        """
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "level": "ALARM",
            "camera_id": camera_id,
            "camera_name": self.CAMERA_LABELS.get(camera_id, "SYSTEM") if camera_id >= 0 else "SYSTEM",
            "message": message
        }
        self.logs.append(log_entry)
        logger.error(f"[ALARM] {message}")
    
    def _log_info(self, camera_id: int, message: str):
        """
        Log info message
        """
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "level": "INFO",
            "camera_id": camera_id,
            "camera_name": self.CAMERA_LABELS.get(camera_id, "SYSTEM") if camera_id >= 0 else "SYSTEM",
            "message": message
        }
        self.logs.append(log_entry)
        logger.info(f"[INFO] {message}")
    
    def get_logs(self, limit: int = 50) -> List[Dict]:
        """
        Get recent logs
        """
        return self.logs[-limit:]


class FrameSynchronizer:
    """
    Ensures synchronized frame capture from all 7 cameras
    Uses zero-copy frame processing for minimal latency
    """
    
    def __init__(self, frame_buffer_size: int = 100):
        """
        Initialize frame synchronizer
        frame_buffer_size: number of frames to buffer per camera
        """
        self.frame_buffers = {i: [] for i in range(7)}
        self.frame_buffer_size = frame_buffer_size
        self.sync_events = {i: asyncio.Event() for i in range(7)}
        self.latest_frames = {i: None for i in range(7)}
    
    async def add_frame(self, camera_id: int, frame_data: bytes, timestamp: float):
        """
        Add frame from camera (zero-copy - just store reference)
        """
        if camera_id not in self.frame_buffers:
            return False
        
        # Store frame with metadata (zero-copy)
        frame_entry = {
            "timestamp": timestamp,
            "data": frame_data,
            "processed": False
        }
        
        # Add to buffer
        self.frame_buffers[camera_id].append(frame_entry)
        
        # Keep buffer size limited
        if len(self.frame_buffers[camera_id]) > self.frame_buffer_size:
            self.frame_buffers[camera_id].pop(0)
        
        # Update latest frame
        self.latest_frames[camera_id] = frame_entry
        
        # Signal that new frame is available
        self.sync_events[camera_id].set()
        
        return True
    
    async def get_synchronized_frames(self) -> Dict:
        """
        Get latest frame from each camera (synchronized)
        Waits until all cameras have at least one frame
        """
        # Wait for at least one frame from each camera (max 1 second)
        try:
            await asyncio.wait_for(
                asyncio.gather(*[event.wait() for event in self.sync_events.values()]),
                timeout=1.0
            )
        except asyncio.TimeoutError:
            return {"status": "TIMEOUT", "error": "Not all cameras provided frames"}
        
        # Get latest frame from each camera
        synchronized_frames = {
            camera_id: frame_data["data"]
            for camera_id, frame_data in self.latest_frames.items()
            if frame_data is not None
        }
        
        if len(synchronized_frames) == 7:
            return {
                "status": "SUCCESS",
                "frames": synchronized_frames,
                "timestamp": datetime.now().isoformat()
            }
        else:
            return {
                "status": "INCOMPLETE",
                "frames_available": len(synchronized_frames),
                "total_required": 7
            }
    
    def get_buffer_stats(self) -> Dict:
        """
        Get statistics about frame buffers
        """
        return {
            camera_id: {
                "buffered_frames": len(buffer),
                "latest_timestamp": buffer[-1]["timestamp"] if buffer else None,
                "processed_count": sum(1 for f in buffer if f["processed"])
            }
            for camera_id, buffer in self.frame_buffers.items()
        }
