# Complete Vehicle Components Inventory (A-Z)
# For AI Detection and SASO Compliance Checking

VEHICLE_COMPONENTS = {
    "A": {
        "alternator": {
            "name": "Alternator",
            "category": "Electrical",
            "check_type": "functional",
            "criteria": "Charging output stable, no grinding noise",
            "mandatory_saso_check": False,
            "detection_method": "visual_inspection",
            "ai_detection_required": False
        },
        "air_filter": {
            "name": "Air Filter",
            "category": "Engine",
            "check_type": "wear",
            "criteria": "Not clogged or dirty",
            "mandatory_saso_check": False,
            "detection_method": "visual_inspection",
            "ai_detection_required": False
        },
        "air_suspension": {
            "name": "Air Suspension System",
            "category": "Suspension",
            "check_type": "functional",
            "criteria": "No leaks, proper inflation",
            "mandatory_saso_check": False,
            "detection_method": "pressure_test",
            "ai_detection_required": False
        }
    },
    "B": {
        "battery": {
            "name": "Battery",
            "category": "Electrical",
            "check_type": "condition",
            "criteria": "Fully charged, no corrosion, secure mount",
            "mandatory_saso_check": False,
            "detection_method": "voltage_test",
            "ai_detection_required": False
        },
        "brake_pads": {
            "name": "Brake Pads",
            "category": "Braking System",
            "check_type": "wear",
            "criteria": "Minimum 2.0mm remaining thickness",
            "mandatory_saso_check": True,
            "saso_reference": "brake_pads_condition",
            "detection_method": "ai_measurement",
            "ai_detection_required": True,
            "threshold_mm": 2.0
        },
        "brake_discs": {
            "name": "Brake Discs",
            "category": "Braking System",
            "check_type": "wear",
            "criteria": "No warping, cracks, or excessive wear",
            "mandatory_saso_check": True,
            "detection_method": "visual_inspection",
            "ai_detection_required": True
        },
        "brake_efficiency": {
            "name": "Brake Efficiency",
            "category": "Braking System",
            "check_type": "performance",
            "criteria": "Trucks: >50%, Cars: >45%",
            "mandatory_saso_check": True,
            "saso_reference": "brake_efficiency",
            "detection_method": "brake_roller_test",
            "ai_detection_required": False,
            "threshold_truck": 50,
            "threshold_car": 45
        },
        "bumper": {
            "name": "Bumper",
            "category": "Body",
            "check_type": "condition",
            "criteria": "No cracks, dents, or misalignment",
            "mandatory_saso_check": False,
            "detection_method": "visual_inspection",
            "ai_detection_required": False
        }
    },
    "C": {
        "chassis": {
            "name": "Chassis",
            "category": "Structure",
            "check_type": "condition",
            "criteria": "No rust, cracks, or corrosion",
            "mandatory_saso_check": True,
            "detection_method": "visual_inspection",
            "ai_detection_required": True,
            "ai_focus": "rust_and_cracks"
        },
        "catalytic_converter": {
            "name": "Catalytic Converter",
            "category": "Emission Control",
            "check_type": "condition",
            "criteria": "Intact, no damage or missing",
            "mandatory_saso_check": True,
            "detection_method": "visual_inspection",
            "ai_detection_required": True
        },
        "cv_joint": {
            "name": "CV Joint",
            "category": "Drivetrain",
            "check_type": "condition",
            "criteria": "No tears in boots, no clicking noise",
            "mandatory_saso_check": False,
            "detection_method": "visual_inspection",
            "ai_detection_required": False
        }
    },
    "D": {
        "drive_shaft": {
            "name": "Drive Shaft",
            "category": "Drivetrain",
            "check_type": "condition",
            "criteria": "No bending, cracks, or runout",
            "mandatory_saso_check": False,
            "detection_method": "visual_inspection",
            "ai_detection_required": False
        },
        "differential": {
            "name": "Differential",
            "category": "Drivetrain",
            "check_type": "condition",
            "criteria": "No leaks, proper fluid level",
            "mandatory_saso_check": False,
            "detection_method": "visual_inspection",
            "ai_detection_required": False
        }
    },
    "E": {
        "engine_block": {
            "name": "Engine Block",
            "category": "Engine",
            "check_type": "condition",
            "criteria": "No oil leaks, cracks, or corrosion",
            "mandatory_saso_check": True,
            "detection_method": "visual_inspection",
            "ai_detection_required": True,
            "ai_focus": "oil_leakage"
        },
        "exhaust_system": {
            "name": "Exhaust System",
            "category": "Emission Control",
            "check_type": "emissions",
            "criteria": "No leaks, emission levels within limits",
            "mandatory_saso_check": True,
            "saso_reference": "emissions",
            "detection_method": "emission_test",
            "ai_detection_required": False,
            "threshold_truck_ppm": 300,
            "threshold_car_ppm": 200
        }
    },
    "F": {
        "fuel_tank": {
            "name": "Fuel Tank",
            "category": "Fuel System",
            "check_type": "condition",
            "criteria": "No leaks, cracks, or corrosion",
            "mandatory_saso_check": True,
            "detection_method": "visual_inspection",
            "ai_detection_required": True,
            "ai_focus": "fuel_leakage"
        },
        "fan_belt": {
            "name": "Fan Belt",
            "category": "Engine",
            "check_type": "wear",
            "criteria": "No cracks, fraying, or glazing",
            "mandatory_saso_check": False,
            "detection_method": "visual_inspection",
            "ai_detection_required": False
        }
    },
    "G": {
        "gearbox": {
            "name": "Gearbox",
            "category": "Drivetrain",
            "check_type": "condition",
            "criteria": "No leaks, smooth shifting",
            "mandatory_saso_check": True,
            "detection_method": "visual_inspection",
            "ai_detection_required": True,
            "ai_focus": "transmission_leakage"
        }
    },
    "H": {
        "headlights": {
            "name": "Headlights",
            "category": "Lighting",
            "check_type": "functional",
            "criteria": "Both functional, proper alignment",
            "mandatory_saso_check": True,
            "detection_method": "functional_test",
            "ai_detection_required": True
        },
        "horn": {
            "name": "Horn",
            "category": "Safety",
            "check_type": "functional",
            "criteria": "Sound level 100-125 dB",
            "mandatory_saso_check": True,
            "saso_reference": "horn",
            "detection_method": "decibel_test",
            "ai_detection_required": False,
            "threshold_db_min": 100,
            "threshold_db_max": 125
        },
        "handbrake": {
            "name": "Handbrake (Parking Brake)",
            "category": "Braking System",
            "check_type": "functional",
            "criteria": "Holds vehicle on grade, no slip",
            "mandatory_saso_check": True,
            "detection_method": "functional_test",
            "ai_detection_required": False
        }
    },
    "I": {
        "ignition_system": {
            "name": "Ignition System",
            "category": "Engine",
            "check_type": "functional",
            "criteria": "Proper spark, no misfiring",
            "mandatory_saso_check": False,
            "detection_method": "diagnostic_scan",
            "ai_detection_required": False
        },
        "intake_manifold": {
            "name": "Intake Manifold",
            "category": "Engine",
            "check_type": "condition",
            "criteria": "No cracks, leaks, or damage",
            "mandatory_saso_check": False,
            "detection_method": "visual_inspection",
            "ai_detection_required": False
        }
    },
    "J": {
        "jack": {
            "name": "Jack (Emergency Kit)",
            "category": "Safety Equipment",
            "check_type": "condition",
            "criteria": "Present, functional, properly stored",
            "mandatory_saso_check": True,
            "detection_method": "visual_inspection",
            "ai_detection_required": False
        }
    },
    "K": {
        "kingpin": {
            "name": "Kingpin (Trailer Coupling)",
            "category": "Coupling",
            "check_type": "condition",
            "criteria": "No wear, proper lubrication, secure connection",
            "mandatory_saso_check": True,
            "detection_method": "visual_inspection",
            "ai_detection_required": True
        }
    },
    "L": {
        "license_plate": {
            "name": "License Plate",
            "category": "Registration",
            "check_type": "visibility",
            "criteria": "Clearly visible, not obscured, correct format",
            "mandatory_saso_check": True,
            "detection_method": "ocr_recognition",
            "ai_detection_required": True,
            "ai_focus": "license_plate_ocr"
        },
        "leaf_springs": {
            "name": "Leaf Springs",
            "category": "Suspension",
            "check_type": "condition",
            "criteria": "No cracks, proper ride height",
            "mandatory_saso_check": False,
            "detection_method": "visual_inspection",
            "ai_detection_required": False
        }
    },
    "M": {
        "muffler": {
            "name": "Muffler",
            "category": "Exhaust",
            "check_type": "condition",
            "criteria": "No rust, holes, or loose connections",
            "mandatory_saso_check": False,
            "detection_method": "visual_inspection",
            "ai_detection_required": False
        },
        "mirrors": {
            "name": "Mirrors (Side and Rear)",
            "category": "Safety",
            "check_type": "condition",
            "criteria": "Intact, properly adjusted, clear view",
            "mandatory_saso_check": True,
            "detection_method": "visual_inspection",
            "ai_detection_required": True
        }
    },
    "O": {
        "oil_filter": {
            "name": "Oil Filter",
            "category": "Engine",
            "check_type": "condition",
            "criteria": "Not leaking, proper mounting",
            "mandatory_saso_check": False,
            "detection_method": "visual_inspection",
            "ai_detection_required": False
        },
        "oxygen_sensor": {
            "name": "Oxygen Sensor",
            "category": "Emission Control",
            "check_type": "functional",
            "criteria": "Responsive, no error codes",
            "mandatory_saso_check": True,
            "detection_method": "diagnostic_scan",
            "ai_detection_required": False
        }
    },
    "P": {
        "power_steering_pump": {
            "name": "Power Steering Pump",
            "category": "Steering",
            "check_type": "condition",
            "criteria": "No leaks, proper pressure, smooth operation",
            "mandatory_saso_check": False,
            "detection_method": "visual_inspection",
            "ai_detection_required": False
        },
        "pistons": {
            "name": "Pistons",
            "category": "Engine",
            "check_type": "condition",
            "criteria": "No scoring, carbon buildup within limits",
            "mandatory_saso_check": False,
            "detection_method": "engine_compression_test",
            "ai_detection_required": False
        }
    },
    "R": {
        "radiator": {
            "name": "Radiator",
            "category": "Cooling",
            "check_type": "condition",
            "criteria": "No leaks, no blockages, proper coolant level",
            "mandatory_saso_check": False,
            "detection_method": "visual_inspection",
            "ai_detection_required": False
        },
        "rear_underrun_guard": {
            "name": "Rear Underrun Guard (Rear Barrier)",
            "category": "Safety Barriers",
            "check_type": "structural",
            "criteria": "Maximum 550mm height from ground, properly secured",
            "mandatory_saso_check": True,
            "saso_reference": "rear_guards",
            "detection_method": "ai_measurement",
            "ai_detection_required": True,
            "threshold_max_height_mm": 550
        }
    },
    "S": {
        "side_slip": {
            "name": "Side Slip (Steering Alignment)",
            "category": "Alignment",
            "check_type": "alignment",
            "criteria": "±7 mm/m maximum deviation",
            "mandatory_saso_check": True,
            "saso_reference": "side_slip",
            "detection_method": "side_slip_test",
            "ai_detection_required": True,
            "threshold_mm_per_meter": 7
        },
        "side_guards": {
            "name": "Side Protective Devices (Barriers)",
            "category": "Safety Barriers",
            "check_type": "structural",
            "criteria": "Maximum 550mm height, maximum 300mm gap from tire",
            "mandatory_saso_check": True,
            "saso_reference": "side_guards",
            "detection_method": "ai_measurement",
            "ai_detection_required": True,
            "threshold_max_height_mm": 550,
            "threshold_max_gap_mm": 300
        },
        "suspension": {
            "name": "Suspension System",
            "category": "Suspension",
            "check_type": "condition",
            "criteria": "No leaks, shocks functional, springs intact",
            "mandatory_saso_check": True,
            "detection_method": "visual_inspection",
            "ai_detection_required": True,
            "ai_focus": "suspension_condition"
        },
        "seatbelts": {
            "name": "Seatbelts",
            "category": "Safety",
            "check_type": "functional",
            "criteria": "All belts functional, no fraying or damage",
            "mandatory_saso_check": True,
            "detection_method": "functional_test",
            "ai_detection_required": False
        }
    },
    "T": {
        "tires": {
            "name": "Tires",
            "category": "Tires",
            "check_type": "wear",
            "criteria": "Minimum 2.4mm tread depth, no damage, proper inflation, age <10 years",
            "mandatory_saso_check": True,
            "saso_reference": "tire_condition",
            "detection_method": "ai_measurement",
            "ai_detection_required": True,
            "threshold_min_tread_mm": 2.4,
            "threshold_max_age_years": 10
        },
        "tie_rods": {
            "name": "Tie Rods",
            "category": "Steering",
            "check_type": "condition",
            "criteria": "No looseness, wear, or damage",
            "mandatory_saso_check": False,
            "detection_method": "visual_inspection",
            "ai_detection_required": False
        }
    },
    "U": {
        "undercarriage": {
            "name": "Undercarriage",
            "category": "Structure",
            "check_type": "condition",
            "criteria": "No oil leaks, rust, cracks, or corrosion",
            "mandatory_saso_check": True,
            "detection_method": "visual_inspection",
            "ai_detection_required": True,
            "ai_focus": "leakage_and_rust"
        }
    },
    "V": {
        "valves": {
            "name": "Valves",
            "category": "Engine",
            "check_type": "condition",
            "criteria": "No excessive carbon, proper seating",
            "mandatory_saso_check": False,
            "detection_method": "diagnostic_scan",
            "ai_detection_required": False
        },
        "vin_plate": {
            "name": "VIN Plate",
            "category": "Registration",
            "check_type": "visibility",
            "criteria": "Clearly visible, not tampered or obscured",
            "mandatory_saso_check": True,
            "detection_method": "ocr_recognition",
            "ai_detection_required": True,
            "ai_focus": "vin_detection"
        }
    },
    "W": {
        "wiper_blades": {
            "name": "Wiper Blades",
            "category": "Visibility",
            "check_type": "wear",
            "criteria": "No streaking, tears, or skipping",
            "mandatory_saso_check": False,
            "detection_method": "functional_test",
            "ai_detection_required": False
        },
        "wheel_bearings": {
            "name": "Wheel Bearings",
            "category": "Wheels",
            "check_type": "condition",
            "criteria": "No noise, play, or excessive heat",
            "mandatory_saso_check": False,
            "detection_method": "tactile_test",
            "ai_detection_required": False
        }
    }
}

# Summary statistics
TOTAL_COMPONENTS = sum(len(components) for components in VEHICLE_COMPONENTS.values())
MANDATORY_SASO_COMPONENTS = sum(
    1 for category in VEHICLE_COMPONENTS.values()
    for component in category.values()
    if component.get('mandatory_saso_check', False)
)
AI_DETECTION_REQUIRED = sum(
    1 for category in VEHICLE_COMPONENTS.values()
    for component in category.values()
    if component.get('ai_detection_required', False)
)
