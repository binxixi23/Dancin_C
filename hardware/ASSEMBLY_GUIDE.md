# 🏗 Assembly Guide

Quy trình lắp ráp Robot Dancin_C tuân thủ các bước để đảm bảo tính Back-drivable.

### Bước 1: Khung cơ khí (Mechanical Frame)
- Sử dụng nhôm định hình hoặc nhựa in 3D (PETG/Carbon Fiber) để đảm bảo độ cứng.
- Gắn động cơ BLDC vào khung thông qua bộ truyền động Quasi-Direct (tỉ lệ giảm tốc thấp 1:6 hoặc 1:9).

### Bước 2: Cảm biến lực (Interaction Point)
- Dán cảm biến FSR vào mặt trong của tay nắm robot.
- Đảm bảo có lớp đệm cao su mềm (Silicone) để lực truyền vào cảm biến đều hơn.

### Bước 3: Cân chỉnh (Calibration)
1. **Zero Moment Point (ZMP):** Đặt robot đứng yên và chạy script `calibrate_imu.ino`.
2. **Force Threshold:** Chỉnh mức ngưỡng lực nắm (Grip) trong `main_controller.ino` để robot phân biệt được lực "tựa vào" và lực "vô ý chạm".

> **Lưu ý:** Luôn kiểm tra nhiệt độ động cơ BLDC khi chạy ở chế độ High Impedance trong thời gian dài.
