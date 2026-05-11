from src.agent_orchestrator import DancinCOrchestrator

def test_run():
    print("--- KHỞI ĐỘNG GIẢ LẬP DANCIN_C ---")
    brain = DancinCOrchestrator()
    
    # Giả lập tình huống 1: Người học đang nhảy tốt
    print("\n[Tình huống 1]: Người học nhảy đúng nhịp...")
    decision1 = brain.process_cycle(pose_data={"score": 0.9}, force_val=0.2)
    print(f"Quyết định của Agent: {decision1}")

    # Giả lập tình huống 2: Người học mất thăng bằng (Lực nắm tăng mạnh)
    print("\n[Tình huống 2]: Phát hiện lực nắm cực mạnh (người học sắp ngã)...")
    decision2 = brain.process_cycle(pose_data={"score": 0.4}, force_val=0.9)
    print(f"Quyết định của Agent: {decision2}")

if __name__ == "__main__":
    test_run()
