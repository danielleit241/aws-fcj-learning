QUẢN LÝ TÀI NGUYÊN BẰNG TAG VÀ RESOURCE GROUPS

- ĐỂ GIÚP QUẢN LÝ CÁC MÁY ẢO, Ổ ĐĨA VÀ CÁC TÀI NGUYÊN KHÁC EC2 
	-> trong bài lab này ta sẽ thực hành gán các metadata của mỗi tài nguyên dưới dạng TAG (thẻ) và sử dụng RESOURCE GROUP

- TAG (THẺ):
	- Là nhãn mà ta gán cho tài nguyên AWS, mỗi thẻ bao gồm một cặp key=value
	- Thẻ cho phép ta phân loại các tài nguyên AWS theo nhiều cách khác nhau:
		+ Theo mục đích, người sở hữu, môi trường
	- Điều này trở nên hữu ích khi có nhiều tài nguyên cùng loại -> giúp ta nhanh chóng xác định một tài nguyên cụ thể dựa trên tag đã được gán cho nó

- AWS RESOURCE GROUPS:
	- Là một tính năng cho phép ta quản lý và tự động hóa các thao tác cho nhiều tài nguyên cùng một lúc
	- Một Resource Group là một nhóm các tài nguyên được phân loại theo TAG (tag-based) hoặc theo CloudFormation stack (CloudFormation stack-based)

01. SỬ DỤNG TAG TRÊN CONSOLE
- Trong bước này, ta sẽ thực hiện các thao tác với các thẻ trên AWS Management Console

1.1 TẠO EC2 INSTANCE CÓ TAG
- Chúng ta sẽ sử dụng region ap-southeast-1 (Singapore)
- Ngay lúc tạo EC2 Instances ta có thể gắn các tag để dễ dàng nhận biết

1.2 THÊM HOẶC XÓA TAG (CÁC THAO TÁC TRÊN 1 TAG HOẶC NHIỀU TAGs)

1.3 LỌC TÀI NGUYÊN THEO TAG
- Sau khi thêm các Tags vào trong các ec2 instances -> chúng ta có thể tìm kiếm các ec2 instances thông qua key=value
-> hỗ trợ việc tìm kiếm các ec2 tạo theo môi trường, chủ sở hữu, mục đích, ...

02. SỬ DỤNG TAG TRÊN CLI

- CÂU LỆNH THÊM TAG CHO CÁC TÀI NGUYÊN HIỆN CÓ: 
'aws ec2 create-tags --resources <ResourceID> --tags Key=<Key>,Value=<Value>'

03. TẠO MỘT RESOURCE GROUP
- Ở bước này ta sẽ tạo một resource goups được phân loại theo thẻ (Tag-based)
	
	+ CREATE RESOURCE GROUP
	+ CREATE QUERY-BASED GROUP -> GROUP TYPE -> TAG-BASED 
	+ GROUPING CRITERIA
		+ Chọn Resource types (loại tài nguyên) là AWS::EC2::Instance. 
		+ Bạn có thể chọn tối đa 20 loại tài nguyên.
	+ Ở mục Group details, nhập các thông số PHÙ HỢP
	


