# SASO Compliance Mapping
# Maps all inspection components to SASO standards with mandatory checks
# Reference: الدليل الإرشادي التفصيلي لحواجز الشاحنات والمقطورات

SASO_COMPLIANCE_MAPPING = {
    # ==================== CRITICAL STRUCTURAL COMPONENTS ====================
    
    "front_guards": {
        "saso_reference": "الحواجز الأمامية - Front Protective Devices",
        "saso_standard": "Standards for Truck & Trailer Protective Barriers",
        "mandatory_check": True,
        "pass_criteria": {
            "height_mm_min": 400,
            "height_mm_max": 1200,
            "description": "Height must be between 400-1200 mm from ground level"
        },
        "fail_criteria": {
            "height_below_min": "Height below 400 mm - insufficient protection",
            "height_above_max": "Height above 1200 mm - reduces visibility",
            "damage_detected": "Damage, cracks, or structural failure"
        },
        "inspection_priority": "CRITICAL",
        "ai_detection_required": True,
        "detection_method": "AI measurement from images",
        "manual_override_allowed": False,
        "audit_trail_required": True
    },
    
    "side_guards": {
        "saso_reference": "الحواجز الجانبية - Side Protective Devices",
        "saso_standard": "Standards for Truck & Trailer Protective Barriers",
        "mandatory_check": True,
        "pass_criteria": {
            "height_mm_max": 550,
            "gap_from_tire_mm_max": 300,
            "cabin_height_mm_min": 550,
            "description": "Max 550mm height from ground AND max 300mm gap from tire"
        },
        "fail_criteria": {
            "height_exceeds_550mm": "Height exceeds 550mm - creates gap for pedestrians",
            "gap_exceeds_300mm": "Gap from tire exceeds 300mm",
            "gap_and_height_combined": "Gap >300mm AND cabin height >550mm = DANGEROUS",
            "damage_detected": "Damage, cracks, or missing sections",
            "rust_or_corrosion": "Structural weakening from rust/corrosion"
        },
        "inspection_priority": "CRITICAL",
        "ai_detection_required": True,
        "detection_method": "AI measurement from side view images",
        "manual_override_allowed": False,
        "audit_trail_required": True,
        "image_reference": "صورة هـ - 5, صورة هـ - 16"
    },
    
    "rear_guards": {
        "saso_reference": "الحواجز الخلفية - Rear Underrun Protection",
        "saso_standard": "Standards for Truck & Trailer Protective Barriers",
        "mandatory_check": True,
        "pass_criteria": {
            "height_mm_max": 550,
            "description": "Maximum 550mm height from ground level"
        },
        "fail_criteria": {
            "height_exceeds_550mm": "Height exceeds 550mm",
            "missing_or_removed": "Guard completely missing or removed",
            "damage_detected": "Damage, bending, or structural failure"
        },
        "inspection_priority": "CRITICAL",
        "ai_detection_required": True,
        "detection_method": "AI measurement from rear view images",
        "manual_override_allowed": False,
        "audit_trail_required": True
    },
    
    # ==================== CRITICAL BRAKING COMPONENTS ====================
    
    "brake_efficiency": {
        "saso_reference": "كفاءة الفرامل - Brake System Efficiency",
        "saso_standard": "Ministry of Interior - Vehicle Inspection Standards",
        "mandatory_check": True,
        "pass_criteria": {
            "truck_percent_min": 50,
            "car_percent_min": 45,
            "description": "Trucks: >50%, Cars: >45% braking efficiency"
        },
        "fail_criteria": {
            "truck_below_50": "Truck braking efficiency below 50%",
            "car_below_45": "Car braking efficiency below 45%",
            "uneven_braking": "Left-right braking imbalance >10%"
        },
        "inspection_priority": "CRITICAL",
        "ai_detection_required": False,
        "detection_method": "Brake roller test machine",
        "manual_override_allowed": False,
        "audit_trail_required": True,
        "test_equipment": "Brake Roller Test Machine (HVMS or similar)"
    },
    
    "brake_pads": {
        "saso_reference": "أثواب الفرامل - Brake Pad Condition",
        "saso_standard": "Vehicle Component Standards",
        "mandatory_check": True,
        "pass_criteria": {
            "min_thickness_mm": 2.0,
            "description": "Minimum 2.0mm remaining thickness"
        },
        "fail_criteria": {
            "thickness_below_2mm": "Brake pad thickness below 2.0mm",
            "uneven_wear": "Severe uneven wear between wheels",
            "damaged_or_cracked": "Pads damaged, cracked, or disintegrating"
        },
        "inspection_priority": "CRITICAL",
        "ai_detection_required": True,
        "detection_method": "AI measurement from brake assembly images",
        "manual_override_allowed": False,
        "audit_trail_required": True
    },
    
    "hydraulic_system": {
        "saso_reference": "نظام الفرامل الهيدروليكي - Hydraulic Brake System",
        "saso_standard": "Brake System Standards",
        "mandatory_check": True,
        "pass_criteria": {
            "no_leakage": True,
            "no_corrosion": True,
            "description": "No leakage, corrosion, or loose connections"
        },
        "fail_criteria": {
            "active_leakage": "Oil leakage detected",
            "severe_corrosion": "Corrosion weakening structural integrity",
            "loose_connections": "Loose or disconnected pipes"
        },
        "inspection_priority": "CRITICAL",
        "ai_detection_required": True,
        "detection_method": "AI detection of leakage/corrosion from images",
        "manual_override_allowed": False,
        "audit_trail_required": True
    },
    
    # ==================== MAJOR ALIGNMENT & SUSPENSION ====================
    
    "side_slip": {
        "saso_reference": "انحراف جانبي - Side Slip (Steering Alignment)",
        "saso_standard": "Wheel Alignment & Steering Standards",
        "mandatory_check": True,
        "pass_criteria": {
            "max_slip_mm_per_meter": 7,
            "description": "±7 mm/m maximum deviation (±7mm in 1 meter)"
        },
        "fail_criteria": {
            "slip_exceeds_7mm_per_meter": "Side slip exceeds ±7 mm/m",
            "inconsistent_steering": "Vehicle pulls to one side",
            "tire_wear_indication": "Uneven tire wear from misalignment"
        },
        "inspection_priority": "MAJOR",
        "ai_detection_required": True,
        "detection_method": "Side slip test with measurement equipment",
        "manual_override_allowed": False,
        "audit_trail_required": True
    },
    
    "suspension": {
        "saso_reference": "نظام التعليق - Suspension System",
        "saso_standard": "Suspension & Damping Standards",
        "mandatory_check": True,
        "pass_criteria": {
            "no_leakage": True,
            "shocks_functional": True,
            "springs_intact": True,
            "description": "No leaks, shocks functional, springs intact"
        },
        "fail_criteria": {
            "oil_leakage": "Shock absorber oil leakage",
            "broken_springs": "Broken or cracked springs",
            "vehicle_sagging": "Uneven ride height/sagging"
        },
        "inspection_priority": "MAJOR",
        "ai_detection_required": True,
        "detection_method": "AI analysis of suspension images + visual inspection",
        "manual_override_allowed": False,
        "audit_trail_required": True
    },
    
    "tire_condition": {
        "saso_reference": "حالة الإطارات - Tire Condition & Tread Depth",
        "saso_standard": "Tire Safety Standards",
        "mandatory_check": True,
        "pass_criteria": {
            "min_tread_depth_mm": 2.4,
            "max_age_years": 10,
            "no_damage": True,
            "proper_inflation": True,
            "description": "Min 2.4mm tread (legal min 1.6mm), age <10 years, no damage"
        },
        "fail_criteria": {
            "tread_below_2_4mm": "Tread depth below 2.4mm (legal minimum 1.6mm)",
            "age_exceeds_10_years": "Tires older than 10 years",
            "visible_damage": "Cracks, bulges, or sidewall damage",
            "uneven_wear": "Severe uneven wear pattern"
        },
        "inspection_priority": "MAJOR",
        "ai_detection_required": True,
        "detection_method": "AI measurement of tread depth from images",
        "manual_override_allowed": False,
        "audit_trail_required": True
    },
    
    # ==================== CRITICAL STRUCTURAL COMPONENTS ====================
    
    "chassis": {
        "saso_reference": "الهيكل الأساسي - Chassis Frame",
        "saso_standard": "Structural Integrity Standards",
        "mandatory_check": True,
        "pass_criteria": {
            "no_cracks": True,
            "no_rust": True,
            "no_corrosion": True,
            "description": "No rust, cracks, or corrosion"
        },
        "fail_criteria": {
            "visible_cracks": "Visible cracks in chassis frame",
            "severe_rust": "Rust reducing structural strength",
            "welding_failures": "Failed or weak weld joints"
        },
        "inspection_priority": "CRITICAL",
        "ai_detection_required": True,
        "detection_method": "AI detection of rust/cracks from undercarriage images",
        "manual_override_allowed": False,
        "audit_trail_required": True
    },
    
    "undercarriage": {
        "saso_reference": "قاع السيارة - Undercarriage",
        "saso_standard": "Undercarriage Protection & Integrity Standards",
        "mandatory_check": True,
        "pass_criteria": {
            "no_oil_leaks": True,
            "no_rust": True,
            "no_cracks": True,
            "description": "No oil leaks, rust, cracks, or corrosion"
        },
        "fail_criteria": {
            "active_oil_leakage": "Active oil dripping from engine/transmission",
            "severe_rust": "Extensive rust affecting structural integrity",
            "visible_cracks": "Cracks in undercarriage components"
        },
        "inspection_priority": "CRITICAL",
        "ai_detection_required": True,
        "detection_method": "AI analysis of undercarriage images",
        "manual_override_allowed": False,
        "audit_trail_required": True
    },
    
    "engine_block": {
        "saso_reference": "كتلة المحرك - Engine Block",
        "saso_standard": "Engine Component Standards",
        "mandatory_check": True,
        "pass_criteria": {
            "no_oil_leaks": True,
            "no_cracks": True,
            "no_corrosion": True,
            "description": "No oil leaks, cracks, or corrosion"
        },
        "fail_criteria": {
            "active_oil_leakage": "Active oil leakage from block",
            "visible_cracks": "Visible cracks in engine block",
            "coolant_leakage": "Coolant leakage"
        },
        "inspection_priority": "CRITICAL",
        "ai_detection_required": True,
        "detection_method": "AI detection of leakage from engine bay images",
        "manual_override_allowed": False,
        "audit_trail_required": True
    },
    
    "fuel_tank": {
        "saso_reference": "خزان الوقود - Fuel Tank",
        "saso_standard": "Fuel System Safety Standards",
        "mandatory_check": True,
        "pass_criteria": {
            "no_leakage": True,
            "no_cracks": True,
            "no_corrosion": True,
            "description": "No leaks, cracks, or corrosion"
        },
        "fail_criteria": {
            "active_fuel_leakage": "Active fuel leakage (FIRE HAZARD)",
            "visible_cracks": "Visible cracks or holes",
            "severe_corrosion": "Rust perforation of tank"
        },
        "inspection_priority": "CRITICAL",
        "ai_detection_required": True,
        "detection_method": "AI detection from fuel tank area images",
        "manual_override_allowed": False,
        "audit_trail_required": True
    },
    
    "gearbox": {
        "saso_reference": "علبة التروس - Gearbox/Transmission",
        "saso_standard": "Drivetrain Component Standards",
        "mandatory_check": True,
        "pass_criteria": {
            "no_leakage": True,
            "smooth_shifting": True,
            "description": "No leaks, smooth gear shifting"
        },
        "fail_criteria": {
            "active_leakage": "Transmission fluid leakage",
            "grinding_noise": "Grinding or unusual noises",
            "delayed_shifting": "Delayed gear engagement"
        },
        "inspection_priority": "CRITICAL",
        "ai_detection_required": True,
        "detection_method": "AI detection of leakage + functional test",
        "manual_override_allowed": False,
        "audit_trail_required": True
    },
    
    # ==================== MAJOR EMISSION & ENGINE COMPONENTS ====================
    
    "exhaust_system": {
        "saso_reference": "نظام العادم - Exhaust System & Emissions",
        "saso_standard": "Emission Control Standards",
        "mandatory_check": True,
        "pass_criteria": {
            "truck_ppm_max": 300,
            "car_ppm_max": 200,
            "no_leakage": True,
            "description": "Trucks: ≤300 ppm, Cars: ≤200 ppm CO2; No leaks"
        },
        "fail_criteria": {
            "truck_exceeds_300ppm": "Truck emissions exceed 300 ppm",
            "car_exceeds_200ppm": "Car emissions exceed 200 ppm",
            "visible_leakage": "Exhaust leakage before muffler",
            "rust_holes": "Rust holes in exhaust pipe"
        },
        "inspection_priority": "MAJOR",
        "ai_detection_required": False,
        "detection_method": "Emission test machine + visual inspection",
        "manual_override_allowed": False,
        "audit_trail_required": True
    },
    
    "catalytic_converter": {
        "saso_reference": "محول حفاز - Catalytic Converter",
        "saso_standard": "Emission Control Standards",
        "mandatory_check": True,
        "pass_criteria": {
            "intact": True,
            "not_damaged": True,
            "not_missing": True,
            "description": "Intact, no damage, not removed/missing"
        },
        "fail_criteria": {
            "missing_or_removed": "Catalytic converter missing/removed",
            "damaged_internal": "Internal failure (rattling sound)",
            "exterior_damage": "Dent or external damage"
        },
        "inspection_priority": "MAJOR",
        "ai_detection_required": True,
        "detection_method": "AI detection from engine bay images",
        "manual_override_allowed": False,
        "audit_trail_required": True
    },
    
    # ==================== SAFETY LIGHTING & VISIBILITY ====================
    
    "headlights": {
        "saso_reference": "مصابيح أمامية - Headlights",
        "saso_standard": "Lighting & Visibility Standards",
        "mandatory_check": True,
        "pass_criteria": {
            "both_functional": True,
            "proper_alignment": True,
            "description": "Both lights functional with proper alignment"
        },
        "fail_criteria": {
            "one_or_both_broken": "One or both headlights non-functional",
            "poor_alignment": "Lights pointing wrong direction"
        },
        "inspection_priority": "MAJOR",
        "ai_detection_required": True,
        "detection_method": "Functional test + AI detection",
        "manual_override_allowed": False,
        "audit_trail_required": True
    },
    
    "mirrors": {
        "saso_reference": "المرايا الجانبية - Side/Rear Mirrors",
        "saso_standard": "Visibility Standards",
        "mandatory_check": True,
        "pass_criteria": {
            "intact": True,
            "properly_adjusted": True,
            "clear_view": True,
            "description": "Intact, properly adjusted, clear view"
        },
        "fail_criteria": {
            "cracked_or_missing": "Cracked or missing mirror",
            "loose_mount": "Loose or wobbly mounting",
            "dirty_unclear": "Excessive dirt/damage blocking view"
        },
        "inspection_priority": "MAJOR",
        "ai_detection_required": True,
        "detection_method": "AI detection from vehicle images",
        "manual_override_allowed": False,
        "audit_trail_required": True
    },
    
    "horn": {
        "saso_reference": "البوق - Horn",
        "saso_standard": "Safety & Sound Standards",
        "mandatory_check": True,
        "pass_criteria": {
            "db_min": 100,
            "db_max": 125,
            "description": "Sound level 100-125 dB"
        },
        "fail_criteria": {
            "too_quiet": "Horn too quiet (<100 dB)",
            "too_loud": "Horn too loud (>125 dB)",
            "non_functional": "Horn completely non-functional"
        },
        "inspection_priority": "MINOR",
        "ai_detection_required": False,
        "detection_method": "Decibel meter test",
        "manual_override_allowed": True,
        "audit_trail_required": True
    },
    
    # ==================== REGISTRATION & IDENTIFICATION ====================
    
    "license_plate": {
        "saso_reference": "لوحة الترخيص - License Plate",
        "saso_standard": "Registration & Identification Standards",
        "mandatory_check": True,
        "pass_criteria": {
            "clearly_visible": True,
            "not_obscured": True,
            "correct_format": True,
            "description": "Clearly visible, not obscured, correct format"
        },
        "fail_criteria": {
            "obscured": "License plate obscured or damaged",
            "invalid_format": "Invalid plate format",
            "tampered": "Evidence of tampering"
        },
        "inspection_priority": "CRITICAL",
        "ai_detection_required": True,
        "detection_method": "OCR (Optical Character Recognition)",
        "manual_override_allowed": False,
        "audit_trail_required": True
    },
    
    "vin_plate": {
        "saso_reference": "رقم الهيكل - VIN (Vehicle Identification Number)",
        "saso_standard": "Registration & Identification Standards",
        "mandatory_check": True,
        "pass_criteria": {
            "clearly_visible": True,
            "not_obscured": True,
            "not_tampered": True,
            "description": "Clearly visible, not obscured, not tampered"
        },
        "fail_criteria": {
            "obscured": "VIN obscured or damaged",
            "tampered_evidence": "Evidence of tampering/grinding",
            "illegible": "VIN illegible or worn out"
        },
        "inspection_priority": "CRITICAL",
        "ai_detection_required": True,
        "detection_method": "OCR detection + visual inspection",
        "manual_override_allowed": False,
        "audit_trail_required": True
    },
    
    # ==================== SAFETY EQUIPMENT ====================
    
    "jack": {
        "saso_reference": "رافعة الطوارئ - Emergency Jack",
        "saso_standard": "Safety Equipment Standards",
        "mandatory_check": True,
        "pass_criteria": {
            "present": True,
            "functional": True,
            "properly_stored": True,
            "description": "Present, functional, properly stored"
        },
        "fail_criteria": {
            "missing": "Jack completely missing",
            "damaged": "Jack damaged or non-functional",
            "improper_storage": "Jack stored unsafely"
        },
        "inspection_priority": "MAJOR",
        "ai_detection_required": False,
        "detection_method": "Visual inspection",
        "manual_override_allowed": True,
        "audit_trail_required": True
    },
    
    "seatbelts": {
        "saso_reference": "حزام الأمان - Seatbelts",
        "saso_standard": "Occupant Safety Standards",
        "mandatory_check": True,
        "pass_criteria": {
            "all_functional": True,
            "no_damage": True,
            "proper_retraction": True,
            "description": "All belts functional, no fraying or damage"
        },
        "fail_criteria": {
            "non_functional_belts": "One or more belts non-functional",
            "damaged_or_frayed": "Belts damaged or severely frayed",
            "poor_retraction": "Belts don't retract properly"
        },
        "inspection_priority": "MAJOR",
        "ai_detection_required": False,
        "detection_method": "Functional test",
        "manual_override_allowed": False,
        "audit_trail_required": True
    }
}

# Summary of Mandatory Checks
MANDATORY_CHECKS_COUNT = sum(
    1 for component in SASO_COMPLIANCE_MAPPING.values()
    if component.get("mandatory_check", False)
)

CRITICAL_CHECKS_COUNT = sum(
    1 for component in SASO_COMPLIANCE_MAPPING.values()
    if component.get("inspection_priority") == "CRITICAL"
)

MAJOR_CHECKS_COUNT = sum(
    1 for component in SASO_COMPLIANCE_MAPPING.values()
    if component.get("inspection_priority") == "MAJOR"
)

MINOR_CHECKS_COUNT = sum(
    1 for component in SASO_COMPLIANCE_MAPPING.values()
    if component.get("inspection_priority") == "MINOR"
)

# Inspection cannot PASS unless ALL of these are checked
CRITICAL_BLOCKING_COMPONENTS = [
    component for component, details in SASO_COMPLIANCE_MAPPING.items()
    if details.get("inspection_priority") == "CRITICAL" and details.get("mandatory_check")
]
