GIỚI HẠN QUYỀN CỦA USER VỚI IAM PERMISSION BOUNDARY

- Sau khi chúng ta hiểu cách hoạt động của IAM User, Group, Role -> tiếp tục tìm hiểu về IAM Permission Boundary

- IAM PERMISSION BOUNDARY: là một tính năng cao cấp cho phép ta giới hạn quyền tối đa của một User hoặc Group 
	- Giả sử ta áp dụng Permission Boundary chỉ cho phép user EC2Admin quản trị dịch vụ EC2 thì anh ấy sẽ không thể có quyền truy cập trên một dịch vụ nào khác -> cho dù có gán quyền policy cao hơn
	
	- DO ĐÓ, quyền hạn có hiệu lực (effective permissions) của user EC2Admin sẽ bao gồm những quyền được cho phép bởi cả Permission Boundary và chính sách quyền của EC2Admin (identity-based policy)
		=> Cho phép cả 2 của permission boundary + identity-based policy

- TẠI SAO CẦN SỬ DỤNG: 
	- Khi ta trao quyền cho các IAM User, ta chỉ nghĩ rằng CHỈ CẦN XÂY DỰNG POLICY cho user một cách cẩn thận
	- Tuy nhiên khi số lượng user tăng lên và những thay đổi xảy ra một cách liên tục -> ta phải tạo thêm nhiều policy mới -> việc quản trị trở nên phức tạp -> tạo ra các lỗ hổng cho leo thang đặc quyền (privilege escalation)
	
	==> ĐỂ ĐƠN GIẢN HÓA CÔNG TÁC QUẢN LÝ QUYỀN, THAY VÌ TA PHẢI CHỈNH SỬA TỪNG POLICY -> ÁP DỤNG PERMISSION BOUNDARY MỘT CÁCH NHANH CHÓNG VÀ ĐỒNG LOẠT -> HẠN CHẾ LỖ HỔNG PRIVILEGE ESCALATION

01. TẠO POLICY GIỚI HẠN

- Đầu tiên ta sẽ tạo một policy dùng để giới hạn quyền tối đa, trong policy này chúng ta chỉ cho phép người dùng có toàn quyền ec2 trên 1 region chỉ định

02. TẠO IAM USER GIỚI HẠN

- Sau khi tạo policy với giới hạn quyền tối đa trên 1 region thì ta sẽ tạo một IAM User và áp giới hạn quyền lên user đó

==> SAU KHI GÁN POLICY EC2FULLACCESS VÀ KÈM THÊM PERMISSION BOUNDARY -> CHỈ CÓ USER ĐÓ Ở TẠI REGION ĐÓ MỚI ĐƯỢC TẠO EC2 INSTANCES -> ĐỐI VỚI REGION KHÁC THÌ ĐIỀU NÀY KHÔNG HOẠT ĐỘNG
	