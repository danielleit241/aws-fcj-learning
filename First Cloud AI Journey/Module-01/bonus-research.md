==============================================================

NGHIÊN CỨU BỔ SUNG: AWS WELL ARCHITECTED FRAMEWORK



? Các khái niệm, nguyên tắc thiết kế và biện pháp thực hành tốt nhất về kiến trúc để thiết kế và vận hành hệ thống của ta trong môi trường cloud

? Trả lời các câu hỏi qua đó ta sẽ biết được mức độ phù hợp giữa các kiến trúc

? Sử dụng AWS WAF tích hợp trên AWS Management Console -> cải thiện kiến trúc của mình





* KHÁI NIỆM CỦA WAF:

&nbsp;	- AWS Well Architected Framework (WAF) là BỘ NGUYÊN TẮC VÀ CÂU HỎI giúp ta kiểm tra -> cải thiện kiến trúc hệ thống trên AWS -> an toàn, ổn định, nhanh và tiết kiệm chi phí

&nbsp;	- Workload = một phần áp dụng/ứng dụng bạn muốn đánh giá



* TỔNG CỘNG CÓ 6 TRỤ CỘT:

&nbsp;	- Operational Excellence:

&nbsp;		+ Có cách vận hành rõ ràng, tự động và dễ khôi phục

&nbsp;		+ Ví dụ: Dùng CI/CD để deploy tự động

&nbsp;	- Security:

&nbsp;		+ Bảo vệ dữ liệu và quyền truy cập

&nbsp;		+ Không dùng Root Account để làm việc; mà tạo IAM User với các quyền tối thiểu

&nbsp;	- Reliability:

&nbsp;		+ Hệ thống chịu lỗi và tự phục hồi

&nbsp;		+ Ví dụ: Dùng 2 AZs, và backup các database quan trọng 

&nbsp;	- Cost optimization:

&nbsp;		+ Không lãng phí tiền với những dịch vụ ít, ko sử dụng

&nbsp;		+ Dùng các budget types để quản lý các chi tiêu và cảnh báo

&nbsp;	- Sustainability:

&nbsp;		+ Giảm các tác động môi trường (dùng tài nguyên một cách hiệu quả)

&nbsp;		+ Chọn các serverless nếu có thể



* HOẶC ĐƠN GIẢN HƠN TA CÓ THỂ DÙNG WELL ARCHITECTED TOOL





* Các câu hỏi cơ bản:

&nbsp;	- Security: “Ai có quyền truy cập dữ liệu này?” → Nếu câu trả lời là ‘mọi người’, đó là rủi ro.



&nbsp;	- Reliability: “Nếu 1 server chết, hệ thống có tiếp tục hoạt động không?” → nếu không → cần multi-AZ hoặc backup.



&nbsp;	- Cost: “Có tài nguyên nào chạy 24/7 mà không cần không?” → nếu có → tắt khi không cần.

