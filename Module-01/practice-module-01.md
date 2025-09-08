##### \* LAB 01: 

1\. Tạo tài khoản AWS

2\. Thiết lập MFA cho tài khoản AWS (root)

3\. Tài khoản và nhóm Admin

4\. Hỗ trợ xác thực tài khoản



\- Tạo tài khoản AWS theo hướng dẫn trong bài lab: 

&nbsp;	+ Cài đặt MFA để bảo mật tài khoản

&nbsp;	+ Vào IAM -> Tạo user group (admin-group) -> add thêm policy Admin access

&nbsp;	+ Tạo Users -> thêm các thông tin cơ bản (username-password) -> thêm vào group vừa tạo -> Cài đặt MFA cho user vừa tạo

&nbsp;	+ Tạo asscess key cho User vừa tạo -> sử dụng cho AWS CLI 

(nếu muốn xóa access key -> deactive key đó rồi mới bắt đầu xóa)

(nên sử dụng các TAG khi sử dụng các tài nguyên của AWS)



=> BEST PRACTICES: 

&nbsp;	+ Không nên đăng nhập bằng tài khoản root mà hãy đăng nhập bằng tài khoản IAM User

&nbsp;	+ Luôn bảo mật các thông tin liên quan đến các key và xóa hoặc vô hiệu hóa các key nếu ta không sử dụng

&nbsp;	



\- Nếu có vấn đề gì trong quá trình trên ta có thể liên hệ với AWS Support Console điền các thông tin bao gồm cả hình ảnh bằng chứng để AWS có thể hỗ trợ nhanh nhất



* AWS Management Console:

&nbsp;	- Cung cấp giao diện web an toàn để truy cập và quản lý các AWS Service

&nbsp;	- Hỗ trợ xác thực qua root user hoặc IAM User

=> Tất cả các tương tác trên giao diện đều được chuyển đổi thành các lệnh gọi AWS API ở phía sau



=> Để tăng cường bảo mật, luôn sử dụng người dùng IAM thay vì tài khoản root cho các hoạt động hàng ngày. Tài khoản root chỉ nên được sử dụng cho việc thiết lập ban đầu và các tác vụ quản lý tài khoản quan trọng.



&nbsp;	- 1: Set up default region

&nbsp;	- 2: 

--------------------------------------------------------------



##### \* LAB 07: 

1\. Tạo cost budget

2\. Tạo usage budget

3\. Tạo reservation budget

4\. Tạo saving plans budget



--------------------------------------------------------------



##### \* LAB 09: 

1\. Các gói hỗ trợ AWS

2\. Truy cập AWS support

3\. Quản lý yêu cầu hỗ trợ



==============================================================

NGHIÊN CỨU BỔ SUNG: AWS WELL ARCHITECTED FRAMEWORK



\- Các khái niệm, nguyên tắc thiết kế và biện pháp thực hành tốt nhất về kiến trúc để thiết kế và vận hành hệ thống của ta trong môi trường cloud

\- Trả lời các câu hỏi qua đó ta sẽ biết được mức độ phù hợp giữa các kiến trúc

\- Sử dụng AWS WAF tích hợp trên AWS Management Console -> cải thiện kiến trúc của mình

