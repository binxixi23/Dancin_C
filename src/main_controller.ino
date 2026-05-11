#include <esp_timer.h> // Thư viện để chạy vòng lặp chính xác 1ms

// Định nghĩa các chân kết nối
const int FSR_PIN = 34;    // Cảm biến lực (Force Feedback)
const int MOTOR_PIN = 25;  // Giả lập lệnh cho Motor (PWM hoặc CAN Bus)

// Biến trạng thái
float current_impedance = 0.5; // Độ cứng của khớp (0.0 - 1.0)
float target_position = 0.0;
float feedback_force = 0.0;

// Vòng lặp điều khiển 1000Hz (1ms)
void IRAM_ATTR onTimer(void* arg) {
    // 1. Đọc dữ liệu cảm biến lực từ người dùng (Force Feedback)
    feedback_force = analogRead(FSR_PIN) / 4095.0;

    // 2. Thuật toán Trở kháng (Impedance Control) đơn giản
    // Nếu người dùng đẩy mạnh, robot sẽ "mềm" đi để nương theo
    float output_torque = (target_position - feedback_force) * current_impedance;

    // 3. Gửi lệnh tới Motor (Thực tế sẽ gửi qua CAN Bus)
    // dacWrite(MOTOR_PIN, output_torque * 255);
}

void setup() {
    Serial.begin(115200);
    pinMode(FSR_PIN, INPUT);

    // Khởi tạo Timer cho vòng lặp 1ms
    const esp_timer_create_args_t timer_args = {
        .callback = &onTimer,
        .name = "control_loop"
    };
    esp_timer_handle_t timer;
    esp_timer_create(&timer_args, &timer);
    esp_timer_start_periodic(timer, 1000); // 1000 microseconds = 1ms
}

void loop() {
    // Nhận lệnh từ Python (Agent Orchestrator)
    if (Serial.available() > 0) {
        String data = Serial.readStringUntil('\n');
        // Format: "POS:90,IMP:0.8"
        if (data.startsWith("POS:")) {
            target_position = data.substring(4, data.indexOf(',')).toFloat();
            current_impedance = data.substring(data.indexOf("IMP:") + 4).toFloat();
        }
    }

    // Gửi ngược dữ liệu cảm biến lên AI Brain để phân tích Mastery Score
    static uint32_t last_send = 0;
    if (millis() - last_send > 100) { // Gửi mỗi 100ms để không nghẽn Serial
        Serial.printf("FORCE:%.2f\n", feedback_force);
        last_send = millis();
    }
}
