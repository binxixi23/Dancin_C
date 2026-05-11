import serial
import time
from crewai import Agent, Task, Crew

class DancinCOrchestrator:  # Kiểm tra kỹ tên này
    def __init__(self):
        self.sensei = Agent(
            role='Dance Sensei',
            goal='Analyze skeletal pose',
            backstory='Expert instructor.',
            verbose=True
        )
        self.safety = Agent(
            role='Safety Guard',
            goal='Monitor safety',
            backstory='Safety first.',
            verbose=True
        )

    def process_cycle(self, pose_data, force_val):
        instruction = "MOVE_FORWARD"
        impedance = 0.8
        if force_val > 0.7:
            instruction = "STAY_AND_SUPPORT"
            impedance = 1.0
        return instruction
