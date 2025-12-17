# Cloud Technology & Services

# SET 1:

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

✔ A is correct: AWS Fargate is a serverless compute engine for containers that works with both Amazon ECS and Amazon EKS, allowing you to run containers without13 managing servers or clusters.

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

✔ A is correct: Amazon S3 (Simple Storage Service) is an object storage service offering industry-leading scalability, data availability, security, and performance,14 suitable for storing and retrieving any amount of unstructured data.

✖ B: EFS (Elastic File System) is a scalable file storage for EC2 instances, not primarily for massive unstructured data archiving.

✖ C: RDS (Relational Database Service) stores structured relational data.

✖ D: AWS Backup is a service for centralizing and automating data protection, not the primary storage service itself.

---

### Câu 5

A \*8popular news website** experiences **varying levels of traffic** throughout the day, with **major spikes\*\* during breaking news events.

They have **multiple Amazon EC2 instances** serving their web application and need to **distribute incoming web traffic** efficiently across these instances to ensure responsiveness and **high availability**.

Which AWS service should be used to **automatically distribute** incoming application traffic across multiple EC2 instances?

A. Elastic Load Balancing (ELB)

B. Amazon Route 53

C. AWS Auto Scaling

D. AWS CloudFront

**Đáp án:** A. Elastic Load Balancing (ELB)

**Giải thích:**

✔ A is correct: Elastic Load Balancing (ELB) automatically distributes incoming application traffic across multiple targets, such as EC2 instances,15 in multiple Availability Zones, ensuring high availability and fault tolerance.

✖ B: Amazon Route 53 is a DNS web service that routes user requests to internet applications.

✖ C: AWS Auto Scaling automatically adjusts the number of EC2 instances based on demand, but ELB is responsible for distributing traffic among those instances.

✖ D: AWS CloudFront is a Content Delivery Network (CDN) for delivering content to users with low latency, not for balancing traffic across EC2 instances.

---

### Câu 6

A pharmaceutical research firm needs to **analyze vast amounts of genomic data**, often in the **petabyte range**, to identify patterns and correlations.

They require a **fully managed service** that can run **open-source big data frameworks** like Apache Spark and Hadoop **without the operational complexity of setting up and managing clusters.**

Which AWS service is most suitable for processing these **large-scale datasets** using distributed computing frameworks?

A. Amazon Athena

B. AWS Glue

C. Amazon EMR

D. Amazon Redshift

**Đáp án:** C. Amazon EMR

**Giải thích:**

✔ C is correct: Amazon EMR (Elastic MapReduce) is a managed cluster platform that simplifies running big data frameworks, such as Apache Hadoop and Apache Spark, on AWS to process and analyze vast amounts16 of data.

✖ A: Amazon Athena is a serverless query service for S3 data, not a general-purpose big data processing framework.

✖ B: AWS Glue is a serverless data integration service for ETL (Extract, Transform, Load) operations, not for running full-fledged distributed computing frameworks for analysis.

✖ D: Amazon Redshift is a data warehousing service for analytical queries, not designed for general big data processing frameworks.

---

### Câu 7

A smart home device company wants **to process events** generated by their devices (e.g., motion detection, temperature changes) in **real-time**.

They **need a compute service** that can execute **small pieces of code** in response to these events, **without needing to provision or manage any servers**.

Which AWS service allows users to **run serverless code** in **response to events**, such as changes in an S3 bucket or messages in an IoT stream?

A. Amazon EC2

B. AWS Lambda

C. AWS Batch

D. Amazon Elastic Beanstalk

**Đáp án:** B. AWS Lambda

**Giải thích:**

✔ B is correct: AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers. It automatically scales17 and can be triggered by various AWS services and custom events.

✖ A: EC2 requires managing servers and infrastructure.

✖ C: AWS Batch is for running batch computing jobs, not real-time event-driven functions.

✖ D: Amazon Elastic Beanstalk is for deploying and scaling web applications and services, but it still manages underlying servers.

---

### Câu 8

A global online education platform provides video lectures to students worldwide.

They want to ensure that video content is **delivered with the fastest possible speed** and **lowest latency** to students, regardless of their geographical location.

Which AWS service should they use to **efficiently distribute** their video content globally?

A. Amazon CloudFront

B. Amazon S3

C. Amazon Route 53

D. AWS Global Accelerator

**Đáp án:** A. Amazon CloudFront

**Giải thích:**

✔ A is correct: Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency and high transfer speeds.18

✖ B: S3 stores the videos but does not optimize their global delivery.

✖ C: Route 53 is a DNS service that translates domain names to IP addresses, not a content delivery service.

✖ D: Global Accelerator improves application performance for TCP/IP traffic by routing it through the AWS global network, but CloudFront is specifically optimized for content delivery.

---

### Câu 9

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

### Câu 10

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

### Câu 11

A developer wants to **quickly deploy** a new version of their **Python-based web application**.

They want to **focus on writing code** and not worry about provisioning servers, configuring load balancers, or setting up Auto Scaling.

Which AWS service enables them to **deploy** web applications rapidly **without managing** the underlying infrastructure?

A. AWS Elastic Beanstalk

B. Amazon EC2

C. Amazon ECS

D. AWS CloudFormation

**Đáp án:** A. AWS Elastic Beanstalk

**Giải thích:**

✔ A is correct: AWS Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services developed with various programming languages19 and servers. It handles the deployment, capacity provisioning, load balancing, and auto-scaling.

✖ B: EC2 requires manual setup and server management.

✖ C: ECS is used for container orchestration, which provides more control but still requires some cluster management.

✖ D: CloudFormation is for defining infrastructure as code, not directly for deploying applications.

---

### Câu 12

A mobile gaming company **needs a database** to store player scores, game progress, and in-game inventory.

This data will **experience extremely high read and write volumes**, especially during peak gaming hours, and the data schema might evolve over time.

They need a **fully managed**, scalable, and highly available **NoSQL database** that can handle millions of requests per second. Which AWS service is the best choice?

A. Amazon Aurora

B. Amazon ElastiCache

C. Amazon RDS

D. Amazon DynamoDB

**Đáp án:** D. Amazon DynamoDB

**Giải thích:**

✔ D is correct: Amazon DynamoDB is a fully managed, serverless, key-value and document NoSQL database designed for internet-scale applications with single-digit millisecond performance at any scale.

✖ A: Aurora is a relational database, not NoSQL.

✖ B: ElastiCache is primarily an in-memory caching service, not a persistent NoSQL database for primary storage.

✖ C: RDS supports SQL databases, not NoSQL.

---

### Câu 13

An online ticketing service anticipates **massive spikes in demand shortly** after concert tickets go on sale.

They need to ensure that their application's compute capacity can **automatically increase** to handle these surges and then **scale back down** when demand subsides.

Which AWS feature should they use to automatically adjust compute capacity based on demand?

A. Auto Scaling

B. Amazon VPC

C. Amazon Route 53

D. AWS IAM

**Đáp án:** A. Auto Scaling

**Giải thích:**

✔ A is correct: AWS Auto Scaling helps you maintain application availability and allows you to automatically adjust your Amazon EC2 capacity to maintain steady, predictable performance at the lowest possible cost.

✖ B: VPC (Virtual Private Cloud) controls networking isolation.

✖ C: Route 53 manages DNS.

✖ D: IAM handles access control.

---

### Câu 14

A financial application **processes millions of asynchronous transactions daily**.

To ensure that transactions are processed **reliably and independently**, even if one processing **module fails or slows down**, the development team wants to implement a **message-based communication** system to **decouple** the transaction processing components.

Which service should they choose to decouple components of a microservices application using a message-based communication system?

A. Amazon MQ

B. Amazon SQS

C. Amazon SNS

D. AWS Step Functions

**Đáp án:** B. Amazon SQS

**Giải thích:**

✔ B is correct: Amazon SQS (Simple Queue Service) provides a reliable, scalable, and highly available message queue service that is ideal for decoupling components and ensuring asynchronous processing of messages.

✖ A: Amazon MQ is a managed message broker service that supports open messaging protocols, often used for migrating existing applications that rely on message brokers. SQS is generally preferred for cloud-native decoupling.

✖ C: SNS (Simple Notification Service) is a pub/sub messaging service, primarily for broadcasting messages to multiple subscribers, not for direct message queuing between services.

✖ D: Step Functions coordinate workflows composed of multiple steps, not primarily for simple message queuing between microservices.

---

### Câu 15

A technology company is adopting **Kubernetes** for **container orchestration** to manage its microservices.

They want to **leverage the power of Kubernetes** but want to offload the operational burden of managing the Kubernetes control plane (e.g., master nodes, etcd).

Which AWS service should they use to run containerized applications using Kubernetes without managing the control plane?

A. Amazon ECS

B. AWS Lambda

C. Amazon EKS

D. AWS Fargate

**Đáp án:** C. Amazon EKS

**Giải thích:**

✔ C is correct: Amazon EKS (Elastic Kubernetes Service) is a fully managed Kubernetes service that allows you to run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane.20

✖ A: ECS (Elastic Container Service) is AWS's own container orchestration service, not Kubernetes-compatible.

✖ B: Lambda runs serverless functions, not directly Kubernetes containers.

✖ D: Fargate is a serverless compute engine for containers that can be used with both ECS and EKS, but EKS is the service for managed Kubernetes itself.

---

### Câu 16

A photography business **receives thousands of new images daily** that need to be resized, watermarked, and categorized **before being stored** in a content management system.

They want this processing to **happen automatically** as soon as an **image is uploaded** to their Amazon **S3 bucket**, with **minimal operational** overhead and the ability to scale to handle varying upload volumes.

Which solution meets these requirements most efficiently?

A. Amazon EC2 instances running image processing scripts triggered by cron jobs.

B. AWS Lambda functions triggered by Amazon S3 object creation events.

C. Amazon ECS cluster with EC2 launch type running a long-running processing application.

D. AWS Batch jobs initiated manually after a certain number of uploads.

**Đáp án:** B. AWS Lambda functions triggered by Amazon S3 object creation events.

**Giải thích:**

✔ B is correct: AWS Lambda can be directly integrated with Amazon S3 events. When an object is uploaded to an S3 bucket, Lambda can automatically trigger a function to perform the image processing, scaling automatically based on the number of events, and incurring costs only for the compute time used.

✖ A: EC2 instances require continuous management, patching, and manual scaling. Cron jobs are scheduled, not event-driven.

✖ C: While scalable, ECS with EC2 launch type still involves managing EC2 instances and an ECS cluster.

✖ D: AWS Batch is suitable for large-scale, asynchronous batch processing, but typically requires more setup and isn't ideal for real-time, event-driven processing with minimal management like Lambda.

---

### Câu 17

A conversational AI startup is **developing a new chatbot service**. They anticipate unpredictable usage patterns, from a **few users to millions** of concurrent conversations.

They want the chatbot's backend logic to be entirely **serverless**, **automatically scaling** to meet demand, and **only paying for the actual compute** time consumed.

Which AWS service should it use as the backend compute layer for its AI chatbot?

A. Amazon EC2 Auto Scaling

B. Amazon SageMaker

C. AWS Lambda

D. Amazon Elastic Container Service (ECS)

**Đáp án:** C. AWS Lambda

**Giải thích:**

✔ C is correct: AWS Lambda is a serverless compute service that runs your code in response to events and automatically manages the underlying compute resources. It scales automatically to handle millions of requests and you only pay for the compute time consumed. This aligns perfectly with serverless requirements for unpredictable workloads.

✖ A: EC2 Auto Scaling manages EC2 instances, which are servers you still have to manage.

✖ B: Amazon SageMaker is primarily for building, training, and deploying machine learning models, not for hosting the general application logic of a chatbot.

✖ D: ECS runs containers, but typically requires managing clusters unless paired with Fargate (which is an execution mode, not the service itself for the core compute logic in this context).

---

### Câu 18

An online training platform needs to run **several containerized microservices** for its user authentication and course management.

They prioritize speed of deployment and scaling, and explicitly want to **avoid managing** the **underlying EC2 instances or Kubernetes clusters**.

They are looking for a serverless container platform. Which AWS service should the company use to run its containerized microservices?

A. Amazon EC2

B. Amazon ECS with EC2 launch type

C. Amazon ECS with Fargate

D. Amazon Elastic Kubernetes Service (EKS)

**Đáp án:** C. Amazon ECS with Fargate

**Giải thích:**

✔ C is correct: Amazon ECS (Elastic Container Service) with Fargate launch type allows you to run containers without having to provision, manage, or scale servers. Fargate handles the underlying infrastructure, making it a serverless container platform.

✖ A: EC2 requires managing virtual servers.

✖ B: ECS with EC2 launch type still requires managing the underlying EC2 instances in the cluster.

✖ D: EKS manages the Kubernetes control plane, but you still typically manage the worker nodes (EC2 instances) or use Fargate with EKS (which is a specific configuration of EKS, not EKS itself as the serverless part).

---

### Câu 19

A non-profit organization collects **vast amounts of publicly available environmental data** in various formats and stores it in an **Amazon S3 data lake**.

Researchers need to perform ad-hoc **SQL queries** on this data **without setting up or managing** a traditional database infrastructure.

How does this architecture, leveraging Amazon S3 and Amazon Athena, help reduce infrastructure costs and improve agility for data analysis?

A. Athena provisions a persistent cluster of servers that can be reused for queries.

B. Athena requires users to load all data into a managed database before querying.

C. Athena runs serverless SQL queries directly on data stored in S3, paying only for queries executed.

D. Athena permanently caches queried data in dedicated storage to reduce future costs.

**Đáp án:** C. Athena runs serverless SQL queries directly on data stored in S3, paying only for queries executed.

**Giải thích:**

✔ C is correct: Amazon Athena is a serverless interactive query service that makes it easy to analyze data directly in Amazon S3 using standard SQL. You only pay for the queries you run, making it cost-effective and agile as there's no infrastructure to manage.

✖ A: Athena is serverless and does not provision persistent clusters for users.

✖ B: Athena queries data directly in S3; it doesn't require loading data into a separate database.

✖ D: Athena queries S3 directly; while it uses a query results location, it doesn't permanently cache data in dedicated storage for cost reduction.

---

### Câu 20

A pharmaceutical company is storing **highly sensitive clinical trial data** in **Amazon RDS** for PostgreSQL.

To meet **stringent regulatory compliance** and **ensure data recovery**, they need automated, **point-in-time recovery** capabilities and **strong encryption** for their data at rest and in transit.

What AWS feature can help them meet compliance and security requirements with minimal operational effort for their RDS database?

A. Enable S3 versioning for database backups.

B. Manually create RDS snapshots daily.

C. Enable RDS automated backups and encryption for the database instances.

D. Migrate the database to Amazon EC2 and configure custom backup scripts.

**Đáp án:** C. Enable RDS automated backups and encryption for the database instances.

**Giải thích:**

✔ C is correct: Amazon RDS provides automated backups, including point-in-time recovery, and built-in encryption options (using KMS) for data at rest and in transit, which are crucial for compliance and disaster recovery with minimal operational effort.

✖ A: S3 versioning is for S3 objects, not directly for RDS database backups.

✖ B: Manually creating snapshots is not automated and less robust than automated backups for point-in-time recovery.

✖ D: Migrating to EC2 would increase operational effort as the customer would be responsible for all database management, including backups and encryption.

---

### Câu 21

A global online gaming company needs to **ensure its game servers** remain available even if an entire data center experiences an outage.

They decide to **deploy their Amazon EC2 instances** across multiple **Availability Zones** within **an AWS Region.**

Which AWS cloud design principle does this strategy primarily demonstrate?

A. Automate everything

B. Use managed services

C. Design for failure

D. Implement defense in depth

**Đáp án:** C. Design for failure

**Giải thích:**

✔ C is correct: Deploying resources across multiple Availability Zones is a core strategy for designing for failure, ensuring that the application remains available even if one AZ experiences an outage.

✖ A: Automate everything is a best practice but not the direct principle demonstrated by multi-AZ deployment for resilience.

✖ B: While EC2 is a cloud service, this principle is about designing for failure, not solely about using managed services.

✖ D: Defense in depth refers to layered security mechanisms, not fault tolerance of infrastructure.

---

### Câu 22

A large IoT company **collects vast streams** of sensor data from **millions of devices in real-time**.

They need to **continuously analyze** this incoming data to **detect anomalies** and **trigger alerts** as soon as possible.

They want a **fully managed service** that can perform **real-time analytics** on **streaming data** without provisioning servers.

Which AWS service should they use for this near real-time log and stream analytics?

A. Amazon QuickSight

B. Amazon Kinesis Data Analytics

C. AWS Glue

D. Amazon EMR

**Đáp án:** B. Amazon Kinesis Data Analytics

**Giải thích:**

✔ B is correct: Amazon Kinesis Data Analytics is a fully managed service that allows you to easily analyze streaming data in real time with standard SQL or Apache Flink, without having to provision or manage any servers.

✖ A: QuickSight is a business intelligence (BI) service for creating dashboards and visualizations from existing data, not for real-time stream processing.

✖ C: AWS Glue is an ETL (Extract, Transform, Load) service, typically used for batch processing and preparing data for analytics, not real-time stream analysis.

✖ D: EMR is for big data processing using frameworks like Hadoop and Spark, often used for batch processing or large-scale, but Kinesis Data Analytics is specifically designed for real-time streaming analytics in a serverless manner.

---

### Câu 23

A fintech startup processes **high volumes of financial transactions** and needs to store **frequently accessed** lookup data (e.g., currency exchange rates, client profiles) in a **very fast, in-memory store**.

This data requires **sub-millisecond latency** for **read and write operations** to support their **high-throughput trading system**. Which service should they use for this high-speed, in-memory data storage?

A. Amazon Aurora

B. Amazon DynamoDB

C. Amazon ElastiCache

D. Amazon S3

**Đáp án:** C. Amazon ElastiCache

**Giải thích:**

✔ C is correct: Amazon ElastiCache provides a fully managed, high-performance, in-memory data store for Caching, Redis, and Memcached, delivering sub-millisecond latency for applications requiring extremely fast data access.

✖ A: Aurora is a high-performance relational database but is primarily disk-backed and not optimized for in-memory caching for sub-millisecond latency.

✖ B: DynamoDB is a fast NoSQL database but is not an in-memory store and generally has slightly higher latency than ElastiCache for caching patterns.

✖ D: S3 is object storage, designed for durability and scalability, but not for ultra-low latency operational data access.

---

# SET 2:

### Câu 1

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 2

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 3

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 4

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 5

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 6

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 7

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 8

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 9

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 10

**...**

**Đáp án:**

**Giải thích:**

---

# SET 3:

### Câu 1

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 2

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 3

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 4

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 5

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 6

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 7

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 8

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 9

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 10

**...**

**Đáp án:**

**Giải thích:**
