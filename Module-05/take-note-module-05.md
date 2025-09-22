#### CÁC DỊCH VỤ BẢO MẬT TRÊN AWS



* ĐÂY LÀ MỘT TRONG NHỮNG VẤN ĐỀ AWS ĐẶT LÊN HÀNG ĐẦU, AWS CÓ TRIẾT LÍ "SECURY IS JOB ZERO" -> VIỆC BẢO MẬT LÀ QUAN TRỌNG NHẤT KHI SỬ DỤNG CÁC DỊCH VỤ TRÊN AWS



##### 01\. Share Responsibility Model



* Khi sử dụng dịch vụ của nhà cung cấp điện toán đám mây -> việc bảo mật sẽ là trách nhiệm của nhà cung cấp dịch vụ và khách hàng
* KHÁCH HÀNG sẽ chịu trách nhiệm

&nbsp;	+ Việc cấu hình

&nbsp;	+ Áp dụng các best practices

&nbsp;	+ Sử dụng các dịch vụ đảm bảo việc bảo mật từ mức Hypervisor tới mức dữ liệu/ứng dụng

&nbsp;		+ Mã hóa dữ liệu

&nbsp;		+ Hệ điều hành, mạng, tường lửa

&nbsp;		+ Xác thực

&nbsp;		+ ...

&nbsp;		+ Dữ liệu



&nbsp;	-> Trách nhiệm của khách hàng không có nghĩa là sẽ bắt đầu từ con số 0 

&nbsp;	-> AWS đã cung cấp sẵn một tập các dịch vụ đám ứng nhu cầu bảo mật khác nhau của các tổ chức khác nhau

&nbsp;		-> Vì không nên áp đặt một tiêu chuẩn bảo mật lên tất cả các tổ chức



* AWS sẽ chịu trách nhiệm:

&nbsp;	+ Đảm bảo các phần hạ tầng và các dịch vụ của AWS

&nbsp;		+ Compute 

&nbsp;		+ Storage 

&nbsp;		+ Database 

&nbsp;		+ ...



* TUY NHIÊN MÔ HÌNH CHIA SẺ TRÁCH NHIỆM KHÔNG PHẢI FIXED HOÀN TOÀN KHÁC NHAU GIỮA CÁCH DỊCH VỤ KHÁC NHAU ĐƯỢC CHIA LÀM 3 NHÓM:

&nbsp;	+ Các dịch vụ ở mức hạ tầng	

&nbsp;	+ Các dịch vụ quản lý ở mức kết hợp

&nbsp;	+ Các dịch vụ quản lý hoàn toàn bởi AWS



==> VẤN ĐỀ BẢO MẬT TRÊN AWS SẼ LÀ SỰ CHIA SẺ TRÁCH NHIỆM GIỮA KHÁCH HÀNG VÀ NHÀ CUNG CẤP DỊCH VỤ - VÀ TRÁCH NHIỆM NÀY SẼ KHÁC NHAU DỰA TRÊN CÁC NHÓM DỊCH VỤ 

&nbsp;	-> XU HƯỚNG SẼ CHỌN QUẢN LÝ HOÀN TOÀN BỞI AWS ĐỂ TẬP TRUNG VÀO VIỆC PHÁT TRIỂN ỨNG DỤNG





##### 02\. AMAZON IDENTITY AND ACCESS MANAGEMENT



* DỊCH VỤ QUẢN LÝ ĐỊNH DANH VÀ QUYỀN TRUY CẬP



* ROOT ACCOUNT:

&nbsp;	- THÔNG TIN ĐĂNG KÍ ACCOUNT LÚC BAN ĐẦU

&nbsp;	- TÀI KHOẢN NÀY CÓ TOÀN QUYỀN TRUY CẬP VÀO TẤT CẢ CÁC DỊCH VỤ VÀ TÀI NGUYÊN AWS, VÀ CÓ THỂ GỠ BỎ CÁC CHÍNH SÁCH QUYỀN ĐÃ GÁN VÀO TÀI NGUYÊN



&nbsp;		+ THÔNG TIN PHÍ

&nbsp;		+ DỮ LIỆU CÁ NHÂN

&nbsp;		+ KO BỊ GIỚI HẠN QUYỀN

&nbsp;	

&nbsp;	- BEST PRACTICES:

&nbsp;		+ TẠO VÀ SỬ DỤNG IAM ADMINISTRATOR USER

&nbsp;		+ KHÓA THÔNG TIN XÁC THỰC ROOT USER (CHIA 2 NGƯỜI GIỮ)

&nbsp;		+ ĐẢM BẢO RENEW THÔNG TIN DOMAIN VÀ EMAIL CỦA ROOT USER



* IAM là dịch vụ giúp ta kiểm soát quyền try cập vào các dịch vụ và tài nguyên trong AWS account của mình



* IAM cho phpes tạo nhiều tài khoản người dùng (IAM User) với thông tin xác thực (credintials) và quyền hạn khác nhau



* IAM Principal (chủ thể IAM) là một thực thể có thể thực hiện các hành động trên tài nguyên nhất định trong AWS Account

&nbsp;	- AWS account and root user

&nbsp;	- IAM User

&nbsp;	- Federate users 

&nbsp;	- IAM Roles

&nbsp;	- Assumed-role sessions

&nbsp;	- AWS services

&nbsp;	- Anonymous users (ko khuyến nghị)



* Người dùng IAM (IAM user) không phải là 1 tài khoản AWS riêng biệt

&nbsp;	- IAM User sẽ có mật khẩu riêng để truy cập vào management console hoặc access key/secret key để thực hiện AWS CLI và AWS SDK

&nbsp;	

&nbsp;	- Mặc định IAM User được tạo ra không có quyền gì

&nbsp;	- IAM User ko được dùng để quản lý truy cập vào ứng dụng hay hệ điều hành

&nbsp;	- Để cấp quyền cho IAM User chúng ta phải gán IAM Policy vào IAM User

&nbsp;	- Để quản lý các User dễ dàng thì ta có thể gom vào thành 1 IAM Group

&nbsp;	- IAM Group không thể là thành viên của 1 group khác



* IAM POLICY được viết dưới dạng JSON:

&nbsp;	- IAM Policy có 2 loại:

&nbsp;		+ Identity based Policy gán với 1 IAM Principal

&nbsp;		+ Resource based Policy gán với 1 AWS Resource



&nbsp;	- CÁCH THỨC TÍNH QUYỀN CỦA IAM LUÔN ƯU TIÊN DENY SO VỚI ALLOW



* IAM ROLE 

&nbsp;	- Cho phép xác định một tập hợp quyền truy cập vào các tài nguyên (thông qua việc gán IAM Policy vào IAM Role)

&nbsp;	- IAM Role không có thông tin chứng thực (Credentials) để truy cập vào management console hay CLI/SDK

&nbsp;	

&nbsp;	- Khi một IAM User muốn sử dụng IAM Role -> IAM User sẽ cần assume 1 IAM Role

&nbsp;		-> Sau khi assume role thì quyền hiện tại của User sẽ được thay bằng quyền đang được cấp cho IAM Role

&nbsp;		-> Ngoài ra thông tin xác thực bảo mật tạm thời sẽ được cấp cho IAM User hoặc AWS Service để có thể truy cập tới các dịch vụ AWS

&nbsp;	=> VIỆC ASSUME ROLE SẼ LÀM VIỆC VỚI DỊCH VỤ AWS STS - SECURITY TOKEN SERVICE GIÚP TẠO RA CÁC THÔNG TIN CHỨC THỰC TẠM THỜI



&nbsp;	- LÝ DO IAM ROLE RA ĐỜI:

&nbsp;		+ VÍ DỤ:

&nbsp;			- Có 1 user quản lý máy chủ nhưng chỉ quản lý trong 1 khung giờ nhất định 

&nbsp;		-> nếu cấp qua policy thì giờ nào cũng quản lý được -> có statement là allow -> nhưng khi cho full quyền mà ta muốn đưa thêm các ràng buộc khác thì khó

&nbsp;		-> ràng buộc với địa chỉ ip doanh nghiệp hoặc tổ chức mới có quyền, hoặc giờ giấc cụ thể mới có quyền

&nbsp;		=> thông qua IAM Role để có những chi tiết ràng buộc chặt chẽ hơn



&nbsp;	- ĐỂ USER CÓ THỂ SỬ DỤNG IAM ROLE, IAM ROLE SẼ ĐƯỢC GÁN 1 RESOURCE BASE IAM POLICY HAY CÒN GỌI LÀ IAM ROLE TRUST POLICY QUY ĐỊNH XEM AI CÓ THỂ SỬ DỤNG IAM ROLE

&nbsp;	- IAM ROLE THƯỜNG ĐƯỢC DÙNG TRONG THỰC TẾ ĐỂ ĐẢM BẢO NGUYÊN TẮC CẤP QUYỀN TỐI THIỂU VÀ DÙNG TRONG TRƯỜNG HỢP CẤP QUYỀN CHO CÁC AWS ACCOUNT KHÁC TRUY CẬP VÀO TÀI NGUYÊN AWS ACCOUNT HIỆN TẠI



&nbsp;	- NGOÀI ĐƯỢC SỬ DỤNG CHO IAM USER, IAM ROLE CÒN ĐƯỢC SỬ DỤNG ĐỂ CẤP QUYỀN TRUY CẬP CÁC RESOURCE CỦA AWS CHO CHÍNH CÁC AWS SERVICE

&nbsp;	- TRƯỜNG HỢP SỬ DỤNG THƯỜNG THẤY NHẤT LÀ DÙNG IAM ROLE ĐỂ CẤP QUYỀN CHO CÁC ỨNG DỤNG CHẠY BÊN TRONG DỊCH VỤ EC2

##### 

##### 03\. AMAZON COGNITO



* Amazon Cognito là dịch vụ được quản lý bởi AWS có chức năng xác thực, cấp phép và quản lý người dùng cho các ứng dụng web và di động.
* Người dùng có thể đăng nhập trực tiếp bằng tên người dùng và mật khẩu hoặc thông qua một bên thứ 3 như Facebook, Amazon, Google
* Hai thành phần chính của Amazon Cognito là User Pool và Identity Pool

&nbsp;	- USER POOL: là thư mục người dùng cung cấp các tùy chọn đăng ký, đăng nhập cho người dùng ứng dụng

&nbsp;	- IDENTITY POOL: cấp cho người dùng quyền truy cập vào các dịch vụ AWS khác

&nbsp;	-> Sau khi đăng nhập với user pool, người dùng ứng dụng có thể gọi đến API Endpoint (Backend) mà ứng dụng cho phép



&nbsp;	-> Khi user pool kết với với identity pool có thể giúp người dùng truy cập vào các dịch vụ và tài nguyên của AWS theo user được quản lý bởi User pool

##### 

##### 04\. AWS Organization



* Là một dịch vụ giúp quản lý và điều hành tập trung môi trường của mình bao gồm nhiều AWS Account
* AWS Organization có thể tạo các tài khoản AWS mới và phân bổ tài nguyên, sắp xếp các AWS account theo OU (Org Unit), đồng thời đơn giản việc thanh toán với thanh toán tập trung (cosolidated billing)
* AWS Organization có thể áp các chính sách kiểm soát dịch vụ (Service Control Policies) lên các OU hoặc các AWS Account
* Service Control Policies chỉ thiết lập giới hạn quyền tối đa cho các IAM User hoặc IAM Role trong OU hoặc AWS account được gán và cũng cho phép thiết lập deny-based policy

##### 

##### 05\. AWS Indentity Center



* AWS Indentity Center giúp quản lý quyền truy cập tới AWS Account và cả ứng dụng bên ngoài

&nbsp;	- Identity Source có thể nằm trong AWS Identity Center hoặc được liên kết với Active Directory 



* Permission Set xác định khả năng truy cập mà User và Group có đối với các tài khoản AWS trong AWS Org

&nbsp;	- Các bộ quyền được lưu trữ trong AWS Identity Center và được cung cấp cho tài khoản AWS dưới dạng IAM Roles

&nbsp;	- Ta có thể gán nhiều quyền cho một User

-> SỬ DỤNG CHUNG VỚI AWS ORGANIZATION



* CÁC STEPS:

&nbsp;	- B1: GOM NHÓM USER THEO USER GROUP

&nbsp;	- B2: TẠO CÁC PERMISSION SET

&nbsp;	- B3: GÁN PERMISSION SETS VÀO USER



06\. AMAZON KEY MANAGEMENT SERVICE



* AWS KEY MANAGEMENT SERVICE GIÚP TẠO VÀ QUẢN LÝ CÁC ENCRYPTION KEY, PHỤC VỤ CHO MỤC ĐÍCH ENCRYPT/DECRYPT DỮ LIỆU TRÊN AWS 
* ENCRYPTION KEY LUÔN NẰM TRONG AWS KMS, ĐẢM BẢO TIÊU CHUẨN FIPS 140-2
* CMK (CUSTOMER MANAGED KEY) ĐÓNG VAI TRÒ LÀ TÀI NGUYÊN CHÍNH TRONG AWS KMS

&nbsp;	- CMK có thể có kích thước tới 4kb, tuy nhiên thông thường, chúng ta chỉ sử dụng CMK cho mục đích tạo, mã hóa và giải mã Data key - loại khóa được dùng bên ngoài AWS KMS để mã hóa dữ liệu



07\. AWS SECURITY HUB



* AWS SECURITY HUB là dịch vụ cho phép ta thực hiện kiểm tra bảo mật dựa trên các tiêu chuẩn và best practices
* Security Hub chạy liên tục, kiểm tra cấu hình các dịch vụ trong tài khoản AWS và kiểm tra bảo mật dựa trên các best practice của AWS và tiêu chuẩn ngành 
* Security Hub cung cấp kết quả kiểm tra dưới dạng ĐIỂM SỐ và giúp ta xác định các tài khoản và tài nguyên cụ thể cần được lưu ý
