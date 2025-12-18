# Security & Compliance

# SET 1:

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

✔ A is correct: AWS WAF (Web Application Firewall) helps protect web applications from common web exploits that could affect application availability, compromise security,2 or consume excessive3 resources.

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

✔ C is correct: AWS Key Management Service (KMS) is a managed service that makes it easy for you to create and control the encryption keys used to encrypt your4 data.

✖ A: IAM handles access control, not encryption key management.

✖ B: Macie detects sensitive data, it doesn't manage encryption keys.

✖ D: CloudTrail logs API activity, it doesn't manage encryption keys.

---

### Câu 6

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

### Câu 7

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

### Câu 8

A **DevOps team** manages several applications that rely on **various third-party API keys** and **database credentials**.

They need a **secure way to store, retrieve**, and **automatically rotate** these secrets to enhance their security posture.

Which AWS service provides this functionality?

A. AWS Systems Manager Parameter Store
B. AWS Secrets Manager
C. Amazon S3
D. Amazon Macie

**Đáp án:** B. AWS Secrets Manager

**Giải thích:**

✔ B is correct: AWS Secrets Manager helps you protect secrets needed to access your applications, services, and IT resources. It enables you to easily rotate, manage, and retrieve5 database credentials, API keys, and other secrets throughout their lifecycle.

✖ A: Systems Manager Parameter Store can store secrets but **lacks the automatic rotation** and comprehensive management features of Secrets Manager.

✖ C: S3 is object storage and not designed for secure secret management and rotation.

✖ D: Macie scans for sensitive data, not secure storage and rotation of credentials.

---

### Câu 9

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

### Câu 10

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

### Câu 11

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

✖ D: Config tracks resource configurations and changes, not access history

---

### Câu 12

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

### Câu 13

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

### Câu 14

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

### Câu 15

A company has a **strict security policy** requiring that all Amazon S3 buckets must have **server-side encryption** enabled.

They want a **solution** that **not only identifies non-compliant buckets** but also automatically remediates them by **enabling encryption**.

Which AWS service is best suited for monitoring and automatically remediating non-compliant resources in AWS?

A. AWS IAM
B. AWS CloudTrail
C. AWS Config
D. Amazon Macie

**Đáp án:** C. AWS Config

**Giải thích:**

✔ C is correct: AWS Config continuously monitors and records your AWS resource configurations and allows you to automate the evaluation of recorded configurations against desired configurations.10 It can also trigger automated remediation actions using AWS Systems Manager Automation documents.

✖ A: IAM controls access, not compliance monitoring or remediation.

✖ B: CloudTrail logs actions but does not actively remediate.

✖ D: Macie identifies sensitive data but doesn't enforce or remediate compliance configurat

---

### Câu 16

A growing online gaming platform is experiencing **frequent attacks** targeting their web login pages and APIs, including **brute-force** attempts and **content scraping bots**.

They need a service that can **intelligently filter out malicious traffic** and **allow legitimate users** to access their applications.

Which AWS service should they use for this specific protection?

A. AWS Shield
B. AWS WAF
C. Amazon GuardDuty
D. AWS Firewall Manager

**Đáp án:** B. AWS WAF

**Giải thích:**

✔ B is correct: AWS WAF (Web Application Firewall) is designed to protect web applications from common web exploits and bots by allowing you to create custom rules to block or allow traffic based on various criteria.

✖ A: Shield primarily focuses on DDoS protection at a higher level, not application-layer exploits and bots specifically.

✖ C: GuardDuty provides threat detection but doesn't actively block traffic at the web application layer.

✖ D: Firewall Manager helps manage WAF rules across multiple accounts, but WAF itself is the service that does the blocking.

---

### Câu 17

A company requires that all employees **accessing the AWS Management Console** enable an **additional layer** of security beyond their username and password, such as a **virtual MFA device** or a **hardware token**.

What is the best AWS service or feature to implement **multi-factor authentication (MFA)** for users accessing the AWS Management Console?

A. AWS IAM
B. AWS Directory Service
C. AWS Organizations
D. Amazon Cognito

**Đáp án:** A. AWS IAM

**Giải thích:**

✔ A is correct: AWS IAM (Identity and Access Management) is the service used to manage users, groups, and roles, and it supports the configuration of MFA for individual IAM users accessing the AWS Management Console.

✖ B: Directory Service provides managed Microsoft AD and integrates with IAM, but MFA is configured directly within IAM.

✖ C: Organizations manages accounts but does not handle MFA for individual users.

✖ D: Cognito is for authentication for your own applications, not for AWS console access.

---

### Câu 18

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

---

### Câu 19

A compliance officer at a financial institution needs to **ensure that all data encrypted** in various AWS services (e.g., S3, RDS, EBS) uses **customer-managed keys** for added control and auditability.

They require a centralized service to create, store, and manage these encryption keys. Which AWS service should be used for this purpose?

A. AWS Secrets Manager
B. AWS Key Management Service (KMS)
C. AWS Certificate Manager
D. AWS CloudHSM

**Đáp án:** B. AWS Key Management Service (KMS)

**Giải thích:**

✔ B is correct: AWS Key Management Service (KMS) allows you to create and control the encryption keys used to encrypt your data across a wide range of AWS services and in your applications.

✖ A: Secrets Manager stores credentials and API keys, not general encryption keys.

✖ C: Certificate Manager manages SSL/TLS certificates, not encryption keys for data at rest.

✖ D: CloudHSM provides dedicated hardware security modules (HSMs) for highly sensitive key storage, but KMS is the more common and integrated service for central key management for most use cases.

---

### Câu 20

A forensics team is investigating a **potential security incident** in their AWS account.

They need to **reconstruct a timeline of events**, including **which users or services** made specific **API calls, modified resources, or accessed data**.

Which AWS service can help them **audit and review user activity** and **API calls across your AWS infrastructure** to support their investigation?

A. AWS CloudTrail
B. Amazon Inspector
C. AWS Trusted Advisor
D. AWS Config

**Đáp án:** A. AWS CloudTrail

**Giải thích:**

✔ A is correct: AWS CloudTrail provides a complete history of API calls made in your AWS account, including who made the call, when, from where, and what resources were affected, making it invaluable for security auditing and forensic investigations.

✖ B: Inspector assesses vulnerabilities on EC2 instances.

✖ C: Trusted Advisor offers recommendations for cost optimization, performance, security, etc., but doesn't log activity.

✖ D: Config tracks resource configurations and changes, but not detailed API call history for user activity.

---

# SET 2:

### Câu 1

Which AWS service is used to **centrally manage user access** and **permissions** across **multiple AWS accounts**?

A. Amazon GuardDuty

B. AWS IAM

C. AWS Organizations

D. AWS Shield

**Đáp án:** C. AWS Organizations

**Giải thích:**

✔ C is correct: AWS Organizations allows centralized management of accounts and permissions.

✖ A: GuardDuty is for threat detection.✖ B: IAM controls permissions but not across accounts.

✖ D: AWS Shield is for DDoS protection.

---

### Câu 2

What AWS service **helps protect web applications** from common web exploits like SQL injection?

A. AWS WAF

B. AWS IAM

C. Amazon Inspector

D. AWS Trusted Advisor

**Đáp án:** A. AWS WAF

**Giải thích:**

✔ A is correct: AWS WAF filters malicious traffic such as SQL injection.

✖ B: IAM handles access control.

✖ C: Inspector scans for vulnerabilities, not exploits in web traffic.

✖ D: Trusted Advisor gives best practice suggestions, not filtering.

---

### Câu 3

Which AWS feature **allows assigning** fine-grained **permissions to users and resources**?

A. Amazon Macie

B. IAM policies

C. AWS KMS

D. AWS CloudTrail

**Đáp án:** B. IAM policies

**Giải thích:**

✔ B is correct: IAM policies allow detailed control over AWS actions.

✖ A: Macie detects sensitive data.

✖ C: KMS is for encryption key management.

✖ D: CloudTrail logs API activity.

---

### Câu 4

Which of the following is a **shared responsibility** between the **customer and AWS**?

A. Hardware maintenance

B. Managing IAM roles

C. Physical security of data centers

D. Disk destruction after decommission

**Đáp án:** B. Managing IAM roles

**Giải thích:**

✔ B is correct: IAM configuration is the customer's responsibility under the shared model.

✖ A/C/D: AWS handles physical aspects.

---

### Câu 5

A financial company **needs to encrypt** all data **stored in S3**. Which AWS service can help **manage encryption keys**?

A. AWS IAM

B. Amazon Macie

C. AWS Key Management Service (KMS)

D. AWS CloudTrail

**Đáp án:** C. AWS Key Management Service (KMS)

**Giải thích:**

✔ C is correct: AWS KMS manages keys used to encrypt/decrypt data.

✖ A: IAM handles access, not encryption.

✖ B: Macie finds sensitive data.

✖ D: CloudTrail tracks access but doesn't manage keys.

---

### Câu 6

Which of the following **services records API activity** and **user actions** in an AWS account?

A. AWS CloudTrail

B. AWS CloudWatch

C. Amazon Macie

D. AWS Secrets Manager

**Đáp án:** A. AWS CloudTrail

**Giải thích:**

✔ A is correct: CloudTrail records API activity.

✖ B: CloudWatch is for monitoring and logging performance.

✖ C: Macie is for PII data discovery.

✖ D: Secrets Manager manages secrets, not logs.

---

### Câu 7

An e-commerce startup wants to **restrict access** to its AWS account using **temporary credentials**. What service should it use?

A. AWS CloudTrail

B. Amazon Macie

C. AWS IAM Roles

D. Amazon Inspector

**Đáp án:** C. AWS IAM Roles

**Giải thích:**

✔ C is correct: IAM Roles provide temporary credentials with defined permissions.

✖ A: Logs activities, not used for access.

✖ B: For sensitive data detection.

✖ D: Used for vulnerability scans.

---

### Câu 8

What AWS service **enables secure** storage and **rotation** of **API keys and credentials**?

A. AWS Systems Manager

B. AWS Secrets Manager

C. Amazon S3

D. Amazon Macie

**Đáp án:** B. AWS Secrets Manager

**Giải thích:**

✔ B is correct: Secrets Manager securely stores and rotates credentials.

✖ A: Systems Manager has Parameter Store, but less secure than Secrets Manager.

✖ C: S3 isn’t designed for secrets.

✖ D: Macie scans for sensitive data, not secure storage.

---

### Câu 9

Which AWS service can be used to **detect malicious** or **unauthorized behavior** in your AWS environment?

A. AWS WAF

B. AWS GuardDuty

C. Amazon CloudWatch

D. AWS Config

**Đáp án:** B. AWS GuardDuty

**Giải thích:**

✔ B is correct: GuardDuty provides intelligent threat detection.

✖ A: WAF protects web apps, not overall environment.

✖ C: CloudWatch monitors logs, not threats directly.

✖ D: Config tracks resource compliance.

---

### Câu 10

What is the purpose of AWS Shield?

A. Detect insider threats

B. Protect web applications from XSS

C. Protect against DDoS attacks

D. Encrypt sensitive data

**Đáp án:** C. Protect against DDoS attacks

**Giải thích:**

✔ C is correct: AWS Shield protects from Distributed Denial of Service (DDoS) attacks.

✖ A/B/D: Not the primary function of Shield.

---

### Câu 11

A healthcare organization must **comply with HIPAA** and wants to **monitor who accesses** sensitive patient data in **Amazon S3**. Which service should they use?

A. AWS Macie

B. AWS IAM

C. AWS CloudTrail

D. AWS Config

**Đáp án:** C. AWS CloudTrail

**Giải thích:**

✔ C is correct: CloudTrail logs all access to S3 buckets and objects.

✖ A: Macie discovers PII, but doesn’t track access logs.

✖ B: IAM defines permissions, doesn’t record access.

✖ D: Config tracks configuration, not access history.

---

### Câu 12

Which of the following AWS services helps **ensure compliance** by **assessing and auditing** your AWS resources?

A. AWS Trusted Advisor

B. AWS Config

C. AWS GuardDuty

D. Amazon Inspector

**Đáp án:** B. AWS Config

**Giải thích:**

✔ B is correct: AWS Config tracks changes and evaluates configuration compliance.

✖ A: Trusted Advisor offers general best practices, not detailed compliance tracking.

✖ C: GuardDuty detects threats, not compliance.

✖ D: Inspector is used for vulnerability assessment.

---

### Câu 13

What AWS service helps customers **detect the storage of sensitive personal data** such as **names or credit card numbers**?

A. Amazon Detective

B. AWS WAF

C. AWS Macie

D. AWS Config

**Đáp án:** C. AWS Macie

**Giải thích:**

✔ C is correct: Macie uses machine learning to detect sensitive data like PII.

✖ A: Detective helps with security investigations.

✖ B: WAF protects web apps from exploits.

✖ D: Config is for resource configurations.

---

### Câu 14

Which AWS service **lets organizations set permissions boundaries** using **Service Control Policies (SCPs)**?

A. AWS IAM

B. AWS Organizations

C. AWS Shield

D. Amazon Inspector

**Đáp án:** B. AWS Organizations

**Giải thích:**

✔ B is correct: AWS Organizations lets you define SCPs for accounts and OUs.

✖ A: IAM manages individual roles/users but doesn’t use SCPs.

✖ C: Shield provides DDoS protection.

✖ D: Inspector assesses vulnerabilities, not permissions.

---

### Câu 15

A company wants to **monitor and automatically** remediate **non-compliant resources** in AWS. Which service is best suited for this?

A. AWS IAM

B. AWS CloudTrail

C. AWS Config

D. Amazon Macie

**Đáp án:** C. AWS Config

**Giải thích:**

✔ C is correct: AWS Config can monitor and trigger remediation for compliance issues.

✖ A: IAM controls access, not compliance monitoring.

✖ B: CloudTrail logs actions but doesn’t remediate.

✖ D: Macie identifies sensitive data but doesn’t enforce remediation.

---

### Câu 16

A company wants to **protect its web applications** from **common web exploits and malicious bots**. Which AWS service should it use?

A. AWS Shield

B. AWS WAF

C. Amazon GuardDuty

D. AWS Firewall Manager

**Đáp án:** B. AWS WAF

**Giải thích:**

✔ B is correct: AWS WAF is a web application firewall that protects web apps from exploits and bots.

✖ A: Shield focuses on DDoS protection, not web application attacks.

✖ C: GuardDuty is for threat detection, not active blocking.

✖ D: Firewall Manager manages multiple firewalls but does not itself block attacks.

---

### Câu 17

What is the best AWS service to **provide multi-factor authentication (MFA)** for users accessing the **AWS Management Console**?

A. AWS IAM

B. AWS Directory Service

C. AWS Organizations

D. Amazon Cognito

**Đáp án:** A. AWS IAM

**Giải thích:**

✔ A is correct: IAM supports MFA for user accounts to enhance security.

✖ B: Directory Service provides managed Microsoft AD, but MFA setup is in IAM.

✖ C: Organizations manages accounts but does not handle MFA.

✖ D: Cognito is for app user authentication, not AWS console users.

---

### Câu 18

Which AWS **service provides threat detection** for **malicious or unauthorized activity** in your **AWS environment**?

A. AWS Config

B. Amazon GuardDuty

C. AWS CloudTrail

D. AWS Macie

**Đáp án:** B. Amazon GuardDuty

**Giải thích:**

✔ B is correct: GuardDuty provides continuous threat detection using machine learning.

✖ A: Config tracks compliance, not threats.

✖ C: CloudTrail logs activity but does not analyze for threats.

✖ D: Macie detects sensitive data exposure, not threats.

---

### Câu 19

A company wants to **centrally manage encryption keys** used to **protect data in AWS services**. Which AWS service should be used?

A. AWS Secrets Manager

B. AWS Key Management Service (KMS)

C. AWS Certificate Manager

D. AWS CloudHSM

**Đáp án:** B. AWS Key Management Service (KMS)

**Giải thích:**

✔ B is correct: AWS KMS manages encryption keys centrally.

✖ A: Secrets Manager stores credentials, not encryption keys.

✖ C: Certificate Manager manages SSL/TLS certificates.

✖ D: CloudHSM provides hardware security modules, but KMS is easier and more integrated.

---

### Câu 20

Which AWS service can help **audit and review** user **activity and API calls** across your **AWS infrastructure**?

A. AWS CloudTrail

B. Amazon Inspector

C. AWS Trusted Advisor

D. AWS Config

**Đáp án:** A. AWS CloudTrail

**Giải thích:**

✔ A is correct: CloudTrail logs all API calls for auditing.

✖ B: Inspector assesses vulnerabilities but doesn’t log activity.

✖ C: Trusted Advisor offers recommendations, not logs.

✖ D: Config tracks resource configurations, not user/API activity.

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
