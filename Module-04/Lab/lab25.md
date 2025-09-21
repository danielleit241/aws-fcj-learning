### Triển khai FSx trên Windows



* KIẾN TRÚC CỦA AMAZON FSx BAO GỒM NHIỀU THÀNH PHẦN (COMPONENT) HOẠT ĐỘNG CÙNG NHAU ĐỂ CUNG CẤP DỊCH VỤ LƯU TRỮ FILE HIỆU SUẤT CAO, CÓ QUY MÔ ĐƯỢC QUẢN LÝ HOÀN TOÀN



* Ở CẤP ĐỘ CAO, KIẾN TRÚC CỦA AMAZON FSx BAO GỒM CÁC THÀNH PHẦN SAU:

&nbsp;	- FILE SERVERS 

&nbsp;		-> ĐÂY LÀ CÁC EC2 INSTANCES CHẠY WINDOW FILE SERVER SẼ TRUY CẬP QUA GIAO THỨC SMB

&nbsp;	

&nbsp;	- STORAGE

&nbsp;		-> LƯU TRỮ DỮ LIỆU CƠ BNAR ĐƯỢC CUNG CẤP BỞI AMAZON S3

&nbsp;	

&nbsp;	- VPC

&nbsp;		-> AMAZON FSx ĐƯỢC TRIỂN KHAI TRONG VPC ĐỂ TĂNG CƯỜNG BẢO MẬT VÀ CÔ LẬP MẠNG



&nbsp;	- NETWORKING

&nbsp;		-> AMAZON FSx SỬ DỤNG ELASTIC NETWORK INTERFACES ĐỂ CUNG CẤP MỘT MẠNG CÓ KHẢ NĂNG MỞ RỘNG VÀ KHẢ DỤNG CAO ĐỂ TRUY CẬP VÀO FILE STORAGE

&nbsp;	

&nbsp;	- DATA REPLCICATION

&nbsp;		-> TỰ ĐỘNG SAO CHÉP DỮ LIỆU TRÊN NHIỀU AZ

&nbsp;	

&nbsp;	- MANAGEMENT AND MONITORING

&nbsp;		-> AMAZON FSx ĐƯỢC AWS QUẢN LÝ HOÀN TOÀN



&nbsp;	

##### 

1. ##### GIỚI THIỆU

&nbsp;	- Amazon FSx cho Window File Server cung cấp bộ lưu trữ dùng chung được quản lý toàn phần

&nbsp;	- Được tích hợp trên window server và cung cấp vô số tính năng quản trị, quản lý và truy cập dữ liệu





