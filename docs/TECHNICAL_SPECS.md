## Hệ thống truyền động (Drive System)
- **Actuators:** Động cơ BLDC kết hợp Quasi-Direct Drive giúp robot có khả năng "back-drivable" (người dùng có thể đẩy tay robot mà không hỏng bánh răng).
- **Control Rate:** 1000Hz (1ms) cho vòng lặp điều khiển motor để đảm bảo sự mượt mà.

## Thuật toán ổn định (Stability)
- **ZMP (Zero Moment Point):** Giữ cho robot không ngã khi khách hàng tựa vào.
- **Force Feedback:** Sử dụng EKF (Extended Kalman Filter) để hợp nhất dữ liệu từ cảm biến lực (FSR) và IMU.
