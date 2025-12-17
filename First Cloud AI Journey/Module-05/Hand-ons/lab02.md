QUẢN TRỊ QUYỀN TRUY CẬP VỚI AWS IDENTITY AND ACCESS MANAGEMENT (IAM)

- MỤC TIÊU TRONG BÀI LAB NÀY:
	- 1. THIẾT LẬP CẤU TRÚC:
		+ TẠO VÀ QUẢN LÝ IAM GROUPS ĐỂ TỔ CHỨC USER
		+ ÁP DỤNG IAM POLICIES ĐỂ PHẦN QUYỀN
		+ QUẢN LÝ IAM USERS THEO NHÓM

	- 2. TRIỂN KHAI BẢO MẬT CAO VỚI IAM ROLES:
		+ SỬ DỤNG IAM ROLES THAY VÌ CẤP QUYỀN TRỰC TIẾP
		+ THIẾT LẬP CƠ CHẾ TRUY CẬP TẠM THỜI
		+ ÁP DỤNG NGUYÊN TẮC QUYỀN TỐI THIỂU


I. GIỚI THIỆU

- IAM LÀ DỊCH VỤ QUẢN LÝ QUYỀN TRUY CẬP TẬP TRUNG CỦA AWS CHO PHÉP:
	+ KIỂM SOÁT CHI TIẾT QUYỀN TRUY CẬP VÀO TÀI NGUYÊN AWS
	+ QUẢN LÝ NGƯỜI DÙNG, NHÓM VÀ VAI TRÒ 1 CÁCH AN TOÀN
	+ TRIỂN KHAI CÁC CHÍNH SÁCH BẢO MẬT THEO TIÊU CHUẨN DOANH NGHIỆP

=> LUÔN TUÂN THỦ THEO NGUYÊN TẮC "QUYỀN TỐI THIỂU" KHI CẤP QUYỀN TRUY CẬP TRONG IAM


- TẠO IAM GROUP VÀ IAM USER:
	+ IAM Groups: nhóm quản lý tập trung các người dùng
		+ Chứa nhiều IAM Users
		+ Được gán các IAM Policy để phân quyền
		+ Tự động áp dụng quyền cho thành viên
		
	+ IAM Users: tài khoản người dùng cá nhân hoặc ứng dụng
		+ Root user: tài khoản quản trị cao nhất, được tạo khi đăng kí AWS Account
		+ IAM User: tài khoản thông thường với quyền hạn được cấp phát
	=> HẠN CHẾ SỬ DỤNG ROOT USER CHO CÁC TÁC VỤ HẰNG NGÀY, THAY VÀO ĐÓ TẠO CÁC IAM USER RIÊNG BIỆT VỚI QUYỀN HẠN PHÙ HỢP

- IAM POLICY:
	- Là tài liệu định nghĩa quyền truy cập chi tiết trong AWS và có thể gán cho Groups, Users, Roles
	- Cấu trúc và phạm vi:
		+ Effect: cho phép (allow) hoặc từ chối (deny) quyền
		+ Action: các hành động được cho phép truy cập quyền
		+ Resource: tài nguyên AWS được áp dụng
		+ Condition: điều kiện bổ sung (nếu có)

- IAM ROLES:
	- Là cơ chế phân quyền linh hoạt trong AWS cho phép cấp quyền truy cập TẠM THỜI cho:
		+ Users, cross-account
		+ AWS Services, external services

	- Có các đặc điểm quan trọng:
		+ Không có thông tin truy cập cố định
		+ Cung cấp quyền truy cập tạm thời có thời hạn
		+ Tự động luân chuyển credentials
		+ Yêu cầu trust policy để xác định ai có thể assume role

	=> Sử dụng IAM Role thay vì gán quyền trực tiếp
		-> Tăng cường bảo mật thông qua quyền tạm thời
		-> Đơn giản hóa quản lý các quyền truy cập
		-> Tuân thủ nguyên tắc đặc quyền tối thiểu

II. TẠO IAM GROUP VÀ IAM USER

- TRONG PHẦN NÀY, TA SẼ THIẾT LẬP VÀ QUẢN LÝ QUYỀN QUẢN TRỊ VIÊN TRONG AWS THEO BEST PRACTICES

- CÁC BƯỚC CHÍNH:
	- 1. TẠO IAM ADMIN GROUP
		+ THIẾT LẬP NHÓM VỚI QUYỀN AdministratorAccess
		+ ÁP DỤNG CÁC CHÍNH SÁCH BẢO MẬT PHÙ HỢP
		
	- 2. TẠO IAM ADMIN USER
		+ TẠO USER VỚI THÔNG TIN XÁC THỰC AN TOÀN
		+ THÊM USER VÀO ADMIN GROUP
		+ THIẾT LẬP CÁC YÊU CẦU MẬT KHẨU MẠNH

	- 3. THIẾT LẬP BẢO MẬT NÂNG CAO
		+ KÍCH HOẠT MFA
		+ CẤU HÌNH CHÍNH SÁCH BẢO MẬT
		+ THIẾT LẬP GIÁM SÁT HOẠT ĐỘNG


III. TẠO IAM ROLE VÀ IAM USER

- Security Note:
	- IAM Roles tuân theo nguyên tắc đặc quyền tối thiểu
	- Quyền truy cập được cấp tạm thời và tự động hết hạn
	- Không cần quản lý thông tin xác thực dài hạn
	- Hỗ trợ luân chuyển tự động của thông tin xác thực

- MỤC TIÊU THỰC HÀNH:
	- 1. Tạo IAM Role Admin với policy AdministratorAccess
	- 2. Tạo IAM User OperatorUser
	- 3. Cấu hình cho phép OperatorUser assume IAM Role Admin


IV. CHUYỂN ĐỔI IAM ROLE

- TRONG PHẦN NÀY, TA SẼ HỌC CÁCH SWITCH SANG IAM ROLE ĐÃ ĐƯỢC TẠO TRƯỚC ĐÓ THÔNG QUA TÀI KHOẢN AWS, VIỆC CHUYỂN ĐỔI ROLE CHO PHÉP TA TẠM THỜI NHẬN CÁC QUYỀN ĐƯỢC ĐỊNH NGHĨA TRONG ROLE ĐÓ MÀ KHÔNG CẦN THAY ĐỔI CẤU HÌNH IAM USER GỐC


	

