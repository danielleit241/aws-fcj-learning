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

 	+ Public Subnet và Private Subnet bản chất giống như nhau

 	+ Nếu đặt tên 1 subnet là Public Subnet và cấu hình nó như 1 public subnet thì những tài nguyên và máy chủ ảo có quyền được ra ngoài Internet (QUY ƯỚC)

 

* ROUTE TABLE (BẢNG ĐỊNH TUYẾN):

 	+ Tập hợn các Route, để xác định đường đi cho mạng

 	+ Khi tạo VPC, AWS sẽ tại ra Default Route table -> bảng này không thể bị xóa -> chỉ chứa 1 Route duy nhất là Route cho phép tất cả các Subnet trong VPC liên lạc với nhau

 	+ Route table sẽ được gán vào Subnet

 	+ Ta có thể tạo custom route table nhưng không thể xóa default route (VPC CIDR - Local)

 		+ Custom route table -> tạo được Public subnet

 

* ELASTIC NETWORK INTERFACE (ENI):

 	+ Mỗi một máy chủ ảo tương ứng với một địa chỉ IP -> không trực tiếp gán vào tài nguyên máy chủ -> gắn vào các card mạng -> ENI -> Được AWS gán một cách tự động (tạo máy chủ ảo -> gán vào ENI)

 	+ Là một card mạng ảo -> có thể chuyển sang các EC2 Instance khác

 	+ Chúng ta có thể thay đổi máy chủ tùy chỉnh mà card mạng ảo này vẫn được duy trì (IP Private, Elastic IP address, MAC)

 		+ Elastic IP address: là một địa chỉ public IPv4 tĩnh, có thể liên kết với một ENI -> và địa chỉ IP này được tính phí -> không thay đổi khi máy chủ ảo restart



* VPC Endpoint:

 	+ Cho phép chúng ta kiết nối các tài nguyên nằm trong VPC tới các dịch vụ AWS mà không cần kết nối internet (vì thông qua mạng private nội bộ của AWS - AWS private link)



 	+ Interface Endpoint: Sử dụng một Elastic network interface trong VPC cùng 1 IP private để kết nối

 	+ Gateway Endpoint: Sử dụng một rout table để đinh tuyến tới endpoint của dịch vụ (S3 và Dynamo DB)



 	- Việc kết nối các dịch vụ từ VPC ra ngoài internet thông qua địa chỉ public -> từ VPC --- S3 -> tính chi phí và tốc độ sẽ chậm

 	- AWS mới tạo ra S3 - VPC Gateway Endpoint đi qua mạng VPC và kết nối thông qua địa chỉ private



* Internet Gateway:

 	- Nếu ta muốn một máy chủ từ public subnet ra ngoài internet bằng địa chỉ IP public -> tuy nhiên việc gán đó chưa đủ điều kiện

 		-> ta cần thực việt tạo ra một Internet Router - Internet Gateway có khả năng mở rộng máy chủ theo chiều ngang (scale out) có thể truyền thông tin ra ngoài Internet

 	- IG được quản lý bởi AWS cho nên ta không cần cấu hình network

 

 	- YÊU CẦU RA NGOÀI INTERNET PHẢI ĐÁP ỨNG CÁC YÊU CẦU SAU:

 		+ ĐỊA CHỈ IP PUBLIC

 		+ ROUTE TABLE PHẢI CÓ TARGET DẪN TỚI INTERNET GATEWAY TRONG VPC



* TRONG THỰC TẾ TA SẼ ĐỂ MÁY CHỦ ẢO Ở TRONG MÔI TRƯỜNG PRIVATE SUBNET THAY VÌ PUBLIC SUBNET -> NHƯNG LẠI MUỐN MÁY CHỦ RA NGOÀI ĐƯỢC INTERNET THÌ TA SẼ LÀM NHƯ SAU:

 	- NAT GATEWAY: CHO PHÉP MÁY CHỦ TRONG SUBNET TRUY CẬP TỚI INTERNET HOẶC CÁC DỊCH VỤ AWS KHÁC

 		=> CHỈ CHẤP NHẬN KẾT NỐI CHIỀU RA CHỨ KHÔNG CHẤP NHẬN CHIỀU VÀO

 			- TỪ MÁY CHỦ ->>>> INTERNET : OK

 			- TỪ INTERNET ->>>> MÁY CHỦ : KHÔNG ĐƯỢC



 		+ NAT GATEWAY SẼ NẰM TRONG PUBLIC SUBNET !!!

 			-> TẠO CUSTOM ROUTE TABLE -> CẤU HÌNH ROUTE ENDTRY MỚI CHỈ ĐƯỜNG TỚI NAT GATEWAY (THÔNG QUA ID)

 			-> TỪ PUBLIC SUBNET KẾT NỐI VỚI INTERNET GATEWAY -> RA NGOÀI INTERNET



 	EC2 ---------> NAT GATEWAY ---------> INTERNET GATEWAY ----------> INTERNET



 	- ĐA PHẦN MÁY CHỦ SẼ NẰM Ở PRIVATE SUBNET

 		+ CẦN DOWNLOAD CÁC BẢN VÁ

 		+ CẦN GỌI API TỪ BÊN NGOÀI (GỌI GIÁ VÀNG...)

 		- TUY NHIÊN NGƯỜI DÙNG BÊN NGOÀI INTERNET KHÔNG THỂ KẾT NỐI VÀO ĐƯỢC MÁY CHỦ ẢO NÀY



##### 02\. VPC SECURITY \& MULTI-VPC FEATURES

* Các máy chủ trong cùng 1 VPC có thể kết nối với nhau

 	- Ví dụ: ta có máy chủ ở public subnet và muốn kết nối tới máy chủ ở private subnet



* SECURITY GROUP:

 	- Là một tường lửa ảo có lưu giữ trạng thái (stateful) giúp ta dễ dàng kiểm soát lưu lượng truy cập đến và đi trong các tài nguyên AWS

 	- SG có thể hạn chế theo giao thức, địa chỉ nguồn, cổng kết nối, hoặc một SG khác

 	- SG rule chỉ cho phép rule allow

 	- SG sẽ được áp dụng lên các Elastic Network Interface -> Không áp dụng lên các Subnet



 	- MẶC ĐỊNH SG SẼ CHẶN MỌI TRUY CẬP ĐẾN VÀ CHO PHÉP MỌI TRUY CẬP ĐI



* NETWORK ACCESS CONTROL LIST (NACL)

 	- Là một tường lửa không lưu giữ trạng thái (stateless) giúp kiểm soát lưu lượng truy cập đến và đi trong tài nguyên AWS

 		+ Cần phải cấu hình firewall rule cả chiều đến lẫn chiều đi

 		+ Cần phải nghiên cứu kĩ cấu hình đi vào port nào và đi ra port nào

 	- NACL được hạn chế theo giao thức, địa chỉ nguồn, cổng kết nối

 	- NACL được áp dụng lên các Amazon VPC Subnet

 		+ Mức áp dụng của NACL khác với SG -> tác dụng lên các Subnets -> có thể gây ảnh hưởng tới nhiều máy chủ cùng 1 lúc

 	- Mặc định NACL cho phép mọi truy cập đến và đi

 	- Nguyên tắc đọc rule từ trên xuống dưới -> thỏa rule nào thì lấy rule đó



==> Ta sẽ có 2 tường lửa

 	1: Apply vào các card mạng ảo (Elastic Network Interface)

 	2: Apply ở mức subnet



* VPC Flow Logs:

 	- Là một tính năng cho phép ta nắm bắt thông tin về lưu lượng IP đến và đi từ các giao diện mạng trong VPC -> Từ card mạng này đến card mạng khác

 	- Tập tin logs này có thể xuất bản lên Amazon CloudWatch Logs hoặc S3

 	- VPC Flow Logs không capture được nội dung của gói tin

 	- Chỉ có 1 số thông tin sau:

 		+ Account ID

 		+ ENI ID

 		+ Source IP

 		...

 	=> Thông qua VPC Flow Logs này kiểm tra xem các access này có bị từ chối hay không, detect ra được những bất thường...



* VPC Peering

 	- Là tính năng giúp kết nối hai hay nhiều VPC để các tài nguyên bên trong hai hay nhiều VPC có thể liên lạc trực tiếp với nhau không cần thông qua Internet -> tăng cường bảo mật cho các VPC

 	- VPC Peering là kết nối 1 : 1 giữa 2 VPC thành viên

 	  không hỗ trợ transitive routing

 	- VPC Peering không hỗ trợ 2 VPC bị overlap IP address space

 	- VPC kết nối với nhau thông qua IP Private, thông qua Peering connection và phải cấu hình route table thủ công

 		+ Nếu chỉ muốn 1 subnet trong VPC thì chỉ kết nối địa chỉ IP của subnet đó

 		+ Nếu muốn kết nối luôn cả VPC thì kết nối IP của VPC đó



\- TUY NHIÊN TRONG THỰC TẾ CÓ RẤT NHIỀU VPC VÀ PEERING => TỐN RẤT NHIỀU CÔNG SỨC ĐỂ CẤU HÌNH CÁC PEERING CONNECTIONS

 	+ VÍ DỤ: 30 VPC = 435 PC



* TRANSIT GATEWAY

 	- Được dùng để kết nối các VPC vào mạng on-premises thông qua một hub trung tâm

 	- Điều này đơn giản hóa mạng và kết thúc các mối quuan hệ định tuyến phức tạp

 	-> ĐƠN GIẢN HÓA MÔ HÌNH MẠNG, GIẢM BỚT PHỨC TẠP TRONG CẤU HÌNH ROUTE TABLE

 

 	- TRANSIT GATEWAY ATTACHMENT là một công cụ để gán các subnet của từng VPC cần kết nối với nhau vào Transit Gateway đã được khỏi tạo

 		-> Transit Gateway Attachment hoạt động ở quy mô AZ

 	- Trong VPC khi một subnet ở một AZ có TGA với một TGW -> các subnet khác trong cùng AZ đều có thể kết nối tới TGW đó



 	=> CŨNG TƯƠNG TỰ NHƯ PEERING CONNECTION CŨNG CẦN PHẢI CẤU HÌNH BẢNG ĐỊNH TUYẾN (ROUTE TABLE) ĐẾN IP CỦA TGW

 	   VÀ CŨNG PHẢI CẤU HÌNH BẢNG ĐỊNH TUYẾN CỦA TGW ĐẾN TỪNG CÁC TWA TƯƠNG ỨNG



##### 03\. VPN - DirectConnect - LoadBalancer - ExtraResources



* Các tính năng giúp hỗ trợ kết nối giữa môi trường on-premise và môi trường cloud với nhau (hay còn gọi là hybird)



* VPN SITE TO SITE

&nbsp;	- Kết nối toàn bộ site on premise và kết nối với môi trường VPC của AWS (thông qua VPN site to site)

&nbsp;	- Việc kết nối cần 2 đầu endpoint ở phía AWS và phía khách hàng

&nbsp;		+ VIRTUAL PRIVATE GATEWAY: được quản lý hoàn toàn bởi AWS (chia làm 2 endpoints ở 2 đầu AZ)

&nbsp;		+ CUSTOMER GATEWAY: đầu endpoint phía khách hàng có thể là thiết bị phần cứng hoặc application 

&nbsp;	

* VPN CLIENT TO SIDE

&nbsp;	- THỰC TẾ CHI PHI RẤT CAO

&nbsp;	- NẾU MUỐN DÙNG DỊCH VỤ VPN CTS -> THÌ NÊN DÙNG THIRD PARTY

&nbsp;	- VPN CTS SẼ TÍNH TIỀN THEO GIỜ



* DIRECT CONNECT

&nbsp;	- LÀ DỊCH VỤ CHO PHÉP TẠO KẾT NỐI RIÊNG CHO TỪNG DATA CENTER ON PREMISE TỚI AWS

&nbsp;	- ĐỘ TRỄ ỔN ĐỊNH VÀ CHẤT LƯỢNG ĐƯỜNG TRUYỀN ỔN ĐỊNH

&nbsp;		+ 20MS - 30MS

&nbsp;		+ TẤT CẢ CÁC KẾT NỐI TỪ VIỆT NAM -> ĐỀU PHẢI THÔNG QUA DIRECT PARNERS (VIETTEL, FPT, ...) -> HOẠT ĐỘNG DƯỚI DẠNG HOSTED CONNECTIONS (NẾU TỪ AWS SẼ LÀ ĐEICATED CONNECTIONS)

&nbsp;			+ HOSTED CONNECTIONS: có thể thay đổi băng thông lên xuống theo nhu cầu của khách hàng

&nbsp;	- Không thực hiện mã hóa dữ liệu (vẫn phải cần VPN site to site để kết nối)



* ELASTIC LOAD BALANCING:

&nbsp;	- Là một dịch vụ cân bằng tải được quản lý bởi AWS, có chức năng phân phối lưu lượng cho nhiều EC2 Instance hoặc Container

&nbsp;	- Sử dụng giao thức HTTP, HTTPs, TCP, SSL (TPC bảo mật)

&nbsp;	- Có thể nằm ở public hoặc private subnet

&nbsp;		+ Làm lab: ở public subnet -> nhận request của người dùng 

&nbsp;		+ Tuy nhiên ta có thể đặt ở private subnet

&nbsp;	- Mỗi Elastic Load Balancing sẽ được cấp tên DNS và kết nối thông qua DNS

&nbsp;		+ Chỉ kết nối qua tên DNS

&nbsp;		+ Dùng Network Load Balancer hỗ trợ gán IP tĩnh



&nbsp;	- Elastic Load Balancing có tính năng heath check, không gửi lưu lượng đến các Instance không đạt heath check

&nbsp;	

&nbsp;	- Có 4 loại Load Balancer:

&nbsp;		+ Application Load Balancer 

&nbsp;		+ Network Load Balancer

&nbsp;		+ Classic Load Balancer

&nbsp;		+ Gateway Load Balancer

&nbsp;		=> Chỉ có Network load balancer dùng địa chỉ IP để kết nối, còn tất cả các load balancer còn lại đều dùng tên DNS



&nbsp;	- CÁC ĐẶC TÍNH CỦA LOAD BALANCER:

&nbsp;		+ STICKY SESSION (SESSION AFINITY): TÍNH NĂNG CHO PHÉP CÁC KẾT NỐI ĐƯỢC GÁN VÀO MỘT TARGET NHẤT ĐỊNH

&nbsp;			-> ĐẢM BẢO YÊU CẦU TỪ USER TRONG MỘT SESSION SẼ ĐƯỢC GỬI TỚI CÙNG 1 TARGET

&nbsp;			=> CẦN THIẾT TRONG TRƯỜNG HỢP CÁC MÁY CHỦ ỨNG DỤNG LƯU TRỮ THÔNG TIN VÀ TRẠNG THÁI CỦA NGƯỜI DÙNG TẠI SERVER ĐÓ

&nbsp;		+ LƯU TRỮ LOGS TRUY CẬP (ACCESS LOGS) -> DÙNG ĐỂ PHÂN TÍCH TRUY CẬP, TROUBLE SHOOT

&nbsp;			=> LOGS TRUY CẬP SẼ LƯU VÀO DỊCH VỤ LƯU TRỮ OBJET LÀ AMAZON S3 (SIMPLE STORAGE SERVICE)



&nbsp;	- APPLICATION LOAD BALANCER:

&nbsp;		+ LÀ MỘT DỊCH VỤ CÂN BẰNG TẢI ĐƯỢC QUẢN LÝ BỞI AWS HOẠT ĐỘNG Ở LAYER 7 (APPLICATIONS)

&nbsp;		+ SỬ DỤNG CÁC GIAO THỨC HTTP, HTTPS

&nbsp;		+ TÍNH NĂNG: PATH-BASED ROUTING

&nbsp;			+ NẾU NGƯỜI DÙNG MOBILE -> /MOBILE

&nbsp;				 	DESKTOP -> /DESKTOP

&nbsp;			-> ROUTE ĐƯỢC TỚI 2 TARGET GROUP KHÁC NHAU -> HIỂU LÀ MÁY CHỦ XỬ LÝ YÊU CẦU CỦA NGƯỜI DÙNG

&nbsp;		+ CHO PHÉP ROUTE TRAFFIC TỚI CÁC TARGET NẰM NGOÀI VPC (IP ADDRESS), EC2, LAMBDA, CONTAINER



&nbsp;	- NETWORK LOAD BALANCER:

&nbsp;		+ LÀ MỘT DỊCH VỤ QUẢN LÝ HOÀN TOÀN BỞI AWS, HOẠT ĐỘNG Ở LAYER 4 (TRANSPORT)

&nbsp;		+ SỬ DỤNG GIAO THỨC TCP, TLS

&nbsp;		+ HỖ TRỢ TÍNH NĂNG SET IP TĨNH

&nbsp;		+ HỖ TRỢ HIỆU NĂNG CAO NHẤT TRONG CÁC LOẠI LOAD BALANCER CÓ KHẢ NĂNG XỬ LÝ LÊN ĐẾN HÀNG TRIỆU REQUEST

&nbsp;		+ CHO PHÉP ROUTE TRAFFIC TỚI TARGET NẰM NGOÀI VPC, EC2, CONTAINER



&nbsp;	- CLASSIC LOAD BALANCER (CLB):

&nbsp;		+ LÀ MỘT DỊCH VỤ CÂN BẰNG TẢI ĐƯỢC QUẢN LÝ BỞI AWS, HOẠT ĐỘNG Ở LAYER 4 VÀ LAYER 7

&nbsp;		+ KẾT HỢP CỦA APPLICATION VÀ NETWORK LOAD BALANCER



&nbsp;	- GATEWAY LOAD BALANCER (GLB):

&nbsp;		+ LÀ MỘT DỊCH VỤ CÂN BẰNG TẢI ĐƯỢC QUẢN LÝ BỞI AWS, HOẠT ĐỘNG Ở LAYER 3

&nbsp;		+ LẮNG NGHE TOÀN BỘ IP PACKETS VÀ FORWARD TỚI TARGET GROUP ĐÃ ĐƯỢC CHỈ ĐỊNH

&nbsp;		+ SỬ DỤNG GENEVE PROTOCOL TRÊN PORT 6081

&nbsp;		+ CHO PHÉP ROUTE TRAFFIC TỚI CÁC VIRTUAL APPLIANCE ĐƯỢC AWS HỖ TRỢ

