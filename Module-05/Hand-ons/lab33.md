MÃ HÓA Ở TRẠNG THÁI LƯU TRỮ VỚI AWS KMS



01. GIỚI THIỆU

1.1 AWS KEY MANAGEMENT SERVICE (KMS)

- Key management service là dịch vụ dùng để tạo và quản lý keys.
- AWS đảm bảo key của ta được quản lý hoàn toàn độc lập và được bảo mật chặt chẽ -> ngay cả các kĩ sư của AWS cũng không thể biết key của ta

- Ở KMS ta có thể lựa chọn Symmetric key hoặc Asymmetric key để làm CMK (customer master key) 
- Sau khi tạo khóa thì có thể thiết lập đặt key policy để control quyền access và sử dụng key đó -> có thể kết hợp với AWS CloudTrail để ghi lại logs

- KHÓA ĐỐI XỨNG - SYMMETRIC KEY:
	+ Một khóa duy nhất: chỉ sử dụng một khóa duy nhất để thực hiện cả 2 tác vụ mã hóa và giải mã dữ liệu

	+ Dễ dàng chia sẻ: có thể chia sẻ an toàn giữa những người dùng được tin cậy cần truy cập vào dữ liệu đã mã hóa

	+ Nhanh hơn: mã hóa và giải mã dữ liệu bằng khóa đối xứng thường nhanh hơn so với bất đối xứng

	+ Bảo mật yêu cầu cao: việc giữ an toàn cho khóa đối xứng rất quan trọng vì bất kì ai có quyền truy cập vào khóa đều có thể giải mã dữ liệu

- KHÓA BẤT ĐỐI XỨNG - ASYNMMETRIC KEY:
	+ Cặp khóa: gồm một bộ đôi khóa, một khóa public, một khóa private

	+ Public và Private: khóa public được phân phối cho những người cần mã hóa dữ liệu, còn khóa private được giữ bí mật

	+ Mã hóa và giải mã riêng biệt: khóa public chỉ dùng để mã hóa dữ liệu, còn khóa private dùng để giải mã dữ liệu
	
	+ Phân phối an toàn hơn: khóa public có thể được phân phối rộng rãi mà không ảnh hưởng đến tính bảo mật của dữ liệu, chỉ cần giữ an toàn cho khóa private

	+ Chậm hơn: việc mã hóa và giải mã bằng khóa bất đối xứng thường chậm hơn

1.2 AMAZON S3

- Là một dịch vụ lưu trữ đối tượng cung cấp khả năng thay đổi quy mô, mức độ sẵn sàng của dữ liệu, độ bảo mật và hiệu suất hàng đầu
- Tùy vào các dữ liệu cần được lưu trữ thì ta có thể tối ưu hóa chi phí, quy mô tổ chức dữ liệu và cấu hình các biện pháp kiểm soát quyền truy cập được tinh chỉnh và đáp ứng yêu cầu của tổ chức

- S3 có khả năng mở rộng cao vì nó tự động tăng dung lượng lưu trữ của ta theo yêu cầu và ta chỉ cần trả tiền cho bộ nhớ ta đang sử dụng

1.3 AWS CLOUDTRAIL

- Là một dịch vụ cho phép thực hiện việc quản lý, kiểm tra vận hành và đánh giá rủi ro cho tài khoản AWS của bạn. Với CloudTrail, bạn có thể ghi nhật ký, giám sát liên tục và duy trì hoạt động của tài khoản có liên quan đến các hoạt động diễn ra trên cơ sở hạ tầng AWS của bạn.

1.4 AMAZON ATHENA

- Là dịch vụ truy vấn dữ liệu tương tác trên Amazon S3, cho phép ta thực hiện các truy vấn SQL trên dữ liệu được lưu trữ trong các tệp tin được lưu trữ trong S3 mà không phải di chuyển hoặc sao chép dữ liệu vào cơ sở dữ liệu truyền thống

- ATHENA giúp ta dễ dàng truy vấn và phân tích dữ liệu lớn lưu trữ trong S3 mà không cần triển khai hoặc quản lý CSDL


02. CÁC BƯỚC CHUẨN BỊ

- TẠO POLICY VÀ ROLE: Ở BƯỚC NÀY TA SẼ TẠO RA CÁC CHÍNH SÁCH ĐỂ CÓ QUYỀN TRUY CẬP VÀO: S3, CLOUDTRAIL, ...
- TẠO GROUP VÀ USER: Ở BƯỚC NÀY TA SẼ PHÂN QUYỀN GROUP VÀ TẠO USER ĐỂ THỬ NGHIỆM TRUY CẬP VÀO TÀI NGUYÊN MÀ QUẢN TRỊ VIÊN ĐÃ MÃ HÓA TRÊN S3 VÀ CHIA SẺ DỮ LIỆU

03. TẠO KEY MANAGEMENT SERVICE

04. TẠO AMAZON S3
- TẠO BUCKET
- TẢI DỮ LIỆU LÊN S3

05. Tạo AWS CloudTrail và Amazon Athena

- AWS CloudTrail ghi lại mọi hoạt động diễn ra trong tài khoản AWS của bạn, bao gồm cả những thay đổi đối với tài nguyên AWS, truy cập API và hoạt động của người dùng. Bằng cách theo dõi các bản ghi này, bạn có thể xem ai đã thực hiện hành động nào, khi nào và từ đâu. Điều này có thể giúp bạn giải quyết sự cố, phát hiện hoạt động đáng ngờ và tuân thủ các yêu cầu quy định.

- Amazon Athena là một dịch vụ truy vấn dữ liệu lớn, tương tác và phi máy chủ được cung cấp bởi Amazon Web Services (AWS). Nó cho phép bạn dễ dàng phân tích petabyte dữ liệu được lưu trữ trong Amazon S3 bằng cách sử dụng ngôn ngữ truy vấn SQL tiêu chuẩn.


