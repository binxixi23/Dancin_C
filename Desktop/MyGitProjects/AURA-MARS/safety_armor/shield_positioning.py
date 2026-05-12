# Defensive Positioning & Shielding Logic
class GuardianAgent:
    def __init__(self):
        self.threat_direction = 0 # Degrees

    def calculate_shield_angle(self, ballistic_threat_vector, patient_position):
        # Logic: Rotate the armored chassis to block the threat vector
        # ensuring the patient is in the 'shadow' of the robot's armor.
        shield_angle = (ballistic_threat_vector + 180) % 360
        print(f"[GUARDIAN] Deploying Ballistic Shield at {shield_angle} degrees.")
        return shield_angle
