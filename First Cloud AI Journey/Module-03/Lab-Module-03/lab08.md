1. Giới thiệu

&nbsp;	- Amazon Cloudwatch là dịch vụ theo dõi và quản lý cung cấp dữ liệu và thông tin định hướng hành động cho cơ sở hạ tầng AWS, hybird, on-premise

&nbsp;	- Ta có thể thu thập và truy cập tất cả dữ liệu về hiệu năng, và hoạt động dưới hình thức logs và metrics trong 1 nền tảng (thay vì theo dõi riêng lẻ)

&nbsp;	- Cloudwatch cho phép ta theo dõi end-to-end 

&nbsp;	

&nbsp;	- Cloudwatch cung cấp thông tin định hướng hành động, hỗ trợ việc tối ưu hóa hiệu năng sử dụng của ứng dụng

&nbsp;	- Hiển thị dữ liệu metrics, logs đến từng giây, lưu trữ dữ liệu trong 15 tháng và cho phép thực hiện các tính toán trên metrics



=> Việc thiết lập giám sát đúng cách với CloudWatch không chỉ giúp tối ưu hiệu suất mà còn là một phần quan trọng trong chiến lược bảo mật, giúp phát hiện các hoạt động bất thường trong hệ thống của bạn.



2\. Các bước chuẩn bị

&nbsp;	- Triển khai CloudFormation Stack dựa trên template đã có sẵn

&nbsp;	-> Khi Stack hiển thị trạng thái CREATE\_COMPLETE với màu xanh lá, điều này xác nhận rằng tất cả tài nguyên đã được triển khai thành công và bạn đã sẵn sàng để tiếp tục với các bài thực hành Amazon CloudWatch.



3\. CLOUDWATCH METRIC

&nbsp;	- Khi làm việc với Amazon CloudWatch, chúng ta chủ yếu tập trung vào việc “quan sát”. CloudWatch cung cấp các biểu đồ trực quan và bảng dữ liệu chi tiết để theo dõi các Metric.

&nbsp;	+ Khi sử dụng thanh tìm kiếm, CloudWatch mặc định sẽ tìm theo Metric name, giúp bạn nhanh chóng lọc ra các metrics cụ thể cần theo dõi.	

&nbsp;	+ Cloudwatch metric hỗ trợ những tính năng như cấu hình graph, thực hiện tính toán và label dữ liệu



4\. CloudWatch Logs

&nbsp;	- Amazon CloudWatch Logs là dịch vụ giám sát và lưu trữ logs tập trung, cho phép bạn thu thập, phân tích và lưu trữ logs từ các ứng dụng, hệ thống và dịch vụ AWS. Logs là thành phần không thể thiếu trong mỗi hệ thống

&nbsp;	-> Việc phân tích logs hiệu quả không chỉ giúp khắc phục sự cố nhanh chóng mà còn hỗ trợ tối ưu hóa hiệu suất và phát hiện các mẫu hành vi bất thường trong hệ thống của bạn.

&nbsp;	- Việc cấu hình thời gian lưu trữ logs là rất quan trọng để tối ưu chi phí. Logs lưu trữ quá lâu sẽ làm tăng chi phí lưu trữ, trong khi thời gian lưu trữ quá ngắn có thể khiến bạn mất dữ liệu quan trọng khi cần phân tích sự cố.



5\. CloudWatch Alarms

&nbsp;	- Amazon CloudWatch Alarms giúp bạn tự động giám sát các metrics và logs, kích hoạt hành động khi các ngưỡng được vượt qua. 

&nbsp;	- Với CloudWatch Alarms đã thiết lập, bạn có thể mở rộng hệ thống giám sát bằng cách tích hợp với các dịch vụ khác như AWS Lambda để tự động khắc phục sự cố, hoặc AWS Systems Manager để thực hiện các hành động tự động trên tài nguyên bị ảnh hưởng.



6\. CloudWatch Dashboards

&nbsp;	- Amazon CloudWatch Dashboards là công cụ trực quan hóa mạnh mẽ cho phép bạn tạo các bảng điều khiển tùy chỉnh để giám sát tài nguyên AWS trong thời gian thực. Dashboards giúp tập hợp các metrics, logs và alarms quan trọng vào một nơi duy nhất, tạo điều kiện thuận lợi cho việc giám sát và phân tích hệ thống.

&nbsp;	- Đặt tên dashboard có ý nghĩa và phân loại rõ ràng sẽ giúp bạn dễ dàng quản lý khi số lượng dashboards tăng lên trong môi trường thực tế. Cân nhắc sử dụng các tiền tố như “Prod-”, “Dev-”, hoặc tên ứng dụng để phân loại.





