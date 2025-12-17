IAM ROLE & CONDITION

- Ở BÀI LAB BẮT ĐẦU VỚI IAM CHÚNG TA ĐÃ TẠO IAM USER CÓ QUYỀN ADMIN, TRONG THỰC TẾ CHÚNG TA THƯỜNG CHỈ CẤP QUYỀN VỪA ĐỦ CHO ADMIN (LEAST PRIVILEGE)

- TRONG BÀI NÀY TA SẼ ÔN LẠI KHÁI NIỆM VỀ IAM, SAU ĐÓ TIẾN HÀNH TẠO CÁC USER/GROUP ĐÓNG VÀI TRÒ ADMIN CHO TỪNG DỊCH VỤ EC2, RDS, ...

- TẠO CÁC ROLE VÀ TĂNG CƯỜNG TÍNH BẢO MẬT BẰNG CÁCH ĐẶT THÊM ĐIỀU KIỆN GIỚI HẠN IP, VÀ THỜI GIAN

I. GIỚI THIỆU VỀ IAM

- Định nghĩa: là công cụ để kiểm soát cách con người hoặc chương trình sử dụng hạ tầng của AWS. Vẫn giữ nguyên định nghĩa về xác thực truyền thống như user, group và chính sách kiểm soát truy cập để kiểm soát AWS Account, Service

- ỨNG DỤNG:
	- IAM không có khả năng xác thực đối với ứng dụng, và đối với hệ điều hành
	- Giống như hầu hết các services khác của AWS, IAM có thể điều khiển qua: console, cli, sdk
	- Một số thao tác quan trọng thường làm IAM như: tạo user, group, role, policy

1. REQUEST TỚI AWS SERVICE

- Request: khi một principal cố gắng thực hiện một thao tác sử dụng AWS Console, AWS API hoặc AWS CLI, principal đó sẽ phải gửi đi một request.
 
- Thông tin của request bao gồm:
	+ Action: hành động mà principal muốn thực hiện
	+ Resource: thông tin tài nguyên sẽ bị tác động
	+ Principal: thông tin về người dùng hoặc ứng dụng (bao gồm cả policy đc attach)
	+ Evn Data: thông tin về IP, user agent
	+ Resource data: thông tin liên quan

2. CHỨNG THỰC CÁC REQUEST

- AUTHENTICATION: một principal phải có khả năng xác thực truy cập để có thể gửi request tới AWS
	- Đối với root user: khi login cần thông tin địa chỉ email và password (dài hạn)
	- Đối với IAM User: cần thông tin ID hoặc alias, và user + password tương ứng (dài hạn)
	- Để xác thực IAM user qua AWS API hay CLI chúng ta có thể sử dụng Access key và Secret access key 
		+ Hoặc sử dụng IAM Role và thông tin chứng thực tạm thời (AWS STS)

3. QUÁN TRÌNH ASSUME ROLE

- CÁC QUÁ TRÌNH MỘT IAM USER THỰC HIỆN ASSUME ROLE VÀ LẤY THÔNG TIN CHỨNG THỰC TẠM THỜI:

	- 1. IAM USER SẼ CÓ THÔNG TIN CHỨNG THỰC DÀI HẠN -> REQUEST TỚI AWS STS VÀ THỰC HIỆN ACTION sts:AssumeRole
	- 2. STS SẼ THỰC HIỆN KIỂM RA IAM USER CÓ QUYỀN THỰC HIỆN ACTION NÀY KHÔNG 
	- 3. NẾU THÀNH CÔNG -> THÔNG TIN XÁC THỰC TẠM THỜI
	- 4. IAM USER SẼ SỬ DỤNG THÔNG TIN CHỨNG THỰC TẠM THỜI ĐỂ REQUEST TỚI CÁC DỊCH VỤ AWS THÔNG QUA API


II. TẠO IAM GROUP
	- Tạo một IAM Group có tên: ec2-rds-admin-group
	- Sau đó attach các policies: AmazonEC2FullAccess, AmazonRDSFullAccess và DatabaseAdministrator
	- Create group

III. TẠO IAM USER
	- TA SẼ TẠO LẦN LƯỢT 4 USER:
		+ EC2-admin-user -> dành cho ec2
		+ RDS-admin-user -> dành cho RDS
		+ Group-user -> user gán quyền quản trị
		+ No-permission-user 
	-> SAU KHI TẠO THÀNH CÔNG CÁC USER -> TA SẼ KIỂM TRA BẰNG CÁCH TẠO CÁC SERVICE DỰA TRÊN VAI TRÒ CỦA USER ĐÓ

IV. CẤU HÌNH ROLE CONDITION

- VIỆC SỬ DỤNG ROLE LÀ MỘT PHƯƠNG PHÁP THỰC HÀNH TỐT TRONG HỆ THỐNG AWS. Ở BƯỚC NÀY CHÚNG TA KHÔNG CHỈ CẤU HÌNH CHO PHÉP NGƯỜI DÙNG SỬ DỤNG 1 ROLE CỤ THỂ Ở BẤT CỨ LÚC NÀO MÀ CÒN THÊM VÀO CÁC CONDTION
	-> CHỈ KHI THỎA MÃN ĐIỀU KIỆN VỀ IP HOẶC THỜI GIAN NGƯỜI DÙNG MỚI CÓ THỂ THỰC HIỆN SWITCH ROLE

- 1. TẠO ADMIN IAM ROLE
- 2. CẤU HÌNH SWITCH ROLE CHO PHÉP NO-PERMISSION USER SỬ DỤNG ROLE NÀY
- 3. GIỚI HẠN TRUY CẬP ROLE
	-> MỤC ĐÍCH LÀ SIẾT CHẶT KHẢ NĂNG SỬ DỤNG ROLE ADMIN THEO ĐỊA CHỈ IP VÀ THỜI GIAN

	- GIỚI HẠN IP ĐƯỢC PHÉP SWITCH ROLE
	- GIỚI HẠN THỜI GIAN ĐƯỢC PHÉP SWICTH ROLE