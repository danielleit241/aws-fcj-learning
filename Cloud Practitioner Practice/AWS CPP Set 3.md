# AWS Cloud Practitioner Practice - Set 3

## Cloud Concepts

### Câu 1

A rapidly expanding tech company needs to **provision dozens of new development** and **testing environments** for a new project.

They want to **avoid delays** associated with **hardware procurement and manual setup**.

Which AWS concept enables them to **rapidly deploy** these resources without traditional long procurement cycles?

A. Elastic Load Balancing

B. Availability Zones

C. On-demand provisioning

D. Security groups

**Đáp án:** C. On-demand provisioning

**Giải thích:**

✔ C is correct: On-demand provisioning allows users to quickly and automatically provision computing resources without human interaction or traditional procurement processes.

✖ A: Elastic Load Balancing distributes traffic.

✖ B: Availability Zones are for fault tolerance and high availability.

✖ D: Security groups control network traffic. These are service features, not the core concept of rapid provisioning.

---

### Câu 2

A media production company is building **a new video rendering pipeline** on AWS.

They are **concerned** about **potential vendor lock-in** and want to ensure they can **easily migrate** their rendering jobs to **another cloud provider** or **on-premises** if needed.

What architectural approach would best support this goal while building on AWS?

A. Heavily relying on AWS-specific managed services with tight integrations.

B. Developing custom application logic deeply tied to proprietary AWS APIs.

C. Designing a loosely coupled architecture using open standards and portable data formats.

D. Hosting all components in a single AWS Region with no replication.

**Đáp án:** C. Designing a loosely coupled architecture using open standards and portable data formats.

**Giải thích:**

✔ C is correct: A loosely coupled architecture with open standards and portable data formats makes it easier to swap out components or migrate to different environments.

✖ A/B: These actions increase vendor lock-in.

✖ D: Hosting in a single region doesn't relate to avoiding vendor lock-in; it actually increases risk.

---

### Câu 3

A **small** software development team wants to **quickly test** new features and **deploy** updates to their web application **several times a day**.

They need an **environment** that supports **fast experimentation** and allows them to **adapt quickly** to user feedback.

How does AWS support this business requirement?

A. By enforcing strict long-term planning for resource allocation.

B. By providing tools for rapid prototyping, deployment, and iteration.

C. By restricting the speed at which new resources can be provisioned.

D. By requiring a fixed infrastructure model for stability.

**Đáp án:** B. By providing tools for rapid prototyping, deployment, and iteration.

**Giải thích:**

✔ B is correct: AWS provides services and a flexible environment that enables rapid experimentation, deployment, and iteration, which are hallmarks of business agility.

✖ A/C/D: These statements describe traditional IT constraints that hinder agility, which is the opposite of what AWS provides.

---

### Câu 4

A **large enterprise** has significant **on-premises investments in legacy systems** and **highly sensitive data** that cannot be moved to the public cloud due to **regulatory restrictions**.

However, they want to **leverage AWS for new**, less sensitive applications and for burst capacity during peak loads.

Which deployment model best describes this strategy?

A. Multi-cloud

B. Public cloud

C. Private cloud

D. Hybrid cloud

**Đáp án:** D. Hybrid cloud

**Giải thích:**

✔ D is correct: A hybrid cloud model combines on-premises infrastructure with public cloud resources, allowing organizations to leverage both environments.

✖ A: Multi-cloud involves using multiple public cloud providers.

✖ B: Public cloud refers to entirely running on a public cloud provider.

✖ C: Private cloud refers to infrastructure managed and owned solely by the organization, often on-premises.

---

### Câu 5

A student is **learning** about cloud computing and wants to **experiment with different AWS services** like Amazon EC2, S3, and Lambda **without incurring significant costs**.

They want to be able to **try out** services and **dispose** of them if they don't work out, with **minimal financial risk**.

Which AWS concept best supports this learning approach?

A. Complex change approval process

B. Dedicated hardware acquisition

C. Manual deployment process

D. Pay-as-you-go pricing

**Đáp án:** D. Pay-as-you-go pricing

**Giải thích:**

✔ D is correct: Pay-as-you-go pricing allows users to experiment with services and only pay for what they use, minimizing financial risk for experimentation.

✖ B/C: These add cost, time, and risk, which are contrary to the goal of minimal financial risk.

✖ A: Complex change approval processes are not a benefit of experimentation; they are a barrier.

---

## Cloud Technology & Services

### Câu 1

A developer wants to **quickly deploy** a new version of their **Python-based web application**.

They want to **focus on writing code** and not worry about provisioning servers, configuring load balancers, or setting up Auto Scaling.

Which AWS service enables them to **deploy** web applications rapidly **without managing** the underlying infrastructure?

A. AWS Elastic Beanstalk

B. Amazon EC2

C. Amazon ECS

D. AWS CloudFormation

**Đáp án:** A. AWS Elastic Beanstalk

**Giải thích:**

✔ A is correct: AWS Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services developed with various programming languages and servers. It handles the deployment, capacity provisioning, load balancing, and auto-scaling.

✖ B: EC2 requires manual setup and server management.

✖ C: ECS is used for container orchestration, which provides more control but still requires some cluster management.

✖ D: CloudFormation is for defining infrastructure as code, not directly for deploying applications.

---

### Câu 2

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

### Câu 3

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

### Câu 4

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

### Câu 5

A technology company is adopting **Kubernetes** for **container orchestration** to manage its microservices.

They want to **leverage the power of Kubernetes** but want to offload the operational burden of managing the Kubernetes control plane (e.g., master nodes, etcd).

Which AWS service should they use to run containerized applications using Kubernetes without managing the control plane?

A. Amazon ECS

B. AWS Lambda

C. Amazon EKS

D. AWS Fargate

**Đáp án:** C. Amazon EKS

**Giải thích:**

✔ C is correct: Amazon EKS (Elastic Kubernetes Service) is a fully managed Kubernetes service that allows you to run Kubernetes on AWS without needing to install, operate, and maintain your own Kubernetes control plane.

✖ A: ECS (Elastic Container Service) is AWS's own container orchestration service, not Kubernetes-compatible.

✖ B: Lambda runs serverless functions, not directly Kubernetes containers.

✖ D: Fargate is a serverless compute engine for containers that can be used with both ECS and EKS, but EKS is the service for managed Kubernetes itself.

---

## Security & Compliance

### Câu 1

A financial institution stores **customer transaction data** in Amazon **S3 buckets**.

Due to **strict auditing** and **regulatory requirements**, they need to **know precisely who** accessed specific S3 objects, when, and from where.

Which AWS service should they enable to record all access events for their S3 data?

A. AWS Macie
B. AWS IAM
C. AWS CloudTrail
D. AWS Config

**Đáp án:** C. AWS CloudTrail

**Giải thích:**

✔ C is correct: CloudTrail logs all API calls to AWS services, including data events for S3 objects, providing a complete audit trail of who accessed what, when, and from where.

✖ A: Macie discovers sensitive data but doesn't track access logs.

✖ B: IAM defines permissions, but doesn't record access history.

✖ D: Config tracks resource configurations and changes, not access history.

---

### Câu 2

A company is **preparing for a compliance audit** (e.g., PCI DSS, HIPAA). They need a way to **continuously assess** whether their AWS resources **comply with internal and external regulations**, and to **identify any deviations** from their defined security baselines.

Which AWS service helps ensure this ongoing compliance by assessing and auditing your AWS resource configurations?

A. AWS Trusted Advisor
B. AWS Config
C. AWS GuardDuty
D. Amazon Inspector

**Đáp án:** B. AWS Config

**Giải thích:**

✔ B is correct: AWS Config enables you to assess, audit, and evaluate the configurations of your AWS resources. Config continuously monitors and records your AWS resource configurations and allows you to automate the evaluation of recorded configurations against desired configurations.

✖ A: Trusted Advisor provides general best practice recommendations and cost optimization, not detailed compliance tracking against specific rules.

✖ C: GuardDuty detects threats, not compliance deviations.

✖ D: Inspector is for vulnerability assessment of EC2 instances, not overall resource configuration compliance.

---

### Câu 3

A large legal firm **stores various** client documents, including contracts and personal identifiable information (PII), in **Amazon S3**.

They are **concerned about accidentally exposing sensitive data** and need a service that can **automatically identify** and **classify PII or other sensitive information** within their S3 buckets.

Which AWS service **helps detect** the storage of sensitive personal data?

A. Amazon Detective
B. AWS WAF
C. AWS Macie
D. AWS Config

**Đáp án:** C. AWS Macie

**Giải thích:**

✔ C is correct: Amazon Macie is a data security and data privacy service that uses machine learning and pattern matching to discover, classify, and protect sensitive data in AWS, such as PII and financial information.

✖ A: Detective helps with security investigations and analysis of findings, not sensitive data discovery.

✖ B: WAF protects web applications.

✖ D: Config tracks resource configurations.

---

### Câu 4

An enterprise with a **complex organizational structure** in AWS (multiple accounts, organizational units) wants to **enforce certain maximum permissions for all IAM users** and **roles within specific OUs**.

For example, no IAM identity in the "Development" OU should ever be able to delete production S3 buckets, regardless of the individual IAM policy.

Which AWS service enables organizations to set these permissions boundaries **using Service Control Policies (SCPs)**?

A. AWS IAM
B. AWS Organizations
C. AWS Shield
D. Amazon Inspector

**Đáp án:** B. AWS Organizations

**Giải thích:**

✔ B is correct: AWS Organizations enables you to use Service Control Policies (SCPs) to centrally manage permissions for all accounts in your organization, acting as a "guardrail" to set maximum available permissions.

✖ A: IAM manages individual users and roles within an account but does not use SCPs to set organization-wide boundaries.

✖ C: Shield provides DDoS protection.

✖ D: Inspector assesses vulnerabilities, not permissions boundaries.

---

### Câu 5

A company has a **strict security policy** requiring that all Amazon S3 buckets must have **server-side encryption** enabled.

They want a **solution** that **not only identifies non-compliant buckets** but also automatically remediates them by **enabling encryption**.

Which AWS service is best suited for monitoring and automatically remediating non-compliant resources in AWS?

A. AWS IAM
B. AWS CloudTrail
C. AWS Config
D. Amazon Macie

**Đáp án:** C. AWS Config

**Giải thích:**

✔ C is correct: AWS Config continuously monitors and records your AWS resource configurations and allows you to automate the evaluation of recorded configurations against desired configurations. It can also trigger automated remediation actions using AWS Systems Manager Automation documents.

✖ A: IAM controls access, not compliance monitoring or remediation.

✖ B: CloudTrail logs actions but does not actively remediate.

✖ D: Macie identifies sensitive data but doesn't enforce or remediate compliance configurations.

---

## Billing, Pricing & Support

### Câu 1

What is the **primary function of Cost Allocation Tags** in AWS?

A. To automatically optimize resource spending.

B. To categorize and track AWS costs by project, department, or other criteria.

C. To provide real-time security alerts for resources.

D. To set hard limits on spending for specific resources.

**Đáp án:** B. To categorize and track AWS costs by project, department, or other criteria.

**Giải thích:**

✔ B is correct: Cost Allocation Tags are key-value pairs that you can attach to AWS resources to organize them. When you activate these tags, AWS uses them to organize your resource costs on your cost allocation report, making it easier to categorize and track your AWS costs.

✖ A: Tags do not automatically optimize spending; they only help in tracking and reporting.

✖ C: This is the function of services like Amazon GuardDuty or AWS Security Hub.

✖ D: Tags cannot set spending limits; that is the function of AWS Budgets.

---

### Câu 2

A **non-profit organization** wants to **estimate the monthly cost** of a new application they plan to host on AWS, which will use Amazon EC2, Amazon S3, and Amazon RDS.

Which tool can they use to get a **detailed estimate before migrating?**

A. AWS Cost & Usage Report

B. AWS Budgets

C. AWS Cost Explorer

D. AWS Pricing Calculator

**Đáp án:** D. AWS Pricing Calculator

**Giải thích:**

✔ D is correct: The AWS Pricing Calculator is a web-based service that you can use to create cost estimates for your AWS use cases. It allows you to model your solutions before building them, explore the price points, and review the calculations behind your estimates.

✖ A: The Cost & Usage Report is a detailed billing file containing data about your _actual_ usage, not for estimating future costs.

✖ B: AWS Budgets is for setting alerts on your spending, not for creating an initial estimate.

✖ C: AWS Cost Explorer is for analyzing your _current_ and past costs, not for estimating a new workload.

---

### Câu 3

What benefit does the **consolidated billing feature** of **AWS Organizations** provide?

A. It provides a separate invoice for each AWS account in the organization.

B. It combines the usage from all accounts to a single bill, potentially qualifying for volume pricing discounts.

C. It applies a security policy to all accounts automatically.

D. It gives every account a dedicated Technical Account Manager (TAM).

**Đáp án:** B. It combines the usage from all accounts to a single bill, potentially qualifying for volume pricing discounts.

**Giải thích:**

✔ B is correct: Consolidated billing allows you to get a single bill for multiple AWS accounts. A key benefit is that you can combine the usage across all accounts to share volume pricing discounts, Reserved Instance discounts, and Savings Plans.

✖ A: It does the opposite; it creates a single, consolidated bill.

✖ C: This is the function of Service Control Policies (SCPs), not consolidated billing itself.

✖ D: A TAM is a feature of the Enterprise Support plan, not a feature of consolidated billing.

---

### Câu 4

A company **has several idle Amazon RDS** instances and **underutilized Amazon EBS volumes** that are incurring unnecessary costs.

Which AWS service can **automatically scan** their environment and provide **specific recommendations to reduce this waste?**

A. Amazon CloudWatch

B. AWS Config

C. AWS Trusted Advisor

D. AWS Cost Explorer

**Đáp án:** C. AWS Trusted Advisor

**Giải thích:**

✔ C is correct: AWS Trusted Advisor acts like your cloud expert and helps you provision your resources by following AWS best practices. The cost optimization pillar specifically checks for things like idle load balancers, underutilized EBS volumes, and idle RDS instances.

✖ A: CloudWatch monitors resource metrics but does not provide cost-saving recommendations on its own.

✖ B: AWS Config checks for compliance with configuration rules, not for cost optimization opportunities.

✖ D: Cost Explorer helps you visualize costs but does not perform automated checks to identify specific underutilized resources.

---

### Câu 5

A security team wants to enhance their AWS security posture by **proactively identifying potential security vulnerabilities** and **deviations from best practices** within their EC2 instances.

They need an **automated service** that can **continuously scan** for misconfigurations, known vulnerabilities, and security exposures.

Which AWS service provides **threat detection** for malicious or unauthorized activity in your AWS environment?

A. AWS Config
B. Amazon GuardDuty
C. AWS CloudTrail
D. AWS Macie

**Đáp án:** B. Amazon GuardDuty

**Giải thích:**

✔ B is correct: Amazon GuardDuty is a continuous security monitoring service that analyzes and processes VPC Flow Logs, AWS CloudTrail management event logs, and DNS logs. It uses threat intelligence feeds and machine learning to identify malicious activity and unauthorized behavior.

✖ A: Config tracks compliance and resource changes, not active threats.

✖ C: CloudTrail logs activity but doesn't analyze for threats.

✖ D: Macie detects sensitive data exposure, not malicious activity or broader threats.
