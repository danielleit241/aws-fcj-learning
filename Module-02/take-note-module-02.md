### **Module 02: Các dịch vụ mạng trên AWS**

##### 

* Sau khi đã tìm hiểu các khái niệm tổng quan về AWS, ta sẽ bắt đầu vào các dịch vụ mạng trên nền tảng AWS
* Hệ thống mạng (network) là xương sống của bất kì cấu trúc điện toán đám mây nào -> đóng vai trò thiết yếu cho việc kết nối các tài nguyên cũng như các dịch vụ khác nhau trên AWS
* Ta sẽ có nhiều dịch vụ mạng khác nhau để thiết kế cũng như đáp ứng các nhu cầu đa dạng từ cơ bản đến nâng cao
* Các dịch vụ mạng quan trọng nhất trên AWS:



 	+ AMAZON VIRTUAL PRIVATE CLOUD (VPC)

 		+ Đây là một dịch vụ cốt lõi cho phép ta tạo ra một mạng riêng ảo, cô lập khỏi các mạng riêng khác

 		+ Ta sẽ khám phá và thiết lập các VPC, Subnet, định tuyến... và các dịch vụ tường lửa đi kèm



 	+ VPC PEERING \& TRANSIT GATEWAY

 		+ Khi ta có nhiều VPC thì việc kết nối chúng lại với nhau là quan trọng

 		+ VPC Peering cho phép ta kết nối 2 VPC và Transit Gateway giải pháp cho ta kết nối số lượng lớn VPC một cách dễ dàng và hiệu quả



 	+ VPN \& DIRECT CONNECT

 		+ Ngoài việc kết nối giữa các VPC thì ta cũng cần kết nối các môi trường AWS với các Data center nằm ở local (on premise)

 

 	+ ELASTIC LOAD BALANCING

 		+ Dịch vụ đóng vai trò phân phối lượng truy cập (hay còn gọi là CÂN BẰNG TẢI) trên nhiều máy chủ

 		+ ELB đóng vai tròn quan trọng trong khả năng chịu lỗi - đảm bảo khả năng mở rộng cho ứng dụng của ta

##### 

##### 01\. AWS Virtual Private Cloud (VPC)

* Là một dịch vụ cung cấp môi trường mạng ảo riêng tư, được cô lập logic khỏi các mạng khác trên AWS cloud
* VPC cho phép khởi tạo các tài nguyên trên AWS như: cân bằng tải, cơ sở dữ liệu ... -> trong môi trường mạng ảo riêng mà chúng ta có quyền kiểm soát hoàn toàn
* VPC trên AWS khác hoàn toàn với khái niệm private cloud truyền thống

 	+ private cloud truyền thống được hiểu là các doanh nghiệp, họ sẽ xây dựng một hệ thống ảo hóa chung trên môi trường on premise với các tính năng mô phỏng theo các nhà cung cấp dịch vụ cloud lớn

 	+ Amazon VPC: cho phép khỏi tạo các tài nguyên AWS vào một mạng ảo mà ta đã xác định



* VPC sẽ bao quát nhiều Availability Zone để có thể chạy máy chủ ảo trên nhiều AZ khác nhau -> triển khai trên multi AZ (đảm bảo độ sẵn sàng cao)
* VPC sẽ nằm trong 1 Region, khi tạo VPC cần khai báo 1 lớp mạng CIDR IPv4 (bắt buộc) và IPv6 (tùy chọn)

 	+ Giới hạn của VPC hiện tại là 5 VPC trên 1 AWS Region trên 1 account AWS

 	+ Mục đích chính sử dụng VPC thường dùng để phân tách các môi trường (Production/Dev/Test/Staging)



* SUBNET: được chia ra từ AWS VPC thành các mạng con

 	+ Mỗi một VPC Subnet này sẽ nằm trong 1 AZ cụ thể nào đó

 	+ Không gian mạng của Subnet bắt buộc phải là tập hơn con của VPC CIDR

 	+ Trong mỗi Subnet, AWS sẽ giữa 5 địa chỉ IP:

 		+ Ví dụ Subnet có CIDR: 10.10.1.0/24

 			+ Địa chỉ network: 10.10.1.0

 			+ Địa chỉ broadcast: 10.10.1.255

 			+ Địa chỉ cho bộ định tuyến: 10.10.1.1

 			+ Địa chỉ cho DNS: 10.10.1.2

 			+ Địa chỉ cho tính năng tương lai: 10.10.1.3

 	=> AWS sẽ giữ IP từ 0 - 3 và IP 255, các IP này sẽ không được sử dụng để gán vào máy chủ của ta được



* Public Subnet | Private Subnet

&nbsp;	+ Public Subnet và Private Subnet bản chất giống như nhau

&nbsp;	+ Nếu đặt tên 1 subnet là Public Subnet và cấu hình nó như 1 public subnet thì những tài nguyên và máy chủ ảo có quyền được ra ngoài Internet (QUY ƯỚC)

&nbsp;	

* ROUTE TABLE (BẢNG ĐỊNH TUYẾN):

&nbsp;	+ Tập hợn các Route, để xác định đường đi cho mạng

&nbsp;	+ Khi tạo VPC, AWS sẽ tại ra Default Route table -> bảng này không thể bị xóa -> chỉ chứa 1 Route duy nhất là Route cho phép tất cả các Subnet trong VPC liên lạc với nhau

&nbsp;	+ Route table sẽ được gán vào Subnet

&nbsp;	+ Ta có thể tạo custom route table nhưng không thể xóa default route (VPC CIDR - Local)

&nbsp;		+ Custom route table -> tạo được Public subnet

&nbsp;	

* ELASTIC NETWORK INTERFACE (ENI):

&nbsp;	+ Mỗi một máy chủ ảo tương ứng với một địa chỉ IP -> không trực tiếp gán vào tài nguyên máy chủ -> gắn vào các card mạng -> ENI -> Được AWS gán một cách tự động (tạo máy chủ ảo -> gán vào ENI)

&nbsp;	+ Là một card mạng ảo -> có thể chuyển sang các EC2 Instance khác

&nbsp;	+ Chúng ta có thể thay đổi máy chủ tùy chỉnh mà card mạng ảo này vẫn được duy trì (IP Private, Elastic IP address, MAC)

&nbsp;		+ Elastic IP address: là một địa chỉ public IPv4 tĩnh, có thể liên kết với một ENI -> và địa chỉ IP này được tính phí -> không thay đổi khi máy chủ ảo restart



* VPC Endpoint:

&nbsp;	+ Cho phép chúng ta kiết nối các tài nguyên nằm trong VPC tới các dịch vụ AWS mà không cần kết nối internet (vì thông qua mạng private nội bộ của AWS - AWS private link)



&nbsp;	+ Interface Endpoint: Sử dụng một Elastic network interface trong VPC cùng 1 IP private để kết nối

&nbsp;	+ Gateway Endpoint: Sử dụng một rout table để đinh tuyến tới endpoint của dịch vụ (S3 và Dynamo DB)



&nbsp;	- Việc kết nối các dịch vụ từ VPC ra ngoài internet thông qua địa chỉ public -> từ VPC --- S3 -> tính chi phí và tốc độ sẽ chậm

&nbsp;	- AWS mới tạo ra S3 - VPC Gateway Endpoint đi qua mạng VPC và kết nối thông qua địa chỉ private



* Internet Gateway: 

&nbsp;	- Nếu ta muốn một máy chủ từ public subnet ra ngoài internet bằng địa chỉ IP public -> tuy nhiên việc gán đó chưa đủ điều kiện

&nbsp;		-> ta cần thực việt tạo ra một Internet Router - Internet Gateway có khả năng mở rộng máy chủ theo chiều ngang (scale out) có thể truyền thông tin ra ngoài Internet

&nbsp;	- IG được quản lý bởi AWS cho nên ta không cần cấu hình network

&nbsp;	

&nbsp;	- YÊU CẦU RA NGOÀI INTERNET PHẢI ĐÁP ỨNG CÁC YÊU CẦU SAU:

&nbsp;		+ ĐỊA CHỈ IP PUBLIC

&nbsp;		+ ROUTE TABLE PHẢI CÓ TARGET DẪN TỚI INTERNET GATEWAY TRONG VPC



* TRONG THỰC TẾ TA SẼ ĐỂ MÁY CHỦ ẢO Ở TRONG MÔI TRƯỜNG PRIVATE SUBNET THAY VÌ PUBLIC SUBNET -> NHƯNG LẠI MUỐN MÁY CHỦ RA NGOÀI ĐƯỢC INTERNET THÌ TA SẼ LÀM NHƯ SAU:

&nbsp;	- NAT GATEWAY: CHO PHÉP MÁY CHỦ TRONG SUBNET TRUY CẬP TỚI INTERNET HOẶC CÁC DỊCH VỤ AWS KHÁC

&nbsp;		=> CHỈ CHẤP NHẬN KẾT NỐI CHIỀU RA CHỨ KHÔNG CHẤP NHẬN CHIỀU VÀO

&nbsp;			- TỪ MÁY CHỦ ->>>> INTERNET : OK

&nbsp;			- TỪ INTERNET ->>>> MÁY CHỦ : KHÔNG ĐƯỢC



&nbsp;		+ NAT GATEWAY SẼ NẰM TRONG PUBLIC SUBNET !!!

&nbsp;			-> TẠO CUSTOM ROUTE TABLE -> CẤU HÌNH ROUTE ENDTRY MỚI CHỈ ĐƯỜNG TỚI NAT GATEWAY (THÔNG QUA ID)

&nbsp;			-> TỪ PUBLIC SUBNET KẾT NỐI VỚI INTERNET GATEWAY -> RA NGOÀI INTERNET



&nbsp;	EC2 ---------> NAT GATEWAY ---------> INTERNET GATEWAY ----------> INTERNET



&nbsp;	- ĐA PHẦN MÁY CHỦ SẼ NẰM Ở PRIVATE SUBNET

&nbsp;		+ CẦN DOWNLOAD CÁC BẢN VÁ 

&nbsp;		+ CẦN GỌI API TỪ BÊN NGOÀI (GỌI GIÁ VÀNG...)

&nbsp;		- TUY NHIÊN NGƯỜI DÙNG BÊN NGOÀI INTERNET KHÔNG THỂ KẾT NỐI VÀO ĐƯỢC MÁY CHỦ ẢO NÀY

