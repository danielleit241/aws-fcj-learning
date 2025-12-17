#### Khởi Đầu Với Amazon S3



* S3 là một dịch vụ lưu trữ dạng đối tượng (object) cung cấp khả năng mở rộng theo nhu cầu, đảm bảo tính khả dụng của dữ liệu và độ bảo mật và hiệu năng ở mức cao nhất



* LỰA CHỌN HIỆN ĐẠI: Aws khuyến nghị sử dụng AWS Amplify Hosting để host trang website tĩnh vì báo mật tốt hơn

 	+ Https mặc định

 	+ CDN toàn cầu mà không cấu hình CloudFront thủ công



1. GIỚI THIỆU:

 	- S3 ĐƯỢC THIẾT KẾ ĐỂ ĐẠT ĐỘ BỀN 11 SỐ 9 (99.999999999 %) và lưu trữ dữ liệu cho hàng triệu người dùng trên thế giới



\- S3 Bucket vs Object:

 	- S3 BUCKET:

 		+ S3 bucket là container cấp cao nhất, chứa các object

 		+ Tên của s3 bucket phải là duy nhất trên tất cả tòi khoản của AWS

 		+ S3 sẽ hoạt động trong một Region cụ thể và tối đa sẽ có 100 bucket/1 tài khoản AWS

 		+ CHỨC NĂNG:

 			+ Tổ chức các nhóm object

 			+ Áp dụng chính sách và quyền

 			+ Cấu hình tính năng (versioning, encryption, logging)

 			+ Định nghĩa kiểm soát truy cập

 

 	- OBJECT:

 		+ Object là các tệp/dữ liệu lưu trữ bên trong bucket

 		+ Cách đặt theo theo key name, chỉ cần duy nhất trong bucket đó

 		+ Kích thước một tệp sẽ giao động trong khoảng 0-5 TB và không giới hạn các object trong 1 bucket

 		+ CHỨC NĂNG:

 			+ Chứa dữ liệu thực tế

 			+ Có metadata riêng

 			+ Có thể có quyền riêng lẻ (với ACL)

 

 	- CẤU TRÚC MỐI QUAN HỆ GIỮA S3 BUCKET VÀ OBJECT:

 		Bucket: my-website-bucket

 		├── index.html (Object)

 		├── about.html (Object)

 		├── css/

 		│	└── style.css (Object)

 		└── images/

    			├── logo.png (Object)

 	    		└── banner.jpg (Object)





2\. CÁC BƯỚC CHUẨN BỊ



* TẠO S3 BUCKET:

 	- 1. TRUY CẬP VÀO DỊCH VỤ S3

 	- 2. KHỞI TẠO S3 BUCKET

 	- 3. CẤU HÌNH CÀI ĐẶT S3 CƠ BẢN

 		Hiểu về Object Ownership:

 			- ACLs disabled (khuyến nghị): Chủ sở hữu bucket tự động sở hữu tất cả đối tượng. Quản lý quyền đơn giản hơn.

 			- ACLs enabled: Cho phép quyền cấp đối tượng. Phức tạp hơn nhưng cung cấp kiểm soát chi tiết.

 	- 4. CẤU HÌNH CÀI ĐẶT TRUY CẬP CÔNG KHAI

 	- 5. TẠO BUCKET



* TẢI DỮ LIỆU LÊN BUCKET:





3\. BẬT TÍNH NĂNG STATIC WEBSITE:



* Lưu trữ website tĩnh cho phép ta lưu trữ một website trực tiếp từ S3 bucket, không giống như các website động cần xử lý từ phía máy chủ
* Các website tĩnh bao gồm nội dung cố định (html, css, javascript, hình ảnh) được gửi trực tiếp đến trình duyệt của người dùng



* LỢI ÍCH:

 	+ Tiết kiệm chi phí

 	+ Có thể scale

 	+ Đáng tin cậy, nhanh, đơn giản



* CẤU HÌNH TỪNG BƯỚC:

 	- 1. Truy cập vào Properties của Bucket

 	- 2. Static website hosting

 	- 3. Cấu hình và cài đặt website hosting

 		+ Static website hosting: Enable

 		+ Hosting type: chọn host a static

 		+ Index document: index.html

 		+ Error document: tùy chọn (error.html)

 	- 4. Sau khi cấu hình cài đặt xong S3 Bucket sẽ cung cấp cho ta một DNS dưới dạng sau: http://aws-first-cloud-journey-24102004.s3-website-us-east-1.amazonaws.com





4\. CẤU HÌNH BLOCK PUBLIC ACCESS



* SAU KHI CẤU HÌNH STATIC WEBSITE HOSTING XONG -> TA CHƯA THỂ TRUY CẬP TRỰC TIẾP VÀO WEBSITE VỪA HOST
* ĐỂ TRUY CẬP VÀO WEBBITE CHÚNG TA CẦN CẤU HÌNH LẠI BLOCK PUBLIC ACCESS:

 	- 1. Chọn Permission trong S3 Bucket

 	- 2. Bỏ tick chọn Block All...

 	- 3. Xác nhận thay đổi

 



5\. CẤU HÌNH PUBLIC OBJECT:

* PUBLIC OBJECT: nghĩa là bất kì ai trên internet cũng có thể truy cập đến chúng -> điều này chỉ làm cho nội dung ta dự định công khai. Ko bao giờ làm công khai các dữ liệu nhạy cảm
* CẤU HÌNH TỪNG BƯỚC:

 	- 1. Truy cập vào Permissions

 	- 2. Tìm và cài đặt Access Control List

 		Bạn sẽ thấy "Bucket owner enforced" hiện đang được chọn

 		Điều này có nghĩa là ACL bị tắt và chủ sở hữu bucket kiểm soát tất cả đối tượng

 	- 3. Bật ACL cho Kiểm soát Cấp Đối tượng

 		- Tick chọn I acknowledge that ACLs will be restored.

 		- Tick Bucket owner preferred

 	- 4. Điều hướng lại object, chọn những object ta muốn public và vào action để thao tác



6\. TĂNG TỐC STATIC WEBSITE VỚI CLOUDFRONT



* 6.1 CHẶN TẤT CẢ CÁC TRUY CẬP CÔNG CỘNG VÀO S3

 	- 1. CHỌN PERMISSTION TRONG S3 BUCKET

 		- BẬT LẠI CHỨC NĂNG BLOCK ALL...



* 6.2 CẤU HÌNH AMAZON CLOUDFRONT

 	- Sử dụng bảng điều khiển quản lý AWS để tạo CloudFront distribution và cấu hình dịch vụ này phục vụ s3 Bucket mà chúng ta đã tạo trước đó.

 		- 1. Vào Amazon CloudFront

 		- 2. Tạo một CloudFront distribution

 		- 3. Cài đặt cấu hình:

 			- Origin domain chọn S3 bucket đã tạo

 			- Origin access chọn Legacy ...

 			- Create new OAI

 		- 4. Bucket policy -> chọn yes

 		- 5. Tại phần Web Application Firewall (WAF), trong khuôn khổ bài lab này, chọn Do not enable security protections.

 			Trong phần Settings:

 				Chọn Use North America, Europe, Asia, Middle East, and Africa.

 				Tại Default root object - optional, điền index.html là object bạn đã upload trong bước 2.2 (Tải dữ liệu).

Giữ nguyên các giá trị mặc định và chọn Create distribution.



* 6.3 KIỂM TRA AMAZON CLOUDFRONT



7\. BUCKET VERSIONING



* Versioning trong Amazon S3 là một tính năng cho phép bạn giữ nhiều biến thể của một đối tượng trong cùng một bucket. Khi versioning được bật, bạn có thể bảo toàn, truy xuất và khôi phục mọi phiên bản của mọi đối tượng được lưu trữ trong bucket của mình, cung cấp một lớp bảo vệ dữ liệu bổ sung chống lại việc xóa hoặc sửa đổi ngoài ý muốn.



8\. DI CHUYỂN OBJECT



* Với hành động move trong bảng điều khiển S3, bạn có thể di chuyển một object đến một thư mục khác trong cùng một bucket hoặc sang bucket khác.
