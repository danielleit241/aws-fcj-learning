##### **1. Điện toán đám mây là gì?**

\- Điện toán đám mây là việc phân phối các tài nguyên CNTT theo nhu cầu sử dụng qua mạng internet với CHÍNH SÁCH THANH TOÁN theo mức sử dụng

\- Thay vì ta mua các thiết bị phần cứng, thiết bị mạng -> thì ta chỉ cần gửi yêu cầu đến nhà cung cấp -> tạo máy chủ ảo -> kết nối đến máy chủ ảo để sử dụng

\- Lợi ích của điện toán đám mây:

 	+ Sử dụng bao nhiêu tính bấy nhiêu -> khả năng tối ưu chi phí

 	+ Tăng tốc độ phát triển -> nhờ vào việc tự động hóa và quản trị

 	+ Linh hoạt trong việc thêm, bớt các tài nguyên theo nhu cầu

 	+ Mở rộng quy mô ứng dụng lên toàn cầu



##### **2. Điều gì tạo nên sự khác biệt của AWS?**

\- Dẫn đầu trong nhà cung cấp hạ tầng cloud trong 13 năm liên tiếp \[hết năm 2023]

\- Triết lý về giá của AWS: khách hàng sẽ càng ngày càng trả tiền ít hơn cho cùng dịch vụ/tính năng/tài nguyên sử dụng

 	-> Càng sử dụng thì giá tiền sẽ trở nên hời hơn

\- LEADERSHIP PRINCIPLES:

 	+ ĐẶT KHÁCH HÀNG LÊN HÀNG ĐẦU

 	+ COI SẢN PHẨM VÀ CÔNG VIỆC NHƯ LÀ CỦA CHÍNH MÌNH

 	...

 	+ TẬP TRUNG VÀO KẾT QUẢ CUỐI CÙNG !!!

##### 

##### **3. Bắt đầu hành trình lên mây như thế nào**

\- Học hỏi trên trang web của AWS

 	+ Số lượng dịch vụ và tính năng của AWS tăng trưởng rất nhanh

 	+ Không hoạt động một cách độc lập - giữa các tính năng luôn có sự tương tác với nhau

-> Kết bạn và cùng nhau học hỏi những thứ mới



\- KHÔNG NÊN HẠN CHẾ BẢN THÂN TRONG MÔI TRƯỜNG LAB (CỦA AWS), tuy nhiên nên đăng kí tài khoản AWS và làm việc trên tài khoản thực tế thông qua các hạn mức Free tier

##### 

##### **4. Hạ tầng toàn cầu của AWS**

\* Khái niệm:

\- TRUNG TÂM DỮ LIỆU (DATA CENTER)

 	+ Chứa hàng chục nghìn máy chủ có quy mô rất lớn

 	+ Trung tâm dữ liệu của AWS đều được sử dụng các thiết bị tối ưu hóa dành riêng cho các hoạt động của AWS



\- Availability Zone (AZ):

 	+ Một AZ bao gồm một hoặc nhiều Data Center

 	+ Các AZ được thiết kế để không xảy ra sự cố ảnh hưởng đồng thời 2 AZ một lúc (fault isolation)

 	+ Các thiết kế về điện, mạng giữa 2 AZ đều được thiết kế độc lập

 	+ Giữa 2 AZ là đường kết nối riêng tốc độ cao

 	+ AWS khuyến nghị nên triển khai ứng dụng tối thiểu trên 2 AZ (best-practice)

 

\- Region:

 	+ Một AWS Region bao gồm tối thiểu 3 Availability Zone

 	+ Hiện tại có hơn 25 region trên toàn cầu

 	+ Các Region được kết nối với nhau bởi mạng backbone của AWS

 	+ Mặc định dữ liệu và dịch của ở các Region độc lập với nhau (trừ một số dịch vụ ở quy mô Global)

 		+ Ưu tiên dùng các Region gần khu vực của mình làm việc

 	+ Một số dịch vụ đặc thù như GenAI thì sẽ nằm ở US

 	+ Đúng với triết lý của AWS thì các Region có số lượng người dùng nhiều sẽ luôn rẻ hơn các Region mới và ít người dùng



\- Edge Locations:

 	+ Là mạng lưới trung tâm dữ liệu AWS được thiết kế để cung cấp dịch vụ với độ trễ thấp nhất có thể

 	+ Các dịch vụ AWS hoạt động tại Edge Locations (POP) bao gồm:

 		+ CloundFront (CDN)

 			+ Content Delivery Network là mạng phân phối nội dung giúp phân phối dữ liệu (web, hình ảnh, video) thường đã được cache lại -> nhanh hơn và ổn định hơn

 		+ Web Application Firewall (WAF)

 			+ Đóng vai trò là lớp bảo vệ web -> hạn chế tấn công DDOS

 		+ Route 53 (DNS Service)

 			+ Tạo những domain

##### 

##### 5\. Công cụ quản lý AWS services

\- AWS Management Console - ROOT LOGIN

&nbsp;	+ Ta sẽ có 2 cơ chế để đăng nhập vào AWS

&nbsp;		+ Root user (tài khoản ta đăng kí AWS account đầu tiên bao gồm username + password) -> quan trọng và hạn chế dùng root account

&nbsp;		+ IAM User: không phải là 1 tài khoản user hoàn chỉnh - mà là tài khoản con giúp ta truy suất và sử dụng AWS hiệu quả			+ Khi Login bằng IAM User thì ta cần cung cấp thêm 1 chuỗi 12 số là Account ID AWS



\- Service search:

&nbsp;	+ Sau khi login vào ta có thể tìm kiếm các service của AWS

&nbsp;	+ Mỗi dịch vụ sẽ có trang quản lý riêng -> feature của dịch vụ đó



\- AWS Command Line Interface (CLI)

&nbsp;	+ Giao diện dòng lệnh AWS (AWS CLI) là một công cụ mã nguồn mở cho phép ta tương tác với các dịch vụ AWS bằng command line

&nbsp;	+ Cho phép chạy các lệnh triển khai chức năng tương đương với AWS Management Console trên trình duyệt

&nbsp;	+ Ta có thể dung Access key/Secret Access key để đăng nhập dùng AWS CLI



\- AWS SDK 

&nbsp;	+ Đơn giản hóa việc sử dụng AWS services 

&nbsp;	+ Cung cấp 1 bộ thư viện cho nhiều ngôn ngữ khác nhau

&nbsp;	+ AWS SDK cung cấp hỗ trợ cho những công việc quản lý vòng đời API với AWS Services 



##### 6\. Tối ưu hóa chi phí trên AWS và làm việc với AWS Support

\- Lựa chọn cấu hình tài nguyên và nơi lưu trữ dữ liệu phù hợp

&nbsp;	+ Ở truyền thống thường sẽ không bao giờ chạy full tải 100% mà phải phòng hờ 1 lượng tài nguyên nhất định để hệ thống có thể scale lên

&nbsp;	+ Hệ thống chỉ cần 5-10% để chạy nhưng lại cấu hình cao hơn -> lãng phí

\- Tận dụng các phương thức thanh toán giảm giá

&nbsp;	+ Reserved instance

&nbsp;	+ Saving plan

&nbsp;	+ Spot

&nbsp;		-> Nếu chạy theo mô hình "on demand" (theo giờ, phút, giây) -> đắt đỏ nhất

&nbsp;		-> Cam kết sử dụng dịch vụ lâu dài sẽ có những mức discount tương ứng

&nbsp;		-> Spot: tài nguyên tạm, sẵn sàng khi cần có thể mở rộng quy mô, nếu không dùng thì rất lãng phí -> chi phí rất thấp

\- Các tài nguyên không sử dụng, ta có thể bật tắt tự động các tài nguyên không cần phải chạy 24/7

\- Tận dụng các dịch vụ serverless (phi máy chủ)

&nbsp;	+ Có những dịch vụ không cần phải quản lý máy chủ -> ví dụ quản lý database (AWS sẽ quản lý thay vì ta)



=> QUAN TRỌNG: THIẾT KẾ KIẾN TRÚC TỐI ƯU -> giải quyết các nhu cầu và yêu cầu đề ra

&nbsp;	+ Dựa vào các bài toán, các yêu cầu, đáp ứng được các ràng buộc là điều tối quan trọng với việc TỐI ƯU HÓA chi phí

&nbsp;	+ Đồng thời cũng cải thiện hiệu năng (thay vì yêu cầu máy chủ cao hơn)



\- Cài đặt và sử dụng AWS Budget -> cảnh bảo các mức sử dụng theo ngày, tuần, tháng

\- Quản lý chi phí theo phòng ban/ ứng dụng với cost allocation tag

\- LIÊN TỤC theo dõi và tối ưu hóa chi phí

&nbsp;	+ Liên tục theo dõi, cập nhật tính năng mới để tối ưu



=> GIÚP DOANH NGHIỆP KIẾM TIỀN, GIÚP DOANH NGHIỆP TIẾT KIỆM HƠN



\- CÁC CÔNG CỤ TÍNH TOÁN CHI PHÍ

&nbsp;	+ Cho phép tạo các estimate cho các dịch vụ

&nbsp;	+ Chia sẻ estimate cho người khác

&nbsp;	+ Chi phí sẽ khác biệt với các Region tương ứng

