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

A company needs a **fully managed** service to run **relational databases** without managing the underlying hardware.

Which AWS service should the company choose?

A. Amazon RDS

B. Amazon Redshift

C. Amazon DynamoDB

D. Amazon Aurora Serverless

**Đáp án:** A. Amazon RDS

**Giải thích:**

✔ A is correct: RDS is a managed service for relational databases.

✖ B: Redshift is for data warehousing, not general relational databases.

✖ C: DynamoDB is NoSQL, not relational.

✖ D: Aurora Serverless is relational but limited to Aurora engines.

---

### Câu 2

A retail company wants to **deploy Docker containers** **without managing** servers. Which AWS service should they use?

A. AWS Fargate

B. Amazon EC2

C. AWS Lambda

D. Amazon ECS (with EC2 launch type)

**Đáp án:** A. AWS Fargate

**Giải thích:**

✔ A is correct: Fargate runs containers without managing servers.

✖ B: EC2 requires server provisioning and maintenance.

✖ C: Lambda runs code, not full container workloads.

✖ D: ECS with EC2 requires managing EC2 instances.

---

### Câu 3

A software company **needs a scalable messaging service** to **decouple microservices**. Which service should it use?

A. Amazon SQS

B. Amazon SNS

C. Amazon MQ

D. AWS Step Functions

**Đáp án:** A. Amazon SQS

**Giải thích:**

✔ A is correct: SQS provides reliable, scalable message queuing.

✖ B: SNS is for pub/sub, not message queuing.

✖ C: MQ supports open protocols but is more complex.

✖ D: Step Functions orchestrate workflows, not queues.

---

### Câu 4

A startup wants to **store and retrieve** any amount of **unstructured data** globally with **high durability**. Which service is best suited?

A. Amazon S3

B. Amazon EFS

C. Amazon RDS

D. AWS Backup

**Đáp án:** A. Amazon S3

**Giải thích:**

✔ A is correct: S3 offers scalable, durable object storage.

✖ B: EFS is for file system storage, not object storage.

✖ C: RDS stores structured relational data.

✖ D: AWS Backup automates backups, not storage itself.

---

### Câu 5

A company runs **a stateless web application** and wants to **automatically distribute incoming traffic** across **multiple EC2** instances. Which AWS service should be used?

A. Elastic Load Balancing (ELB)

B. Amazon Route 53

C. AWS Auto Scaling

D. AWS CloudFront

**Đáp án:** A. Elastic Load Balancing (ELB)

**Giải thích:**

---

### Câu 6

A data analytics company wants to **process large-scale** data sets using a **distributed computing framework**. Which AWS service is most suitable?

A. Amazon Athena

B. AWS Glue

C. Amazon EMR

D. Amazon Redshift

**Đáp án:** C. Amazon EMR

**Giải thích:**

✔ C is correct: Amazon EMR is designed for big data processing using frameworks like Apache Spark and Hadoop.

✖ A: Athena is for querying data in S3, not processing large data sets.

✖ B: Glue is for ETL, not full big data computation frameworks.

✖ D: Redshift is for data warehousing, not distributed compute.

---

### Câu 7

Which AWS service allows users to **run serverless code** in response to events, such as **changes** in an S3 bucket or messages in an SQS queue?

A. Amazon EC2

B. AWS Lambda

C. AWS Batch

D. Amazon Elastic Beanstalk

**Đáp án:** B. AWS Lambda

**Giải thích:**

✔ B is correct: Lambda runs code in response to events without server management.

✖ A: EC2 requires managing servers and infrastructure.

✖ C: AWS Batch is for batch computing jobs, not event-based.

✖ D: Elastic Beanstalk deploys applications but isn't event-triggered by default.

---

### Câu 8

A media company wants to **deliver videos** with **low latency** to users **around the world**. Which AWS service should they use?

A. Amazon CloudFront

B. Amazon S3

C. Amazon Route 53

D. AWS Global Accelerator

**Đáp án:** A. Amazon CloudFront

**Giải thích:**

✔ A is correct: CloudFront is AWS’s CDN that delivers content globally with low latency.

✖ B: S3 stores the videos but doesn’t optimize delivery.

✖ C: Route 53 handles DNS, not content delivery.

✖ D: Global Accelerator improves application performance, not content delivery.

---

### Câu 9

A business needs to **run a MySQL database** with **high availability and automated backups**. Which AWS service should they choose?

A. Amazon DynamoDB

B. Amazon EC2 with MySQL

C. Amazon RDS

D. Amazon Neptune

**Đáp án:** C. Amazon RDS

**Giải thích:**

✔ C is correct: RDS supports MySQL with high availability, replication, and backups.

✖ A: DynamoDB is NoSQL, not MySQL-compatible.

✖ B: EC2 requires manual management of high availability and backups.

✖ D: Neptune is a graph database, not relational.

---

### Câu 10

A gaming company wants to **store player session data** in a fast, **in-memory database** with **sub-millisecond latency**. Which AWS service should be used?

A. Amazon Aurora

B. Amazon DynamoDB

C. Amazon ElastiCache

D. Amazon Redshift

**Đáp án:** C. Amazon ElastiCache

**Giải thích:**

✔ C is correct: ElastiCache is an in-memory data store with very low latency.

✖ A: Aurora is a high-performance relational DB but not in-memory.

✖ B: DynamoDB is fast but not purely in-memory like ElastiCache.

✖ D: Redshift is used for analytics, not low-latency session storage.

---

### Câu 11

A developer wants to **build and deploy** web applications **quickly without managing** the underlying infrastructure. Which AWS service should they use?

A. AWS Elastic Beanstalk

B. Amazon EC2

C. Amazon ECS

D. AWS CloudFormation

**Đáp án:** A. AWS Elastic Beanstalk

**Giải thích:**

✔ A is correct: Elastic Beanstalk allows quick app deployment with automatic provisioning and management.

✖ B: EC2 requires manual setup and server management.

✖ C: ECS is used for container orchestration, not ideal for quick web app setup.

✖ D: CloudFormation is used for infrastructure as code, not app deployment.

---

### Câu 12

A startup needs a **scalable, managed NoSQL database** to handle millions of user profiles with variable access patterns. Which AWS service is the best choice?

A. Amazon Aurora

B. Amazon ElastiCache

C. Amazon RDS

D. Amazon DynamoDB

**Đáp án:** D. Amazon DynamoDB

**Giải thích:**

✔ D is correct: DynamoDB is a fully managed NoSQL database suitable for high-scale applications.

✖ A: Aurora is relational, not NoSQL.

✖ B: ElastiCache is in-memory and best for caching, not persistent NoSQL storage.

✖ C: RDS supports SQL, not NoSQL.

---

### Câu 13

A financial services firm needs to ensure that **compute capacity** can **scale automatically based on demand**. Which AWS feature should they use?

A. Auto Scaling

B. Amazon VPC

C. Amazon Route 53

D. AWS IAM

**Đáp án:** A. Auto Scaling

**Giải thích:**

✔ A is correct: Auto Scaling automatically adjusts compute resources based on demand.

✖ B: VPC controls networking, not scaling.

✖ C: Route 53 manages DNS, not compute scaling.

✖ D: IAM handles access control, not resource scaling.

---

### Câu 14

A customer wants to **decouple components** of a **microservices application** using a **message-based communication** system. Which service should they choose?

A. Amazon MQ

B. Amazon SQS

C. Amazon SNS

D. AWS Step Functions

**Đáp án:** B. Amazon SQS

**Giải thích:**

✔ B is correct: SQS is ideal for decoupling components using message queues.

✖ A: Amazon MQ is for legacy applications needing traditional brokers.

✖ C: SNS is for pub/sub, not direct message queuing.

✖ D: Step Functions coordinate workflows, not messaging between microservices.

---

### Câu 15

A business needs to run **containerized applications** using **Kubernetes without managing** the control plane. Which AWS service should they use?

A. Amazon ECS

B. AWS Lambda

C. Amazon EKS

D. AWS Fargate

**Đáp án:** C. Amazon EKS

**Giải thích:**

✔ C is correct: EKS provides managed Kubernetes service with control plane management.

✖ A: ECS is AWS-native, not Kubernetes-compatible.

✖ B: Lambda runs serverless functions, not containers via Kubernetes.

✖ D: Fargate runs containers but doesn’t manage Kubernetes specifically.

---

### Câu 16

A media company is **building a photo processing pipeline** that must **automatically process images** as they are **uploaded into Amazon S3**.

The company wants **minimal management** overhead and **needs scalable compute resources**.

Which solution meets these requirements most efficiently?

A. Amazon EC2 instances with a scheduled cron job

B. AWS Lambda with Amazon S3 event triggers

C. Amazon ECS with a Fargate launch type

D. AWS Batch scheduled jobs

**Đáp án:** B. AWS Lambda with Amazon S3 event triggers

**Giải thích:**

✔ B is correct: Lambda can be triggered by S3 events and scales automatically.

✖ A: EC2 requires manual scaling and more management.

✖ C: ECS Fargate is scalable but needs more setup than Lambda.

✖ D: Batch is ideal for large-scale batch jobs, not real-time triggers.

---

### Câu 17

A startup wants to **develop an AI chatbot without managing** underlying servers.

It also wants to **scale automatically based on user interactions**. Which AWS service should it use as the backend compute layer?

A. Amazon EC2 Auto Scaling

B. Amazon SageMaker

C. AWS Lambda

D. Amazon Elastic Container Service (ECS)

**Đáp án:** C. AWS Lambda

**Giải thích:**

✔ C is correct: Lambda supports serverless, event-driven architecture with auto-scaling.

✖ A: EC2 needs manual scaling and instance management.

✖ B: SageMaker is for ML model training/deployment, not chatbot logic.

✖ D: ECS requires container orchestration and setup.

---

### Câu 18

A retail company needs to run **containerized microservices** that must **start quickly and scale automatically**.

They prefer a **serverless container** platform **without managing** servers or clusters.

Which AWS service should the company use?

A. Amazon EC2

B. Amazon ECS with EC2 launch type

C. Amazon ECS with Fargate

D. Amazon Elastic Kubernetes Service (EKS)

**Đáp án:** C. Amazon ECS with Fargate

**Giải thích:**

✔ C is correct: ECS with Fargate allows running containers serverlessly.

✖ A: EC2 requires infrastructure management.

✖ B: ECS with EC2 still requires cluster management.

✖ D: EKS involves managing Kubernetes resources.

---

### Câu 19

A global education company **stores large datasets** in **Amazon S3** and runs analytics using **Amazon Athena**.

How does this architecture **help reduce infrastructure costs** and **improve performance**?

A. Athena provisions a persistent cluster that can be reused

B. Athena integrates with EC2 to accelerate queries

C. Athena runs serverless SQL queries directly on S3 data

D. Athena caches data permanently to reduce cost

**Đáp án:** C. Athena runs serverless SQL queries directly on S3 data

**Giải thích:**

✔ C is correct: Athena enables serverless querying on S3 without provisioning infrastructure.

✖ A: Athena doesn’t use persistent clusters.

✖ B: EC2 is not required or used directly with Athena.

✖ D: Athena doesn’t cache data long-term.

---

### Câu 20

A healthcare company uses \*_Amazon RDS for storing sensitive patient data_.

What AWS feature can help them meet **compliance and security** requirements with **minimal operational effort**?

A. Enable S3 versioning

B. Use RDS snapshots

C. Enable RDS automated backups and encryption

D. Migrate to Amazon EC2 with a MySQL installation

**Đáp án:** C. Enable RDS automated backups and encryption

**Giải thích:**

✔ C is correct: Automated backups and encryption help with compliance and operational ease.

✖ A: S3 versioning is unrelated to RDS.

✖ B: Snapshots are manual and not enough alone.

✖ D: EC2 requires full database management.

### Câu 21

A company wants to **improve application fault tolerance**. They deploy **Amazon EC2** instances across **multiple Availability Zones** (AZs). Which **AWS design** principle does this demonstrate?

A. Automate everything

B. Use managed services

C. Design for failure

D. Implement defense in depth

**Đáp án:** C. Design for failure

**Giải thích:**

✔ C is correct: Spreading instances across AZs helps tolerate failures.

✖ A: Not directly related to availability.

✖ B: EC2 is not a managed service.

✖ D: Refers to layered security, not fault tolerance.

---

### Câu 22

A finance firm **wants to offload log** analytics from their application server and use a **fully managed service** that can **8analyze massive logs** in near **real-time**.

Which AWS service should they use?

A. Amazon QuickSight

B. Amazon Kinesis Data Analytics

C. AWS Glue

D. Amazon EMR

**Đáp án:** B. Amazon Kinesis Data Analytics

**Giải thích:**

✔ B is correct: Kinesis Data Analytics is designed for real-time data stream analysis.

✖ A: QuickSight is for BI dashboards, not stream processing.

✖ C: Glue is used for ETL, not real-time analytics.

✖ D: EMR is powerful but not serverless or real-time by default.

---

### Câu 23

A gaming company **stores session data in memory** and needs **ultra-fast access with sub-millisecond latency**. Which service should they use?

A. Amazon Aurora

B. Amazon DynamoDB

C. Amazon ElastiCache

D. Amazon S3

**Đáp án:** C. Amazon ElastiCache

**Giải thích:**

✔ C is correct: ElastiCache delivers in-memory speed with sub-millisecond latency.

✖ A: Aurora is fast but not in-memory.

✖ B: DynamoDB is fast but not suitable for in-memory workloads.

✖ D: S3 is for object storage, not real-time access.

---

# SET 3:

### Câu 1

A development team wants to **deploy** a standard web application **built with PHP**.

They want to **focus on writing code** and have **AWS handle the provisioning** of servers, load balancing, and auto-scaling automatically. Which AWS service is the most appropriate choice?

A. Amazon EC2

B. AWS Lambda

C. AWS Elastic Beanstalk

D. AWS CloudFormation

**Đáp án:** C. AWS Elastic Beanstalk

**Giải thích:**

✔ C is correct: AWS Elastic Beanstalk is a Platform as a Service (PaaS) that abstracts away the underlying infrastructure, allowing developers to simply upload their code and have Elastic Beanstalk handle the deployment, from capacity provisioning and load balancing to auto-scaling.

✖ A: Amazon EC2 is Infrastructure as a Service (IaaS) and would require the team to manually configure servers, load balancers, and scaling.

✖ B: AWS Lambda is for running serverless functions, not for deploying entire web applications.

✖ D: AWS CloudFormation is an Infrastructure as Code (IaC) service for defining resources, but it does not manage the application deployment itself like Elastic Beanstalk does.

---

### Câu 2

A company needs to **store customer invoices** that will be **accessed frequently for the first 30 days**, then accessed **infrequently for up to a year.**

After one year, the invoices must be **archived for 7 years** for compliance but do not **need instant retrieval.**

Which service and feature should they use to automate this process cost-effectively?

A. Amazon EFS with a custom script to move data

B. Amazon S3 with lifecycle policies

C. Amazon EBS with scheduled snapshots

D. AWS Backup to move data between vaults

**Đáp án:** B. Amazon S3 with lifecycle policies

**Giải thích:**

✔ B is correct: Amazon S3 lifecycle policies can be configured to automatically transition objects between storage classes (e.g., from S3 Standard to S3 Infrequent Access, and then to S3 Glacier Deep Archive) based on their age, which perfectly matches this use case and optimizes costs.

✖ A: Amazon EFS is a file storage service and would be more expensive and complex for this object storage use case.

✖ C: EBS is block storage for EC2 instances and is not suitable for storing invoices directly in this manner.

✖ D: AWS Backup is for backing up resources, not for managing the lifecycle of application data like invoices.

---

### Câu 3

Which AWS service is **fundamentally a managed Domain Name System (DNS)** web service?

A. Amazon VPC

B. AWS Direct Connect

C. Amazon CloudFront

D. Amazon Route 53

**Đáp án:** D. Amazon Route 53

**Giải thích:**

✔ D is correct: Amazon Route 53 is a highly available and scalable cloud Domain Name System (DNS) web service, designed to give developers and businesses a reliable way to route end users to internet applications.

✖ A: Amazon VPC is for creating isolated network environments in AWS.

✖ B: AWS Direct Connect is for establishing a dedicated private network connection to AWS.

✖ C: Amazon CloudFront is a Content Delivery Network (CDN).

---

### Câu 4

A **large enterprise** needs a dedicated, private, **high-bandwidth network connection** between its **on-premises data center** and **its AWS environment** to **handle consistent and large data transfers**. Which AWS service should they use?

A. AWS VPN

B. AWS Direct Connect

C. AWS Global Accelerator

D. Public Internet

**Đáp án:** B. AWS Direct Connect

**Giải thích:**

✔ B is correct: AWS Direct Connect is a cloud service solution that makes it easy to establish a dedicated network connection from your premises to AWS. It provides a more consistent network experience than internet-based connections.

✖ A: AWS VPN establishes a connection over the public internet and is better suited for less consistent or lower-bandwidth needs.

✖ C: AWS Global Accelerator improves the performance of applications over the public internet but is not a private connection.

✖ D: The public internet does not offer the dedicated, private, and consistent bandwidth of Direct Connect.

---

### Câu 5

A data analytics team needs to **run complex business intelligence queries** on a **petabyte-scale** structured dataset.

They need a **fully managed** **data warehouse** solution optimized for this purpose. Which AWS service is the best fit?

A. Amazon RDS

B. Amazon DynamoDB

C. Amazon Redshift

D. Amazon EMR

**Đáp án:** C. Amazon Redshift

**Giải thích:**

✔ C is correct: Amazon Redshift is a fast, fully managed, petabyte-scale data warehouse service that makes it simple and cost-effective to analyze all your data using standard SQL and your existing Business Intelligence (BI) tools.

✖ A: Amazon RDS is a relational database service (OLTP) and is not optimized for data warehousing (OLAP) queries at this scale.

✖ B: DynamoDB is a NoSQL database, not a data warehouse.

✖ D: Amazon EMR is for big data processing using frameworks like Spark and Hadoop, not a data warehouse.

---

### Câu 6

What AWS **compute service** allows you to **run code for functions** or backend services **without provisioning or managing** any servers?

A. Amazon EC2

B. AWS Fargate

C. AWS Lambda

D. Amazon Lightsail

**Đáp án:** C. AWS Lambda

**Giải thích:**

✔ C is correct: AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers. You pay only for the compute time you consume.

✖ A: EC2 requires you to provision and manage virtual servers.

✖ B: Fargate is a serverless compute engine for _containers_, while Lambda is for running event-driven _functions_. Lambda is the more direct answer for "running code."

✖ D: Lightsail provides a simplified way to launch servers, but you are still managing a server.

---

### Câu 7

A media company wants to **deliver** its video content and **web assets to users across the globe** with the **lowest possible latency.**

Which service should they use to **cache content** in locations close to end-users?

A. Amazon S3 Transfer Acceleration

B. AWS Global Accelerator

C. Amazon CloudFront

D. Elastic Load Balancing

**Đáp án:** C. Amazon CloudFront

**Giải thích:**

✔ C is correct: Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency and high transfer speeds by caching content at edge locations.

✖ A: S3 Transfer Acceleration speeds up uploads to S3 but is not a CDN for content delivery.

✖ B: AWS Global Accelerator improves application performance for TCP/UDP traffic but is not a content cache.

✖ C: ELB distributes traffic to backend servers in a region, it does not cache content globally.

---

### Câu 8

A startup is building an application on a **fleet of Amazon EC2 instances**. They need to **ensure that if one of their instances fails**, **traffic is automatically redirected** to healthy instances.

How should they distribute the incoming traffic?

A. By using an AWS Auto Scaling group

B. By using an Elastic Load Balancer (ELB)

C. By configuring multiple Elastic IP addresses

D. By using Amazon Route 53 health checks

**Đáp án:** B. By using an Elastic Load Balancer (ELB)

**Giải thích:**

✔ B is correct: An Elastic Load Balancer automatically distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, and only sends traffic to healthy instances.

✖ A: An Auto Scaling group manages the number of instances, but ELB is what distributes traffic among them.

✖ C: Manually managing Elastic IPs would not be an automatic or scalable solution for failover.

✖ D: Route 53 health checks can route traffic away from a failing _endpoint_ at the DNS level, but ELB is the standard for distributing traffic across a fleet of _instances_.

---

### Câu 9

What is the **primary use case** for **Amazon S3?**

A. A relational database service for structured data.

B. A managed NoSQL database.

C. A highly scalable and durable object storage for unstructured data.

D. A block storage service for EC2 instances.

**Đáp án:** C. A highly scalable and durable object storage for unstructured data.

**Giải thích:**

✔ C is correct: Amazon S3 (Simple Storage Service) is an object storage service offering industry-leading scalability, data availability, security, and performance for unstructured data like images, videos, backups, and log files.

✖ A: This describes Amazon RDS.

✖ B: This describes Amazon DynamoDB.

✖ D: This describes Amazon EBS.

---

### Câu 10

A company needs to **provide a shared, scalable file storage solution** for a large number of **Linux-based Amazon EC2** instances to access **simultaneously**. Which AWS storage service is designed for this use case?

A. Amazon S3

B. Amazon EBS

C. Amazon EFS

D. AWS Storage Gateway

**Đáp án:** C. Amazon EFS

**Giải thích:**

✔ C is correct: Amazon EFS (Elastic File System) provides a simple, scalable, fully managed elastic NFS file system for use with AWS Cloud services and on-premises resources. It is designed for shared access from multiple EC2 instances.

✖ A: S3 is object storage and cannot be mounted as a shared file system in the same way as EFS.

✖ B: EBS volumes are block storage that can typically only be attached to a single EC2 instance at a time.

✖ D: Storage Gateway is for hybrid cloud storage, connecting on-premises environments to AWS storage.

---

### Câu 11

An application's architecture is **being designed to be highly available**. What is the **best practice** regarding **Availability Zones (AZs)**?

A. Deploy all resources into a single AZ to reduce latency.

B. Deploy resources across multiple AWS Regions.

C. Deploy resources across multiple Availability Zones within a single Region.

D. Use only one AZ and rely on snapshots for recovery.

**Đáp án:** C. Deploy resources across multiple Availability Zones within a single Region.

**Giải thích:**

✔ C is correct: Deploying an application across multiple AZs within a Region is a common strategy for high availability. It protects the application from failure of a single data center.

✖ A: Using a single AZ creates a single point of failure.

✖ B: Deploying across Regions is a strategy for disaster recovery or global reach, not the primary method for standard high availability within a single geographical area.

✖ C: Relying on snapshots is a backup strategy, not a high availability strategy.

---

### Câu 12

A team is **deploying a containerized** application using **Docker**. They want to use a **container orchestration service** but want to completely **avoid managing** the underlying servers where the containers run.

Which AWS service or feature allows this?

A. Amazon ECS with EC2 launch type

B. Amazon EKS with managed node groups

C. AWS Fargate

D. Amazon EC2 with Docker installed

**Đáp án:** C. AWS Fargate

**Giải thích:**

✔ C is correct: AWS Fargate is a serverless compute engine for containers that works with both Amazon ECS and EKS. It allows you to run containers without having to manage the underlying servers or clusters.

✖ A: The EC2 launch type for ECS requires you to manage the EC2 instances in your cluster.

✖ B: EKS with managed node groups still involves EC2 instances that are part of your account, even if managed.

✖ D: This approach involves maximum server management effort.

---

### Câu 13

Which **AWS database service** is a fast and **flexible NoSQL database** service for applications that need consistent, single-digit millisecond latency at any scale?

A. Amazon RDS

B. Amazon DynamoDB

C. Amazon Redshift

D. Amazon Aurora

**Đáp án:** B. Amazon DynamoDB

**Giải thích:**

✔ B is correct: Amazon DynamoDB is a key-value and document NoSQL database that delivers single-digit millisecond performance at any scale.

✖ A: RDS is a service for relational (SQL) databases.

✖ C: Redshift is a data warehouse, not an operational NoSQL database.

✖ D: Aurora is a high-performance relational (SQL) database.

---

### Câu 14

A financial services application needs to **send automated notifications** to customers via **SMS and email** when certain **transactions occur.**

Which AWS service is best suited for **sending these multi-channel notifications** to end-users?

A. Amazon SQS

B. Amazon SES

C. Amazon SNS

D. AWS Step Functions

**Đáp án:** C. Amazon SNS

**Giải thích:**

✔ C is correct: Amazon SNS (Simple Notification Service) is a fully managed messaging service for both application-to-application (A2A) and application-to-person (A2P) communication. It supports sending messages to a large number of subscribers via multiple protocols, including SMS and email.

✖ A: SQS is a message queue for decoupling applications, not for sending notifications directly to users.

✖ B: SES (Simple Email Service) is specifically for email, while SNS is a broader pub/sub and notification service that includes email, SMS, and more.

✖ D: Step Functions orchestrate workflows, they don't send notifications.

---

### Câu 15

A developer wants to **define their entire** AWS infrastructure including VPCs, subnets, EC2 instances, and databases in a **JSON or YAML** template file.

What AWS service enables this **Infrastructure as Code (IaC)** approach?

A. AWS Elastic Beanstalk

B. AWS Config

C. AWS CloudFormation

D. AWS Service Catalog

**Đáp án:** C. AWS CloudFormation

**Giải thích:**

✔ C is correct: AWS CloudFormation provides a common language for you to model and provision all the infrastructure resources in your cloud environment. You create a template that describes all the AWS resources that you want, and CloudFormation takes care of provisioning and configuring those resources for you.

✖ A: Elastic Beanstalk is a PaaS for deploying applications, not a general IaC service.

✖ B: AWS Config is for auditing and compliance, not provisioning.

✖ D: Service Catalog is for creating a curated list of deployable services.

---

### Câu 16

A company's website **experiences predictable traffic** spikes **every weekday morning.**

They want to **automatically increase** the **number of EC2 instances** during these hours and decrease them during off-peak hours to save costs. Which AWS service or feature should they configure?

A. Elastic Load Balancing

B. Scheduled scaling with AWS Auto Scaling

C. Amazon CloudWatch alarms

D. On-Demand capacity reservations

**Đáp án:** B. Scheduled scaling with AWS Auto Scaling

**Giải thích:**

✔ B is correct: AWS Auto Scaling allows for scheduled scaling actions, which let you set your own scaling schedule for predictable load changes. This is the perfect solution for scaling up and down at specific times of the day.

✖ A: ELB distributes traffic but does not add or remove instances.

✖ C: CloudWatch alarms are used for dynamic scaling based on metrics (like CPU utilization), not for predictable time-based scaling.

✖ D: Capacity reservations ensure capacity is available, but they don't automatically scale instances up and down.

---

### Câu 17

Which of the following is a **block-level storage volume** that can be **attached to a running Amazon EC2 instance?**

A. Amazon S3 bucket

B. Amazon Glacier vault

C. Amazon EFS file system

D. Amazon EBS volume

**Đáp án:** D. Amazon EBS volume

**Giải thích:**

✔ D is correct: Amazon EBS (Elastic Block Store) provides high-performance block storage volumes for use with Amazon EC2. They behave like raw, unformatted block devices that you can mount as a disk.

✖ A: S3 is object storage.

✖ B: Glacier is archival storage.

✖ C: EFS is file-level storage.

---

### Câu 18

A mobile app developer is building a new application and **wants to enable user sign-up, sign-in, and access control.**

They need a **managed service** that can handle **user management and authentication**. Which AWS service is designed for this?

A. AWS IAM

B. Amazon Cognito

C. AWS Directory Service

D. AWS SSO

**Đáp án:** B. Amazon Cognito

**Giải thích:**

✔ B is correct: Amazon Cognito lets you add user sign-up, sign-in, and access control to your web and mobile apps quickly and easily. It scales to millions of users and supports sign-in with social identity providers and enterprise identity providers.

✖ A: IAM is for managing access to AWS services and resources, not for authenticating users of your own application.

✖ C: Directory Service is for connecting to Microsoft Active Directory.

✖ D: AWS SSO (now IAM Identity Center) is for providing single sign-on to AWS accounts and business applications, not for a custom mobile app's user base.

---

### Câu 19

What component of an Amazon VPC **controls inbound and outbound traffic at the subnet level?**

A. Security Group

B. Route Table

C. Internet Gateway

D. Network ACL (NACL)

**Đáp án:** D. Network ACL (NACL)

**Giải thích:**

✔ D is correct: A Network Access Control List (NACL) is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets.

✖ A: A Security Group acts as a firewall at the instance level, not the subnet level.

✖ B: A Route Table determines where network traffic is directed.

✖ C: An Internet Gateway enables communication between your VPC and the internet.

---

### Câu 20

A company needs to run a **database that uses the PostgreSQL engine**.

They want **AWS to handle the database management** tasks such as provisioning, patching, backup, recovery, and monitoring. Which service should they use?

A. Amazon DynamoDB

B. Amazon EC2 with a manual PostgreSQL installation

C. Amazon Redshift

D. Amazon RDS

**Đáp án:** D. Amazon RDS

**Giải thích:**

✔ D is correct: Amazon RDS (Relational Database Service) is a managed service that supports multiple database engines, including PostgreSQL. It automates time-consuming administration tasks such as hardware provisioning, database setup, patching, and backups.

✖ A: DynamoDB is a NoSQL database.

✖ B: This would require the company to perform all management tasks manually.

✖ C: Redshift is a data warehouse, not an OLTP database service like RDS.

---

### Câu 21

An analytics company needs to **process a massive, continuous stream** of incoming data in **real time.**

Which AWS service is designed to ingest and **process large streams of data records?**

A. Amazon SQS

B. Amazon Kinesis

C. AWS Glue

D. AWS Data Pipeline

**Đáp án:** B. Amazon Kinesis

**Giải thích:**

✔ B is correct: Amazon Kinesis makes it easy to collect, process, and analyze real-time, streaming data so you can get timely insights and react quickly to new information.

✖ A: SQS is a message queue, typically used for decoupling components, not for real-time stream processing and analytics.

✖ C: AWS Glue is an ETL service primarily for batch data preparation.

✖ D: AWS Data Pipeline is for orchestrating data-driven workflows, usually on a schedule.

---

### Câu 22

A company is **deploying a critical application** and must ensure it can **withstand the failure** of an entire **Availability Zone.**

What is the minimum configuration to achieve this?

A. Deploy EC2 instances in a single AZ with an ELB.

B. Deploy EC2 instances across multiple AZs in one Region.

C. Deploy EC2 instances across multiple Regions.

D. Deploy EC2 instances in a single AZ and enable AWS Backup.

**Đáp án:** B. Deploy EC2 instances across multiple AZs in one Region.

**Giải thích:**

✔ B is correct: To be resilient to the failure of a single Availability Zone, the application must be deployed with resources (like EC2 instances in an Auto Scaling group behind an ELB) running in at least two Availability Zones within the same AWS Region.

✖ A: This configuration has a single point of failure at the AZ level.

✖ C: This is a disaster recovery strategy, which is more complex than what is needed for simple AZ failure resilience.

✖ D: Backups are for data recovery, not for maintaining high availability during an outage.

---

### Câu 23

A team needs a central place to **store and version-control** their application's source code. They are looking for a **fully-managed service** that hosts **secure Git-based repositories**. Which AWS service should they use?

A. Amazon S3

B. AWS CodeCommit

C. AWS CodeDeploy

D. AWS CodeArtifacts

**Đáp án:** B. AWS CodeCommit

**Giải thích:**

✔ B is correct: AWS CodeCommit is a secure, highly scalable, managed source control service that hosts private Git repositories.

✖ A: S3 can store files and supports versioning, but it is not a Git repository.

✖ C: CodeDeploy is a service for automating code deployments to servers.

✖ D: CodeArtifact is a secure artifact repository for storing software packages.
