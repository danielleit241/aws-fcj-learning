### Câu 1
Which AWS service is used to provide encryption for Amazon EBS?

A.
AWS Certificate Manager
B.
AWS Systems Manager
C.
AWS KMS
D.
AWS Config

**Đáp án: C**

---

### Câu 2
Which of the following is a recommended design principle for AWS Cloud architecture?

A.
Design tightly coupled components.
B.
Build a single application component that can handle all the application functionality.
C.
Make large changes on fewer iterations to reduce chances of failure.
D.
Avoid monolithic architecture by segmenting workloads.

**Đáp án: D**

---

### Câu 3
A company is designing its AWS workloads so that components can be updated regularly and so that changes can be made in small, reversible increments. Which pillar of the AWS Well-Architected Framework does this design support?

A.
Security
B.
Performance efficiency
C.
Operational excellence
D.
Reliability

**Đáp án: C**

---

### Câu 4
A company has a workload that will run continuously for 1 year. The workload cannot tolerate service interruptions. Which Amazon EC2 purchasing option will be MOST cost-effective?

A.
All Upfront Reserved Instances
B.
Partial Upfront Reserved Instances
C.
Dedicated Instances
D.
On-Demand Instances

**Đáp án: A**

---

### Câu 5
Which AWS service helps protect against DDoS attacks?

A.
AWS Shield
B.
Amazon Inspector
C.
Amazon GuardDuty
D.
Amazon Detective

**Đáp án: A**

---

### Câu 6
Which AWS tool or feature acts as a VPC firewall at the subnet level?

A.
Security group
B.
Network ACL
C.
Traffic Mirroring
D.
Internet gateway

**Đáp án: B**

---

### Câu 7
Which AWS service can be used to decouple applications?

A.
AWS Config
B.
Amazon Simple Queue Service (Amazon SQS)
C.
AWS Batch
D.
Amazon Simple Email Service (Amazon SES)

**Đáp án: B**

---

### Câu 8
Which disaster recovery option is the LEAST expensive?

A.
Warm standby
B.
Multisite
C.
Backup and restore
D.
Pilot light

**Đáp án: C**

---

### Câu 9
Which type of AWS storage is ephemeral and is deleted when an Amazon EC2 instance is stopped or terminated?

A.
Amazon Elastic Block Store (Amazon EBS)
B.
Amazon EC2 instance store
C.
Amazon Elastic File System (Amazon EFS)
D.
Amazon S3

**Đáp án: B**

---

### Câu 10
Which of the following is a characteristic of the AWS account root user?

A.
The root user is the only user that can be configured with multi-factor authentication (MFA).
B.
The root user is the only user that can access the AWS Management Console.
C.
The root user is the first sign-in identity that is available when an AWS account is created.
D.
The root user has a password that cannot be changed.

**Đáp án: C**

---

### Câu 11
A company hosts an application on an Amazon EC2 instance. The EC2 instance needs to access several AWS resources, including Amazon S3 and Amazon DynamoDB. What is the MOST operationally efficient solution to delegate permissions?

A.
Create an IAM role with the required permissions. Attach the role to the EC2 instance.
B.
Create an IAM user and use its access key and secret access key in the application.
C.
Create an IAM user and use its access key and secret access key to create a CLI profile in the EC2 instance
D.
Create an IAM role with the required permissions. Attach the role to the administrative IAM user.

**Đáp án: A**

---

### Câu 12
Which of the following is a component of the AWS Global Infrastructure?

A.
Amazon Alexa
B.
AWS Regions
C.
Amazon Lightsail
D.
AWS Organizations

**Đáp án: B**

---

### Câu 13
What is the purpose of having an internet gateway within a VPC?

A.
To create a VPN connection to the VPC
B.
To allow communication between the VPC and the internet
C.
To impose bandwidth constraints on internet traffic
D.
To load balance traffic from the internet across Amazon EC2 instances

**Đáp án: B**

---

### Câu 14
Which AWS service allows users to download security and compliance reports about the AWS infrastructure on demand?

A.
Amazon GuardDuty
B.
AWS Security Hub
C.
AWS Artifact
D.
AWS Shield

**Đáp án: C**

---

### Câu 15
A company is planning an infrastructure deployment to the AWS Cloud. Before the deployment, the company wants a cost estimate for running the infrastructure. Which AWS service or feature can provide this information?

A.
Cost Explorer
B.
AWS Trusted Advisor
C.
AWS Cost and Usage Report
D.
AWS Pricing Calculator

**Đáp án: D**

---

### Câu 16
Which AWS service of tool helps to centrally manage billing and allow controlled access to resources across AWS accounts?

A.
AWS Identity and Access Management (IAM)
B.
AWS Organizations
C.
Cost Explorer
D.
AWS Budgets

**Đáp án: B**

---

### Câu 17
Which of the following are Amazon Virtual Private Cloud (Amazon VPC) resources?

A.
Objects; access control lists (ACLs)
B.
Subnets; internet gateways
C.
Access policies; buckets
D.
Groups; roles

**Đáp án: B**

---

### Câu 18
A company needs to identify the last time that a specific user accessed the AWS Management Console. Which AWS service will provide this information?

A.
Amazon Cognito
B.
AWS CloudTrail
C.
Amazon Inspector
D.
Amazon GuardDuty

**Đáp án: B**

---

### Câu 19
A company launched an Amazon EC2 instance with the latest Amazon Linux 2 Amazon Machine Image (AMI). Which actions can a system administrator take to connect to the EC2 instance? (Choose two.)

A. Use Amazon EC2 Instance Connect.
B. Use a Remote Desktop Protocol (RDP) connection.
C. Use AWS Batch
D. Use AWS Systems Manager Session Manager.
E. Use Amazon Connect

**Đáp án: A, D**

---

### Câu 20
A company wants to perform sentiment analysis on customer service email messages that it receives. The company wants to identify whether the customer service engagement was positive or negative. Which AWS service should the company use to perform this analysis?

A.
Amazon Textract
B.
Amazon Translate
C.
Amazon Comprehend
D.
Amazon Rekognition

**Đáp án: C**

---

### Câu 21
What is the total amount of storage offered by Amazon S3?

A.
100MB
B.
5 GB
C.
5 TB
D.
Unlimited

**Đáp án: D**

---

### Câu 22
A company is migrating to Amazon S3. The company needs to transfer 60 TB of data from an on-premises data center to AWS within 10 days. Which AWS service should the company use to accomplish this migration?

A.
Amazon S3 Glacier
B.
AWS Database Migration Service (AWS DMS)
C.
AWS Snowball
D.
AWS Direct Connect

**Đáp án: C**

---

### Câu 23
What type of database is Amazon DynamoDB?

A.
In-memory
B.
Relational
C.
Key-value
D.
Graph

**Đáp án: C**

---

### Câu 24
A large organization has a single AWS account. What are the advantages of reconfiguring the single account into multiple AWS accounts? (Choose two.)

A. It allows for administrative isolation between different workloads.
B. Discounts can be applied on a quarterly basis by submitting cases in the AWS Management Console.
C. Transitioning objects from Amazon S3 to Amazon S3 Glacier in separate AWS accounts will be less expensive.
D. Having multiple accounts reduces the risks associated with malicious activity targeted at a single account.
E. Amazon QuickSight offers access to a cost tool that provides application-specific recommendations for environments running in multiple accounts.

**Đáp án: A, D**

---

### Câu 25
A retail company has recently migrated its website to AWS. The company wants to ensure that it is protected from SQL injection attacks. The website uses an Application Load Balancer to distribute traffic to multiple Amazon EC2 instances. Which AWS service or feature can be used to create a custom rule that blocks SQL injection attacks?

A.
Security groups
B.
AWS WAF
C.
Network ACLs
D.
AWS Shield

**Đáp án: B**

---

### Câu 26
Which of the following is an advantage that users experience when they move on-premises workloads to the AWS Cloud?

A.
Elimination of expenses for running and maintaining data centers
B.
Price discounts that are identical to discounts from hardware providers
C.
Distribution of all operational controls to AWS
D.
Elimination of operational expenses

**Đáp án: A**

---

### Câu 27
Which AWS services offer gateway VPC endpoints that can be used to avoid sending traffic over the internet? (Choose two.)

A. Amazon Simple Notification Service (Amazon SNS)
B. Amazon Simple Queue Service (Amazon SQS)
C. AWS CodeBuild
D. Amazon S3
E. Amazon DynamoDB

**Đáp án: D, E**

---

### Câu 28
Why is an AWS Well-Architected review a critical part of the cloud design process?

A.
A Well-Architected review is mandatory before a workload can run on AWS.
B.
A Well-Architected review helps identify design gaps and helps evaluate design decisions and related documents.
C.
A Well-Architected review is an audit mechanism that is a part of requirements for service level agreements.
D.
A Well-Architected review eliminates the need for ongoing auditing and compliance tests.

**Đáp án: B**

---

### Câu 29
A company implements an Amazon EC2 Auto Scaling policy along with an Application Load Balancer to automatically recover unhealthy applications that run on Amazon EC2 instances. Which pillar of the AWS Well-Architected Framework does this action cover?

A.
Security
B.
Performance efficiency
C.
Operational excellence
D.
Reliability

**Đáp án: D**

---

### Câu 30
What does the AWS Concierge Support team provide?

A.
A technical expert dedicated to the user
B.
A primary point of contact for AWS Billing and AWS Support
C.
A partner to help provide scaling guidance for an event launch
D.
A dedicated AWS staff member who reviews the user's application architecture

**Đáp án: B**

---

### Câu 31
A company needs to generate reports that can break down cloud costs by product, by company-defined tags, and by hour, day, and month. Which AWS tool should the company use to meet these requirements?

A.
Reserved Instance utilization and coverage reports
B.
Savings Plans utilization reports
C.
AWS Budgets reports
D.
AWS Cost and Usage Reports

**Đáp án: D**

---

### Câu 32
A company has a serverless application that includes an Amazon API Gateway API, an AWS Lambda function, and an Amazon DynamoDB database. Which AWS service can the company use to trace user requests as they move through the application's components?

A.
AWS CloudTrail
B.
Amazon CloudWatch
C.
Amazon Inspector
D.
AWS X-Ray

**Đáp án: D**

---

### Câu 33
A company needs to set up a petabyte-scale data warehouse in the AWS Cloud. Which AWS service will meet this requirement?

A.
Amazon DynamoDB
B.
Amazon RDS
C.
Amazon Redshift
D.
Amazon ElastiCache

**Đáp án: C**

---

### Câu 34
Which AWS service is always provided at no charge?

A.
Amazon S3
B.
AWS Identity and Access Management (IAM)
C.
Elastic Load Balancers
D.
AWS WAF

**Đáp án: B**

---

### Câu 35
Which benefit is included with an AWS Enterprise Support plan?

A.
AWS Partner Network (APN) support at no cost.
B.
Designated support from an AWS technical account manager (TAM)
C.
On-site support from AWS engineers
D.
AWS managed compliance as code with AWS Config

**Đáp án: B**

---

### Câu 36
Which AWS service or tool can a company use to visualize, understand, and manage AWS spending and usage over time?

A.
AWS Trusted Advisor
B.
Amazon CloudWatch
C.
Cost Explorer
D.
AWS Budgets

**Đáp án: C**

---

### Câu 37
A company requires an isolated environment within AWS for security purposes. Which action can be taken to accomplish this?

A.
Create a separate Availability Zone to host the resources.
B.
Create a separate VPC to host the resources.
C.
Create a placement group to host the resources.
D.
Create an AWS Direct Connect connection between the company and AWS.

**Đáp án: B**

---

### Câu 38
Which AWS service is a highly available and scalable DNS web service?

A.
Amazon VPC
B.
Amazon CloudFront
C.
Amazon Route 53
D.
Amazon Connect

**Đáp án: C**

---

### Câu 39
A company wants to improve its security and audit posture by limiting Amazon EC2 inbound access. What should the company use to access instances remotely instead of opening inbound SSH ports and managing SSH keys?

A.
EC2 key pairs
B.
AWS Systems Manager Session Manager
C.
AWS Identity and Access Management (IAM)
D.
Network ACLs

**Đáp án: B**

---

### Câu 40
After selecting an Amazon EC2 Dedicated Host reservation, which pricing option would provide the largest discount?

A.
No upfront payment
B.
Hourly on-demand payment
C.
Partial upfront payment
D.
All upfront payment

**Đáp án: D**

---

### Câu 41
A company would like to host its MySQL databases on AWS and maintain full control over the operating system, database installation, and configuration. Which AWS service should the company use to host the databases?

A.
Amazon RDS
B.
Amazon EC2
C.
Amazon DynamoDB
D.
Amazon Aurora

**Đáp án: B**

---

### Câu 42
How does the AWS global infrastructure offer high availability and fault tolerance to its users?

A.
The AWS infrastructure is made up of multiple AWS Regions within various Availability Zones located in areas that have low flood risk, and are interconnected with low-latency networks and redundant power supplies.
B.
The AWS infrastructure consists of subnets containing various Availability Zones with multiple data centers located in the same geographic location.
C.
AWS allows users to choose AWS Regions and data centers so that users can select the closest data centers in different Regions.
D.
The AWS infrastructure consists of isolated AWS Regions with independent Availability Zones that are connected with low-latency networking and redundant power supplies.

**Đáp án: D**

---

### Câu 43
A user is able to set up a master payer account to view consolidated billing reports through:

A.
AWS Budgets.
B.
Amazon Macie.
C.
Amazon QuickSight.
D.
AWS Organizations.

**Đáp án: D**

---

### Câu 44
According to the AWS shared responsibility model, which task is the customer's responsibility?

A.
Maintaining the infrastructure needed to run AWS Lambda
B.
Updating the operating system of Amazon DynamoDB instances
C.
Maintaining Amazon S3 infrastructure
D.
Updating the guest operating system on Amazon EC2 instances

**Đáp án: D**

---

### Câu 45
A company is moving multiple applications to a single AWS account. The company wants to monitor the AWS Cloud costs incurred by each application. What can the company do to meet this requirement?

A.
Set up invoiced billing.
B.
Use AWS Artifact.
C.
Set budgets in Cost Explorer.
D.
Create cost allocation tags.

**Đáp án: D**

---

### Câu 46
Which design principle is achieved by following the reliability pillar of the AWS Well-Architected Framework?

A.
Vertical scaling
B.
Manual failure recovery
C.
Testing recovery procedures
D.
Changing infrastructure manually

**Đáp án: C**

---

### Câu 47
A user needs to quickly deploy a non-relational database on AWS. The user does not want to manage the underlying hardware or the database software. Which AWS service can be used to accomplish this?

A.
Amazon RDS
B.
Amazon DynamoDB
C.
Amazon Aurora
D.
Amazon Redshift

**Đáp án: B**

---

### Câu 48
Which task is an AWS responsibility when a workload is running in Amazon RDS?

A.
Creating the database table
B.
Updating the database schema
C.
Installing the database engine
D.
Dropping the database records

**Đáp án: C**

---

### Câu 49
A development team wants to publish and manage web services that provide REST APIs. Which AWS service will meet this requirement?

A.
AWS App Mesh
B.
Amazon API Gateway
C.
Amazon CloudFront
D.
AWS Cloud Map

**Đáp án: B**

---

### Câu 50
A company has a social media platform in which users upload and share photos with other users. The company wants to identify and remove inappropriate photos. The company has no machine learning (ML) scientists and must build this detection capability with no ML expertise. Which AWS service should the company use to build this capability?

A.
Amazon SageMaker
B.
Amazon Textract
C.
Amazon Rekognition
D.
Amazon Comprehend

**Đáp án: C**

---

### Câu 51
An online retail company wants to migrate its on-premises workload to AWS. The company needs to automatically handle a seasonal workload increase in a cost- effective manner. Which AWS Cloud features will help the company meet this requirement? (Choose two.)

A. Cross-Region workload deployment
B. Pay-as-you-go pricing
C. Built-in AWS CloudTrail audit capabilities
D. Auto Scaling policies
E. Centralized logging

**Đáp án: B, D**

---

### Câu 52
Which AWS service helps developers use loose coupling and reliable messaging between microservices?

A.
Elastic Load Balancing
B.
Amazon Simple Notification Service (Amazon SNS)
C.
Amazon CloudFront
D.
Amazon Simple Queue Service (Amazon SQS)

**Đáp án: D**

---

### Câu 53
A company needs to implement identity management for a fleet of mobile apps that are running in the AWS Cloud. Which AWS service will meet this requirement?

A.
Amazon Cognito
B.
AWS Security Hub
C.
AWS Shield
D.
AWS WAF

**Đáp án: A**

---

### Câu 54
A company has multiple applications and is now building a new multi-tier application. The company will host the new application on Amazon EC2 instances. The company wants the network routing and traffic between the various applications to follow the security principle of least privilege. Which AWS service or feature should the company use to enforce this principle?

A.
Security groups
B.
AWS Shield
C.
AWS Global Accelerator
D.
AWS Direct Connect gateway

**Đáp án: A**

---

### Câu 55
Which AWS service or feature gives a company the ability to control incoming traffic and outgoing traffic for Amazon EC2 instances?

A.
Security groups
B.
Amazon Route 53
C.
AWS Direct Connect
D.
Amazon VPC

**Đáp án: A**

---

### Câu 56
A company is starting to build its infrastructure in the AWS Cloud. The company wants access to technical support during business hours. The company also wants general architectural guidance as teams build and test new applications. Which AWS Support plan will meet these requirements at the LOWEST cost?

A.
AWS Basic Support
B.
AWS Developer Support
C.
AWS Business Support
D.
AWS Enterprise Support

**Đáp án: B**

---

### Câu 57
A company is migrating its public website to AWS. The company wants to host the domain name for the website on AWS. Which AWS service should the company use to meet this requirement?

A.
AWS Lambda
B.
Amazon Route 53
C.
Amazon CloudFront
D.
AWS Direct Connect

**Đáp án: B**

---

### Câu 58
A company needs to evaluate its AWS environment and provide best practice recommendations in five categories: cost, performance, service limits, fault tolerance, and security. Which AWS service can the company use to meet these requirements?

A.
AWS Shield
B.
AWS WAF
C.
AWS Trusted Advisor
D.
AWS Service Catalog

**Đáp án: C**

---

### Câu 59
Which AWS service provides the capability to view end-to-end performance metrics and troubleshoot distributed applications?

A.
AWS Cloud9
B.
AWS CodeStar
C.
AWS Cloud Map
D.
AWS X-Ray

**Đáp án: D**

---

### Câu 60
Which cloud computing benefit does AWS demonstrate with its ability to offer lower variable costs as a result of high purchase volumes?

A.
Pay-as-you-go pricing
B.
High availability
C.
Global reach
D.
Economies of scale

**Đáp án: D**

---

### Câu 61
Which AWS service provides threat detection by monitoring for malicious activities and unauthorized actions to protect AWS accounts, workloads, and data that is stored in Amazon S3?

A.
AWS Shield
B.
AWS Firewall Manager
C.
Amazon GuardDuty
D.
Amazon Inspector

**Đáp án: C**

---

### Câu 62
Which AWS service can a company use to store and manage Docker images?

A.
Amazon DynamoDB
B.
Amazon Kinesis Data Streams
C.
Amazon Elastic Container Registry (Amazon ECR)
D.
Amazon Elastic File System (Amazon EFS)

**Đáp án: C**

---

### Câu 63
A company needs an automated security assessment report that will identify unintended network access to Amazon EC2 instances. The report also must identify operating system vulnerabilities on those instances. Which AWS service or feature should the company use to meet this requirement?

A.
AWS Trusted Advisor
B.
Security groups
C.
Amazon Macie
D.
Amazon Inspector

**Đáp án: D**

---

### Câu 64
A global company is building a simple time-tracking mobile app. The app needs to operate globally and must store collected data in a database. Data must be accessible from the AWS Region that is closest to the user. What should the company do to meet these data storage requirements with the LEAST amount of operational overhead?

A.
Use Amazon EC2 in multiple Regions to host separate databases
B.
Use Amazon RDS cross-Region replication
C.
Use Amazon DynamoDB global tables
D.
Use AWS Database Migration Service (AWS DMS)

**Đáp án: C**

---

### Câu 65
Which task is a customer's responsibility, according to the AWS shared responsibility model?

A.
Management of the guest operating systems
B.
Maintenance of the configuration of infrastructure devices
C.
Management of the host operating systems and virtualization
D.
Maintenance of the software that powers Availability Zones

**Đáp án: A**

---
