1. Giới thiệu

&nbsp;	- Trong bài thực hành này, bạn sẽ làm quen với việc sử dụng AWS Backup (Dịch vụ Sao lưu AWS) để tạo ra một kế hoạch sao lưu (backup plan) cho các tài nguyên đang hoạt động trên AWS như EBS Volumes (Volumes EBS), RDS Databases (Cơ sở dữ liệu RDS), DynamoDB Tables (Bảng DynamoDB), hay EFS File Systems (Hệ thống Tệp EFS). Đồng thời, bạn cũng sẽ biết được làm thế nào để khôi phục lại dữ liệu từ các bản sao lưu và tự động hóa toàn bộ quá trình.



2\. CÁC BƯỚC CHUẨN BỊ

&nbsp;	- DÙNG CLOUDFORMATION ĐỂ TRIỂN KHAI HẠ TẦNG

&nbsp;	- TẠO S3 ĐỂ LƯU CÁC TÀI NGUYÊN DỊCH VỤ 



3\. TẠO BACKUP PLAN

&nbsp;	- Để đảm bảo một chiến lược sao lưu hoàn hảo, cần có sự cân nhắc kỹ lưỡng và đa chiều. Thành công của một tổ chức phụ thuộc nhiều yếu tố, trong đó có chiến lược dự phòng.

&nbsp;		+ Các yếu tố chủ yếu ảnh hưởng đến chiến lược sao lưu bao gồm Mục tiêu thời gian khôi phục (RTO) và Mục tiêu điểm khôi phục (RPO)

&nbsp;		-> Chú ý rằng RTO và RPO cần được xác định cụ thể cho từng khối lượng công việc cụ thể, không phải cho toàn bộ tổ chức hoặc cơ sở hạ tầng.



4\. THIẾT LẬP THÔNG BÁO

&nbsp;	- . AWS Backup sử dụng dịch vụ AWS SNS (Simple Notification Service) để gửi thông báo liên quan đến các hoạt động sao lưu đang diễn ra. Điều này cho phép bạn theo dõi trạng thái công việc sao lưu, khôi phục và các lỗi có thể xảy ra, giúp nhóm Vận hành phản ứng kịp thời và thích hợp.

