* LAB 02-01: CREATE VPC

1. GIỚI THIỆU AMAZON VPC
	- Dịch vụ mạng ảo tùy chỉnh nằm trong AWS Cloud -> cho phép tạo môi trường riêng biệt 
	- Tính năng:
		+ Kiểm soát 
		+ Khởi tạo và quản lý tài nguyên AWS
		+ Tùy chỉ IP và phân đoạn mạng
		+ Cấu hình định tuyến
		+ Hỗ trợ IPv4 và IPv6

	- VPC có thể tạo nhiều trong 1 Region
		-> Mỗi VPC được định danh bằng dải địa chỉ IP riêng
	
		+ Cấu hình: 
			- Sử dụng Classless Inter-Domain Routing (CIDR) 
			- Phạm vi từ /16 (65k đchi) đến /28 (16 đchi)
			- CIDR ko thể thay đổi khi tạo
			
	
2. TƯỜNG LỬA TRONG VPC - DONE
3. THỰC HÀNH TẠO 1 VPC - DONE
4. CẤU HÌNH VPN SITE TO SITE - NOT YET

* LAB 02-02: SESSION MANAGER

1. CHUẨN BỊ
	- Session manager là một chức năng nằm trong dịch vụ Sytem Manager của AWS -> quản lý các máy chủ một cách an toàn không cần mở port SSH, không cần bastion host hoặc quản lý SSH key.
	
2. TẠO KẾT NỐI ĐẾN MÁY CHỦ EC2
3. QUẢN LÝ SESSION LOGS
4. PORT FORWARDING

* LAB 02-03: SETTING VPC PEERING

1. CHUẨN BỊ
2. CẬP NHẬT NETWORK ACL
3. KẾT NỐI PEERING
4. CẤU HÌNH ROUTE TABLES
5. KÍCH HOẠT CROSS-PEER DNS


* LAB 02-04: SETTING TRANSIT GATEWAY

1. THIẾT LẬP HẠ TẦNG
2. TẠO TRANSIT GATEWAY
3. TRANSIT GATEWAY ATTACHMENTS
4. TẠO ROUTE TABLE CHO TGW
5. THÊM GATEWAY VÀO ROUTE TABLES
6. KIỂM TRA KẾT QUẢ

* LAB 02-05: HYBIRD DNS

1. THIẾT LẬP HYBIRD DNS
2. TẠO OUTBOUND ENDPOINT
3. TẠO ROUTE 53 RESOLVER RULE
4. TẠO INBOUND ENDPOINT

===============================================
NGUYÊN CỨU BỔ SUNG: AWS ADVANCE NETWORKING - SPECIALTY STUDY GUIDE

- TÀI LIỆU GIÚP CHUẨN BỊ KIẾN THỨC CHO BÀI THÌ AWS ADVANCE NETWORKING - SPECIALTY
- ĐÁNH GIÁ CỦA CHUYÊN GIA VỀ CÁC NGUYÊN TẮC THIẾT KẾ CỦA AWS PHÙ HỢP VỚI MỤC TIÊU THI VÀ GIẢI THÍCH CHI TIẾT VỀ CÁC CHỦ ĐỀ THI CHÍNH KẾT HỢP VỚI CÁC KỊCH BẢN TRONG THỰC TẾ
