# Billing, Pricing & Support

# SET 1:

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

They need a tool that provides **visual report**s and allows them to **identify cost trends and anomalies**.

Which AWS tool provides a visualization of historical usage and cost data, and supports forecasting?

A. AWS Budgets

B. AWS Cost Explorer

C. AWS Marketplace

D. AWS Config

**Đáp án:** B. AWS Cost Explorer

**Giải thích:**

✔ B is correct: AWS Cost Explorer is a free tool that allows you to view and analyze your AWS costs and usage. You can visualize your cost and usage data at a high level (e.g., total costs for all accounts) or analyze it by specific dimensions (e.g., service, region, tags) and also forecast future costs.

✖ A: AWS Budgets allows you to set custom budgets and receive alerts when your costs or usage exceed (or are forecasted to exceed) your budgeted amount.23 It doesn't primarily focus on historical visualization and forecasting.

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

A **small startup** is operating on a **tight budget** and is w**orried about unexpected increases** in their monthly AWS bill as their usage grows.

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

---

### Câu 6

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

### Câu 7

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

# SET 2:

### Câu 1

A company wants to **track AWS usage costs** by department. Which feature should they implement to **break down billing per department**?

A. AWS Trusted Advisor

B. Consolidated Billing

C. Cost Allocation Tags

D. Amazon CloudWatch Logs

**Đáp án:** C. Cost Allocation Tags

**Giải thích:**

✔ C is correct: Tags let you allocate usage and costs by department.

✖ A: Trusted Advisor gives best practices, not billing breakdowns.

✖ B: Consolidated Billing combines bills but doesn’t divide them.

✖ D: CloudWatch Logs monitor performance, not costs.

---

### Câu 2

Which AWS tool **provides a visualization of historical usage and cost data**, and supports **forecasting**?

A. AWS Budgets

B. AWS Cost Explorer

C. AWS Marketplace

D. AWS Config

**Đáp án:** B. AWS Cost Explorer

**Giải thích:**

✔ B is correct: Cost Explorer helps visualize past usage and forecast future costs.

✖ A: Budgets are for setting cost thresholds, not exploration.

✖ C: Marketplace is for buying software, not usage visualization.

✖ D: Config tracks resource configurations, not costs.

---

### Câu 3

A company is comparing **Reserved Instances and Savings Plans** for its consistent **Amazon EC2 usage**. What is a **key benefit** of using **Savings Plans over Reserved Instances**?

A. They apply only to compute usage in one Region

B. They require a long-term upfront payment

C. They offer more flexibility across instance types and regions

D. They apply only to specific EC2 instance families

**Đáp án:** C. They offer more flexibility across instance types and regions

**Giải thích:**

✔ C is correct: Savings Plans offer flexibility across instance families, sizes, and regions.

✖ A: Reserved Instances are more restrictive than Savings Plans.

✖ B: Upfront is optional for Savings Plans.

✖ D: RIs have family restrictions; Savings Plans don’t.

---

### Câu 4

A startup wants to **avoid unexpected AWS charges**. Which AWS service allows them to **set alerts** when their usage or **costs exceed** a threshold?

A. AWS Billing Dashboard

B. AWS Budgets

C. AWS Cost Explorer

D. AWS Organizations

**Đáp án:** B. AWS Budgets

**Giải thích:**

✔ B is correct: AWS Budgets lets users set cost thresholds and sends alerts.

✖ A: Billing Dashboard shows costs but doesn’t alert.

✖ C: Cost Explorer is for visualizing, not alerting.

✖ D: Organizations helps with multi-account management, not budget alerts.

---

### Câu 5

A company plans to run an **EC2-based workload for 3 years with consistent usage**. Which purchasing option is the **most cost-effective**?

A. On-Demand Instances

B. Spot Instances

C. Reserved Instances

D. Savings Plans

**Đáp án:** D. Savings Plans

**Giải thích:**

✔ D is correct: Savings Plans offer high savings and flexibility for long-term workloads.

✖ A: On-Demand is most expensive for sustained use.

✖ B: Spot is not suitable for guaranteed availability.

✖ C: RIs are cost-effective but less flexible than Savings Plans.

---

### Câu 6

Which of the following is **included in the AWS Free Tier**?

A. 750 hours/month of Amazon EC2 t2.micro for 12 months

B. 10 TB of S3 Standard storage per month

C. 1 year of AWS Support at the Business level

D. Unlimited AWS Lambda function executions

**Đáp án:** A. 750 hours/month of Amazon EC2 t2.micro for 12 months

**Giải thích:**

✔ A is correct: The Free Tier offers 750 hours of EC2 t2.micro for the first 12 months.

✖ B: Only 5 GB of S3 is free.

✖ C: Support plans are paid.

✖ D: Lambda has free usage limits, not unlimited.

---

### Câu 7

A company needs support for **AWS infrastructure with 24/7 access to Cloud Support Engineers** and a **designated Technical Account Manager.** Which AWS Support Plan is required?

A. Developer

B. Basic

C. Business

D. Enterprise

**Đáp án:** D. Enterprise

**Giải thích:**

✔ D is correct: Enterprise support includes TAM and 24/7 access.

✖ A: Developer doesn’t include TAM or 24/7 support.

✖ B: Basic plan offers only billing support.

✖ C: Business includes 24/7 but not a TAM.

---

# SET 3:

### Câu 1

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

### Câu 2

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

### Câu 3

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

---

### Câu 4

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

### Câu 5

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

### Câu 6

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

### Câu 7

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
