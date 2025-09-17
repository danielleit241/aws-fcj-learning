### DỊCH VỤ LƯU TRỮ TRÊN AWS

##### 

##### I. Amazon Simple Storage Service (S3)

&nbsp;	- Amazon S3 là 'kho lưu trữ' ở mức ĐỐI TƯỢNG có nghĩa là nếu muốn thay đổi một phần của tập tin thì ta phải thực hiện thay đổi rồi tải lại toàn bộ tập tin đã sửa đổi

&nbsp;		-> Hiểu đơn giản là ta override lại object (ghi đè)



&nbsp;	- S3 phù hợp với các loại dữ liệu ghi một lần đọc nhiều lần (WORM - Write One Read Many)

&nbsp;	

&nbsp;	- ĐẶC TÍNH:

&nbsp;		+ Amazon S3 không giới hạn tổng khối lượng lưu trữ dữ liệu -> Hiểu đơn giản là S3 có thể lưu trữ không giới hạn (tốc độ thêm dung lượng lưu trữ của aws sẽ nhanh hơn tốc độ upload lên S3)

&nbsp;		+ Mỗi object không được lớn hơn 5TB

&nbsp;		+ Theo mặc định, dữ liệu trong Amazon S3 được duplication trên 3 AZ khác nhau trong 1 Region (# ELB 3 nhân bản chỉ nằm trong 1 AZ)

&nbsp;		+ Ngoài ra S3 có khả năng kích hoạt sự kiện (trigger event) cho phép kích hoạt tự động các hành động khi một số sự kiện xảy ra -> VD: upload ảnh -> trigger -> giảm size ảnh (serverless function)

&nbsp;	

&nbsp;	- TOÀN VẸN DỮ LIỆU:

&nbsp;		+ Amazon S3 được thiết kế để đạt được độ bền (durability) 99.999999999% và độ sẵn sàng (high availability) 99.99%

&nbsp;			-> Độ bền dữ liệu với xác suất cực kì THẤP

&nbsp;			-> Các dịch vụ online đảm bảo up time 99.99%		+ Amazon S3 hỗ trợ multipart upload để upload các đối tượng lớn trên bucket

&nbsp;		-> Tạo các S3 Bucket để có thể lưu trữ các object trong Amazon S3

&nbsp;			=> https://\[tên-bucket].s3.amazonaws.com

&nbsp;			=> https://\[tên-bucket].s3.amazonaws.com/capture.mp4

&nbsp;	



&nbsp;	- UPLOAD VÀ TRUY CẬP DỮ LIỆU TRÊN S3:

&nbsp;		+ # VỚI BLOCK STORAGE TRUYỀN THỐNG -> DÙNG PROTOCOL

&nbsp;		 	-> Ta sẽ dùng protocol HTTP PUT để upload dữ liệu lên S3

&nbsp;			+ Ví dụ: 

&nbsp;			  PUT - photo.gif -> KEY = photo.gif

&nbsp;			  PUT - /image/photo.gif -> KEY = /image/photo.gif



&nbsp;			  GET - photo.gif -> 200 OK photo.gif



&nbsp;		==> LÀM VIỆC VỚI S3 THÔNG QUA REST API (HTTP)

&nbsp;		==> Mặc dù /image/photo.gif có phân chia các folder nhưng trong S3 thì không có	cây thư mục phân cấp trong file system thông thường

&nbsp;	

&nbsp;	- ACCESS POINT

&nbsp;		+ Access point là tính năng cho phép tạo các điểm kết nối (hostname unique) dành cho ứng dụng, người dùng đơn lẻ hoặc theo nhóm

&nbsp;		-> Một điểm kết nối này chỉ kết nối vào 1 bucket duy nhất

&nbsp;		-> Ta có thể cấu hình phân quyền khác nhau cho mỗi access point được tạo ra

&nbsp;	

&nbsp;	- STORAGE CLASS

&nbsp;		- AMAZONE S3 CHIA VÙNG LƯU TRỮ DỮ LIỆU RA NHIỀU LỚP (STORAGE CLASS) -> TỐI ƯU HÓA CHI PHÍ

&nbsp;		- CÁC CẤP LƯU TRỮ TRONG S3:

&nbsp;			+ S3 Standard -> dữ liệu được truy cập thường xuyên

&nbsp;				-> GIÁ LƯU TRỮ CAO, GIÁ REQUEST THẤP



&nbsp;			+ S3 Standard IA -> dữ liệu không truy cập thường xuyên

&nbsp;				-> GIÁ LƯU TRỮ THẤP, GIÁ REQUEST CAO

&nbsp;	

&nbsp;			+ S3 Intelligent Tiering -> tự động di chuyển các đối tượng giữa các cấp lưu trữ theo số ngày đối tượng không được truy cập



&nbsp;			+ S3 One Zone ID -> dữ liệu có thể tái tạo lại, lưu trữ dài hạn, không truy cập thường xuyên nhưng cần truy cập nhanh

&nbsp;				-> KHÔNG ĐƯỢC REPLICATE TRONG 3 AZ, MÀ CHỈ NẰM TRONG 1 AZ

&nbsp;	

&nbsp;			+ Amazon Glacier/ Deep Archive -> lưu trữ dữ liệu CỰC KÌ ít truy cập

&nbsp;				-> KHÔNG ĐỌC TRỰC TIẾP NẾU OBJECT NẰM TRONG 2 CLASS NÀY (CLASS ĐẶC BIỆT)					

&nbsp;	

&nbsp;		=> S3 CÓ 2 CHI PHÍ CHÍNH:

&nbsp;			+ TỔNG DUNG LƯỢNG LƯU TRONG S3

&nbsp;			+ SỐ LƯỢNG REQUEST VÀO S3



&nbsp;		=> KHI ĐƯA DỮ LIỆU VÀO S3 THÌ TA CÓ THỂ QUẢN LÝ VÒNG ĐỜI CỦA DỮ LIỆU (Object Life Cycle Management) -> Bằng cách sử dụng chính sách vòng đời -> ta có thể luân chuyển dữ liệu trong 1 S3 bucket giữa các CẤP LƯU TRỮ theo thời gian ngày TÙY CHỈNH



&nbsp;  --------------------------------90days-------------------------->

&nbsp;  ------------------60days---------------->

&nbsp;  -------30days-------->

S3 Standard ---> S3 Standard IA ---> S3 One Zone IA ---> Glacier/Deep Archive



&nbsp;	=> OBJECT LIFE CYCLE MANAGEMENT SẼ DI CHUYỂN OBJECT SAU SỐ NGÀY CHÚNG TA QUY ĐỊNH, ĐƯỢC TÍNH TỪ NGÀY OBJECT ĐƯỢC TẠO





