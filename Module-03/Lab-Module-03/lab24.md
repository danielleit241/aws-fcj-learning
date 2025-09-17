Triển khai File Storage Gateway

 	- Chúng ta sẽ triển khai File Storage Gateway để thiết lập một File Sharing kết nối với máy chủ on-premise



1. Chuẩn bị

 	- Tạo S3 Bucket

 	- Tạo EC2 cho Storage Gateway



2\. Sử dụng AWS Storage Gateway

 	- Trong phần này, chúng ta sẽ thực hiện các bước sau để sử dụng AWS Storage Gateway: tạo Storage Gateway, tạo File Share và kết nối ổ đĩa này với máy của bạn.



 	- Lưu ý: Khi triển khai thực tế trong môi trường On-premise, Storage Gateway Appliance sẽ được đặt trong hệ thống của bạn để tạo một File Share và đồng bộ lưu trữ dữ liệu giữa môi trường On-premise và môi trường AWS. Bạn có nhiều tùy chọn để triển khai Storage Gateway Appliance trong môi trường của bạn. AWS hỗ trợ triển khai trên môi trường ảo hóa như VMWare / Hyper-V / KVM. Ngoài ra, AWS cung cấp cả thiết bị vật lý để bạn có thể đặt trong hệ thống.

