# AWS Cloud Practitioner Practice - Set 2

## Cloud Concepts

### Câu 1

A new SaaS company is designing its multi-tenant application on AWS. They are responsible for **managing the application** code, customer data, and network configurations for their application.

AWS is **responsible for the physical security** of the data centers, hardware, and global infrastructure.

Which **aspect of the AWS Shared Responsibility Model** does this scenario illustrate?

A. AWS is responsible for security in the cloud.

B. The customer is responsible for security of the cloud.

C. The customer is responsible for security in the cloud, and AWS is responsible for security of the cloud.

D. Both AWS and the customer share responsibility equally for all aspects.

**Đáp án:** C. The customer is responsible for security in the cloud, and AWS is responsible for security of the cloud.

**Giải thích:**

✔ C is correct: The Shared Responsibility Model states AWS is responsible for the security of the cloud (infrastructure), and the customer is responsible for security in the cloud (their data, applications, configurations).

✖ A: Incorrect, AWS is responsible for security of the cloud.

✖ B: Incorrect, the customer is responsible for security in the cloud.

✖ D: While shared, the responsibilities are distinctly divided, not equally for all aspects.

---

### Câu 2

A major **streaming service** plans to expand its user base to **remote regions with limited internet** infrastructure.

They want to ensure that **content is delivered efficiently** to these users with **optimized performance**.

Which AWS benefit is most crucial for achieving this goal?

A. Enhanced labor cost

B. Fixed infrastructure model

C. Global reach and localized delivery

D. Predictable latency across all locations

**Đáp án:** C. Global reach and localized delivery

**Giải thích:**

✔ C is correct: AWS's global infrastructure, including edge locations and CDNs like CloudFront, allows for content delivery closer to end-users, ensuring global reach and low latency even in remote areas.

✖ A: Labor cost isn't the primary benefit for content delivery optimization.

✖ B: AWS offers a dynamic, not fixed, infrastructure model.

✖ D: While AWS strives for low latency, it's not always perfectly predictable across all varied global network conditions.

---

### Câu 3

A financial trading firm **needs to automate** its **continuous integration and continuous deployment (CI/CD) pipeline** to release new trading algorithms **multiple times a day.**

They **require tools** that integrate seamlessly with their development environment.

Which AWS feature directly enables them to achieve this high velocity of deployment?

A. Long-term hardware provisioning

B. Self-managed data centers

C. Automation and DevOps tools

D. Static resource allocation

**Đáp án:** C. Automation and DevOps tools

**Giải thích:**

✔ C is correct: AWS provides a wide range of automation services (e.g., AWS CodePipeline, CodeBuild) and DevOps tools that streamline the entire software delivery process, enabling faster deployments.

✖ A/B/D: These approaches represent traditional IT challenges that slow down deployment and are not features that enable rapid iteration.

---

### Câu 4

A startup is **developing a new mobile application** and **wants to avoid large upfront** capital expenditures for servers and networking equipment.

They prefer a model where they **only pay** for the computing resources, storage, and bandwidth consumed by their application, **scaling down during low usage**.

Which term best describes this AWS Cloud pricing model?

A. Economies of scale

B. Pay-as-you-go

C. CapEx commitment

D. Licensing upfront

**Đáp án:** B. Pay-as-you-go

**Giải thích:**

✔ B is correct: The pay-as-you-go model means customers only pay for the individual services they use, with no long-term contracts or complex licensing.

✖ A: Economies of scale refer to the cost advantage AWS gains from its massive size, which it passes to customers, but it's not the pricing model itself.

✖ C/D: These terms relate to traditional IT models involving large upfront investments.

---

### Câu 5

A university experiences a **massive surge** in website **traffic during exam registration periods**, which lasts only **a few weeks** each semester.

**Outside of these peaks**, traffic is **significantly lower**. What cloud benefit allows the university to efficiently handle these short-term, fluctuating resource needs without maintaining excess capacity year-round?

A. High latency

B. Elasticity

C. Multi-tenancy

D. Capital investment

**Đáp án:** B. Elasticity

**Giải thích:**

✔ B is correct: Elasticity (or scalability) allows the university to dynamically scale up resources during peak registration and scale down afterwards, paying only for what they use.

✖ A: AWS aims for low latency, not high.

✖ C: Multi-tenancy refers to shared underlying infrastructure, not the ability to scale for fluctuating demand.

✖ D: AWS reduces capital investment, but the specific benefit for short-term needs is scaling.

---

## Cloud Technology & Services

### Câu 1

A pharmaceutical research firm needs to **analyze vast amounts of genomic data**, often in the **petabyte range**, to identify patterns and correlations.

They require a **fully managed service** that can run **open-source big data frameworks** like Apache Spark and Hadoop **without the operational complexity of setting up and managing clusters.**

Which AWS service is most suitable for processing these **large-scale datasets** using distributed computing frameworks?

A. Amazon Athena

B. AWS Glue

C. Amazon EMR

D. Amazon Redshift

**Đáp án:** C. Amazon EMR

**Giải thích:**

✔ C is correct: Amazon EMR (Elastic MapReduce) is a managed cluster platform that simplifies running big data frameworks, such as Apache Hadoop and Apache Spark, on AWS to process and analyze vast amounts of data.

✖ A: Amazon Athena is a serverless query service for S3 data, not a general-purpose big data processing framework.

✖ B: AWS Glue is a serverless data integration service for ETL (Extract, Transform, Load) operations, not for running full-fledged distributed computing frameworks for analysis.

✖ D: Amazon Redshift is a data warehousing service for analytical queries, not designed for general big data processing frameworks.

---

### Câu 2

A smart home device company wants **to process events** generated by their devices (e.g., motion detection, temperature changes) in **real-time**.

They **need a compute service** that can execute **small pieces of code** in response to these events, **without needing to provision or manage any servers**.

Which AWS service allows users to **run serverless code** in **response to events**, such as changes in an S3 bucket or messages in an IoT stream?

A. Amazon EC2

B. AWS Lambda

C. AWS Batch

D. Amazon Elastic Beanstalk

**Đáp án:** B. AWS Lambda

**Giải thích:**

✔ B is correct: AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers. It automatically scales and can be triggered by various AWS services and custom events.

✖ A: EC2 requires managing servers and infrastructure.

✖ C: AWS Batch is for running batch computing jobs, not real-time event-driven functions.

✖ D: Amazon Elastic Beanstalk is for deploying and scaling web applications and services, but it still manages underlying servers.

---

### Câu 3

A global online education platform provides video lectures to students worldwide.

They want to ensure that video content is **delivered with the fastest possible speed** and **lowest latency** to students, regardless of their geographical location.

Which AWS service should they use to **efficiently distribute** their video content globally?

A. Amazon CloudFront

B. Amazon S3

C. Amazon Route 53

D. AWS Global Accelerator

**Đáp án:** A. Amazon CloudFront

**Giải thích:**

✔ A is correct: Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency and high transfer speeds.

✖ B: S3 stores the videos but does not optimize their global delivery.

✖ C: Route 53 is a DNS service that translates domain names to IP addresses, not a content delivery service.

✖ D: Global Accelerator improves application performance for TCP/IP traffic by routing it through the AWS global network, but CloudFront is specifically optimized for content delivery.

---

### Câu 4

A small business is **migrating its legacy application** that uses a **MySQL database**.

They need the **database to be highly available, with automatic failover capabilities, and regular backups handled by AWS**. They have limited database administration expertise.

Which AWS service should they choose to run their MySQL database with these requirements?

A. Amazon DynamoDB

B. Amazon EC2 with MySQL

C. Amazon RDS

D. Amazon Neptune

**Đáp án:** C. Amazon RDS

**Giải thích:**

✔ C is correct: Amazon RDS for MySQL provides managed relational database capabilities, including multi-AZ deployments for high availability with automated failover and automated backups.

✖ A: DynamoDB is a NoSQL database, not compatible with MySQL.

✖ B: Running MySQL on EC2 requires manual setup, management, and configuration of high availability and backups.

✖ D: Neptune is a graph database, not a relational database like MySQL.

---

### Câu 5

A real-time bidding platform for online advertising needs to store rapidly changing session data and user profiles.

This data **requires extremely fast read and write access**, with **sub-millisecond latency**, to support quick decision-making in the bidding process.

Which AWS service should be used for this high-performance, **in-memory data store**?

A. Amazon Aurora

B. Amazon DynamoDB

C. Amazon ElastiCache

D. Amazon Redshift

**Đáp án:** C. Amazon ElastiCache

**Giải thích:**

✔ C is correct: Amazon ElastiCache is a fully managed in-memory caching service that supports Redis and Memcached, providing ultra-fast, sub-millisecond latency for data access.

✖ A: Aurora is a high-performance relational database but is primarily disk-based, not purely in-memory.

✖ B: DynamoDB is a fast NoSQL database, but ElastiCache provides lower latency for in-memory caching use cases.

✖ D: Redshift is a data warehousing service, optimized for analytical queries, not low-latency key-value lookups for operational data.

---

## Security & Compliance

### Câu 1

A security auditor needs to **track all API calls** made **within a company's AWS account** to ensure proper **governance** and **detect any unauthorized** actions.

They need a **chronological record** of all **events** that occurred in the account.

Which AWS service should the auditor use to achieve this?

A. AWS CloudTrail
B. AWS CloudWatch
C. Amazon Macie
D. AWS Secrets Manager

**Đáp án:** A. AWS CloudTrail

**Giải thích:**

✔ A is correct: AWS CloudTrail provides a record of actions taken by a user, role, or an AWS service in AWS. CloudTrail logs all API calls made to your AWS services.

✖ B: CloudWatch is for monitoring and logging performance metrics and application logs, not API activity.

✖ C: Macie is for sensitive data discovery.

✖ D: Secrets Manager securely stores and rotates secrets, not logs API calls.

---

### Câu 2

A development team needs to **grant temporary**, **time-limited access** to an external auditing firm to review specific S3 buckets.

They want to **avoid creating permanent IAM users** for the auditors. What AWS service or feature should they leverage to provide these **temporary credentials** with defined permissions?

A. AWS CloudTrail
B. Amazon Macie
C. AWS IAM Roles
D. Amazon Inspector

**Đáp án:** C. AWS IAM Roles

**Giải thích:**

✔ C is correct: AWS IAM Roles are designed to grant temporary permissions to users or services, ideal for scenarios requiring limited-duration access.

✖ A: CloudTrail logs activities, it doesn't grant access.

✖ B: Macie is for sensitive data detection.

✖ D: Inspector is used for vulnerability scans.

---

### Câu 3

A **DevOps team** manages several applications that rely on **various third-party API keys** and **database credentials**.

They need a **secure way to store, retrieve**, and **automatically rotate** these secrets to enhance their security posture.

Which AWS service provides this functionality?

A. AWS Systems Manager Parameter Store
B. AWS Secrets Manager
C. Amazon S3
D. Amazon Macie

**Đáp án:** B. AWS Secrets Manager

**Giải thích:**

✔ B is correct: AWS Secrets Manager helps you protect secrets needed to access your applications, services, and IT resources. It enables you to easily rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle.

✖ A: Systems Manager Parameter Store can store secrets but **lacks the automatic rotation** and comprehensive management features of Secrets Manager.

✖ C: S3 is object storage and not designed for secure secret management and rotation.

✖ D: Macie scans for sensitive data, not secure storage and rotation of credentials.

---

### Câu 4

A security operations center (SOC) needs to **continuously monitor** their **AWS environment** for potential threats, unusual API calls, and suspicious network activity.

They want an **automated service** that can **detect and alert** on **malicious or unauthorized** behavior.

Which AWS service is specifically designed for intelligent threat detection?

A. AWS WAF
B. AWS GuardDuty
C. Amazon CloudWatch
D. AWS Config

**Đáp án:** B. AWS GuardDuty

**Giải thích:**

✔ B is correct: Amazon GuardDuty is a continuous security monitoring service that analyzes and processes VPC Flow Logs, AWS CloudTrail management event logs, and DNS logs. It uses threat intelligence feeds and machine learning to identify malicious activity and unauthorized behavior.

✖ A: WAF protects web applications, not the entire AWS environment for general threat detection.

✖ C: CloudWatch monitors performance and logs but doesn't inherently provide intelligent threat detection.

✖ D: Config tracks resource compliance and changes, not malicious activity.

---

### Câu 5

A telecommunications company **frequently** experiences distributed denial-of-service **(DDoS) attacks** targeting their public-facing applications **during peak** customer service hours.

They need an AWS service that can **protect their applications** from these volumetric and protocol-based attacks.

What is the **primary purpose of AWS Shield** in this scenario?

A. To detect insider threats
B. To protect web applications from XSS attacks
C. To protect against DDoS attacks
D. To encrypt sensitive data at rest

**Đáp án:** C. To protect against DDoS attacks

**Giải thích:**

✔ C is correct: AWS Shield is a managed DDoS protection service that safeguards applications running on AWS.

✖ A/B/D: These are not the primary functions of AWS Shield. XSS protection is primarily handled by AWS WAF.

---

## Billing, Pricing & Support

### Câu 1

A student is learning about AWS and wants to explore various services without incurring costs.

They want to **understand which services they can use for free**, up to **certain limits**, during their first year of using AWS.

Which of the following is typically included in the AWS Free Tier for new customers?

A. 1 TB of Amazon S3 Standard storage per month.

B. 750 hours/month of Amazon EC2 t2.micro or t3.micro for 12 months.

C. 1 year of AWS Support at the Business level.

D. Unlimited AWS Lambda function executions.

**Đáp án:** B. 750 hours/month of Amazon EC2 t2.micro or t3.micro for 12 months.

**Giải thích:**

✔ B is correct: The AWS Free Tier typically includes 750 hours per month of Amazon EC2 t2.micro or t3.micro (depending on region availability) instances for the first 12 months, along with other free usage tiers for services like S3 and Lambda.

✖ A: The S3 Free Tier includes 5 GB of S3 Standard storage, not 1 TB.

✖ C: AWS Support plans are paid services; the Basic Support plan is included for all AWS customers, but it does not offer 1 year of Business level support for free.

✖ D: AWS Lambda has a free tier for a certain number of requests and compute time, but it's not unlimited.

---

### Câu 2

A **large enterprise** requires the **highest level of support** for their mission-critical AWS workloads.

They need **24/7 access to Cloud Support Engineers** via phone, email, and chat, a designated Technical Account Manager (TAM) for proactive guidance, and access to the AWS Concierge Service for billing and account inquiries.

Which AWS Support Plan provides these features?

A. Developer

B. Basic

C. Business

D. Enterprise

**Đáp án:** D. Enterprise

**Giải thích:**

✔ D is correct: The AWS Enterprise Support plan offers 24/7 technical support from Cloud Support Engineers, a designated Technical Account Manager (TAM), and access to the Concierge Service for billing and account inquiries.

✖ A: Developer Support provides business-hours email access to Cloud Support Associates.

✖ B: Basic Support is included for all AWS customers and offers limited resources like documentation and billing support.

✖ C: Business Support offers 24/7 access to Cloud Support Engineers via phone, email, and chat, but does not include a designated TAM or Concierge Service.

---

### Câu 3

A startup is running a **critical production application** and **needs 24/7 access** to technical **support via phone and email.**

They require a **response time of less than 1 hour for production system-down issues** but do not have the budget for a **dedicated Technical Account Manager (TAM).**

Which AWS Support plan is the most appropriate and cost-effective choice?

A. Basic

B. Developer

C. Business

D. Enterprise

**Đáp án:** C. Business

**Giải thích:**

✔ C is correct: The AWS Business Support plan provides 24/7 access to Cloud Support Engineers via phone, email, and chat, with a < 1-hour response time for production system down issues. It is the most suitable plan without the added cost of a TAM that comes with the Enterprise plan.

✖ A: Basic Support does not offer technical support or guaranteed response times.

✖ B: Developer Support only provides business-hour email support with slower response times.

✖ D: Enterprise Support includes a TAM and is the most expensive plan, exceeding the company's budgetary constraints mentioned.

---

### Câu 4

A company needs to run a **short-term data analysis** job that can be **interrupted without causing issues.**

They want to use **Amazon EC2 instances** at the **lowest possible cost**. Which EC2 purchasing option should they choose?

A. On-Demand Instances

B. Reserved Instances

C. Spot Instances

D. Dedicated Hosts

**Đáp án:** C. Spot Instances

**Giải thích:**

✔ C is correct: Spot Instances offer the largest discounts on EC2 compute capacity (up to 90% off On-Demand prices). They are ideal for fault-tolerant, flexible workloads that can withstand interruptions, as AWS can reclaim the capacity with a short notice.

✖ A: On-Demand Instances are more expensive and are for workloads that cannot be interrupted.

✖ B: Reserved Instances require a 1 or 3-year commitment and are for steady-state workloads.

✖ D: Dedicated Hosts are physical servers dedicated for your use and are the most expensive option, typically used for compliance or licensing reasons.

---

### Câu 5

A finance department wants to **visualize the company's AWS spending over the last 6 months**, filter costs by specific AWS services and linked accounts, and get a **forecast of spending for the next 3 months.**

Which AWS tool should they use?

A. AWS Budgets

B. AWS Cost Explorer

C. AWS Pricing Calculator

D. AWS Trusted Advisor

**Đáp án:** B. AWS Cost Explorer

**Giải thích:**

✔ B is correct: AWS Cost Explorer has an easy-to-use interface that lets you visualize, understand, and manage your AWS costs and usage over time. It includes default reports and forecasting capabilities.

✖ A: AWS Budgets is used to set spending limits and receive alerts, not for detailed visualization and forecasting.

✖ C: AWS Pricing Calculator is for estimating the cost of a _future_ workload, not for analyzing past spending.

✖ D: AWS Trusted Advisor provides optimization recommendations but is not a cost analysis tool.
