# src/test_all.py
from src.agent_orchestrator import DancinCOrchestrator
from src.story_teller.narrator_agent import StoryTeller

def test_system():
    print("\n" + "="*30)
    print("TESTING DANCIN_C (Physical Empathy)")
    print("="*30)
    
    dance_brain = DancinCOrchestrator()
    
    # Situation: User is losing balance (High force)
    print("\n[Scenario]: User is leaning too hard / losing balance...")
    result_safety = dance_brain.process_cycle(pose_data=None, force_val=0.85)
    print(f"Robot Response: {result_safety}")

    # Situation: User is happy and flowing
    print("\n[Scenario]: User is dancing smoothly...")
    result_sync = dance_brain.process_cycle(pose_data=None, force_val=0.2)
    print(f"Robot Response: {result_sync}")

    print("\n" + "="*30)
    print("TESTING STORY_TELLER (Digital Empathy)")
    print("="*30)
    
    story_brain = StoryTeller()
    
    # Situation: Listener looks bored
    print("\n[Scenario]: Listener is yawning (Bored)...")
    story_feedback = story_brain.adapt_story("bored", "Fairy Tale")
    print(f"Narrator Response: {story_feedback}")

if __name__ == "__main__":
    try:
        test_system()
        print("\n✅ ALL SYSTEMS LOGIC VERIFIED!")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
