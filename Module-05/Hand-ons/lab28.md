QUẢN LÝ TRUY CẬP VÀO DỊCH VỤ EC2 RESOURCE TAG VỚI AWS IAM

- Trong bài thực hành này ta sẽ quản lý quyền truy cập EC2 với resource tag thông qua cấu hình chi tiết các chính sách và IAM Role với quyền cụ thể.

- Việc sử dụng resource tag sẽ cực kĩ hữu ích khi chúng ta mở rộng trong việc quản trị phi tập trung

- Ta sẽ tạo các chính sách với các role có thể được sử dụng bởi một số người dùng nhất định, chẳng hạn như quản trị viên ec2.
	+ Các chính sách (policy) này sẽ chỉ cho phép quản trị viên EC2 tạo các tài nguyên liên quan khi nó đáp ứng các yêu cầu đã nêu dựa trên một số Resource tag nhất định

- MỤC TIÊU:
	- Áp dụng phương pháp đặc quyền IAM tối thiểu
	- Đặc tả chính sách IAM kèm theo các điều kiện chi tiết (Điều kiện chính sách IAM)

01. CÁC BƯỚC CHUẨN BỊ
- TẠO IAM USER
	- TẠO USER GROUPS VỚI QUYỀN 'AdministratorAccess'
	- TẠO ADMIN USER

02. TẠO IAM POLICY
- Ở phần trước, các policies sẽ được phân thành 5 chức năng khác nhau nếu muốn bạn có thể tùy ý chỉnh sửa và kết hợp chúng để phù hợp với yêu cầu thực tiễn mà mình đang hướng tới

- Các AWS Regions sau đây sẽ được mặc định sử dụng nhằm tăng cường giới hạn hơn nữa đối với Resource tags
	+ us-east-1 (North Virginia)
	+ us-west-1 (North California)

03. TẠO IAM ROLE
- TA SẼ TIẾN HÀNH TẠO IAM ROLE CHO NGƯỜI DÙNG EC2 ADMINSTARTOR CÙNG VỚI NHỮNG POLICIES TA ĐÃ TẠO Ở PHẦN TRƯỚC ĐÓ

	