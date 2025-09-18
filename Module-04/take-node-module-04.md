### DỊCH VỤ LƯU TRỮ TRÊN AWS

##### 

##### I. Amazon Simple Storage Service (S3)

 	- Amazon S3 là 'kho lưu trữ' ở mức ĐỐI TƯỢNG có nghĩa là nếu muốn thay đổi một phần của tập tin thì ta phải thực hiện thay đổi rồi tải lại toàn bộ tập tin đã sửa đổi

 		-> Hiểu đơn giản là ta override lại object (ghi đè)



 	- S3 phù hợp với các loại dữ liệu ghi một lần đọc nhiều lần (WORM - Write One Read Many)

 

 	- ĐẶC TÍNH:

 		+ Amazon S3 không giới hạn tổng khối lượng lưu trữ dữ liệu -> Hiểu đơn giản là S3 có thể lưu trữ không giới hạn (tốc độ thêm dung lượng lưu trữ của aws sẽ nhanh hơn tốc độ upload lên S3)

 		+ Mỗi object không được lớn hơn 5TB

 		+ Theo mặc định, dữ liệu trong Amazon S3 được duplication trên 3 AZ khác nhau trong 1 Region (# ELB 3 nhân bản chỉ nằm trong 1 AZ)

 		+ Ngoài ra S3 có khả năng kích hoạt sự kiện (trigger event) cho phép kích hoạt tự động các hành động khi một số sự kiện xảy ra -> VD: upload ảnh -> trigger -> giảm size ảnh (serverless function)

 

 	- TOÀN VẸN DỮ LIỆU:

 		+ Amazon S3 được thiết kế để đạt được độ bền (durability) 99.999999999% và độ sẵn sàng (high availability) 99.99%

 			-> Độ bền dữ liệu với xác suất cực kì THẤP

 			-> Các dịch vụ online đảm bảo up time 99.99%		+ Amazon S3 hỗ trợ multipart upload để upload các đối tượng lớn trên bucket

 		-> Tạo các S3 Bucket để có thể lưu trữ các object trong Amazon S3

 			=> https://\[tên-bucket].s3.amazonaws.com

 			=> https://\[tên-bucket].s3.amazonaws.com/capture.mp4

 



 	- UPLOAD VÀ TRUY CẬP DỮ LIỆU TRÊN S3:

 		+ # VỚI BLOCK STORAGE TRUYỀN THỐNG -> DÙNG PROTOCOL

 		 	-> Ta sẽ dùng protocol HTTP PUT để upload dữ liệu lên S3

 			+ Ví dụ:

 			  PUT - photo.gif -> KEY = photo.gif

 			  PUT - /image/photo.gif -> KEY = /image/photo.gif



 			  GET - photo.gif -> 200 OK photo.gif



 		==> LÀM VIỆC VỚI S3 THÔNG QUA REST API (HTTP)

 		==> Mặc dù /image/photo.gif có phân chia các folder nhưng trong S3 thì không có	cây thư mục phân cấp trong file system thông thường

 

 	- ACCESS POINT

 		+ Access point là tính năng cho phép tạo các điểm kết nối (hostname unique) dành cho ứng dụng, người dùng đơn lẻ hoặc theo nhóm

 		-> Một điểm kết nối này chỉ kết nối vào 1 bucket duy nhất

 		-> Ta có thể cấu hình phân quyền khác nhau cho mỗi access point được tạo ra

 

 	- STORAGE CLASS

 		- AMAZONE S3 CHIA VÙNG LƯU TRỮ DỮ LIỆU RA NHIỀU LỚP (STORAGE CLASS) -> TỐI ƯU HÓA CHI PHÍ

 		- CÁC CẤP LƯU TRỮ TRONG S3:

 			+ S3 Standard -> dữ liệu được truy cập thường xuyên

 				-> GIÁ LƯU TRỮ CAO, GIÁ REQUEST THẤP



 			+ S3 Standard IA -> dữ liệu không truy cập thường xuyên

 				-> GIÁ LƯU TRỮ THẤP, GIÁ REQUEST CAO

 

 			+ S3 Intelligent Tiering -> tự động di chuyển các đối tượng giữa các cấp lưu trữ theo số ngày đối tượng không được truy cập



 			+ S3 One Zone ID -> dữ liệu có thể tái tạo lại, lưu trữ dài hạn, không truy cập thường xuyên nhưng cần truy cập nhanh

 				-> KHÔNG ĐƯỢC REPLICATE TRONG 3 AZ, MÀ CHỈ NẰM TRONG 1 AZ

 

 			+ Amazon Glacier/ Deep Archive -> lưu trữ dữ liệu CỰC KÌ ít truy cập

 				-> KHÔNG ĐỌC TRỰC TIẾP NẾU OBJECT NẰM TRONG 2 CLASS NÀY (CLASS ĐẶC BIỆT)

 

 		=> S3 CÓ 2 CHI PHÍ CHÍNH:

 			+ TỔNG DUNG LƯỢNG LƯU TRONG S3

 			+ SỐ LƯỢNG REQUEST VÀO S3



 		=> KHI ĐƯA DỮ LIỆU VÀO S3 THÌ TA CÓ THỂ QUẢN LÝ VÒNG ĐỜI CỦA DỮ LIỆU (Object Life Cycle Management) -> Bằng cách sử dụng chính sách vòng đời -> ta có thể luân chuyển dữ liệu trong 1 S3 bucket giữa các CẤP LƯU TRỮ theo thời gian ngày TÙY CHỈNH



   --------------------------------90days-------------------------->

   ------------------60days---------------->

   -------30days-------->

S3 Standard ---> S3 Standard IA ---> S3 One Zone IA ---> Glacier/Deep Archive



 	=> OBJECT LIFE CYCLE MANAGEMENT SẼ DI CHUYỂN OBJECT SAU SỐ NGÀY CHÚNG TA QUY ĐỊNH, ĐƯỢC TÍNH TỪ NGÀY OBJECT ĐƯỢC TẠO



##### II. S3 Static Website \& CORS - Control Access - Object Key \& Performance - Glacier



 	- S3 Static Website \& CORS:

 		- S3 ngoài việc host các file hình ảnh thì còn hỗ trợ host các static website (html, media, ...)

 		- Phù hợp single page application (SPA) -> đóng vai trò là một static website server

 		- Và để share cho các web server có thể truy cập tới thì S3 hỗ trợ CORS (Cross-origin resource sharing) -> cho phép nhiều tài nguyên khác nhau của một trang web có thể truy vấn từ domain khác với domain của trang đó



 	- CONTROL ACCESS: AMAZON S3 CÓ 2 CƠ CHẾ KIỂM SOÁT TRUYỀN TRUY CẬP TỚI BUCKET

 		+ S3 ACCESS CONTROL LIST (ACL)

 			+ Là một cơ chế kiểm soát truy cập có trước IAM

 			+ ACL S3 được gán bucket và object của S3 -> việc gán policy gán vào các object rất phức tạp



 		+ S3 BUCKET POLICY

 			+ S3 Bucket Policy và IAM policy xác định quyền cấp đối tượng bằng cách cung cấp các đối tượng đó trong Resource trong policy

 			+ Tạo ra policy và gắn trực tiếp vào trong bucket -> quản lý tập trung qua resource

 

 	- ENDPOINT \& VERSIONING

 		- S3 ENDPOINT CHO PHÉP TA TRUY CẬP DỮ LIỆU QUA MẠNG NỘI BỘ CỦA AWS MÀ KHÔNG THÔNG QUA INTERNET

 			+ VÍ DỤ: UPLOAD DỮ LIỆU EC2 -> S3

 				-> DÙNG TÍNH NĂNG S3 ENDPOINT VÌ EC2 VÀ S3 ĐỀU LÀ DỊCH VỤ CỦA AWS

 			- UPLOAD DỮ LIỆU THÔNG QUA GIAO THỨC HTTP -> API -> ĐI QUA ĐỊA CHỈ IP PRIVATE TRONG VPC (KO QUA INTERNET)



 		- S3 VERSIONING CHO PHÉP TA KHÔI PHỤC ĐỐI TƯỢNG SAU KHI VÔ TÌNH XÓA HAY GHI ĐÈ -> ĐỒNG THỜI HỖ TRỢ TRC CÁC TẤN CÔNG RANSOMWARE/ENCRYTION ATTACK

 			+ Nếu xóa -> Amazon S3 Versioning sẽ đánh dấu (MARKER) tập tin đã xóa

 			+ Nếu ghi đè -> thì một phiên bản đổi tượng mới sẽ xuất hiện trong bucket

 			=> TRONG CẢ 2 TRƯỜNG HỢP ĐỀU CÓ THỂ KHÔI PHỤC PHIÊN BẢN TRƯỚC ĐÓ !!!

 			==> NẾU ĐÃ BẬT VERSIONING THÌ TA SẼ KHÔNG THỂ XÓA TÍNH NĂNG ĐÓ - CHỈ TẠM DỪNG (BẬT = TÍNH TIỀN DỰA TRÊN TỔNG DUNG LƯỢNG ĐÃ VERSIONING)





 	- OBJECT KEY \& PERFORMANCE:

 		- Mỗi object trong S3 đều NGANG HÀNG -> không phân cấp -> được gán 1 object key

 		- Sâu bên dưới S3 chia ra các Partitions -> sẽ được chia tự động khi lượng request tăng cao hoặc số lượng object keys lớn (giảm tốc độ tìm kiếm object trong partition)

 		- S3 lưu trữ KEY MAP (key map cũng được chia ra thành nhiều partition và được hash bởi prefix của object key)

 			=> Để tối ưu hiệu năng của S3 ta có thể dùng random prefix -> mục tiêu của việc này là làm S3 lưu trữ các object trên nhiều partitions nhất có thể

 			==> VÌ PERFORMANCE CỦA S3 DỰA TRÊN SỐ LƯỢNG PARTITIONS

 



 	- STORAGE CLASS GLACIER

 		- Là lựa chọn lưu trữ có chi phí thấp -> phù hợp với dữ liệu ko yêu cầu truy xuất trực tiếp, dài hạn

 			+ VÍ DỤ: Có những chứng từ lưu trữ 5-7 năm (lưu để tuân thủ các chính sách) -> cần thời gian để lưu trữ dữ liệu

 		- Vì không thể truy xuất trực tiếp -> ta sẽ thực hiện thao tác RETRIEVE dữ liệu về một S3 Bucket # với GLACIER



 		- CÓ 3 TÙY CHỌN ĐỂ TRUY XUẤT DỮ LIỆU VỚI CHI PHÍ KHÁC NHAU:

 			+ TRUY XUẤT NHANH -> 1-5 PHÚT

 			+ TRUY XUẤT TIÊU CHUẨN -> 3-5 GIỜ

 			+ TRUY XUẤT HÀNG LOẠT -> 5-12 GIỜ

 			==> THỜI GIAN TRUY XUẤT CÀNG CHẬM - CHI PHÍ CÀNG THẤP

 		- KHÔNG CHO PHÉP UPLOAD CÁC FILE TỪ GIAO DIỆN (AWS MANAGEMENT CONSOLE) -> MÀ CHỈ CHO PHÉP UPLOAD DỮ LIỆU QUA CLI/SDK ĐỂ UPLOAD CÁC OBJECT VÀO GLACIER

 		- GLACIER CÓ CHI PHÍ RẺ HƠN ĐẾN 20 LẦN SO VỚI S3 STANDARD

 		- CÒN CÓ MỘT TÍNH NĂNG LÀ OBJECT BLOCK (KO CHO PHÉP XÓA VÀ CHỈNH SỬA DỮ LIỆU) -> SẼ CÓ 24 GIỜ THAY ĐỔI -> SAU 24 GIỜ THÌ SẼ BỊ ÁP CHÍNH SÁCH KHÓA VĨNH VIỄN

 

#### III. SNOW FAMILY - STORAGE GATEWAY - BACKUP



1. ##### SNOW FAMILY



&nbsp;	- CHUYỂN DỮ LIỆU TRẠNG THÁI 'LẠNH' 

&nbsp;		-> CÓ NGHĨA LÀ KHÔNG TRUYỀN DỮ LIỆU TRỰC TIẾP TỪ NGUỒN ĐẾN ĐÍCH 

&nbsp;		-> MÀ MÌNH SẼ EXPORT RA DỮ LIỆU TỪ NGUỒN RA VÀ LƯU LẠI THIẾT BỊ LƯU TRỮ PHẦN CỨNG -> SAU ĐÓ VẬN CHUYỂN TỚI ĐÍCH ĐẾN -> IMPORT

&nbsp;	=> CÁCH THỨC TRÊN ĐƯỢC GỌI LÀ COLD DATA TRANSFER

&nbsp;	 

&nbsp;	- THỰC TẾ TRUYỀN TẢI DỮ LIỆU DUNG LƯỢNG LỚN THÔNG QUA BĂNG THÔNG -> HẠN CHẾ, KÈM THEO ĐỘ TRỄ ĐƯỜNG TRUYỀN

&nbsp;		-> ÁP DỤNG CÁCH VẬN CHUYỂN TRỰC TIẾP



* SNOW BALL:

&nbsp;	- Dịch vụ hỗ trợ migrate dữ liệu từ môi trường on-premise tới AWS ở quy mô PetaByte (PB)

&nbsp;	- Mỗi snowball có thể chứa tới 80 Terabyte (TB)

&nbsp;	- Snowball sẽ được ship trở về AWS region mà chúng ta lựa chọn để lưu trữ dữ liệu -> dữ liệu sẽ được lưu trong các dịch vụ S3, Glacier

&nbsp;	- Ta sẽ cần phải cài Snowball client tại máy local để thực hiện xác minh, nén, mã hóa và transfer dữ liệu



* SNOWBALL EDGE:

&nbsp;	- Đây là phiên bản nâng cấp hơn của SNOWBALL với dung lượng có thể chứa tới 100 Terabyte

&nbsp;	- Các cách thức hoạt động, vận hành, cài đặt đều tương tự so với SNOWBALL

&nbsp;	- Snowball edge là thiết bị đặc biệt có sẵn các tài nguyên tính toán bên trong (máy chủ) -> xử lý dữ liệu local trước 



* SNOWMOBILE

&nbsp;	- Dịch vụ hỗ trợ migrate dữ liệu lên đến EXABYTE

&nbsp;	- Mỗi Snowmobile có thể chứa đến 100 PB

&nbsp;	- Cách thức hoạt động cũng tương tự như 2 snowball trên

##### 

##### 2\. AWS STORAGE GATEWAY



&nbsp;	- Là một giải pháp lưu trữ Hybird, kết hợp dung lượng lưu trữ trên AWS với dung lượng lưu trữ tại chỗ (on-premise)

&nbsp;		-> Cần request nhiều -> On-premise

&nbsp;		-> Cần lưu trữ lâu -> AWS Storage Gateway



&nbsp;	- Chúng ta có thể tận dụng quy mô và giá thành hợp lý của các dịch vụ lưu trữ trên cloud để giúp lưu trữ các dữ liệu lớn -> yêu cầu lưu trữ lâu

&nbsp;	

&nbsp;	- AWS Storage gateway hỗ trợ ba phương thức lưu trữ chính:

&nbsp;		+ File Gateway:

&nbsp;			+ Cho phép ta lưu trữ và truy xuất đối tượng trong S3 bằng cách sử dụng giao thức tệp NFS và SMB

&nbsp;			+ Đối tượng được ghi thông qua cổng kết nối có thể truy cập trực tiếp trong S3

 

&nbsp;		+ Volume Gateway:

&nbsp;			+ Cung cấp dữ liệu dạng khối cho ứng dụng -> giao thức iSCSI

&nbsp;			+ Dữ liệu được lưu trong S3

&nbsp;			+ Để truy cập ổ đĩa iSCSI trong AWS -> có thể tạo EBS Snapshot (tự động bằng AWS Backup) -> tạo thành EBS volumes

&nbsp;		

&nbsp;		+ Type Gateway:

&nbsp;			+ Cung cấp cho ứng dụng sao lưu một giao diện thư viện băng từ ảo (VTL) iSCI, type drive ảo, tape ảo

&nbsp;			+ Dữ liệu tape ảo được lưu trong S3 hoặc Glacier



&nbsp;	- Ngoài lề:

&nbsp;		+ Store volume -> dùng cho các dự án disaster recovery đảm bảo dữ liệu được lưu tại chỗ -> bản copy dữ liệu ở on-premise và aws

&nbsp;		

&nbsp;		+ Cached volume -> tối ưu hóa dung lượng lưu trữ -> trở thành môi trường hybird (ta có thể quyết định dữ liệu lưu trữ trên cloud và on-premise) 



&nbsp;	- DISASTER RECOVERY ON AWS:

&nbsp;		- RTO (RECOVERY TIME OBJECTIVE): THỜI GIAN CẦN THIẾT ĐỂ PHỤC HỒI MỘT DỊCH VỤ -> TRẠNG THÁI BÌNH THƯỜNG

&nbsp;			+ Ví dụ: nếu 1 thảm họa xảy ra 2h chiều và RTO 4 giờ -> phục hồi trễ nhất là 6h tối

&nbsp;		

&nbsp;		- RPO (Recovery Point Objective): THỜI GIAN TỐI ĐA MÀ DỮ LIỆU CÓ THỂ BỊ MẤT

&nbsp;			+ Ví dụ: nếu backup mỗi ngày 1 lần -> trường hợp xấu nhất RPO = 24h

&nbsp;		

&nbsp;	-> CÁC DỊCH VỤ, ỨNG DỤNG CÓ ĐỘ PHỨC TẠP KHÁC NHAU VÀ CÓ MỨC CAM KẾT DỊCH VỤ (SERVICE LEVEL AGREEMENT - SLA) TRONG ĐÓ BAO GỒM RTP/RPO KHÁC NHAU

&nbsp;	-> TÙY VÀO MỨC ĐỘ CAM KẾT TA SẼ LỰA CHỌN CÁC CHIẾN LƯỢC TƯƠNG ỨNG



&nbsp;	- 4 CHIẾN LƯỢC PHỤC HỒI TRÊN AWS:

&nbsp;		+ Sao lưu và khôi phục

&nbsp;		+ Pilot Light (Active - Standby)	

&nbsp;		+ Low Capacity Active - Active	

&nbsp;		+ Full Capacity Active - Active



##### 3\. AWS Backup

&nbsp;	

&nbsp;	- Là một dịch vụ quản lý các tác vụ sao lưu 

&nbsp;	- Có thể cấu hình và lập lịch (backup schedule)

&nbsp;	- Có chính sách sao lưu (backup retention) và giám sát hoạt động sao lưu cho các tài nguyên trên AWS bao gồm:

&nbsp;		+ Amazon EBS

&nbsp;		+ ------ EC2

&nbsp;		+ ------ RDS

&nbsp;		+ ------ DynamoDB

&nbsp;		+ ------ EFS

&nbsp;		+ ------ Storage gateway volumes



&nbsp;	-> Retention sẽ ảnh hưởng đến chi phí lưu trữ trên AWS 

