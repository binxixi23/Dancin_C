import serial
import time

class BridgeSerial:
    def __init__(self, port='COM3', baudrate=115200):
        try:
            self.ser = serial.Serial(port, baudrate, timeout=0.1)
            time.sleep(2) # Wait for ESP32 to reset
            print(f"Connected to Robot Hardware on {port}")
        except:
            print("Warning: No hardware detected. Running in Simulation Mode.")
            self.ser = None

    def send_command(self, position, impedance):
        """Sends control parameters to ESP32."""
        if self.ser:
            cmd = f"POS:{position},IMP:{impedance}\n"
            self.ser.write(cmd.encode())

    def read_sensors(self):
        """Reads Force Feedback from the Robot's hands."""
        if self.ser and self.ser.in_available():
            line = self.ser.readline().decode('utf-8').strip()
            if line.startswith("FORCE:"):
                return float(line.split(":")[1])
        return 0.0 # Default/Simulated force
