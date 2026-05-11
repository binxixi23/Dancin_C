# 🎭 Affective Computing Logic (Tính toán cảm xúc)

Dự án Dancin_C và Story_Teller sử dụng mô hình ánh xạ cảm xúc (Emotion Mapping) để thay đổi hành vi của Robot/Agent.

## 1. Dancin_C (Phản hồi Tiếp xúc & Thị giác)
- **Input:** `Grip_Force` (Cảm biến lực) + `Facial_Expression` (Camera).
- **Logic:**
  - Nếu `Grip_Force > 0.8` (Căng thẳng) + `Expression == "Scared"`: Robot dừng ngay lập tức, chuyển sang chế độ **High Impedance** (Trụ đứng vững).
  - Nếu `Grip_Force < 0.3` (Thả lỏng) + `Expression == "Happy"`: Robot tăng 10% BPM (Tăng nhiệt huyết).

## 2. Story_Teller (Phản hồi Ánh mắt & Sắc mặt)
- **Input:** Video stream xử lý qua Gemini 3 Flash.
- **Logic Branching:**
  - `Bored (Ngáp/Nhìn chỗ khác)` -> Kích hoạt lệnh `CHANGE_GENRE`.
  - `Excited (Mắt mở to/Cười)` -> Kích hoạt lệnh `DEEPEN_DETAILS` (Kể chi tiết hơn).
