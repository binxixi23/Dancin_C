# Hybrid Leg-Wheel Locomotion Controller Logic
class LocomotionAgent:
    def __init__(self):
        self.modes = ["WHEELED", "STEPPING", "CROUCH"]
        self.current_mode = "WHEELED"

    def analyze_terrain(self, lidar_data):
        # Logic: If terrain roughness > threshold, switch to STEPPING
        if lidar_data['roughness'] > 0.5:
            self.switch_mode("STEPPING")
        else:
            self.switch_mode("WHEELED")

    def switch_mode(self, new_mode):
        print(f"[LOCOMOTION] Switching from {self.current_mode} to {new_mode}")
        self.current_mode = new_mode
