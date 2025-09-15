1. Giới thiệu

 	- Khởi tạo và tìm hiểu các tính năng cơ bản của EC2 (Elastic Compute Cloud)

 	- Cài đặt ứng dụng mẫu: AWS User Management (CRUD nodejs)

 	- Triển khai ứng dụng trên EC2



2\. Chuẩn bị

 	- Tạo VPC Linux và VPC Windows (cần thiết lập môi trường mạng an toàn qua VPC)

 		+ Việc thiết lập các VPC và SG riêng biệt giúp cho các instance tăng cường bảo mật và kiểm soát lượng truy cập mạng tốt hơn -> tuân thủ nguyên tắc phân quyền tối thiểu



 	- Tạo các Securiy Group cho 2 VPC Linux và Window



3\. KHỞI TẠO CÁC EC2 INSTANCES CHO WINDOW LÀ LINUX

 	- Kết nối đến Windows instance trên AWS EC2 được thực hiện thông qua Remote Desktop Protocol (RDP) qua cổng 3389. AWS cung cấp cơ chế bảo mật để lấy mật khẩu quản trị viên bằng cách sử dụng key pair đã tạo trước đó.

 	- Có nhiều phương thức để kết nối đến EC2 Linux instance. Trong bài lab này, chúng ta sẽ tìm hiểu hai phương pháp phổ biến: sử dụng MobaXterm và PuTTY. Cả hai đều là SSH clients cho phép bạn kết nối an toàn đến máy chủ Linux từ xa.



4\. Amazon EC2 Cơ bản:



* Thay đổi cấu hình EC2

 	- Trong EC2 có cung cấp nhiều loại instance type khác nhau phù hợp cho các trường hợp sử dụng khác nhau

 	- Trước khi thay đổi cấu hình EC2 phải STOP máy chủ trước -> Sau khi thay đổi instance type thì ta restart lại máy chủ để chạy

 	- Sẽ chờ khoảng 3-4 phút để AWS check lại máy chủ trước khi vào trạng thái running



* Tạo EC2 Snapshot:

 	- Trong khi tạo snapshot ta sẽ có 2 options sau:

 		+ Volume: Bạn sẽ chọn chính xác volume mà bạn muốn thực hiện snapshot

 		+ Instance: Bạn sẽ chọn chính xác EC2 instance mà bạn muốn thực hiện snapshot cho ổ EBS volume. Tuy nhiên, lúc này AWS sẽ snapshot tất cả EBS volume đang được gắn vào EC2 đó.



* Tạo Custome AMI:

 	- Amazon Machine Image (AMI) là một template chứa cấu hình phần mềm (hệ điều hành, ứng dụng và các cài đặt) cần thiết để khởi chạy một EC2 instance.

 	- Tạo Custom AMI cho phép bạn lưu trữ trạng thái hiện tại của một instance để tái sử dụng hoặc triển khai nhiều instance giống nhau.

 	- Phải stop ec2 instance trước khi tạo image -> quá trình tạo sẽ mất khoảng 5 phút



* Tạo Instance từ Customer AMI:

 	- Trong lúc tạo các instance từ AMI ta có thể linh hoạt điều chỉnh lại instance type phù hợp với nhu cầu sử dụng



* Truy cập khi mất Key Pair EC2-Windows bằng SSM:

 	- Key Pair được dùng để mã hóa và giải mã thông tin đăng nhập vào máy chủ ảo EC2.

 	- Khi bị mất Key Pair, AWS Systems Manager (SSM) cung cấp giải pháp an toàn để khôi phục quyền truy cập vào EC2 instance mà không cần tạo lại instance.

 	- Để sử dụng AWS Systems Manager, EC2 instance của bạn cần đáp ứng các yêu cầu sau:

 		+ EC2 cần có kết nối Internet để giao tiếp với AWS Systems Manager thông qua IP public hoặc NAT Gateway

 		+ Hoặc EC2 cần được cấu hình với VPC Endpoint cho AWS Systems Manager

 		+ SSM Agent phải được cài đặt và đang chạy trên instance

 		+ EC2 instance phải có IAM role với quyền SSM thích hợp



6\. Triển khai ứng dụng Node.js trên Amazon Linux Instance

7\. Triển khai ứng dụng Node.js trên Microsoft Instance





