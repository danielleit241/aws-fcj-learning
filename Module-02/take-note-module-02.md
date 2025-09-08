### **Module 02: Các dịch vụ mạng trên AWS**

##### 

* Sau khi đã tìm hiểu các khái niệm tổng quan về AWS, ta sẽ bắt đầu vào các dịch vụ mạng trên nền tảng AWS
* Hệ thống mạng (network) là xương sống của bất kì cấu trúc điện toán đám mây nào -> đóng vai trò thiết yếu cho việc kết nối các tài nguyên cũng như các dịch vụ khác nhau trên AWS
* Ta sẽ có nhiều dịch vụ mạng khác nhau để thiết kế cũng như đáp ứng các nhu cầu đa dạng từ cơ bản đến nâng cao
* Các dịch vụ mạng quan trọng nhất trên AWS:



&nbsp;	+ AMAZON VIRTUAL PRIVATE CLOUD (VPC)

&nbsp;		+ Đây là một dịch vụ cốt lõi cho phép ta tạo ra một mạng riêng ảo, cô lập khỏi các mạng riêng khác

&nbsp;		+ Ta sẽ khám phá và thiết lập các VPC, Subnet, định tuyến... và các dịch vụ tường lửa đi kèm



&nbsp;	+ VPC PEERING \& TRANSIT GATEWAY

&nbsp;		+ Khi ta có nhiều VPC thì việc kết nối chúng lại với nhau là quan trọng

&nbsp;		+ VPC Peering cho phép ta kết nối 2 VPC và Transit Gateway giải pháp cho ta kết nối số lượng lớn VPC một cách dễ dàng và hiệu quả



&nbsp;	+ VPN \& DIRECT CONNECT

&nbsp;		+ Ngoài việc kết nối giữa các VPC thì ta cũng cần kết nối các môi trường AWS với các Data center nằm ở local (on premise)

&nbsp;		

&nbsp;	+ ELASTIC LOAD BALANCING

&nbsp;		+ Dịch vụ đóng vai trò phân phối lượng truy cập (hay còn gọi là CÂN BẰNG TẢI) trên nhiều máy chủ

&nbsp;		+ ELB đóng vai tròn quan trọng trong khả năng chịu lỗi - đảm bảo khả năng mở rộng cho ứng dụng của ta

##### 

##### 01\. AWS Virtual Private Cloud (VPC)

* Là một dịch vụ cung cấp môi trường mạng ảo riêng tư, được cô lập logic khỏi các mạng khác trên AWS cloud
* VPC cho phép khởi tạo các tài nguyên trên AWS như: cân bằng tải, cơ sở dữ liệu ... -> trong môi trường mạng ảo riêng mà chúng ta có quyền kiểm soát hoàn toàn
* VPC trên AWS khác hoàn toàn với khái niệm private cloud truyền thống

&nbsp;	+ private cloud truyền thống được hiểu là các doanh nghiệp, họ sẽ xây dựng một hệ thống ảo hóa chung trên môi trường on premise với các tính năng mô phỏng theo các nhà cung cấp dịch vụ cloud lớn

&nbsp;	+ Amazon VPC: cho phép khỏi tạo các tài nguyên AWS vào một mạng ảo mà ta đã xác định



* VPC sẽ bao quát nhiều Availability Zone để có thể chạy máy chủ ảo trên nhiều AZ khác nhau -> triển khai trên multi AZ (đảm bảo độ sẵn sàng cao)
* VPC sẽ nằm trong 1 Region, khi tạo VPC cần khai báo 1 lớp mạng CIDR IPv4 (bắt buộc) và IPv6 (tùy chọn)

&nbsp;	+ Giới hạn của VPC hiện tại là 5 VPC trên 1 AWS Region trên 1 account AWS

&nbsp;	+ Mục đích chính sử dụng VPC thường dùng để phân tách các môi trường (Production/Dev/Test/Staging)

* SUBNET: được chia ra từ AWS VPC thành các mạng con

&nbsp;	+ Mỗi một VPC Subnet này sẽ nằm trong 1 AZ cụ thể nào đó

&nbsp;	+ Không gian mạng của Subnet bắt buộc phải là tập hơn con của VPC CIDR

&nbsp;	+ Trong mỗi Subnet, AWS sẽ giữa 5 địa chỉ IP:

&nbsp;		+ Ví dụ Subnet có CIDR: 10.10.1.0/24

&nbsp;			+ Địa chỉ network: 10.10.1.0

&nbsp;			+ Địa chỉ broadcast: 10.10.1.255

&nbsp;			+ Địa chỉ cho bộ định tuyến: 10.10.1.1

&nbsp;			+ Địa chỉ cho DNS: 10.10.1.2

&nbsp;			+ Địa chỉ cho tính năng tương lai: 10.10.1.3	

&nbsp;	=> AWS sẽ giữ IP từ 0 - 3 và IP 255, các IP này sẽ không được sử dụng để gán vào máy chủ của ta được



