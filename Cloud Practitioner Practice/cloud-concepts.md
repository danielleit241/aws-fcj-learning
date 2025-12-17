# Cloud Concepts

# SET 1:

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

They also want to **ensure high fault tolerance** for their service. What key advantage of AWS’s global infrastructure does this scenario highlight?

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

### Câu 6

A new SaaS company is designing its multi-tenant application on AWS. They are responsible for **managing the application** code, customer data, and network configurations for their application.

AWS is **responsible for the physical security** of the data centers, hardware, and global infrastructure.

Which **aspect of the AWS Shared Responsibility Model** does this scenario illustrate?

A. AWS is responsible for security in the cloud.

B. The customer is responsible for security of the cloud.

C. The customer is responsible for security in the cloud, and AWS is responsible for security of the cloud.

D. Both AWS and the customer share responsibility equally for all aspects.

**Đáp án:** C. The customer is responsible for security in the cloud, and AWS is responsible for security of the cloud.

**Giải thích:**

✔ C is correct: The Shared Responsibility Model states AWS is responsible for the security of the cloud (infrastructure), and the customer is responsible for security in the cloud1 (their data, applications, configurations).

✖ A: Incorrect, AWS is responsible for security of the cloud.

✖ B: Incorrect, the customer is responsible for security in the cloud.

✖ D: While shared, the responsibilities are distinctly divided, not equally for all aspects.

---

### Câu 7

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

### Câu 8

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

### Câu 9

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

### Câu 10

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

### Câu 11

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

### Câu 12

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

### Câu 13

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

### Câu 14

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

### Câu 15

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

### Câu 11

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 12

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 13

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 14

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 15

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

---

### Câu 11

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 12

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 13

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 14

**...**

**Đáp án:**

**Giải thích:**

---

### Câu 15

**...**

**Đáp án:**

**Giải thích:**
