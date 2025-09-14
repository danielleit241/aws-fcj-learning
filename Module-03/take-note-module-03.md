## MODULE 03 - Compute VM on AWS



##### I. AMAZON ELASTIC COMPUTE CLOUD (EC2)



* Amazon EC2 giống với máy chủ ảo hoặc máy chủ vật lý truyền thống
* EC2 có khả năng khởi tạo nhanh, khả năng co dãn tài nguyên mạnh mẽ, linh hoạt (elasticity)

&nbsp;	-> Khi ta muốn ứng dụng của ta phục vụ lượng người dùng lớn -> máy chủ sẽ tăng lên -> sau khi họ sử dụng xong thời điểm đó -> máy chủ giảm bớt => chi phí được chi trả ít hơn



* Amazon EC2 có thể hỗ trợ các wordload như lưu trữ web, ứng dụng, cơ sở dữ liệu, dịch vụ xác thực và bất cứ công việc nào khác mà máy chủ thông thường có thể đáp ứng

&nbsp;	-> Điểm mạnh so với truyền thống: có thể nâng cấp cấu hình một cách dễ dàng



* Khi ta khởi tạo ra máy chủ EC2:

&nbsp;	+ Ta sẽ lựa chọn các cấu hình EC2 thông qua instance type chứ không được lựa chọn tùy ý  

&nbsp;	+ Instance type sẽ quyết định các yếu tố:

&nbsp;		+ CPU (Intel/AMD/ARM) -> Intel là chi phí cao nhất

&nbsp;		+ GPU

&nbsp;		+ Memory

&nbsp;		+ Network

&nbsp;		+ Storage



* Kiến trúc của EC2:

&nbsp;	- Hardware node (thiết bị phần cứng):

&nbsp;		+ Sẽ được lựa chọn và quản lý bởi AWS dựa vào thông tin khi khởi tạo EC2 (Instance type, placement option, hypervisor, AZ)

&nbsp;			+ Placement option: cho phép ta tạo các máy chủ EC2 ở gần nhau để giảm độ trễ hoặc ở xa nhau để tránh ảnh hường 2 máy chủ EC2

&nbsp;	

&nbsp;	- Trên Hypervisor:

&nbsp;		+ Đóng vai trò quản lý phần cứng, sẽ được lựa chọn lúc ta chọn Amazon Machine Image (template) -> khởi tạo lên máy chủ ảo 

&nbsp;			=> Hypervisor mới nhất là KVM - Nitro (tốc độ chạy nhanh hơn 30%)



&nbsp;	- EC2 Instances:

&nbsp;		+ Các máy chủ ảo có thuật ngữ là instance thay vì là VM (quy ước của AWS)



=> Đây là kiến trúc của EC2:

&nbsp;			-------------------

&nbsp;			| EC2 | EC2 | EC2 |

&nbsp;			-------------------

&nbsp;			|    Hypervisor   |

&nbsp;			-------------------

&nbsp;			|  Hardware node  |

&nbsp;			| 		  |

&nbsp;			|		  |

&nbsp;			-------------------



&nbsp;	

* AMI / BACKUP / KEYPAIR:

&nbsp;	- Amazon Machine Image (AMI): có thể provision ra một hoặc nhiều EC2 Instances cùng lúc

&nbsp;		+ AMI có sẵn của AWS trên AWS market place và custom AMI tự tạo từ EC2 Instances

&nbsp;		+ AMI bao gồm root OS volumes, quyền sử dụng AMI quy định tài khoàn AWS được sử dụng và mapping EBS volume được tạo và gán vào EC2 Instances

&nbsp;	- EC2 Instance có thể được backup bằng cách tạo snapshot:

&nbsp;		+ snapshot đầu tiên full snapshot

&nbsp;		+ snapshot thứ 2 trở đi sẽ là in-cremental snapshot (chỉ lấy những cái thay đổi trên volume đó)

&nbsp;	- Key pair (public key và private key): dùng để mã hóa thông tin đăng nhập cho EC2 Instance



* KHI NHẮC TỚI AMI THÌ TA SẼ CÓ KHÁI NIỆM TIẾP THEO LÀ: ELASTIC BLOC STORE (EBS)

&nbsp;	- Amazon EBS cung cấp block storage và được gán trực tiếp vào EC2 Instance

&nbsp;		+ Tuy được gán trực tiếp như 1 RAW device thì EBS bản chất hoạt động động lập với EC2 và được kết nối thông qua mạng riêng của EBS

&nbsp;	- EBS có 2 nhóm đĩa chính là HDD và SSD được thiết kế để đạt độ sẵn sàng ~ 100% bằng cách replicate dữ liệu giữa 3 storage node trong 1 AZ

&nbsp;		+ HDD: ưu tiên với việc đọc ghi tuần tự

&nbsp;		+ SSD: lưu trữ dạng flash, hỗ trợ đọc ghi ngẫu nhiên cao

---------------------------------------------------------------------------------

&nbsp;				Availability Zone				|

&nbsp;										|

&nbsp;	------------------- <-----EBS Network------ --------------------

 	| EC2 | EC2 | EC2 |			    | EBS |  EBS | EBS |

 	-------------------			    --------------------

 	|    Hypervisor   |	 		    |Storage controller|

 	-------------------			    --------------------

 	|  Hardware node  |			    |	Storage node   |

 	| 		  |			    |		       |

 	|		  |			    |		       |

 	-------------------			    --------------------	|

&nbsp;										|

---------------------------------------------------------------------------------

&nbsp;						

=> EBS về bản chất hoạt động độc lập với EC2 và được kết nối thông qua mạng riêng EBS trong cùng 1 AZ

&nbsp;	-> EC2 không thể hoạt động mà không có EBS

&nbsp;	

&nbsp;	- Một số EC2 Instances đặc thù được tối ưu hóa hiệu năng của EBS (Optimized EBS Instances)

&nbsp;	- EBS volumes mặc định chỉ được gán vào 1 EC2 Instances

&nbsp;		+ Tuy nhiên EC2 chạy trên Hypervisor Nitro có thể dùng 1 EBS volume gắn vào nhiều EC2 (EBS Multi attach)

&nbsp;	- EBS được backup bằng cách thực hiện snapshot vào S3 (Simple storage storage)



* INSTANCE STORE:

&nbsp;	- Là vùng đĩa NVME có tốc độ cực cao, nằm trên physical node chạy các máy ảo EC2 (cao hơn nhiều so với EBS -> hỗ trợ hàng triệu IOPS mỗi giây)

&nbsp;	- Tuy nhiên điểm khác biệt với INSTANCE STORE vs. EBS:

&nbsp;		+ Instance store là thiết bị phần cứng gắn trực tiếp vào hardware node chạy các máy chủ EC2 -> đạt hiệu suất cao và độ trễ thấp

&nbsp;		+ Vì gắn trực tiếp thì sẽ không được replicate dự phòng vào các vùng nhớ khác

&nbsp;			-> Nếu có sự cố xảy ra thì dữ liệu trên instance store sẽ bị mất ngay lập tức

&nbsp;		+ Khi thực hiện thao tác dừng stop-shutdown máy chủ -> dữ liệu bị xóa

&nbsp;		+ Còn restart lại máy hoặc crash thì dữ liệu sẽ không bị xóa

&nbsp;	



&nbsp;	=> Dữ liệu quan trọng thì dùng EBS, dữ liệu cache có thể tái tạo lại được thì dùng instance store

&nbsp;	=> Hoặc để đạt tối đa hiệu năng thì ta nên replicate dữ liệu từ instance store vào trong một EBS volume để đảm bảo an toàn

&nbsp;			

&nbsp;	 		-------------------

 			| EC2 | EC2 | EC2 | <----

 			-------------------	|

 			|    Hypervisor   |	|

 			-------------------	|

 			|  Hardware node  |	|

 			| 		  |	|

 			|  Ephemeral NVME |	|

&nbsp;			|      volume	  | -----

 			|(Instance store) |

&nbsp;			-------------------



* USER DATA:

&nbsp;	- Là đoạn script chạy duy nhất 1 lần khi provision EC2 Instance từ AMI

&nbsp;	- Tùy hệ điều hành mà chúng ta sẽ sử dụng bash shell scripts (Linux)/ powershell (windows)



* META DATA:

&nbsp;	- Là thông tin liên quan đến chính bản thân EC2 instances

&nbsp;		+ Địa chỉ IP private, public, hostname, security groups

&nbsp;	- Một số trường hợp ta muốn triển khai ứng dụng EC2 trên môi trường tự động 

&nbsp;		+ Ta muốn cấu hình EC2 hostname -> lấy cấu hình từ meta data

&nbsp;	

&nbsp;	-> META DATA DƯỢC DÙNG KHI CHẠY SCRIPT TỰ ĐỘNG HÓA (BIẾT ĐƯỢC THÔNG TIN QUA META DATA)

&nbsp;		

* EC2 AUTO SCALING:

&nbsp;	- EC2 AUTO SCALING là tính năng hỗ trợ tăng giảm số lượng EC2 Instance dựa theo các điều kiện cụ thể (scaling policy)

&nbsp;	- Có thể tự đăng kí các EC2 Instance vào Elastic Load Balancer

&nbsp;	- Hoạt động trên nhiều AWS AZ

&nbsp;	- Hỗ trợ nhiều pricing options khác nhau 



##### II. EC2 Autoscaling - EFS/FSx - Lightsail - MGN





