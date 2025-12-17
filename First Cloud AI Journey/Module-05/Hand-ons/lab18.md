AWS SECURITY HUB

- AWS SECURITY HUB cung cấp cho ta cái nhìn toàn diện về các cảnh bảo bảo mật ưu tiên cao và trạng thái tuân thủ trên các tài khoản AWS

- Sẽ có rất nhiều các công cụ bảo mật mạnh mẽ để ta sử dụng:
	+ Tường lửa
	+ Ứng dụng bảo vệ endpoint
	+ Hay các ứng dụng quét lỗ hổng và sự tuân thủ bảo mật

- NHƯNG đôi khi điều này sẽ khiến đội ngũ ta phải chuyển đổi qua lại giữa các công cụ trên
	-> đối phó với hàng trăm, nghìn cảnh báo mỗi ngày

- VỚI SECURITY HUB thì ta sẽ có một nơi tổng hợp duy nhất, sắp xếp và phân độ ưu tiên các cảnh bảo hoặc phát triển bảo mật từ nhiều dịch vụ AWS 

==> CÁC RỦI RO ĐƯỢC TÌM THẤY SẼ ĐƯỢC TRỰC QUAN HÓA VỚI CÁC BIỂU ĐỒ, BẢNG MÀ TA CÓ THỂ TƯƠNG TÁC 
	-> TA CŨNG CÓ THỂ GIÁM SÁT HỆ THỐNG LIÊN TỤC BẰNG CÁCH SỬ DỤNG CHỨC NĂNG KIỂM TRA TỰ ĐỘNG THEO CÁC TIÊU CHUẨN MÀ TA MONG MUỐN

- CHI PHÍ:
	- Thông thường, chi phí sẽ ít hơn 1$ mỗi tháng nếu tài khoản của ta dùng cho mục đích thử nghiệm
	
	- Đối với thực tế:
		+ Kiểm tra bảo mật
			+ 100.000 cho lần đầu -> 0.001$/check
			+ 100.001 - 500.000   -> 0.0008$/check
			+ 500.001 ++          -> 0.0005$/check

		+ Tìm các sk tấn công
			+ 10.000 -- -> miễn phí
			+ 10.001 ++ -> 0.00003$/lần


01. CÁC TIÊU CHUẨN BẢO MẬT

- 1.1: AWS FOUNDATIONAL SECURITY BEST PRACTICES
	- Là một tập hợp các bài kiểm tra xem tài khoản của ta và các tài nguyên đang được triển khai có đang được tuân theo các thực nghiệm tối ưu về bảo mật hay không.
	-> Tiêu chuẩn này được đưa ra bởi các chuyên gia bảo mật của AWS
	==> BỘ TIÊU CHUẨN NÀY GIÚP TA TRONG VIỆC CẢI THIỆN ĐỘ BẢO MẬT CỦA TÀI KHOẢN AWS CỦA TA VÀ VỚI HẦU HẾT CÁC DỊCH VỤ CƠ BẢN VÀ THÔNG DỤNG CỦA AWS

- 1.2: CIS AWS FOUNDATIONS BENCHMARK
	- Là bộ tiêu chuẩn "Center for Internet Security (CIS) AWS Founations Benchmark" là bộ các cấu hình thực nghiệm tối ưu cho AWS
	- Tiêu chuẩn cho Security Hub này được tự động kiểm tra tuân thủ của ta so với từng tập các yêu cầu nhỏ được đưa ra bởi CIS hay k.

- 1.3 PCI DSS
	- Bộ tiêu chuẩn PAYMENT CARD INDUSTRY DATA SECURITY STANDARD (PCI DSS) là tiêu chuẩn an toàn thông tin cho các đối tượng lưu trữ, xử lý và truyền dữ liệu	về thẻ ngân hàng.
	- Tiêu chuẩn cho Security Hub này được tự động kiểm tra sự tuân thủ của ta so với từng tập các yêu cầu nhỏ được đưa ra bởi PCI DSS hay k.


02. KÍCH HOẠT SECURITY HUB

- Để kích hoạt Security Hub, AWS có cung cấp cho người dùng giao diện để tương tác với dịch vụ dễ dàng
- Ở trong bài Lab này ta sẽ thao tác qua AWS Management Console

==> SAU KHI KÍCH HOẠT SECURITY HUB TRÊN GIAO DIỆN CONSOLE, TA CÓ THỂ DỄ DÀNG KIỂM TRA, THAO TÁC MỘT CÁCH DỄ DÀNG