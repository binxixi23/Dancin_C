# 🤖 Dancin_C: The Embodied Affective AI Ecosystem
![Dancin_C Robot](assets/robot_dance.png)


# "Where AI doesn't just process code, but understands your heartbeat and emotions."

# Dancin\_C is a multimodal Embodied AI project designed to bridge the gap between physical interaction and emotional intelligence. By combining Computer Vision, Impedance Control, and Affective Computing, Dancin\_C acts as a steady pillar, a professional coach, and a soulful companion.

# \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

# Real-World Interaction Scenarios

# 1\. The Professional Dance Coach (Guided Pedagogy)

# The learner holds the robot's hands instead of watching a video.

# *	Scenario: A learner struggles with a Waltz step.

# *	AI Response: Gemini 3 Flash detects incorrect posture. The robot adjusts its motors to gently guide the user's hands into the correct trajectory while resisting the wrong movement.

# *	Voice: "You're doing great! Just relax your shoulders and take a slightly larger step with your left foot." (via OpenAI Realtime).

# 2\. The Steady Pillar (Empathetic Partner)

# Dancin\_C is designed to be the "lead" and a source of stability.

# *	Scenario: A learner feels exhausted or loses balance.

# *	AI Response: Force Sensors (FSR) detect the user leaning heavily on the robot. The system switches to High Impedance Mode, turning the robot into a solid, unmoving support structure. It also lowers the music's BPM to create a calming atmosphere.

# 3\. The Mind-Reading Storyteller (Affective Interaction)

# At night, Dancin\_C transitions from the dance floor to a companion.

# *	Scenario: The robot narrates a fairy tale, but the camera detects the user yawning or looking away (boredom).

# *	AI Response: The robot pauses and asks: "This story seems a bit too slow for you. Should we switch to a sci-fi adventure on Mars instead?"

# *	Empathy: The user says, "I had a rough day." The robot analyzes the vocal tone and responds with a warm, comforting voice, offering encouraging philosophical insights.

# \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

# Technical Overview \& Stack

# The Brain (High-Level AI)

# *	Gemini 3 Flash: Processes 60fps video streams for skeletal tracking and facial expression analysis.

# *	OpenAI o3: Handles complex reasoning and conflict resolution between "Performance" and "Safety."

# *	OpenAI Realtime API: Provides natural voice coaching with less than 200ms latency.

# The Reflexes (Low-Level Control)

# *	Control Rate: 1000Hz (1ms) ensures the robot reacts instantly to human force.

# *	Quasi-Direct Drive (QDD): Enables Back-drivability, allowing users to push the robot back naturally without gear damage.

# *	Mastery Score Algorithm:

# \\(MasteryScore=(Pose\\times 0.4)+(Rhythm\\times 0.4)+(GripStability\\times 0.2)\\)

# \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

# Repository Structure

# *	/src: Core control source code (Python \& C++).

# *	/hardware: Wiring diagrams, BOM, and assembly guides.

# *	/docs: Deep dives into VLA models and Emotion Logic mapping.

# *	/assets: Project visuals and demonstration media.

# \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

# Getting Started

# 1\.	Clone the repo: git clone [https://github.com](https://github.com/binxixi23/Dancin_C)

# 2\.	Install dependencies: pip install -r requirements.txt

# 3\.	Configure .env: Add your Gemini and OpenAI API keys.

# 4\.	Run Simulation: python -m src.test\_all

# \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

# Built with the belief that AI should help humans connect with themselves and others in more meaningful ways.

# 


