CẤP QUYỀN CHO ỨNG DỤNG TRUY CẬP DỊCH VỤ AWS VỚI IAM ROLE

- TRONG WORKSHOP NÀY TA SẼ HỌC CÁCH CẤP QUYỀN TRUY CẬP CHO ỨNG DỤNG CÓ THỂ TRUY CẬP TỚI DỊCH VỤ AWS
	- CÁC THỨC CẤP QUYỀN TRUY CẬP QUA KEY (TẠI SAO K NÊN DÙNG)
	- CÁCH THỨC THÔNG QUA IAM ROLE TRÊN EC2

I. CHUẨN BỊ
	- Tạo 1 ec2 instance và 1 s3 bucket

II. SỬ DỤNG ACCESS KEY	
	- TẠO MỘT IAM USER VÀ ACCESS KEY
		-> SAU KHI TẠO ACCESS KEY VỚI FULL QUYỀN S3
	- TA SẼ SỬ DỤNG ACCESS KEY ĐÓ ĐỂ UPLOAD 1 FILE LÊN S3

	- Khi chúng ta sử dụng access key thì chúng ta đang chạy ứng dụng với quyền quản trị full dịch vụ S3 được cấp cho IAM user iamaccesskey mà chúng ta đã tạo.

	==> Việc sử dụng access key như trên sẽ rất nguy hiểm
 		-> Vì dễ bị lộ thông tin access key khi chúng ta upload code lên những public repo như GitHub chẳng hạn

III. IAM ROLE TRÊN EC2

- THAY VÌ SỬ DỤNG ACCESS KEY NHƯ VÍ DỤ Ở TRÊN THÌ TA SẼ SỬ DỤNG IAM ROLE ĐỂ CÓ THỂ UPLOAD FILE LÊN TRÊN S3 BUCKET

- 1. TẠO IAM ROLE VỚI POLICY PHÙ HỢP
- 2. SAU KHI TẠO IAM ROLE VỚI FULL ACCESS S3 THÌ TA VÀO EC2 ĐỂ MODIFY ROLE VÀO