# AWS Cloud Practitioner Practice - Set 1

## Cloud Concepts

### Câu 1

A rapidly growing e-commerce startup is launching its platform and **expects significant fluctuations** in **customer traffic**, especially during **sales events**.

They need to ensure their infrastructure can **handle peak loads** without over-provisioning and incurring unnecessary costs during **low traffic periods**.

Which benefit of the AWS Cloud is most relevant to this scenario?

A. Increased compliance

B. Predictable operational expenditure

C. Elasticity

D. Fixed capacity planning

**Đáp án:** C. Elasticity

**Giải thích:**

✔ C is correct: Elasticity allows automatically scaling resources up or down based on demand, optimizing costs and performance.

✖ A: Compliance is a separate benefit, not directly related to dynamic capacity.

✖ B: While AWS can lead to predictable operational expenditure, elasticity specifically addresses dynamic scaling, not just cost predictability.

✖ D: AWS elasticity removes the need for manual and fixed capacity planning.

---

### Câu 2

A global software company wants to **deploy a new application** that needs to be accessible to users in **various continents** with **minimal latency**.

They also want to **ensure high fault tolerance** for their service. What key advantage of AWS's global infrastructure does this scenario highlight?

A. Reduced manual operations

B. Broad network access

C. High availability and global reach

D. Simplified security audits

**Đáp án:** C. High availability and global reach

**Giải thích:**

✔ C is correct: AWS's global infrastructure, with multiple regions and Availability Zones, provides high availability and allows deploying services closer to users for lower latency.

✖ A: While AWS reduces manual operations, this isn't the primary advantage highlighted for global low latency and fault tolerance.

✖ B: Broad network access refers to accessibility over the internet, not specifically the global distribution for performance and fault tolerance.

✖ D: While security is a benefit, simplified security audits are not the direct advantage of global infrastructure in this context.

---

### Câu 3

A small consulting firm is considering **migrating its on-premises** customer relationship management (CRM) system **to the cloud**.

Their **primary concern** is **reducing upfront costs** for hardware and software licenses. Which economic benefit of the AWS Cloud directly addresses this concern?

A. Pay-as-you-go pricing

B. Increased agility

C. Managed services

D. Global infrastructure

**Đáp án:** A. Pay-as-you-go pricing

**Giải thích:**

✔ A is correct: Pay-as-you-go pricing eliminates the need for large upfront capital expenditures on hardware and software.

✖ B: Agility refers to speed and flexibility, not directly the cost model for upfront investment.

✖ C: Managed services reduce operational burden but don't directly speak to upfront capital reduction.

✖ D: Global infrastructure relates to worldwide deployment, not initial cost avoidance

---

### Câu 4

A government agency requires that their cloud provider **allows them to access computing resources programmatically** via **APIs and a management console**, without needing to interact with a human from the provider for each resource request.

Which characteristic of cloud computing does this requirement represent?

A. Resource pooling

B. Measured service

C. On-demand self-service

D. Broad network access

**Đáp án:** C. On-demand self-service

**Giải thích:**

✔ C is correct: On-demand self-service means consumers can provision computing capabilities, such as server time and network storage, as needed automatically without requiring human interaction with each service provider.

✖ A: Resource pooling describes shared resources across multiple consumers.

✖ B: Measured service refers to the ability to monitor, control, and report usage.

✖ D: Broad network access means capabilities are available over the network and accessed through standard mechanisms.

---

### Câu 5

A game development studio **frequently experiments** with **new game mechanics** and **requires rapid iteration cycles**.

They need an environment where they can **quickly provision and de-provision resources** for **testing** without significant financial overhead if an experiment fails.

Which AWS benefit directly supports this approach?

A. Longer release cycles

B. Manual capacity planning

C. Agility and the ability to experiment quickly

D. Capital expense

**Đáp án:** C. Agility and the ability to experiment quickly

**Giải thích:**

✔ C is correct: AWS allows for rapid provisioning and de-provisioning of resources, enabling teams to experiment and iterate quickly with minimal risk.

✖ A: AWS promotes shorter, faster release cycles, not longer ones.

✖ B: AWS elasticity removes the need for manual capacity planning, supporting quicker experimentation.

✖ D: While AWS reduces capital expense, the benefit here is about the speed and low risk of experimentation.

---

## Cloud Technology & Services

### Câu 1

A startup is building a **new customer-facing application** that **requires a traditional relational database**.

They have **limited operational staff** and want to **avoid the overhead of managing** database servers, including patching, backups, and scaling.

Which AWS service should the company choose to run their relational database with minimal management effort?

A. Amazon RDS

B. Amazon Redshift

C. Amazon DynamoDB

D. Amazon Aurora Serverless

**Đáp án:** A. Amazon RDS

**Giải thích:**

✔ A is correct: Amazon Relational Database Service (RDS) is a fully managed service that makes it easy to set up, operate, and scale a relational database in the cloud.

✖ B: Redshift is a data warehousing service, not a general-purpose relational database.

✖ C: DynamoDB is a NoSQL database, not relational.

✖ D: Aurora Serverless is a specific type of relational database in RDS, but RDS is the overarching service for managed relational databases.

---

### Câu 2

A software development team is **modernizing their application** by **containerizing** it using **Docker**.

They want to **deploy these containers** on AWS but explicitly **do not want to provision, manage, or scale** the underlying virtual machines that host the containers.

Which AWS service allows them to run their Docker containers without managing servers?

A. AWS Fargate

B. Amazon EC2

C. AWS Lambda

D. Amazon ECS (with EC2 launch type)

**Đáp án:** A. AWS Fargate

**Giải thích:**

✔ A is correct: AWS Fargate is a serverless compute engine for containers that works with both Amazon ECS and Amazon EKS, allowing you to run containers without managing servers or clusters.

✖ B: EC2 requires manual server provisioning and maintenance.

✖ C: Lambda runs serverless functions, not full container workloads in the same way.

✖ D: ECS with EC2 launch type still requires you to manage the underlying EC2 instances.

---

### Câu 3

A company **is redesigning** its **monolithic** e-commerce application into **microservices**.

They want to ensure that **different microservices** can **communicate asynchronously** and reliably, even if one service is temporarily unavailable, to improve overall system **resilience**.

Which AWS service provides **a scalable message queuing** solution for decoupling these microservices?

A. Amazon SQS

B. Amazon SNS

C. Amazon MQ

D. AWS Step Functions

**Đáp án:** A. Amazon SQS

**Giải thích:**

✔ A is correct: Amazon Simple Queue Service (SQS) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications.

✖ B: SNS (Simple Notification Service) is a pub/sub messaging service, primarily for broadcasting messages to multiple subscribers, not for message queuing between services.

✖ C: MQ (Managed Message Queue) supports open standard APIs (like AMQP, MQTT) for legacy applications, often for easier migration. SQS is generally preferred for cloud-native decoupling.

✖ D: Step Functions orchestrate workflows composed of multiple steps, not primarily for general message queuing.

---

### Câu 4

A digital archiving company needs to **store petabytes** of **infrequently accessed** but **highly critical historical** documents and media files.

They require **extreme durability**, virtually **unlimited storage** capacity, and **the ability to retrieve** any file when needed, without managing underlying infrastructure.

Which AWS service is best suited for this requirement?

A. Amazon S3

B. Amazon EFS

C. Amazon RDS

D. AWS Backup

**Đáp án:** A. Amazon S3

**Giải thích:**

✔ A is correct: Amazon S3 (Simple Storage Service) is an object storage service offering industry-leading scalability, data availability, security, and performance, suitable for storing and retrieving any amount of unstructured data.

✖ B: EFS (Elastic File System) is a scalable file storage for EC2 instances, not primarily for massive unstructured data archiving.

✖ C: RDS (Relational Database Service) stores structured relational data.

✖ D: AWS Backup is a service for centralizing and automating data protection, not the primary storage service itself.

---

### Câu 5

A popular news website experiences **varying levels of traffic** throughout the day, with **major spikes** during breaking news events.

They have **multiple Amazon EC2 instances** serving their web application and need to **distribute incoming web traffic** efficiently across these instances to ensure responsiveness and **high availability**.

Which AWS service should be used to **automatically distribute** incoming application traffic across multiple EC2 instances?

A. Elastic Load Balancing (ELB)

B. Amazon Route 53

C. AWS Auto Scaling

D. AWS CloudFront

**Đáp án:** A. Elastic Load Balancing (ELB)

**Giải thích:**

✔ A is correct: Elastic Load Balancing (ELB) automatically distributes incoming application traffic across multiple targets, such as EC2 instances, in multiple Availability Zones, ensuring high availability and fault tolerance.

✖ B: Amazon Route 53 is a DNS web service that routes user requests to internet applications.

✖ C: AWS Auto Scaling automatically adjusts the number of EC2 instances based on demand, but ELB is responsible for distributing traffic among those instances.

✖ D: AWS CloudFront is a Content Delivery Network (CDN) for delivering content to users with low latency, not for balancing traffic across EC2 instances.

---

## Security & Compliance

### Câu 1

A **large enterprise** manages **hundreds of AWS accounts** for different departments and projects.

They need a way to **centrally** apply security policies, audit compliance, and manage user access **across all these accounts** from a **single point**.

Which AWS service is designed for this purpose?

A. Amazon GuardDuty
B. AWS IAM
C. AWS Organizations
D. AWS Shield

**Đáp án:** C. AWS Organizations

**Giải thích:**

✔ C is correct: AWS Organizations allows you to centrally manage and govern your environment as you grow and scale your AWS resources, including applying Service Control Policies (SCPs) across accounts.

✖ A: GuardDuty is for threat detection.

✖ B: IAM manages identities and permissions within a single account, not across multiple accounts centrally for governance.

✖ D: AWS Shield is for DDoS protection.

---

### Câu 2

A web development company **hosts several customer-facing applications** on **Amazon EC2** instances.

They recently faced issues with common **web attacks** such as **SQL injection and cross-site scripting (XSS)**.

Which AWS service should they implement to protect these web applications from such exploits?

A. AWS WAF
B. AWS IAM
C. Amazon Inspector
D. AWS Trusted Advisor

**Đáp án:** A. AWS WAF

**Giải thích:**

✔ A is correct: AWS WAF (Web Application Firewall) helps protect web applications from common web exploits that could affect application availability, compromise security, or consume excessive resources.

✖ B: IAM handles access control, not web application firewalling.

✖ C: Inspector scans EC2 instances for vulnerabilities, not for filtering web traffic exploits.

✖ D: Trusted Advisor provides best practice recommendations, not active protection.

---

### Câu 3

An IT administrator needs to ensure that developers **only have permission** to read from **specific Amazon S3 buckets** and launch only a particular **type of EC2 instance** in their **development account**.

They want to **define granular permissions** for each user and resource interaction.

Which AWS feature allows for this precise control over actions?

A. Amazon Macie
B. IAM policies
C. AWS KMS
D. AWS CloudTrail

**Đáp án:** B. IAM policies

**Giải thích:**

✔ B is correct: IAM policies are JSON documents that define permissions for an identity or resource, allowing fine-grained control over actions on AWS resources.

✖ A: Macie detects sensitive data.

✖ C: KMS is for encryption key management.

✖ D: CloudTrail logs API activity, it doesn't define permissions.

---

### Câu 4

A company is running a database on Amazon RDS. They are responsible for **patching the database software** and **managing user access credentials** for the database.

AWS is responsible for the **underlying infrastructure**, including physical security of the servers and patching the operating system of the RDS instance.

Which aspect of the AWS Shared Responsibility Model does this exemplify?

A. AWS is responsible for everything in a managed service.
B. The customer is responsible for patching and user access.
C. AWS is responsible for the application, and the customer is responsible for the infrastructure.
D. The customer is responsible for security in the cloud, and AWS is responsible for security of the cloud.

**Đáp án:** D. The customer is responsible for security in the cloud, and AWS is responsible for security of the cloud.

**Giải thích:**

✔ D is correct: For managed services like RDS, AWS manages the of the cloud aspects (infrastructure, OS patching), while the customer manages in the cloud aspects (database configuration, user access, data encryption).

✖ A: Incorrect; customers still have responsibilities even with managed services.

✖ B: While true, it's a specific example of the broader Shared Responsibility Model.

✖ C: Incorrect; AWS manages the underlying infrastructure, not the application itself for a service like RDS.

---

### Câu 5

A healthcare provider **stores electronic health records (EHR) in Amazon S3**.

Due to **strict HIPAA** compliance requirements, **all sensitive data** must be **encrypted** both at rest and in transit.

Which AWS service is best suited to help the healthcare provider manage the **encryption keys** used for this **sensitive data**?

A. AWS IAM
B. Amazon Macie
C. AWS Key Management Service (KMS)
D. AWS CloudTrail

**Đáp án:** C. AWS Key Management Service (KMS)

**Giải thích:**

✔ C is correct: AWS Key Management Service (KMS) is a managed service that makes it easy for you to create and control the encryption keys used to encrypt your data.

✖ A: IAM handles access control, not encryption key management.

✖ B: Macie detects sensitive data, it doesn't manage encryption keys.

✖ D: CloudTrail logs API activity, it doesn't manage encryption keys.

---

## Billing, Pricing & Support

### Câu 1

A **large enterprise** has **several departments**, and **each department** has its own set of **AWS resources**.

The finance department **needs to track and allocate** AWS costs accurately to each specific department to better manage budgets.

Which AWS feature should they implement to **break down billing per department**?

A. AWS Trusted Advisor

B. Consolidated Billing

C. Cost Allocation Tags

D. Amazon CloudWatch Logs

**Đáp án:** C. Cost Allocation Tags

**Giải thích:**

✔ C is correct: Cost Allocation Tags are labels that you can attach to your AWS resources to organize them. AWS generates a cost allocation report with your usage and costs categorized by these tags, allowing you to easily track costs by department, project, or other criteria.

✖ A: Trusted Advisor provides best practice recommendations, not billing breakdowns.

✖ B: Consolidated Billing aggregates bills from multiple accounts into a single bill, but it doesn't break down costs within accounts by department unless tags are used.

✖ D: CloudWatch Logs monitor application and system logs, not directly related to cost allocation.

---

### Câu 2

The finance team of a growing tech company wants to **understand their historical** AWS spending patterns over the past year and **accurately forecast future costs** for the next quarter.

They need a tool that provides **visual reports** and allows them to **identify cost trends and anomalies**.

Which AWS tool provides a visualization of historical usage and cost data, and supports forecasting?

A. AWS Budgets

B. AWS Cost Explorer

C. AWS Marketplace

D. AWS Config

**Đáp án:** B. AWS Cost Explorer

**Giải thích:**

✔ B is correct: AWS Cost Explorer is a free tool that allows you to view and analyze your AWS costs and usage. You can visualize your cost and usage data at a high level (e.g., total costs for all accounts) or analyze it by specific dimensions (e.g., service, region, tags) and also forecast future costs.

✖ A: AWS Budgets allows you to set custom budgets and receive alerts when your costs or usage exceed (or are forecasted to exceed) your budgeted amount. It doesn't primarily focus on historical visualization and forecasting.

✖ C: AWS Marketplace is an online software store.

✖ D: AWS Config tracks resource configurations and changes, not costs.

---

### Câu 3

A company has a **predictable, steady-state workload running on Amazon EC2** instances that will operate **for at least 3 years**.

They are evaluating **different pricing models** to **optimize costs**. They are considering both **EC2 Reserved Instances and Savings Plans.**

What is a **key benefit** of **using Savings Plans over Reserved Instances** for this type of workload?

A. Savings Plans require a larger upfront payment compared to Reserved Instances.

B. Savings Plans are less flexible and apply only to specific instance types in a single Region.

C. Savings Plans offer more flexibility across compute usage, applying across instance families, sizes, and even different compute services like Fargate and Lambda.

D. Reserved Instances offer better savings for predictable, long-term workloads.

**Đáp án:** C. Savings Plans offer more flexibility across compute usage, applying across instance families, sizes, and even different compute services like Fargate and Lambda.

**Giải thích:**

✔ C is correct: Savings Plans offer significant savings (up to 72%) on compute usage and provide more flexibility compared to Reserved Instances. They apply across EC2 instance family, size, OS, tenancy, and AWS Region, and also cover Fargate and Lambda usage.

✖ A: Savings Plans offer flexible payment options including No Upfront, Partial Upfront, or All Upfront. They don't necessarily require a larger upfront payment.

✖ B: This describes the limitations of Reserved Instances, not Savings Plans. Savings Plans are more flexible.

✖ D: While both offer significant savings, Savings Plans generally offer similar or better savings with much greater flexibility for many long-term, consistent workloads.

---

### Câu 4

A **small startup** is operating on a **tight budget** and is **worried about unexpected increases** in their monthly AWS bill as their usage grows.

They want to be **immediately notified** if their AWS charges for the month **exceed a predefined limit**, so they can take action to control costs.

Which AWS service allows them to **set alerts** when their usage or costs **exceed a threshold**?

A. AWS Billing Dashboard

B. AWS Budgets

C. AWS Cost Explorer

D. AWS Organizations

**Đáp án:** B. AWS Budgets

**Giải thích:**

✔ B is correct: AWS Budgets allows you to set custom budgets to track your costs and usage from the simplest to the most complex use cases. You can create budgets to alert you when your costs or usage exceed (or are forecasted to exceed) your budgeted amount.

✖ A: The AWS Billing Dashboard displays your current and past charges but does not send proactive alerts.

✖ C: Cost Explorer is for visualizing and analyzing historical and forecasted costs, but it's not primarily an alerting service.

✖ D: AWS Organizations helps manage multiple AWS accounts but does not directly provide budgeting and alerting features for individual accounts or budgets.

---

### Câu 5

A company is launching a new batch processing application that will **run continuously for the next three years**, with a **very consistent and predictable compute demand.**

They are looking for **the most cost-effective** purchasing option for their Amazon EC2 instances to **maximize savings** over this long-term commitment.

Which purchasing option is the most cost-effective for a workload with consistent usage for 3 years?

A. On-Demand Instances

B. Spot Instances

C. Reserved Instances

D. Savings Plans

**Đáp án:** D. Savings Plans

**Giải thích:**

✔ D is correct: Savings Plans offer the deepest discounts (up to 72% off On-Demand) in exchange for a commitment to a consistent amount of compute usage (measured in $/hour) for a 1-year or 3-year term. They provide more flexibility than Reserved Instances.

✖ A: On-Demand Instances are the most expensive option and are best for short-term, unpredictable workloads.

✖ B: Spot Instances offer significant discounts but are suitable only for fault-tolerant workloads that can tolerate interruptions, as they can be terminated by AWS with short notice.

✖ C: Reserved Instances (RIs) offer significant discounts for long-term commitment, but Savings Plans generally offer similar or better savings with much greater flexibility across instance types and compute services.
