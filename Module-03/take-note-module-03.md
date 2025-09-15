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



* Kiến trúc hoạt động của EC2 autoscaling 

&nbsp;	- Khi 1 client kết nối vào từ internet -> IG -> Application LB -> EC2

&nbsp;		+ Giả sử khi có lượng kết nối cao: thì tham số 'ActiveConnectionCount' là HIGH (được set)

&nbsp;		-> Khi đạt hiệu ứng cao thì hiệu năng hệ thống bị ảnh hưởng, máy chủ xử lý không kịp

&nbsp;		-> Autoscaling group có thể nằm nhiều AZ

&nbsp;		

&nbsp;	=> Auto scaling group sẽ hỗ trợ tăng số lượng máy chủ -> đăng kí với application load balancer -> chia lượng tải ra 2 máy chủ

&nbsp;	==> ActiveConnectionCount giảm xuống NORMAL



&nbsp;		-> Khi đạt hiệu năng thấp -> thì auto scaling sẽ vào trạng thái scale-in -> terminate các EC2 đi -> TIẾT KIỆM CHI PHÍ



&nbsp;	=> THUẬT NGỮ NHẰM ÁM CHỈ VIỆC SCALE-OUT SCALE-IN ĐƯỢC GỌI LÀ ALASTICITY



* PRICING OPTIONS:

&nbsp;	- EC2 bao gồm 4 tùy chọn loại giá:

&nbsp;		+ On-demand: trả theo nhu cầu sử dụng (giờ/phút/giây)

&nbsp;			-> Giá mắc nhất

&nbsp;			-> Phù hợp cho các workload chạy lên tới 6 tiếng 1 ngày

&nbsp;		+ Reserved Instance: Cam kết sử dụng lâu dài (1-3 năm) sẽ áp dụng discount

&nbsp;			-> Tuy nhiên bị giới hạn EC2 Instance Type

&nbsp;		+ Saving plans: Cam kết sử dụng theo kì hạn (1-3 năm) để lấy discount

&nbsp;			-> Có thể ko giới hạn bởi EC2 Instance Type

&nbsp;		+ Spot Instance: Tận dụng tài nguyên dư, giá rẻ

&nbsp;			-> Khi nào cần thì AWS sẽ terminate instance trong 2 phút

&nbsp;		

&nbsp;	- TRONG MỘT EC2 AUTO SCALING GROUP CÓ THỂ KẾT HỢP NHIỀU PRICING OPTIONS -> TẬN DỤNG LỢI THẾ CỦA PRICING OPTIONS ĐỂ TA TIẾT KIỆM CHI PHÍ NHƯNG VẪN CÓ ĐỦ EC2 ĐỂ HỆ THỐNG HOẠT ĐỘNG ỔN ĐỊNH

&nbsp;	

* AMAZON LIGHTSAIL:

&nbsp;	+ Là một dịch vụ tính toán có chi phí thấp và tính theo tháng (>= 3.5$/Month)

&nbsp;	+ Mỗi một instance lightsail tạo ra cũng sẽ có 1 mức data transfer đi kèm (giá rẻ hơn EC2 khá nhiều)

&nbsp;	+ Amazon lightsail phù hợp cho các workload nhẹ, môi trường test dev -> không yêu cầu lượng tải CPU cao liên tục (> 2h mỗi ngày)



&nbsp;	+ Amazon Lightsail có khả năng sao lưu backup bằng snapshot tương tự EC2

&nbsp;		+ Snapshot này có thể convert qua được EC2 Instance

&nbsp;		

&nbsp;	+ Amazon Lightsail chạy trong 1 VPC đặc biệt (được quản lý bởi dịch vụ lightsail) -> có thể kết nối tới VPC thông thường qua 1 click VPC Peering



* AMAZON ELASTIC FILE SYSTEM (AMAZON EFS)

&nbsp;	- Cho phép tạo ra các NFSv4 Network Volume (ổ cứng mạng) gán vào nhiều EC2 Instances cùng lúc

&nbsp;	- Quy mô lưu trữ lên đến hàng petrabyte

&nbsp;	=> CHỈ SUPPORT LINUX



&nbsp;	- Sử dung EFS chỉ tính theo dung lượng sử dụng (trong khi EBS tính phí theo dung lượng cấp phát)

&nbsp;	- EFS có thể được cấu hình để mount vào môi trường on-premise qua DX hoặc VPN



* AMAZON FSX:

&nbsp;	- Cho phép tạo ra các NTFS volume và gán vào nhiều EC2 Instance cùng lúc sử dụng giao thức SMB (Server Message Block) 

&nbsp;	=> Support cho cả Windows và Linux



&nbsp;	- FSX chỉ tính theo chi phí dung lượng sử dụng

&nbsp;	- Hỗ trợ tính năng DEDUPLICATION (CHỐNG TRÙNG LẶP DỮ LIỆU) -> giảm chi phí 30-50% cho các trường hợp sử dụng thông thường 



* AWS APPLICATION MIGRATION SERVICE (MGN)

&nbsp;	- Dùng để migrate và replicate phục vụ mục đích xây dựng Disaster Recovery Site cho các máy chủ thực - ảo lên môi trường AWS

&nbsp;	- Application Migration Service liên tục sao chép các máy chủ nguồn sang EC2 Instance trên tài khoản AWS (async/sync)



&nbsp;	- MGN trong quá trình sao chép sẽ sử dụng các staging có số lượng và quy mô cấu nhìn nhỏ hơn máy chủ gốc rất nhiều

&nbsp;	- Khi thực hiệt cut-over MGN sẽ tự động tạo và chạy các máy chủ EC2 trên AWS

&nbsp;	

