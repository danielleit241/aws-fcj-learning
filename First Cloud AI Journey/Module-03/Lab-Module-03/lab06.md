1. Giới thiệu

&nbsp;	- Chúng ta sẽ thực hiện triển khai ứng dụng bằng cách sử dụng Amazon EC2 Auto Scaling Group để đảm bảo khả năng mở rộng linh hoạt theo nhu cầu của người truy cập. 

&nbsp;	- Ngoài ra, chúng ta cũng sẽ triển khai Elastic Load Balancing để cân bằng tải và phân phối yêu cầu từ người dùng đến Application Tier của ứng dụng.



&nbsp;	- Auto Scaling Group: Khi ứng dụng của chúng ta đưa vào hoạt động, lượng người truy cập sẽ thay đổi theo thời gian, do đó chúng ta cần thường xuyên thay đổi (scaling) lượng instance nhằm nâng cao tính sẵn sàng và tiết kiệm chi phí. Để tự động hóa và linh hoạt trong công việc scaling, chúng ta sẽ có giải pháp là Auto Scaling Group.



2\. Các bước chuẩn bị:

&nbsp;	Thiết lập hạ tầng mạng

&nbsp;	Khởi tạo EC2 instance

&nbsp;	Khởi tạo Database instance với Amazon RDS

&nbsp;	Cài đặt dữ liệu cho database

&nbsp;	Triển khai máy chủ web

&nbsp;	Chuẩn bị metric cho Predictive scaling



3\. Tạo AMI

&nbsp;	- AMIs (Amazon Machine Images) lưu trữ các thông tin như hệ điều hành, ứng dụng, và cấu hình của EC2 instance mà chúng được tạo từ đó. Việc tạo AMI đảm bảo rằng khi khởi tạo máy chủ mới, tất cả các instance đều giống nhau và có thể hoạt động ngay lập tức.

&nbsp;	- Launch template là một công cụ mà chúng ta dùng để cấu hình việc khởi tạo các EC2 instance mới thông qua AMI được chỉ định, loại instance, cấu hình mạng, và các tùy chọn bảo mật. Khi cần khởi tạo một hoặc nhiều máy chủ giống nhau, chúng ta chỉ cần sử dụng launch template đã được cấu hình sẵn.



4\. Thiết lập Load Balancer

&nbsp;	- Elastic Load Balancing (ELB) là một dịch vụ AWS quan trọng để đảm bảo tính khả dụng cao và khả năng mở rộng cho ứng dụng của bạn. ELB tự động phân phối lưu lượng truy cập đến trên nhiều mục tiêu, như các phiên bản Amazon EC2, container, địa chỉ IP, và các hàm Lambda, giúp tối ưu hóa việc sử dụng tài nguyên, cải thiện hiệu suất và đảm bảo khả năng chịu lỗi.

&nbsp;	- Sử dụng ELB kết hợp với Auto Scaling Groups để tự động điều chỉnh số lượng máy chủ dựa trên nhu cầu thực tế, giúp tối ưu chi phí vận hành.



5\. Tạo auto scaling group

&nbsp;	- Ở phần kiểm thử kết quả trước đó, chúng ta nhận thấy khi ứng dụng nhận nhiều request, hiệu suất không còn ổn định. Giải pháp là tăng số lượng EC2 Instance trong hệ thống và sử dụng Load Balancer để phân phối các yêu cầu từ người dùng.

