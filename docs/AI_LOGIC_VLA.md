# 🧠 Kiến trúc Logic AI & VLA (Thị giác-Ngôn ngữ-Hành động)

Tài liệu này giải thích cách **Dancin_C** xử lý dữ liệu đa phương thức (Hình ảnh, Giọng nói, Cảm biến lực) để đưa ra quyết định vận động trong thời gian thực.

## 1. Mô hình VLA (Thị giác-Ngôn ngữ-Hành động)
Khác với các hệ thống AI thông thường chỉ dừng lại ở văn bản, Dancin_C áp dụng kiến trúc VLA để đóng gói toàn bộ quy trình từ quan sát đến hành động:
- **Vision (Thị giác):** Gemini 3 Flash nhận diện 33 điểm khớp xương (Pose Landmarks) ở tốc độ 60fps.
- **Language (Ngôn ngữ):** OpenAI Realtime xử lý ý định của người dùng (ví dụ: "Tôi mệt quá") và phản hồi huấn luyện.
- **Action (Hành động):** Chuyển đổi xác suất từ mô hình ngôn ngữ thành các giá trị Torque (Mô-men xoắn) và Position cho động cơ BLDC.

## 2. Logic "Cãi nhau" (Multi-Agent Debate)
Cơ chế phản biện được sử dụng để đảm bảo tính sư phạm và an toàn tối đa:

### Kịch bản Xung đột:
1. **Agent Sensei:** Đề xuất: `MOVE_RIGHT_FAST` (Dựa trên nhịp điệu bài nhạc).
2. **Agent Safety:** Phản hồi từ cảm biến lực (Force Sensor) cho thấy người dùng đang bị tụt lại phía sau.
3. **Xử lý Xung đột:**
   - Hệ thống kích hoạt trạng thái **Impedance Adjustment**.
   - Robot sẽ không thực hiện `MOVE_RIGHT_FAST` mà chuyển sang `SUPPORT_STANCE` (Gồng cứng để làm trụ).

## 3. Công thức Mastery Score (Chỉ số Thành thục)
AI liên tục tính toán điểm số để quyết định việc thăng cấp độ (Guided -> Collaborative -> Synchronized):

$$MasteryScore = (P \times 0.4) + (R \times 0.4) + (C \times 0.2)$$

Trong đó:
- **P (Pose Accuracy):** Độ khớp của khung xương với mẫu.
- **R (Rhythm):** Khả năng bắt kịp nhịp BPM (Beats Per Minute).
- **C (Confidence):** Được đo bằng độ ổn định của lực nắm (Grip stability).

## 4. Quản lý trạng thái (State Orchestration)
Dancin_C sử dụng **LangGraph** để quản lý các vòng lặp phản hồi. Nếu điểm **C (Confidence)** giảm đột ngột, hệ thống sẽ tự động kích hoạt "Safety Break" và yêu cầu Agent Voice an ủi người học ngay lập tức.
