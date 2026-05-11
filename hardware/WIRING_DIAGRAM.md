# 🔌 Wiring & Communication Architecture

Hệ thống sử dụng cấu trúc Hybrid: **CAN Bus** cho vận động và **I2C/Analog** cho cảm biến.

### 1. Kết nối Động cơ (Power & Data)
- **Pin 22.2V** -> XT60 Connector -> Động cơ CyberGear (V+ / V-).
- **ESP32 (GPIO 21/22)** -> CAN Transceiver -> CyberGear (CAN_H / CAN_L).

### 2. Kết nối Cảm biến (Senses)
- **FSR Sensor (Tay nắm)** -> Pin 34 (ADC) trên ESP32 -> Đọc lực tương tác.
- **BNO055 (IMU)** -> Pin 21/22 (I2C) trên ESP32 -> Giám sát thăng bằng.

### 3. Kết nối Máy tính (AI Brain)
- **ESP32** --(USB-C Serial)--> **Host PC** (Chạy Agent Orchestrator).
- **Camera** --(USB 3.0)--> **Host PC** (Chạy Vision Module).
