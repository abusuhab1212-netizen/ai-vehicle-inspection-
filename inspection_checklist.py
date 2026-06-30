# SASO Inspection Checklist & Compliance Rules
# Based on: الدليل الإرشادي التفصيلي لحواجز الشاحنات والمقطورات
# Saudi Standards for Truck & Trailer Barriers

from enum import Enum
from typing import Dict, List, Tuple

class InspectionComponent(str, Enum):
    FRONT_GUARDS = "front_guards"
    SIDE_GUARDS = "side_guards"
    REAR_GUARDS = "rear_guards"
    SIDE_SLIP = "side_slip"
    BRAKE_EFFICIENCY = "brake_efficiency"
    TIRE_CONDITION = "tire_condition"
    UNDERCARRIAGE = "undercarriage"
    BRAKE_PADS = "brake_pads"
    HYDRAULIC_LINES = "hydraulic_lines"

class ComplianceStandard:
    """
    SASO Standards for Truck & Trailer Inspection
    Based on: الدليل الإرشادي التفصيلي لحواجز الشاحنات والمقطورات
    """
    
    # Front Guards (Protective Devices)
    FRONT_GUARD_HEIGHT_MIN = 400  # mm
    FRONT_GUARD_HEIGHT_MAX = 1200  # mm
    FRONT_GUARD_GROUND_CLEARANCE_MAX = 550  # mm
    FRONT_GUARD_GAP_MAX = 300  # mm
    
    # Side Guards (Protective Devices)
    SIDE_GUARD_HEIGHT_MAX = 550  # mm from ground
    SIDE_GUARD_GAP_MAX = 300  # mm (distance from barrier to tire)
    SIDE_GUARD_CABIN_HEIGHT_THRESHOLD = 550  # mm
    
    # Rear Guards (Protective Devices)
    REAR_GUARD_HEIGHT_MAX = 550  # mm from ground
    REAR_GUARD_GROUND_CLEARANCE_MAX = 300  # mm
    REAR_GUARD_OVERHANG_MAX = 300  # mm
    
    # Side Slip (Steering Alignment)
    SIDE_SLIP_TOLERANCE = 7  # mm/m (±7 mm per meter)
    
    # Brake Efficiency
    BRAKE_EFFICIENCY_TRUCK_MIN = 50  # %
    BRAKE_EFFICIENCY_CAR_MIN = 45  # %
    
    # Tire Condition
    TIRE_TREAD_DEPTH_MIN = 1.6  # mm (legal limit)
    TIRE_TREAD_DEPTH_RECOMMENDED = 2.4  # mm
    
    # Undercarriage
    UNDERCARRIAGE_MIN_SCORE = 70  # 0-100 scale
    
    # Brake Pads
    BRAKE_PAD_MIN_THICKNESS = 3  # mm
    
    # Hydraulic Lines
    HYDRAULIC_LEAK_ALLOWED = False  # No leakage


class ComplianceChecklist:
    """
    Master Checklist for Vehicle Inspection
    """
    
    def __init__(self):
        self.checklist = {
            InspectionComponent.FRONT_GUARDS: {
                "name": "Front Protective Devices",
                "description": "Front guards height and ground clearance",
                "rules": [
                    {
                        "rule": "height_range",
                        "min": ComplianceStandard.FRONT_GUARD_HEIGHT_MIN,
                        "max": ComplianceStandard.FRONT_GUARD_HEIGHT_MAX,
                        "unit": "mm",
                        "description": "Height must be between 400-1200 mm"
                    },
                    {
                        "rule": "ground_clearance",
                        "max": ComplianceStandard.FRONT_GUARD_GROUND_CLEARANCE_MAX,
                        "unit": "mm",
                        "description": "Ground clearance max 550 mm"
                    },
                    {
                        "rule": "gap_to_tire",
                        "max": ComplianceStandard.FRONT_GUARD_GAP_MAX,
                        "unit": "mm",
                        "description": "Gap between guard and tire max 300 mm"
                    }
                ]
            },
            
            InspectionComponent.SIDE_GUARDS: {
                "name": "Side Protective Devices (Side Barriers)",
                "description": "Side guards for protecting road users",
                "rules": [
                    {
                        "rule": "height_from_ground",
                        "max": ComplianceStandard.SIDE_GUARD_HEIGHT_MAX,
                        "unit": "mm",
                        "description": "Height from ground max 550 mm (صورة هـ - 16)"
                    },
                    {
                        "rule": "gap_to_tire",
                        "max": ComplianceStandard.SIDE_GUARD_GAP_MAX,
                        "unit": "mm",
                        "description": "Gap between barrier and tire max 300 mm (صورة هـ - 5)"
                    },
                    {
                        "rule": "cabin_height_risk",
                        "cabin_height_threshold": ComplianceStandard.SIDE_GUARD_CABIN_HEIGHT_THRESHOLD,
                        "unit": "mm",
                        "description": "If cabin height > 550mm AND gap > 300mm = FAIL (Dangerous)"
                    }
                ]
            },
            
            InspectionComponent.REAR_GUARDS: {
                "name": "Rear Protective Devices",
                "description": "Rear guards for protecting road users",
                "rules": [
                    {
                        "rule": "height_from_ground",
                        "max": ComplianceStandard.REAR_GUARD_HEIGHT_MAX,
                        "unit": "mm",
                        "description": "Height from ground max 550 mm"
                    },
                    {
                        "rule": "ground_clearance",
                        "max": ComplianceStandard.REAR_GUARD_GROUND_CLEARANCE_MAX,
                        "unit": "mm",
                        "description": "Ground clearance max 300 mm"
                    },
                    {
                        "rule": "overhang",
                        "max": ComplianceStandard.REAR_GUARD_OVERHANG_MAX,
                        "unit": "mm",
                        "description": "Overhang max 300 mm"
                    }
                ]
            },
            
            InspectionComponent.SIDE_SLIP: {
                "name": "Side Slip (Steering Alignment)",
                "description": "Vehicle steering alignment check",
                "rules": [
                    {
                        "rule": "side_slip_tolerance",
                        "max": ComplianceStandard.SIDE_SLIP_TOLERANCE,
                        "unit": "mm/m",
                        "description": "Side slip must not exceed ±7 mm/m"
                    }
                ]
            },
            
            InspectionComponent.BRAKE_EFFICIENCY: {
                "name": "Brake Efficiency",
                "description": "Brake system performance test",
                "rules": [
                    {
                        "rule": "truck_min_efficiency",
                        "min": ComplianceStandard.BRAKE_EFFICIENCY_TRUCK_MIN,
                        "unit": "%",
                        "vehicle_type": "truck",
                        "description": "Trucks require minimum 50% brake efficiency"
                    },
                    {
                        "rule": "car_min_efficiency",
                        "min": ComplianceStandard.BRAKE_EFFICIENCY_CAR_MIN,
                        "unit": "%",
                        "vehicle_type": "car",
                        "description": "Cars require minimum 45% brake efficiency"
                    }
                ]
            },
            
            InspectionComponent.TIRE_CONDITION: {
                "name": "Tire Condition",
                "description": "Tire tread depth and wear",
                "rules": [
                    {
                        "rule": "tread_depth_min",
                        "min": ComplianceStandard.TIRE_TREAD_DEPTH_MIN,
                        "unit": "mm",
                        "description": "Minimum tread depth 1.6 mm (legal limit)"
                    },
                    {
                        "rule": "tread_depth_recommended",
                        "recommended": ComplianceStandard.TIRE_TREAD_DEPTH_RECOMMENDED,
                        "unit": "mm",
                        "description": "Recommended tread depth 2.4 mm"
                    }
                ]
            },
            
            InspectionComponent.UNDERCARRIAGE: {
                "name": "Undercarriage Condition",
                "description": "Overall undercarriage condition and rust/damage",
                "rules": [
                    {
                        "rule": "condition_score",
                        "min": ComplianceStandard.UNDERCARRIAGE_MIN_SCORE,
                        "unit": "score",
                        "description": "Minimum condition score 70/100"
                    }
                ]
            },
            
            InspectionComponent.BRAKE_PADS: {
                "name": "Brake Pads Condition",
                "description": "Brake pad thickness and wear",
                "rules": [
                    {
                        "rule": "pad_thickness",
                        "min": ComplianceStandard.BRAKE_PAD_MIN_THICKNESS,
                        "unit": "mm",
                        "description": "Minimum brake pad thickness 3 mm"
                    }
                ]
            },
            
            InspectionComponent.HYDRAULIC_LINES: {
                "name": "Hydraulic Lines & Connections",
                "description": "Check for leaks and damage",
                "rules": [
                    {
                        "rule": "no_leakage",
                        "allowed": ComplianceStandard.HYDRAULIC_LEAK_ALLOWED,
                        "description": "No hydraulic fluid leakage allowed"
                    }
                ]
            }
        }
    
    def get_checklist(self) -> Dict:
        """Return complete checklist"""
        return self.checklist
    
    def get_component_rules(self, component: InspectionComponent) -> Dict:
        """Get rules for specific component"""
        return self.checklist.get(component)
    
    def get_all_components(self) -> List[str]:
        """Get list of all inspection components"""
        return [comp.value for comp in InspectionComponent]
    
    def print_checklist(self):
        """Print formatted checklist"""
        print("\n" + "="*80)
        print("SASO VEHICLE INSPECTION CHECKLIST")
        print("Based on: الدليل الإرشادي التفصيلي لحواجز الشاحنات والمقطورات")
        print("="*80 + "\n")
        
        for idx, (component, details) in enumerate(self.checklist.items(), 1):
            print(f"{idx}. {details['name']}")
            print(f"   Description: {details['description']}")
            print(f"   Rules:")
            for rule in details['rules']:
                print(f"     • {rule['description']}")
            print()


# Initialize global checklist
INSPECTION_CHECKLIST = ComplianceChecklist()

if __name__ == "__main__":
    INSPECTION_CHECKLIST.print_checklist()
