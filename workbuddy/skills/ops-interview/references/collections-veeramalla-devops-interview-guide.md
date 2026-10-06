# DevOps / SRE 真实面试题（iam-veeramalla/DevOps-Interview-Guide，3024 题）

> **来源**：[iam-veeramalla/DevOps-Interview-Guide](https://github.com/iam-veeramalla/DevOps-Interview-Guide)（Abhishek Veeramalla 维护，社区投稿的
> 2025–2026 年 DevOps / SRE / Cloud 真实面试经历，151 份写实、86 家公司 + `Others/`；快照 `6228e04`，2026-08-05）。
> **收录日期**：2026-09-20
> **口径**：仓库未声明许可证；本文件**只收录题目文本**（原文措辞，英文为主，个别拼写按原样保留），按「公司 / 岗位 / 经验年限」保留原仓库分组，
> 不收录投稿者的答案与心得；用于学习与参考并明确标注出处。题目常见主题：Kubernetes、Docker、Terraform、AWS / Azure / GCP、CI/CD（Jenkins / GitHub Actions /
> Azure DevOps）、Ansible、Linux、Shell / Python 脚本、SRE 基础（SLI / SLO / 事故）。
> **怎么用**：面试官按候选人目标公司 / 年限选一份写实做「同款模拟」；也可按主题跨公司抽题。参考答案去 `modules/` 对应模块找（映射见文末）。

## 公司索引

| 公司 | 写实数 | 题量 |
|---|---|---|
| AMEX | 1 | 12 |
| Accenture | 1 | 10 |
| Accion Labs | 1 | 18 |
| Accolite | 1 | 22 |
| Akamai | 1 | 14 |
| Alphadyne | 2 | 30 |
| Altimetrik | 1 | 26 |
| Amadeus Labs | 1 | 12 |
| Amazon | 2 | 33 |
| Arrise Solutions | 1 | 30 |
| Aspire | 1 | 16 |
| BMW TechWorks | 1 | 10 |
| Belcan | 1 | 12 |
| Blue Yonder | 1 | 10 |
| CGI | 1 | 17 |
| CMT | 1 | 17 |
| CTS | 3 | 40 |
| Capgemini | 3 | 68 |
| Cisco | 1 | 22 |
| Commonwealth Bank | 1 | 10 |
| Deloitte | 4 | 82 |
| EPAM | 3 | 83 |
| EXL Service | 1 | 28 |
| EY | 2 | 35 |
| Elixr Labs | 1 | 26 |
| Emphasis | 2 | 26 |
| Encora | 1 | 18 |
| F5 | 1 | 18 |
| Five9 | 1 | 11 |
| Flentas | 1 | 40 |
| HCL | 4 | 59 |
| Hexaware | 1 | 15 |
| IBM | 4 | 78 |
| ITC Infotech | 1 | 6 |
| Infinite Solutions | 1 | 3 |
| Infosys | 4 | 78 |
| Intact Green Services | 1 | 12 |
| JPMorgan | 3 | 79 |
| Koerber Pharma | 1 | 37 |
| LTIMindtree | 5 | 48 |
| L and T | 1 | 24 |
| Marsh McLennan | 1 | 17 |
| Moodys | 1 | 10 |
| Morgan Stanley | 1 | 18 |
| NPCI | 1 | 10 |
| NUOS INFO Systems | 1 | 18 |
| NatWest Group | 1 | 7 |
| Netcracker | 1 | 22 |
| Nextturn | 1 | 22 |
| Nice | 2 | 33 |
| Nisum Technologies | 1 | 14 |
| Nitor Infotech | 1 | 25 |
| OPT IT | 1 | 15 |
| One2N | 1 | 21 |
| Optum | 1 | 9 |
| Oracle | 2 | 21 |
| Orion Innovation | 1 | 12 |
| Perfios | 1 | 14 |
| Persistent Systems | 4 | 58 |
| Plansource ValueLabs | 1 | 13 |
| Publicis Global Delivery | 1 | 7 |
| Qburst | 1 | 17 |
| Qentelli Solutions | 1 | 13 |
| Rapidsoft | 1 | 12 |
| RelevantZ | 1 | 21 |
| SAP | 1 | 12 |
| Sapient | 1 | 25 |
| Sigmoid | 4 | 149 |
| Sonata Software | 2 | 50 |
| Sony | 1 | 31 |
| SquareOps | 1 | 268 |
| Syncortex | 1 | 10 |
| Synechron | 3 | 56 |
| TCS | 4 | 69 |
| Techdome | 1 | 7 |
| Turning | 1 | 9 |
| UST | 1 | 14 |
| Verizon | 1 | 28 |
| Virtusa | 1 | 19 |
| Volkswagen Group Digital | 1 | 12 |
| Wikreate Media | 1 | 6 |
| Wipro | 5 | 76 |
| ZS Associates | 1 | 27 |
| Zensar | 1 | 19 |
| ZopSmart | 1 | 22 |
| Others | 20 | 451 |

---

## AMEX（12 题）

### AMEX — DevOps Engineer（YOE---> 3 yrs）（12 题）

- whats the difference between docker and kubernetes
- how to reduce the downtime with deployments
- what agents you have deployed
- suppose there are 100 applications how do you log analysis
- difference between sre and devops
- did you do any migrations from onpremises to cloud if so what challenges you have faced
- how the end point authentication works in kubernetes
- how did you troubleshoot the pod crashback loop
- what is sla and slo
- provide the agent which you worked for customer or your company
- tell me the cloud architecture which you have worked
- explain the production issue which you have faced

## Accenture（10 题）

### Accenture — DevOps Engineer（EXP- 6yrs）（10 题）

- You have created an IAM user in AWS and configured role-based access in EKS. How do you bind the IAM user to the EKS role?
- Assume you have 10 AWS accounts. How will you securely log in to them, considering access keys are not used for security reasons?
- What are the ways to log in to an AWS account?
- Does Amazon S3 require a VPC?
- What happen when we run terraform init ?
- write a terraform script to create an ec2 instance in multiple region.
- You have defined a multi-region Terraform configuration (region1, region2, region3). If you create an EC2 instance, in which region will it be deployed?
- If the frontend, backend, and database are all deployed in private subnets, how can an end user access the application?
- If secrets are created in AWS Secrets Manager, how can Amazon EKS access those secrets?
- How do you set up RBAC in Amazon EKS?

## Accion Labs（18 题）

### Accion Labs — SRE（Exp---17yrs SRE）（18 题）

- How do you ensure high availability in Kubernetes?
- What are SLO, SLI, and SLA, and why are they important?
- Can you describe a recent major incident you handled and how you resolved it?
- What is the deployment setup in your organization?
- What is the maximum time taken for a node to start after a failure or restart?
- How have you resolved high-performance issues or critical incidents?
- What is the difference between observability and monitoring?
- What is the Linux command used for mounting a file system?
- How do you detect the root cause when an application goes down in the cloud?
- How do you respond when:
- a) the master node goes down?
- b) a worker/slave node goes down?
- How do you configure a VPC for high availability?
- Have you worked on scripting? if so which tool ? explain what you have implemented?
- Have you written Terraform code for deployments? If yes, can you explain the implementation?
- Can you explain your hands-on experience with Docker?
- Why do we use workspaces in Terraform?
- Tell me about Ansible. Have you worked on it before? If yes, in what context?

## Accolite（22 题）

### Accolite — DevOps Engineer（Exp---- 3yr DevOps Engineer）（22 题）

- Write a script to monitor a directory and print the names of new files added every minute. -->In Python
- What is the difference between set and list in python(Counter question of the above)
- You have two tables:
- Customers(customer_id, customer_name)
- Orders(order_id, customer_id, order_date, amount)
- Write a SQL query to find the names of customers who placed more than 3 orders in the last 90 days.
- Write a Python function that takes a list of dictionaries representing job logs. The function should return a list of job IDs where the "status" is "FAILED".
- Example:
- logs = [
- ("job_id": 101, "status":
- "SUCCESS", "timestamp":
- "2025-06-10T10:00:00"), ("job_id": 102, "status":
- "FAILED", "timestamp":
- "2025-06-10T10:05:00"), ("job_jd": 103, "status":
- "FAILED", "timestamp":
- *2025-06-10T10:10:00"),
- "job_jd": 104, "status":
- "SUCCESS", "imestamp";
- "2026-06-10T10:16:00")]
- What is CICD and explain in briefly
- Explain  kubernetes Architecture and component and their uses.
- Note -: Guy,s in Every question, they asked to explain in briefly and the code and how it using and what will be outputs.

## Akamai（14 题）

### Akamai — SRE（Exp---8yrs  SRE）（14 题）

- IPv4 vs IPv6
- IPv4 address starts from
- Write a script to find out if the provided IP is valid IPv4 or not
- Write a unix command to find out all the files which has a size more than 1 GB
- Write a unix command to find the ERROR keyword in a txt file, ERROR will be incase sensitive
- If you're logging to linux machine for the first time, what will be the process
- If you're unable to access linux machine, what you will do
- 5/2 ?? and 5//2 ??
- a = [0] b = {0}, what will be the result of a[0] and b[0]
- How to check the firewall protection
- OSI models ?
- Diff b/w Public and Private hosted zones
- How will you create Kustomize file
- Diff b/w CMD & ENTRYPOINT

## Alphadyne（30 题）

### Alphadyne — DevOps Engineer 1（YOE---> 5 Years）（12 题）

- Interviewer introduced himself and explained the role, team setup, and expectations and asked me to itroduce
- Application is hosted on a public EC2 instance.How to migrate it to a private subnet following AWS best practices (security, networking, HA).
- How to provide HTTPS access to an application hosted in a private subnet.
- Discussion around ALB/NLB, ACM certificates, routing, and security groups.
- Infrastructure changes I have worked on. Deep discussion on architecture changes, optimizations, and real challenges faced.
- One major production Kubernetes issue that I solved and still remember.
- Root cause analysis, troubleshooting approach, fix, and preventive measures.
- Branching strategy discussion in depth.
- Why this strategy was chosen
- How it supports multiple environments, releases, and hotfixes.
- New application scenario:Developer has written only source code As a DevOps engineer, how to design CI/CD...Deploying to DEV / QA / PROD using best practices.
- Multibranch pipeline in Jenkins: How to configure it What problems it solves Why it is preferred over a normal SCM pipeline.

### Alphadyne — DevOps Engineer 2（YOE-->）（18 题）

- Alphadyne assessment ->>
- multiple choice -
- tool should a company use to automatedeploy configuration managing vm and container
- module used to install nginx web server when automating using ansible in new server
- ansible module u useto ensure specific package is installed on a new websrrver while configuring the server
- ansible module u useto ensure specific package is installed on a new websrrver while configuring the server
- Object used to manage kubernetes cluster and ensure pod always has specific resources
- Best pick command to monitor disk write and reads
- i have pub key and i want a dev to provide access to a server. where do u store pub key
- User password on modern linux location
- Coding Task (Terraform on Azure):
- Define an Azure Virtual Network (VNet) with a given IP range
- Create multiple subnets for different layers (bastion, application, database)
- Configure Network Interfaces (NICs) and attach them to the correct subnets
- Provision Virtual Machines (VMs) using those NICs, with username and password authentication
- Create Public IPs where required
- Set up an Azure Bastion Host for secure access to the VMs
- Configure an Azure Load Balancer to route traffic to the application VMs

## Altimetrik（26 题）

### Altimetrik — SRE（26 题）

- Question : How do you import a resource into Terraform that was created manually in AWS or GCP? What command would you use?
- Question : Can you describe your exposure to different environments like Dev, QA, and Prod?
- Question : What is your understanding of software architecture components (Load balancers, web servers, application servers, databases, and integrations)?
- Question : What is your experience with alerts, logging, and incident/problem resolution?
- Question : What is your knowledge of production system sizing, provisioning, setup, maintenance, and closure?
- Question : Describe your experience with infrastructure administration tasks like licensing, billing, cost reduction, and security.
- Question : Walk me through what is there in helm charts and how it is integrated.explain me that what is written on your helm charts?
- what is defined on your value dot yaml file?
- Question : Considering you have different environments and you have one application or which is microservice which is finally going to get deployed into one of the pod in GKE,
- right? So how it is basically getting deployed in cluster? I mean the deployment is basically failing just on the pod is currently in the error state. It is getting terminated. So how are you going to troubleshoot those such kind of Kubernetes issues?
- What is your approach of doing a troubleshooting?
- Question : Can you, talked about the dashboards of observability? Which are the observability framework tools That you're currently using?
- Question : can you tell me are you familiar with setting up dashboards and alerts yourself like creating dashboards and alerts?
- Question : So can you walk me through what all dashboards that you have created, what type of alerts that you have created?
- Question : Have you used it in your day-to-day basis of dashboarding and alerting like based on the principles of SRE golden signals to set up alerts and dashboards?
- Question : Did all those things and have you kind of done anything like SLO based learning?
- Question : can you explain me what is error budget?
- Question : In Observability there is a concept of SLO based alerting. So have you configured that in your project?
- Question : What is what is an ideal burn rate?
- Question : So how you are using terraform to deploy the cluster nodes?
- Question : Set up the nodes and everything. what do you write inside a terraform code basically now what will be inside your provider file provided ATF in your main dotf?
- Question : I'll give you an example like let's talk about AWS. You have you're going to create a VPC and subnet And your provider is AWS and I'm asking you to write in using terraform.
- Like you have to deploy, you have to basically create VPC and map you have to create a subnet and you have to attach let's be the public or a private submit. It's of your choice to attach it to your VPC.
- Question : You have optimized Kubernetes deployment configs. So can you explain me what have what was the role and what what have you done there?
- Question : You mentioned about like the are you have architected a blameless postmortem framework, right? So for continuous learning, so how I mean what have you done to improve occurrence of critical incidents that you have mentioned in your resume.
- You also mentioned about basically to reduce the MTTR so can you explain me what automation that you have done?

## Amadeus Labs（12 题）

### Amadeus Labs — SRE（Exp-5yr SRE）（12 题）

- How to fix pod-level autoscaling not happening, what will be your approach .
- suppose we have application configured with hpa where it was running fine but suddenly it is not running what will be your approach?
- How to access application if Ingress is configured but not accessible to end users, how you will resolve ?
- How Kubernetes handles service discovery can you explain .
- How to ensure all five application teams don't use more than a particular amount of space?
- Leap second in Linux
- what type of autmation you have done in k8
- Tell what type of aumatation you have done that saved time in your project .
- 11 . Can pod be scheduled if have below security constent .
- securityContext:
- runAsNonRoot: true
- runAsUser: 0

## Amazon（33 题）

### Amazon — DevOps Consultant 1（Exp-9years(Devops Consulatnt)）（13 题）

- Sending log files from EC2 to S3, what are the steps ?
- Limiting the resource usage in k8s not through deployment.yam → Through namespace
- Three tier architecture
- Updating worker nodes in k8s
- I’m an admin but I don’t have access to the S3 bucket ? → IAM permission boundary
- Various stages of CI/CD
- How will you build the image during CI and how will you manage it ?
- You have an S3 bucket at us-south-1, is it possible to access that bucket from us-east-1 ?
- Write a Terraform code to create VPC, subnet, EC2, S3 bucket.
- Purpose of using CNI in K8s
- I need to send a logs from EC2 to S3, create an automation part where we need to take the log file, check the CPU metrics and send an alarm through cloud watch to user's.
- Is it possible to create NAT gateway in private subnet ?
- How to configure Cluster auto-scaling, how to do that

### Amazon — DevOps Consultant 2（Exp--7 years ( DevOps Consultant)）（20 题）

- If you’re migrating a monolithic application from on-prem to Cloud and the system has its local file system, which file system you will use in AWS.,
- How will you store all the configurations related to your monolithic app in Cloud,
- What are the observibility needed for app —> Monitoring, Alerting, Logging, Remediation, PD,
- If you’re not allowed to install Filebeat in your worker nodes for logging, then what will be possible option,
- What are the security protocols will be taken into consideration while designing three tier architecture.,
- DB migration, how will you sync the data,
- If DB POD is down, will it affect the data it gets stored,
- How about the sticky session data if POD gets down → Yes the session data will be lost,
- What service to use sticky session as an alternative option → redis,
- During a sticky session problem what will be the cause for LB.,
- Do you create clusters in multi regions, is it possible? If yes, then how will you manage them,
- Onboarded trading app into AWS, how will you make sure availability, scalability, security,
- How will you take a back of your entire cluster regulary ?,
- Write a python script to list the EC2 instances running in your cloud which has the tag of PROD,
- You have been tasked to create 20 EC2 per account and you been provided with 10 AWS accounts, so totally you need to create 200 EC2 machines, how will connect all these machines. Which service will be used?,
- You need to connect your DB running in private subnet, not using NAT gateway or NAT instance or bastion host, what are the other options,
- Explain about OSI model,
- Diff between directory & mount,
- Diff between local and variable in Terraform,
- You created couple of resources using Terraform, how will you make sure that resources are not modified through UI, how will you automate this check

## Arrise Solutions（30 题）

### Arrise Solutions — DevOps Engineer（Exp--7 yrs）（30 题）

- Explain me about three tier architecture
- Diff b/w ALB and NLB in depth
- How to connect a VPC in AWS to VPC in IBM Cloud
- Diff b/w Public and Private subnet
- How to connect your private subnet with Internet
- Does NAT gateway will run in public or private subnet
- K8s architecture
- CoreDNS in k8s
- What’s the purpose of CNI
- How does kube-proxy communicates with nodes
- Purpose of scheduler in k8s
- Layers in Docker
- Diff b/w using VM vs Docker
- Types of storage drivers in Docker
- Types of networking in Docker and explain in detail
- Does Docker have kernel in place
- C name and namespace in docker
- Which network will be used to isolate a communication b/w two containers
- How to check the linux process
- Booting in Linux
- How to check load of linux machine
- While rebooting a Linux machine, what are the stages / layers will be restarted
- Kernel logs are stored under which directory
- How to kill the running process
- States of Linux machine
- When you type google.com, what will happen at backend in browser
- When you type TOP command, what are the components will be displayed
- CloudFront
- I've a client and remote machine, how do certs communicate b/w them ?
- How does SSL certs works

## Aspire（16 题）

### Aspire — DevOps Engineer（EXP--3.4 yr）（16 题）

- Comapny - Aspire
- Position -
- what is the difference between replica sets and daemon sets?
- what is the difference between pv and pvc in kuberenetes?
- what is the differences between git pull and git fetch?
- what is mean by git stash and pop?
- what is the difference between NACL and Security groups?
- what is the use of command terraform fmt?
- what is the the use of terraform import ?
- what is mean by Provisioner and provider in terraform?
- what is mean by CRR in s3?
- in which cases 503 status code errors in devops?
- what are the different types of triggers in lambda aws?
- What is mean by Nat Gateway and Nat instance?
- How to find orphan resources in kubernetes and remove it?
- What is mean by Sticky session in ALB?

## BMW TechWorks（10 题）

### BMW TechWorks — DevOps Engineer（YOE: 3-4yrs）（10 题）

- Introduce yourself and explain your DevOps experience in the current organization.
- If an EC2 instance has a vulnerability, how would you identify and fix it?
- How do you patch EC2 instances?
- Can we separate disk space in an EC2 instance and run the application on one partition and the observability stack on another?
- How do you perform this disk separation, and which AWS services/tools do you use?
- Explain the project that you migrated.
- Have you containerized any application?
- Have you set up any CI/CD pipelines on your own?
- Have you used HashiCorp Vault?
- Have you used Java for coding ?

## Belcan（12 题）

### Belcan — DevOps Engineer（YOE-->9 yr）（12 题）

- Write your jenkins pipeline
- What is the purpose of agent, post-conditions and environment blocks in pipeline
- How do you perform complete backup up of Jenkins including jobs/configurations/authentications
- what are the ways to trigger the pipeline in Jenkins
- I have 5 jenkin jobs and how would you give view only acccess to other users.
- Howmany Loadbalancers avaialble in AWS and explain each one
- Difference between elasticIP and publicIP in AWS
- write down GIT commands which you use on daily basis and explain the cmds
- I have localcopy of repository and I did some changes to one file and want to push the changes to remote repository. what are the git commands you would run
- Brief me about GIT Stash
- what is the terraform statefile
- writedown the few terraform commands and explain each cmd

## Blue Yonder（10 题）

### Blue Yonder — DevOps Engineer（10 题）

- •    How do you use Azure Key vault's secrets in AKS?
- •    How will the application(container/pod) fetch the latest(rotated) secrets form azure vault.
- •    How do you integrate SonarQube & Snyk in Azure pipeline.
- •    How do you secure your AKS cluster?
- •    How do you make your AKS cluster highly available.
- •    How do you perform cost optimization in AKS.
- •    HPA triggers (what and all types of triggers you have used in HPA so far)
- •    Stateful Vs Stateless
- •    How do you manage data of stateless application?
- •    How do you do you integrate And  EntraID with your AKS for authentication?

## CGI（17 题）

### CGI — DevOps Engineer（YOE---> 4.1 yrs）（17 题）

- CI/CD & Jenkins
- How did you reduce a pipeline from 1 hour to 20 minutes?
- Write a checkout stage with Git credentials.
- If everyone wants to use variables, what approach would you use?
- How do you call variables in a Jenkins pipeline?
- What is a Jenkins agent?
- Sample Dockerfile question from the interview.
- Troubleshooting
- Database connection from a pod is not working only for you. How will you troubleshoot?
- Database logs are not being written.
- Security
- What are CVEs?
- What CVEs have you seen in production and how did you resolve them?
- Name 5 tools to identify/fix CVEs.
- Docker
- Write a sample multi-stage Dockerfile.
- Mostly he have asked me CI/CD in depth and write the stages in detailed.

## CMT（17 题）

### CMT — SRE（Exp-  4-5 yrs(SRE)）（17 题）

- which are all the services you used in AWS
- design an high availability, fault tolerance system in aws
- what is dns
- what is tcp and udp
- what is ipv4 and ipv6
- what is pid
- how will you troubleshoot if a system goes down in Linux - tell the commands
- which are the production incidents you had attended , pls explain
- architecture of Kubernetes
- terraform structure
- how would you maintain high availability in ecs + fargate or eks
- what is the difference between alb and nlb, in which scenario you use alb and nlb
- in webserver/app server which metrics is used to monitor the high availability
- did you use any automation in your daily work
- what metrics is used to monitor ec2 instance cpu, memory in aws
- if there is slowness issue in decouple (SQS), how would you handle it
- what are the best practices can be used to keep the systems highly available

## CTS（40 题）

### CTS — DevOps Engineer 1（15 题）

- What is connection drain
- Backend.tf file is showing in repo but it is not showing in storage account, what may be the issue
- How to login VM if VM has private IP
- You have deployed a web app and it was working fine but application went down, and all networking are fine and related ports are open, how to troubleshoot
- Types of load balancers
- What is Az App Gateway and how it encrypt http/https traffic
- App is down and throwing 503 err code, what steps should be taken
- Also for question 4 is the answer the below?
- Check the status of nginx/apache service that was used to host the web app
- Check if any firewall/security group rules are blocking the flow of traffic
- Ping/telnet won't make sense since networking side is fine
- Clearing cache/cookies from browser for stale enteries
- Do nslookup for dns resolution if that works fine
- Check SSL certificate if it has gone corrupt and is working fine
- Lack of memory on the web app server due to which it is failing to load the resources for the app

### CTS — DevOps Engineer 2（Exp->3-4yr）（11 题）

- How do you manage terrform state file
- How would you design an architecture for a 2 tier application
- Difference between subnet and nacl
- Difference between nat gateway and internet gateway
- How would trigger pipeline B in jenkins automatically after pipeline B
- How will you know if a network policy is enabled or not in k8s
- Difference between cluster role and cluster role binding
- What will happen when a IaC managed resource is modified manually, how would you avoid it
- Difference between daemonset and state full set
- How would you set up networking in vpc
- How you will direct traffic to and from a instance in private subnet

### CTS — DevOps Engineer 3（Exp----->）（14 题）

- Day to day tasks
- How did you reduce the sizes of docker images?
- Explain the CICD pipeline used
- What have you done in Kubernetes?
- How did you write deployment files w.r.t microservices in your project and how did you configure services and ingress?
- Did you configure Ingress and Egress rules?
- What have you done in Terraform and how did you do the integration?
- Difference between Terraform destroy and refresh command
- How to prevent someone from running terraform destroy or destroying the infra?
- How did you do cost optimization in your project?
- Write Python script to differentiate items in a list based on whether the item starts with a or b - [‘abc’, ‘vca’, ‘abc’. ‘bca’]
- What have you done in Ansible?
- If an Ansible playbook keeps running for 2-3 hours, what are your next steps?
- Ansible Tower?

## Capgemini（68 题）

### Capgemini — DevOps Engineer 1（Exp- 6+ yrs overall experience (considering 3 yrs in devops)）（6 题）

- How to assign memory to pod and how to make sure if pod should not get memory constraint. What to do if it happens.
- How to pass variable in azure pipeline? how to parameterize pipeline
- What is availability zone and explain the layout on ground level.(in depth)
- How mysql will interact with azure key vault and it should happen thru privately and should not go anything on public
- Diff between git fetch and git pull (what happens in background in depth)
- What happens behind the hood when git add command is provided. File is added but what happens in the background how git knows on this command it has to add file. ( in dept related to git database)

### Capgemini — DevOps Engineer 2（Exp-9yrs Relevant(5yrs in devops)，Ansible，Kubernetes，AWS）（41 题）

- What is an Ansible playbook?
- How to install Ansible on Ubuntu and RedHat, and start services?
- How to create 3 users and map them to prod, task, and QA groups in a single task?
- How to include and input parameters in a playbook?
- What are Ansible roles?
- Use of templates in Ansible
- Difference between templates and roles
- How to initialize a role and push it to Ansible Galaxy for public use
- How to encrypt a playbook?
- How to execute a vault file?
- How to use an environmental variable for passwords?
- Create a MySQL dump from encrypted data using an Ansible playbook — how to execute the steps?
- How to execute on all DB servers *excluding 1 server*?
- How to shut down all servers using an ad-hoc command?
- How to reduce execution time on RDBMS server?
- How to do that from an Ansible file?
- How to increase debug log level?
- Difference between static and dynamic inventory
- What is the architecture of Kubernetes?
- kubectl apply command – how the services are used?
- Deployment YAML file
- What are labels and annotations?
- Traffic coming from outside to a cluster
- What is the control manager’s task?
- Node affinity and anti-affinity
- How to run 2 pods with one depending on another – how to set roles?
- What is taint and toleration?
- Reason for taint in worker nodes
- How to limit resources in Kubernetes?
- Blue-Green deployment
- Canary deployment
- What is CSI?
- AWS Lambda function and Step Function
- What are autoscaling policies and their uses?
- What is a target probe in autoscaling?
- Which role to give to access services in AWS?
- How to configure a role to service accounts?
- Service account end-to-en
- How to create a secret service account?
- Static vs dynamic storage provisioning
- Type of error in pod label

### Capgemini — DevOps Engineer 3（exp----）（21 题）

- What is the difference between NAT Gateway and IGW?
- If your pod is in Pending state, then what are your troubleshoot steps?
- Can you tell me the difference between secondary RDS and read-only RDS?
- So have you built the RDS of your own or you have managed it only?
- You have RDS and tomorrow, I being your client, will tell you that you need to make the configuration in such a way so that only one user can access the RDS at a time. How will you configure that?
- Like where I will set up the RDS, is it?
- To upgrade the version of DB in RDS, suppose you have 7.0 MySQL installed, and you want to upgrade it into 8.0 and above. What is the process?
- In a multi-account environment, if the resources are residing in one account and the users are in different accounts, how will you configure so that the user can access the resources?
- Because you are telling it from the IAM perspective, what about the VPC?
- You have an EC2 instance and you would like to migrate it from one region to another. How will you do it?
- You want to create an EC2, and while creating the instance, you are getting an error like IP address exceeded. How will you troubleshoot and fix it?
- That we can extend the subnet CIDR once it is created?
- Once you create that subnet, the instance will get created, but will it be able to communicate with the old instances?
- Asking different provisioners,
- How will I remove state file from locking?
- Suppose you have created an EC2 instance by logging into the AWS console. And now you would like to manage it using Terraform. How shall you do it?
- …resources in Terraform
- Different types of services in Kubernetes.
- In a multi-cloud environment, if you want to block a pod to go into a particular node, how would you do it?
- PVC.
- If we can use terraform import for existing AWS resources which are not created by Terraform, then what is the use of data source?

## Cisco（22 题）

### Cisco — DevOps Engineer（Exp--->6+）（22 题）

- 1st Round
- Describe a situation where you had to improve the reliability of a critical system.
- What proactive monitoring solutions have you implemented in your projects?
- Write a playbook to deploy an Nginx server and ensure the service is started and enabled on boot. How would you manage secrets in Ansible?
- How would you migrate a Terraform backend from local to a remote backend like S3 with DynamoDB locking?
- What happens if the Terraform state becomes corrupted, and how would you recover from it?
- Write Terraform code to provision an EC2 instance with a security group allowing only SSH access.
- Explain how you would set up a multi-branch Jenkins pipeline for a GitHub repository.
- How would you implement dynamic stages in a Jenkinsfile based on environment variables?
- Explain the upgrade process for a Kubernetes cluster with zero downtime.
- What key things should you verify post-upgrade?
- Write a script to monitor a directory and automatically copy any new files to a remote server using SCP.
- 2nd Round-:
- write a playbook to install apache in VM?
- How do you update the statefile from local to S3 bucket,what will you do if it gets lost.
- Terraform scripts for creating AWS services Jenkinsfile EKS and On Prem Kubernetes cluster upgrade steps.
- Write a shell script where you have one virtual machine ubuntu1, auto ssh enabled, ssh -i for private key, directory path /nobackup to be copied in another VM.
- Jenkins pipeline setup Kubernetes If a pod is getting restarted constantly, what steps are you going to follow?
- For deployment if you get timeout issue,  what kind of api gateway you used?
- And how did you managed security for application level?
- How to secure public api for on prem setup?
- Where and How to check application performance metrics

## Commonwealth Bank（10 题）

### Commonwealth Bank — SRE principal（Exp-4-5 Yrs，Role: Principal SRE）（10 题）

- What is observability architecture? Can you explain it?
- What is DNS? When you type google.com. What exactly happening in the background?
- What is the difference between observability
- and monitoring?
- When we have logs, why we need trace?
- How SLA, SLO are set in an application?
- Don't give me the formula. Just explain it in from business prospective?
- How do you decide SLI in an application?
- Explain metrics, log and trace including all used tools?
- How observability will help in maintainingside reliability?

## Deloitte（82 题）

### Deloitte — DevOps Engineer 1（Exp-:）（21 题）

- What types of nodes did you deploy in AWS?
- What is the difference between Interface Endpoint and Gateway Endpoint?
- How did you set up ECS using EC2 instances?
- Can't we configure Route 53?
- If we want to configure third-party domains like GoDaddy in Route 53, how do we do that?
- What is the difference between AWS Config and AWS CloudTrail?
- What are the node groups you used in AWS EKS?
- What are the types of node groups in AWS EKS?
- If a user wants to access the S3 bucket, what are the processes?
- How does VPC Peering work?
- How does Transit Gateway work and how did you configure it?
- If we connect VPCs to the Transit Gateway, what will you update in the VPC Route Table?
- For all VPCs, will you configure the Transit Gateway attachment with CIDR range?
- What is Route 53?
- What is WAF (Web Application Firewall) and AAF (Application Access Firewall)?
- What is VPC Flow Logs and how will you track the IPs hitting the VPC?
- How to filter a particular IP from AWS CloudWatch Log Group?
- If you are storing logs in S3 Bucket, how will you track that particular IP?
- How do you take the backup of AWS Services?
- Can we create AWS backup using Shell Scripting?
- Once the backup is created, where will you store the log files?

### Deloitte — DevOps Engineer 2（Exp-----> 4yrs(Linkedin)）（23 题）

- 𝗥𝗼𝘂𝗻𝗱 𝟭: 𝗧𝗲𝗰𝗵𝗻𝗶𝗰𝗮𝗹 𝗦𝗰𝗿𝗲𝗲𝗻𝗶𝗻𝗴
- Explain the CI/CD workflow you follow and the kind of pipeline you use. How do you define and invoke pipelines in Jenkins?
- What are shared libraries in Jenkins, and how are they written and defined?
- What kind of applications do you deploy using Jenkins pipelines, and what deployment tools do you use?
- If the Jenkins pipeline runs but the build doesn’t happen, what possible issues could be causing it?
- What is the purpose of a webhook, and how is it used in a CI/CD pipeline?
- How do you create and manage Kubernetes clusters (using tools like Terraform), and what are the master and worker nodes?
- What are common Kubernetes errors you’ve faced (like CrashLoopBackOff, ImagePullError), and how did you resolve them?
- What is the command to access a pod and how can you define or create a Kubernetes class or object?
- Explain the folder structure of a basic Helm chart. What commands do you use to deploy with Helm?
- What are the stages in a Docker image build? Why do we use ENTRYPOINT and CMD instructions?
- How do you manage and connect services like DBs, EC2, EKS, or ECS? Include the command to connect to ECS.
- Which container registry do you use for storing Docker images?
- 𝗥𝗼𝘂𝗻𝗱 𝟮: 𝗜𝗻-𝗱𝗲𝗽𝘁𝗵 𝗧𝗲𝗰𝗵𝗻𝗶𝗰𝗮𝗹 𝗦𝗰𝗿𝗲𝗲𝗻𝗶𝗻𝗴
- What branching strategy do you follow, and how do you handle merges to avoid breaking the release branch? If a bug appears in production, what’s your approach to resolving it?
- Describe your typical deployment flow and CI/CD workflow. What stages do you define in your Jenkins pipeline, and how do you ensure full quality checks during deployment?
- How do you use Jenkins shared libraries? Explain their typical structure and how they are integrated into your Jenkinsfiles.
- Are you aware of security scanning tools? How do you scan Docker images—both during build and at the registry level? Are you using any extensions or tools for image scanning?
- How do you pass environment variables during Docker build commands? What services do you use for storing Docker images?
- How do you establish a connection with databases in your deployments or infrastructure setup?
- How do you handle authentication for EKS clusters and store secrets securely in your environment?
- How do you create AWS Lambda functions and manage the artifacts for deployment? What options do you use to push artifacts to Lambda?
- What is email signing and Helm chart signing? Which tools do you use to sign Helm charts?

### Deloitte — DevOps Engineer 3（EXP- 5yrs）（28 题）

- How do you migrate a git based repo from one of its kind to another git based repo(like GitHub to GitLab) along with its commit history? what are the steps you follow?
- Difference between Git fetch and Git pull? when do you use git fetch and git pull?
- What is Git cherry pick? how do you use it?
- How will you handle merge conflicts? In merge conflicts where do you check the commit history on the source or on the target?
- What kind of CICD tools you use?
- A new installation is given to you and you need to establish the connection between Jenkins repo and GitHub. what are the configuration steps and how many ways can you configure? As a new Jenkins installation, can you achieve communication with GitHub is possible via webhooks or do you foresee any activities to be performed?
- What are the different kind of stages in pipeline?
- Can we have more than two stages run at the same time?
- Have you ever done groovy scripting from scratch? What is a declarative pipeline? Difference between Declarative and scripted pipeline?
- Difference between EKS and ECS?
- What are all the prerequisites for you to setup a EKS cluster with 2 worker nodes and some x no of pods?
- Generally when two or more pods are available how do you manage the load balancing? are you sure you'll be using ALB
- When do you use ALB and When do you use NLB?
- You have a docker file that contains information related to tomcat application running on port 8080. that particular is to be use as docker image and has to be created as docker container that exposes port on 9090? How can you perform this activity?
- What is the use of Helm charts?
- What have you worked on Linux?
- What is the command that you use to get the number of CPU cores? did
- What is cronjob and how is it used?
- In a folder structure in Linux, I want to understand the size of a particular file?
- What kind of installations done on Linux?
- Have you worked on Ansible automations?
- What have you done with terraform in AWS space?
- Difference between terraform and Cloud formation templates?
- An AWS account is given to you and if I ask you to create a VPC, all the services required for a service in EC2 to be exposes to internet, what all services come into picture?
- What is transit gateway?
- What are the top 5 technologies that you are good with?
- Explain me the high level architecture of Kubernetes?
- What have you done with monitoring solutions

### Deloitte — DevOps Engineer 4（YOE-4 yrs）（10 题）

- Web application is not accessible but ec2 is running fine.what are the major reasons
- What measures you will take to reduce the infra cost by 20%
- Write a Terraform configuration file for ec2 with EBS volume attached
- What will you do for zero-downtime when eks cluster upgrade
- Did you write any automation script that will use for cost optimization.
- What is your Terraform file structure for vpc, eks
- I want to take data of how many ec2 running and how many EBS are attached from 50 or 60 aws accounts without logging into individual account . How can we do that
- What is the Terraform init and Terraform refresh
- How you integrate SonarQube to your pipeline
- What is the major issue that you resolved in Kubernetes

## EPAM（83 题）

### EPAM — DevOps Engineer 1（Exp--> 9 years devops -4yrs）（26 题）

- How to Create and Use Custom Resources in Kubernetes
- what are name spaces in k8s
- what is difference between deployment and statefulset
- what is role based control access
- what is cluster auto scaler and horizontal auto scaling
- Terraform:
- what is provider?
- how to manage state in terraform
- Do you store the data in statefile locally or remotely. What is the block you use while storing the statefile.
- what is terraform module.
- how to manage multiple env management in terrfaform
- what is cloud watch uses cases.
- what is the ECS and eks
- what is fargate
- what is limitations of lamda
- how lamda works containers
- what is ec2 instances
- direct connect in aws
- storage gateway in AWS
- VPC, NAT gateway,s3, route53, vpc peering,transit gateway, autoscaling group
- Difference between sG and NACL
- wht is the difference beteen copy and add
- difference between cmd and entrypoint
- what is run and exec command
- what contains inside vat and opt in linux.
- writ a script to search a pattern as 'error' and warning in test.log file. store the pattern with error in one file and  'warning' in another file. pass test.log in the argument

### EPAM — DevOps Engineer 2（Exp-----> 7 YOE - AWS DevOps Engineer）（30 题）

- Diff b/w ALB and NLB
- Purpose of using VPC Endpoint with use case
- Is it possible to take AMI details from Snapshots
- How to check LB health details (monitoring) through AWS service
- Diff type of instance profiles
- AMI vs Snapshots
- Development team changed the AMI configuration to ASG launch template, how will you make sure that the new version is deployed properly.
- 90.00.9/0 - Is Public IP or Private IP
- How to find out if the provided IP is public or Private
- 90.90.88/12 - Is private or Host
- TGW in AWS
- Post connecting diff VPCs through TGW, I want to black the traffic of A to B and B to C, how to perform it
- EC2 in a private subnet should receive inbound traffic, how to enable it ? → NOT NAT Gateway
- Enabling tight security to my LB
- Is it possible to add multiple LBs to my sub web pages
- userdata in EC2
- How to segregate the critical details from VPC flow logs
- Diff b/w Fargate vs EKS worker nodes
- Updating EKS cluster
- ASG is active and the load is heavy, due to that two EC2 instances are launched, but EC2 provision is taking 2 to 3 mins of time because of the ASG terminating the instance, how to avoid it.
- I've huge traffic coming between 5 PM to 8 PM daily, how to configure this in ASG
- Can we create two diff CICR blocks 172. && 192. series in same VPC
- Customizing WAF
- Cloud Front configuration
- AWS Image builder
- Diff type of instances
- If you're storing all your VPC Flow logs in S3 bucket, how to see that
- API Gateway configuration
- Diff between Private and Public IPs
- Diff between Spot VS reserved instances

### EPAM — DevOps Engineer 3（Exp--6 year）（27 题）

- How would you design a scalable, highly available CI/CD system for microservices across multiple teams?
- How would you manage cross-region deployments using Terraform in a multi-cloud setup?
- How do you implement GitOps in a Kubernetes environment?
- Can you explain how you would create a fully automated blue-green deployment in a Kubernetes-based microservices architecture?
- How do you design an end-to-end DevSecOps pipeline for a fintech application with strict compliance requirements (e.g., PCI-DSS)?
- What are some best practices for managing pipeline as code in large, distributed teams?
- How would you dynamically provision ephemeral environments (dev/test) using pipelines?
- In a monorepo setup, how do you ensure that only relevant services are built and deployed in a CI/CD pipeline?
- How do you implement a canary deployment strategy with real-time monitoring rollback in a CI/CD system?
- How do you manage secrets and config securely at scale in Kubernetes without compromising GitOps workflows?
- Explain the control plane components of Kubernetes and how you would harden them for production use.
- How would you scale a Kubernetes cluster horizontally across multiple regions and still ensure zero-downtime upgrades?
- What is a PodDisruptionBudget and how do you use it in critical workloads?
- How do you implement and manage network policies in Kubernetes for strict inter-service communication?
- How would you refactor a legacy Terraform codebase used by multiple teams to follow best practices like DRY and modularity?
- Explain the internals of how Terraform handles dependencies and graph building during the planning phase.
- How do you manage and isolate Terraform state files across multiple environments and teams?
- What's your strategy to prevent and recover from a corrupted or deleted remote backend state file?
- Have you implemented policy-as-code (e.g., Sentinel, OPA) with Terraform? Give a real use case.
- How would you implement a centralized logging solution across multiple cloud platforms and environments?
- What's your approach to securing cloud-native DevOps infrastructure with Identity Federation (e.g., Azure AD + AWS IAM)?
- How do you set up workload identity federation between GitHub Actions and Google Cloud / Azure securely?
- How do you ensure cost-efficient auto-scaling of infrastructure in cloud when managing high workloads in CI/CD?
- Explain a scenario where you had to design a disaster recovery (DR) strategy for DevOps infrastructure.
- How do you enforce compliance and auditability in your CI/CD processes across global regions (e.g., GDPR, HIPAA)?
- What's your strategy for managing container image security across all stages of a DevOps pipeline?
- How would you integrate runtime threat detection in Kubernetes using tools like Falco or Sysdig?

## EXL Service（28 题）

### EXL Service — DevOps Engineer（YOE---> 5 yrs）（28 题）

- You are onboarding a new customer with 5 million+ users. How would you design the complete application architecture as a Solution Architect?
- Explain your complete CI/CD pipeline from code commit to production deployment.
- Explain your Git branching strategy. How do you deploy code from different branches to different environments?
- If Git is already the source of truth, why do we need Argo CD? Why not deploy directly using the CI/CD pipeline with Helm or kubectl?
- Explain the complete request flow when a user accesses www.ingress.com until the request reaches the application pod.
- You need to expose an application internally without using a LoadBalancer or NodePort service. How would you do it?
- Pods in different namespaces can communicate. How would you block that communication? Where would you implement the NetworkPolicy?
- Suppose you are implementing a Canary deployment where only 10% of users receive the new version. How would you implement it through your CI/CD pipeline?
- During a Canary deployment, how would you verify that the 10% deployment is healthy? What metrics would you monitor before proceeding to 100%?
- Do you execute Terraform locally or through a CI/CD pipeline? Explain the complete workflow.
- Two engineers are working on the same Terraform code. How do you prevent conflicts and handle Terraform state locking or drift?
- Draw and explain your Terraform repository structure. How do your dev, qa, and prod environments consume shared modules like the VPC module?
- Two VPCs need to communicate, but their CIDR ranges overlap. Transit Gateway is not allowed. What alternative solution would you recommend?
- Have you worked on Disaster Recovery? Explain your DR strategy, including RTO, RPO, failover, and traffic redirection.
- Explain Rolling Update, Blue-Green, and Canary deployment strategies.
- For a mission-critical production application, which deployment strategy would you choose and why?
- Have you worked on Databricks pipelines? Explain your experience with Databricks.
- What do you know about Apache Hadoop and its ecosystem?
- Which AWS EC2 instance types have you used, and why did you choose them?
- Explain the difference between Git Merge and Git Rebase.
- Give a real-world use case of AWS Lambda.
- Where do you store CI/CD secrets such as pipeline credentials?
- Where do you store application configuration and secrets? (ConfigMaps, Kubernetes Secrets, HashiCorp Vault, etc.)
- A developer accidentally commits AWS credentials to Git. What is your complete incident response process?
- What metrics do you monitor using Prometheus?
- What dashboards and alerts have you configured in Grafana?
- What monitoring agents have you installed in your environment?
- How do you perform infrastructure cost optimization using monitoring and observability tools?

## EY（35 题）

### EY — DevOps Engineer 1（10 题）

- Introduction
- Explain current project
- Asked about k8s ( deployment, services, and configs)
- How to integrate grafana with prometheus
- Terraform
- Service mesh
- Pod disruption budget
- Git sqash
- Git rebase
- Purpose of Docker

### EY — DevOps Engineer 2（experienc---->）（25 题）

- Explain the Kubernetes architecture and how it works.
- What is a Deployment in Kubernetes?
- What is a Service in Kubernetes?
- How does Pod-to-Pod communication work?
- What is Git Rebase?
- Explain your current project.
- What is a Pod Disruption Budget?
- What is the purpose of Docker?
- What is CrashLoopBackOff in Kubernetes?
- Have you deployed both applications and infrastructure? What kind of tech stack have you mainly worked on?
- For Java applications, what tool do you use to build them?
- Have you worked on Jenkins as your CI/CD tool, or used others like GitLab?
- What source code management tool have you used?
- What is the syntax or command you follow to deploy an application using Helm Charts?
- How do you manage concurrent builds in Jenkins and ensure performance doesn’t degrade?
- What is the difference between Declarative and Scripted pipelines?
- Have you used any artifact repositories like Nexus or Artifactory, and where do you store dependencies?
- What happens internally when you run a Maven build — how does it fetch dependencies from the repository?
- Have you used any security tool integrations in your pipelines?
- What is Rolling Strategy and Canary-based deployment?
- What is Hash-based deployment?
- What is a Persistent Volume in Kubernetes?
- What is a ConfigMap in Kubernetes?
- What is a Service Mesh and how does it work?
- What kind of observability tools have you used, and what metrics have you been monitoring?

## Elixr Labs（26 题）

### Elixr Labs — DevOps Engineer（Exp-----> 6yr）（26 题）

- what is land job activity in migration
- what type of basic azure services u will consider
- Hub and Spoke topology
- day to day actives what type of work ur doing is it a support/project
- what type of pipelines ur handling basically it means QA ,UAT
- how many team members are there?
- How about the deployment , IAAS model or Saas  model
- pick one requirement and u deployed end to end by using azure services
- suppose there is a dotnet application which is basically a 3 -tier application ,for webapi deploymment i hvae used azure appservices, for background jobs i have used function apps ,and for messaging i have used servicebus and how about the connectivity to all thses?
- how on-premisis user has to access the application/access the code which was deployed in cloud service . how my connectivity will be configured ( on-premiss to cloud )
- IN general as azure specalist from ur side what is ur recomendation is it a sit-to-site vpn or Expressroute
- lets assume consider banking sector only i dont have that much budget but since ur telling that for low budget go for site-to-site-vpn but on otherside ur saying that express-route is more secure > So how cn u justy that, because banking costumer has a limitation for him
- IN which senario we will go for site-to-site vpn  and Expressroute
- any storage related components have u worked on?
- lets say i have a condition i need to access the data which is stored in storage account but that is huge data which is comming from enduser perspective lets say some cppotency that is recording 24/7 and data will be stored but at the same time if anyone comes and to retrieve the data obviously they will get it from storage account,now i need to implement some cost optimisation techniques on storage account to reduce cose because data to be incresed daytoday ?whta afre the possible ways
- with respective storageaccount
- suppose u have created a storage accouunt with hot-tier is it possible to change to cool-tier
- manually we can change from hottier to cool tier ,but when i have huge data it will take time right .
- Did u face  any challenges while ur taking backup? any issues
- what type of services ur have used for backup .is it azure specific or any on-premisis
- what are the senarios u configured for DR?
- how about the monitoring techniques like any alerts we can
- lets assume we got an requirement that we have a production infra running on azure cloud and we need to setup an alert mechanism where there some thresold values given by customers but considering huge infra but ur getting hundreds of alerts ,in that alert how can u segregate  that we need to findout ,which alert we need to proporitise ,any appriach u have ?
- Any known issues u encountered any pipeline is integrated/ any production code is ur pushing or production any known issue and tell which is critical and how u got resolved
- Have u done any migration form on-premis to azure / from azure to azure with any scenarion and what shot of migrarion s it resource migration or data migration
- what are the prechecks u have to consider before migration

## Emphasis（26 题）

### Emphasis — DevOps Engineer 1（11 题）

- I attended interview for devops role, they were asking very basic questions about devops & aws.
- Explain components in 3-tier architecture
- Explain Kubernetes architecture
- How private subnet connect with outside world
- What is difference between NACL & security groups
- What is the purpose of NAT gateway
- Explain how to write a dockerfile
- From where is the image pulled when you use docker pull image?
- How is the image pulled from private repository
- What is ingress in Kubernetes
- Explain CI/CD pipeline and its stages

### Emphasis — DevOps Engineer 2（15 题）

- What is AWS Lambda and how do you design a serverless application?
- What is the difference between terraform plan and terraform apply?
- What are your roles and responsibilities in your current project?
- Can you explain your end-to-end project?
- What AWS resources have you created using Terraform and how do you promote a read replica to primary using Terraform?
- In Terraform, which parameter or code change is needed to make a read replica the primary?
- What is a 3-tier architecture?
- Which components or resources are required to create a 3-tier architecture using Terraform?
- If the RDS is in a private subnet, how do you access it securely without using public tools like MySQL
- Explain your end-to-end CI/CD pipeline in your current project
- Explain a simple CI/CD pipeline in short.
- Show a sample Jenkins CI/CD pipeline code.
- Explain if a standalone Jenkins server setup will work, and what to consider.
- Explain what an application pipeline is.
- How many ways can you trigger a Jenkins pipeline?

## Encora（18 题）

### Encora — DevOps Engineer（Exp---- 7 yrs）（18 题）

- what is terraform lifecycle
- i had created an resource manually, how to do you implement it through terraform
- for each and count difference, provide examples in terraform
- how do you create an module and how do you refer it in terraform
- how to handle peak traffic after an launch of new product in web app
- there are multiple micro services and multiple websites, I want to ensure security how do you handle it
- what is CSI drivers
- what is helm template and helm install
- what is helpers files in helm
- how do you rotate the secrets in key vault and implement .pfx certificate in application gateway , along with ingress/controller in AKS
- architecture of Kubernetes
- what is Service principle in azure – provide an example
- there is an backend API, I want securely communicate with other, how do you implement it
- what is daemonset and statefulset
- am having an range of ip address 10.0.0.0/16 , I want to have 10.0.0.0/21 subnets , how will I achieve it terraform , how do use locals word and achieve it
- crashloopbackoff – what are the setps you will follow to troubleshoot further
- what are the branching strategies and pipeline creation mechanism
- what are the files present inside helm chart 19.what is CNI plugin

## F5（18 题）

### F5 — Associate Consultant（Exp--(Associate Consultant )）（18 题）

- What is Web Application Firewall,
- How would you secure the web app running in cloud from oswsap10 attacks,
- What happens if tfstate file gets deleted,
- What is terraform lock hcl file,
- What are best practices to be followed on terraform,
- If we have security group configured in the instance do we really need nacl.,
- Difference between Transit gateway and VPC,
- Best practices to be followed for cloud security.,
- HTTP request header and HTTP Methods,
- If thre is an instance we have security group and web application firewall enabled, DDOS attack enabled will it protect from Bot attack.
- There is db I made same entry(Name, Location) through PUT method twice what will happen.,
- Why is PUT request called idempotency in nature. If I made another entry and name is same but location is differnet then what will db store.,
- What happens if I type www.google.com in the background.,
- What is SSL/TLS Handshake.,
- What is DNS Resolution. Suppose I have new system with no cache what happens in the background.Step by step process.
- What is K8. Explain the architecture.,
- Can I run POD inside master-node itself?,
- Have you deployed any security application on Kubernetes?

## Five9（11 题）

### Five9 — DevOps Engineer（Exp---> 7 YOE）（11 题）

- How to find out second largest integer in an array
- How to set a CPU and memory limit in Linux machine
- TLS handshakes
- Apart from storing TF log files in S3, do we have any other options
- Different type of provisioners in TF
- Diff b/w Local and remote provisioners in TF runners
- Diff b/w user-data vs remote provisioner
- AAA and CNAME in DNS
- Fail over mechanism in DNS (if one IP is not reachable)
- How logs are segregated in ELK
- Apart from using password, how to login to EC2

## Flentas（40 题）

### Flentas — DevOps Engineer（exp -----> 3.5 yrs，Experience)）（40 题）

- Interview Questions for Flentas (3.5 Years
- What is your architecture in your current project?
- What applications are deployed in the frontend and backend?
- Why did you not deploy the frontend on S3 and CloudFront, and instead deployed it on EKS?
- What is a namespace in EKS?
- How many namespaces do you currently have?
- What is a node group?
- How do you perform cost optimization on ECS, RDS, and ElastiCache?
- Why have you used RDS Proxy?
- The client application did not have connection pooling — how did you handle it?
- A node is unable to join the cluster. What could be the reason?
- What is the difference between the control plane and the data plane?
- What is the difference between a Pod and a Container?
- What are requests and limits in Kubernetes?
- One node has 8 vCPU and 32 GB RAM. With pod autoscaling up to 4 replicas, each pod having
- limits of 4 vCPU / 16 GB and requests of 2 vCPU / 10 GB RAM, how many instances of the pod will
- run?
- What did you implement in Lambda and API Gateway?
- What is the difference between Redis and Memcached?
- Explain the Terraform folder structure.
- What is the difference between Terraform and Terragrunt?
- What is the state file in Terraform?
- How do you handle resource dependencies in Terraform?
- When you ran terraform apply, did you encounter any unexpected changes?
- If there is a problem in Terraform, how will you roll back the changes?
- I have created an LB using Terraform, and some updates happened on it. Now I want to delete
- the LB only — how will you do it?
- How do you handle secrets in Terraform?
- How will you pass secrets from AWS Secrets Manager to the pipeline?
- Do you commit the tfvars file to Git? While running the pipeline, these parameters need to be
- filled — how do you manage this in Jenkins?
- What is Docker?
- What is the difference between an image and a container?
- What is a Helm chart?
- I want to enable autoscaling in Kubernetes during high traffic. How will you scale both cluster
- nodes and pods?
- Can we use Cluster Autoscaler?
- How do you scale EC2 instances?
- When do we use VPA (Vertical Pod Autoscaler)?
- Have you upgraded the EKS cluster?

## HCL（59 题）

### HCL — DevOps Engineer 1（exp--> 4-5）（11 题）

- What is git branching strategy used in your organisation
- How deployment is done in different environment using git repo
- How and from where to clone repo, is there any local repo you are using and then transferring from local to remote or how? (Honestly I didn’t get this Q, if anyone has real time exposure pls explain)
- What is PAT
- How to configure sonarqube
- How to integrate azure key vault in jenkins / azure pipeline
- How to handle merge conflict in git. If 2 people working on same file and did the commit and got conflict err, in how many ways it can be solved (someone explain pls).
- What is the output of sonarqube, how to fix if any smell code/vurnabilities  found
- Where do you write the code/yaml file for pipeline
- What is inside docker file
- How to schedule pipeline, lets say i have validated the pipeline with some update and i want to schedule it to stage/main branch, how to do? (This also someone explain)

### HCL — DevOps Engineer 2（20 题）

- what is diff between pv and pvc
- Expalin kuberenets arthciecture
- what is diff between deployment and statefullset
- what is calico
- what is etcd
- how to take bakcup of kubenretes cluster
- how to upgrade eks clusetr
- what is rolling update
- what is deployment statgergy you are using
- can we run 1 conatiner with 2 pods
- what is statefullset
- terraform have you build the vm
- what is ingress controller
- Supoose you have taked etcd backup and old vm corrupted ,can we create new vm with backup etcd ?
- what are steps to upgrade eks cluster
- Suppose you have  in satetfull 3 pods which having name mongo-0 , mongo-1, mongo-2 what happen if mongo-0 dies when new pod will create what will be pod new name ?
- have you worked on argo cd , helm
- suppose we have pods 2 running in rolling updates some are in deployments set and some pods are in statefull set , how rolling updates strategy will work here  ?
- what is docker multisatge , why it is used and all
- grafana have you worked

### HCL — DevOps Engineer 3（exp ----- 5 yrs）（21 题）

- Landing zone, guard trail, scp, control tar. —— interviewer ask for this vocabulary ❌ (general)
- Account 1 to Account 2 – send AMI but its KMS encrypted, help me do that ❌ (aws)
- EC2 has IAM roles, what all things can we explore from it ✅ (aws)
- I have EC2 and S3 in same subnet, region how to access that bucket from instance ✅ (aws)
- I have EC2 instance, internet connectivity not there, how to tackle this ❌ (aws)
- Two instances are there what is the best way to communicate with them, create new NIC or attach ❌ (aws)
- I have multiple IAM user which is best approach: 1. attach policy individual to user OR 2. add that user to group and attach policy ✅ (iam)
- Inline policy or attaching policy which is right approach ❌ (iam)
- Have you used permission boundaries ❌ (-)
- S3 lifecycle rules – what is the advantage of using them ✅ (s3)
- Have you worked on transit gateway ❌ (-)
- ALB and NLB have you used it ✅ (aws)
- Public and private subnet is there, NAT gateway is attached to private subnet what is use of that (masking of private ip) ✅ (vpc)
- How does NAT gateway protect my private subnet, what concept does it use to secure the resource (same masking) = masking is protecting the private subnet ✅ (vpc)
- KMS, Secrets Manager have you worked on it ❌ (aws)
- Manually EC2 updated from t3.medium to t3.large manually and updated the code and committed but pipeline not ran. If you run pipeline then what will happen? (nothing will happen – code is in local machine of devops) ✅ (aws)
- Can you use same build spec used in AWS CodeBuild ✅ (terraform)
- Wat is DaemonSet in Kubernetes and what default daemons comes up with Kubernetes ✅ (kubernetes)
- An init container comes up with the Kubernetes cluster ✅ (kubernetes)
- Taint and toleration in Kubernetes what it is ❌ (kubernetes)
- Compute reservation in manifest files ❌ (kubernetes)

### HCL — DevOps Engineer software（Exp---5 years）（7 题）

- How do you display the last 10 lines of a large log file without opening it fully?
- In Kubernetes, how would you configure your deployment to double CPU allocation once usage crosses 70%?
- Can you write a basic Dockerfile for your application?
- What top-level security risks from OWASP do you usually check for?
- How do you configure Prometheus and Grafana for monitoring?
- If you have an on-prem application, how would you migrate and deploy it in a cloud-native environment?
- Can you explain Docker Compose and how it helps in multi-container application deployments?

## Hexaware（15 题）

### Hexaware — DevOps Engineer（Exp--4-5yrs）（15 题）

- write yaml pipeline for ci/cd (overall structure)
- what is the command for auto approval in terraform
- what is deployment.yml
- what is service.yml
- what is replica set
- what is the output of helm chart
- what is storage explorer
- how do you set approval in cd pipeline
- what are the branching strategies you use
- have you written any automation scripts in your daily tasks
- how do you moved the code from one environment to other environment
- what is variable group in azure devops
- what is sonarqube and which purpose it is used for
- Write sample terraform code (overall skeleton)
- what are the files available inside helm chart

## IBM（78 题）

### IBM — Cloud Engineer（Exp-----> 3.3 Year exp）（30 题）

- Tell me about yourself.
- What are your day-to-day activities?
- What is Terraform, and how does it work?
- Where do you run your Terraform code—on your local system or on a specific server in your organization?
- What is a tfstate file?
- Where do you store the tfstate file in your organization?
- What does the tfstate file actually do?
- Suppose another DevOps engineer on your team has made changes to an instance via the UI, and you then run the terraform plan command. What will be the output?
- What do the "+" and "−" symbols mean in the terraform plan output ?
- If changes have been made to an instance via the UI and you run terraform apply without first running terraform plan, what will happen? Will there be an error, and will it still execute?
- Suppose you're running an application and a vulnerability occurs, how would you handle it? Briefly explain.
- If it's a production server and you encounter a vulnerability, what will you do?
- If it’s a Python application and a vulnerability is found in production and fixing it may take 6 months, what is your approach and solution?
- Are you following any standards to handle such issues?
- Have you worked with Ansible?
- What is Ansible?
- Can you write a playbook?
- How do you store credentials in Ansible?
- Are you following any other approach to store secret credentials securely?
- How do you store variables in Ansible?
- How do you debug errors in an Ansible playbook, what is the comamand ?
- Suppose you want to execute a single command without writing a playbook — what is the command, and how do you write it?
- What modules have you worked with in Ansible? List their names.
- How do you deploy your application on AWS? What services do you use?
- When deploying your application to Amazon EKS, what other services do you use along with it?
- Have you worked with shell scripting and Python scripting?
- Where have you used Python in your work? What was the purpose, and what tasks did you perform?
- Have you worked with any monitoring tools? What tools, and what was your role in using them?
- How will you disable the root login into a particular server ?
- What is the file, you have made the changes , can you tell me the file name and pat

### IBM — DevOps Engineer 1（Exp-7years (Devops Enginner)）（15 题）

- Encrypting the EBS volume
- A Jenkins pipeline is randomly failing at the deployment stage to EKS. Logs show timeouts during kubectl apply.
- How do you securely manage TF state files, secrets, and environment isolation?
- How to design an event-driven architecture using S3, Lambda, and SNS for data ingestion
- How will you create HPA
- If I've three Master Node, one is down, what will happen
- Global LB in Kube
- AB Testing
- How will you check the vulnerability of your code
- If there are two clusters running in diff regions, if there is an issue with one cluster, how to shift the traffic to another cluster.
- In Log file, how to fetch 200 status code
- If you type kubectl get pods, what will happen in the backend.
- How to check the kubectl logs of a POD before it restarted
- Reverse proxy
- How will you resolve the git conflict automatically?

### IBM — DevOps Engineer 2（Exp-->5yrs）（15 题）

- Q1: lets say our app is nodejs app how wd u setup cicd pipeline
- and which ci/cd tools would you use?
- Q2: we are going to launch a website with many different products
- running many services and is expected to get high load during black friday
- how would u set up and make it highly available?
- Q3: users are facing slownesss issue, what will u do to resolve?
- Q4: now it is hosted and one of the services is leaking memory, how would you troubleshoot?
- Q5: out of aws and azure what would u choose and why?
- Q6: now the application is hosted and running, the billing is too much, the client asks you to
- reduce the billing by doing the needful, what would you do to reduce billing?
- Q7: diff b/w terraform, cloudformation and arm and what would u prefer?
- Q8: How would you store secure info inside s3?
- Q9: In lambda function, how would you handle failures and how would you set up retries?
- Q10: Lets say we have already hosted and app, now some changes has been made
- How would you redeploy this application with zero down time?

### IBM — DevOps Engineer 3（YOE: 5 +）（18 题）

- Write a script to delete files older than 10 days.
- What is hard and soft link
- What is Iptables in linux?
- How do servers get connected in Linux? explain.
- What tools do you use for configuration management?
- How can you install a patch through ansible in more than 20 servers?
- How can you reduce the build time in jenkins?
- What is a Jenkins agent?
- How can you trigger an automatic build in jenkins?
- Write Jenkins script to trigger simultaneous/ parallel execution.
- Write a terraform script to create EKS Cluster.
- How do pods interact with each other?
- What issues did you face with EKS Cluster?
- What to do when the etcd from EKS goes down?
- How to run a container on ecs cluster.
- In my EKS cluster 2 node groups are there before deploying pods , node group -2 is showing unhealthy why ? I do have all the permission to check, how to troubleshoot and step to avoid such situations on future.
- In my ec2 2 containers are running backend and frontend so i wanto connect my backend container to rds service how
- Terraform tf.state file is deleted  how to recover it( conditions: it was not sync with s3 or any vcs to take a backup)

## ITC Infotech（6 题）

### ITC Infotech — DevOps Engineer（YOE-->4 yr）（6 题）

- How to make connections between on prem to AWS suppose if we want to share files from on prem.
- how to connect S3 with ec2 if a script generates files daily that need to be pushed S3.
- How will you write terraform module for EKS.
- If your application is on EKS how the traffic flows if user hits the URL.
- What is difference between coreDNS and kube-proxy.
- What is OIDC provider in AWS.

## Infinite Solutions（3 题）

### Infinite Solutions — DevOps Engineer（Exp-5 yeras）（3 题）

- How you are mangaing the kubenretes DR
- How you are taking backup kubernetes .
- how you are setting up ingress controller

## Infosys（78 题）

### Infosys — DevOps Engineer 1（15 题）

- Introduce yourself
- git commands used in day to day activities
- write sample docker file
- 4 write sample terraform resource file
- Difference between git rebase and git merge
- difference between cmd and entry point
- explain about Prometheus and grafana
- what will be your approach if pod.yaml failed
- explain about blue green deployment strategy
- explain kubernets architecture
- commands used in kubernets
- if application which you are trying to deploy with kubernets got crashed and you are not able to enter into pod what will be your approach
- explain about your project pipeline
- have you worked on production deployment activity ?
- how frequently do we deploy to production in your current project

### Infosys — DevOps Engineer 2（25 题）

- Introduction
- Current Company project related questions
- What task and activities do you do on daily basis
- What is Prometheus, Grafana, Loki
- What is Kibana
- How does Prometheus collect metrics
- How is Prometheus setup
- How is Kibana set up
- What is log rotate job and how does it work
- What is Jenkins, Ansible
- What is Terraform and how do you use terraform in your project and what all resources have you provisioned
- What are deployments, daemonset, statefulsets
- Basic Kuberntes commands
- What is Docker and how do you use in your project, Any docker file you have written
- What are data sources for Grafana, Kibana
- How is traffic routed inside kuberntes clusters
- ELB, Ingress questions
- How do you receive alerts in your project and how is it setup
- What is pod
- What are indices, index in Kibana
- Cronjobs
- Paas Questions
- How do you handle disk, CPU alerts
- What all Kuberntes issues you have worked on
- If any pod/node goes down how do you troubleshoot/monitor that( via cluster and other monitoring tools)

### Infosys — DevOps Engineer 3（YOE---> 3 yrs）（20 题）

- What is your day to day activities
- How do you reduce docker image size
- What is HPA and how do you implement it
- You branching strategy
- What is pod affinity
- What is your team size
- How many pods do you manage
- Explain k8s architecture
- What is security group and what is the default traffic rule in sg
- Tell me one task or tool that your have done from scratch
- What is difficulties you face while you build a docker image
- Why terraform is used
- What are the terraform modules you use
- What do you work on k8s
- What are the tools you use in your project
- Give me an crisp overview of your client like are they banking project.
- How do you setup Prometheus dashboard
- How the data is fetched to promotheus
- What are the alerts you setup on graffana
- Do you have any experience on python scripting

### Infosys — SRE（Exp---> 5+，Role ---> SRE）（18 题）

- What is SLI, SLA, SLO and Error Budget?
- What is the difference between monitoring and observability?
- The application which you are supporting , the users are complaining that it has latency and you have monitoring tools as well for monitoring your application. So how will your monitoring tool help you in identifying and fixing this latency issue?
- What is Chaos Engineering?
- So what all services do you have used in AWS?
- How do you make your cloud infrastructure more secure?
- How to secure the S3 bucket?
- Suppose you have a VPC , and in your VPC, you have 2 subnets. One is a private subnet, and another one is a public subnet. And in these subnets you have 2 - 3 instances. And for security purposes we need to keep those instances updated right on a regular basis. The instances in the public subnet are okay. They have internet connectivity. They can get updated. How will you update the instances which are in the private subnet?
- If you have experience in working with Ansible, you remember what all modules you used in the Ansible playbook?
- What kind of experience do you have with Terraform?
- Which tool you used for CI, CD pipeline - can you tell me?
- So have you worked on CI/CD creating - setting up CI, CD pipeline? Can you explain to me the CD pipeline, which you created? What all steps were there? What all tools you integrated as part of the pipeline?
- How were you managing your Kubernetes cluster through a helm file or the command line? Have you used Rancher or Argo CD?
- Suppose you have a Kubernetes cluster running and in the cluster there is an issue. You see that one of the pod is in the state - crashloopbackoff. So what could be the possible issues with the pod?
- What kind of experience do you have with Python?
- In your monitoring experience, what tools you have used, what all things you did in the monitoring?
- Do you have experience in managing a team?
- Did you get a chance to work on creating proposals for clients?

## Intact Green Services（12 题）

### Intact Green Services — DevOps Engineer（exp ----- 5 yrs）（12 题）

- What is desired state and in-desired state?
- How do you deploy an application in Kubernetes?
- Have you faced any memory issue in Jenkins pipeline? how would you troubleshoot
- There are 2 VPCs A & B. Give me options so that A communicate to B and vice versa. Also, option where only A has to communicate to B.
- 2 Instances are created using terraform. Statefile is located locally and also in remote backend(S3). If a user deletes 1 instance what would happen? How would you handle this?
- There is issue with docker image due to its size, what are the action plans from you to reduce the size.
- What are the tools you have used for CI/CD pipeline?
- Can we use POD as an agent? What are the drawbacks if we do so?
- Type of services in Kubernetes, give their use case
- What are the different type of Jenkins pipeline?
- What are the advantages of multibranch pipeline?
- You are unable to push docker image to dockerhub due to access issue. What are the sources where you can push your docker image other than dockerhub?

## JPMorgan（79 题）

### JPMorgan — DevOps Engineer 1（Experience--，Round 1，Round 2，Manager Round）（43 题）

- Explain the project you are currently working on.
- What types of Spring Boot starters have you used in the project?
- How have you implemented transaction management?
- How do you connect to two databases, and how do you ensure rollback during exceptions?
- How are you managing code coverage in your project?
- How do you perform load testing for your application?
- How have you implemented security in your project?
- Explain Okta integration for identity and access management.
- How do you secure internal communication between microservices?
- How do you implement a retry mechanism for a failed API call?
- How do you implement blue-green deployment in your project?
- How do you deploy an application to AWS?
- What is serverless in AWS, and how are you using it?
- How would you handle scenarios where the payment succeeds but the order or shipping service fails?
- // List of duplicate color and count it , create a map using stream.
- // Remove a duplicate colors from the list and make it unique list.
- You have two candle how you r going to calculate 45 mins, you are not allow to cut or measure .
- How are you provisioning your AWS services?
- How do you provision container-based services for microservices deployment?
- What database services did you provision along with your application?
- What is the primary difference between ECS and EKS?
- Where do you define auto-scaling parameters?
- What do you know about Serverless architecture?
- How do you optimize cold starts in AWS Lambda ?
- What is Serverless deployment in AWS?
- What is HPA
- What is Region and Availability zone?
- How do you monitor the health of your microservices?
- How do you enable Spring Boot Actuator?
- Are actuator endpoints accessed without authentication?
- Have you worked with Kafka or any other messaging service?
- Have you used any serialization or deserialization frameworks?
- Where do you register the Avro schema you're creating?
- Have you implemented any concurrency APIs in Java?
- How do you combine the responses of three separate APIs?
- What is active-active ?
- How active- passive is differ from active-active ?
- //Find all pairs in an array that sum up to a specific number
- Can you share your previous experience?
- Have you recently worked on any challenging tasks in your project?
- How do you deal with high-pressure situations or multiple critical deadlines?
- If your lead or team member is not technically strong or doesn’t behave well, how do you handle the situation and continue working as a team member?
- What do you do in your free time or on weekends?

### JPMorgan — DevOps Engineer senior（Exp---> Senior DevOps Engineer）（20 题）

- You’ve deployed an app to Azure Kubernetes Service (AKS) and it fails health checks randomly. How do you debug this end-to-end?
- In a canary deployment to production, half the traffic returns 502, while others succeed. Walk us through your troubleshooting approach.
- CI/CD pipeline takes 40 mins to deploy a small change. What would you do to optimize it?
- You see high CPU usage in one pod, but logs look clean. What next?
- You’re asked to design a highly available logging system for 100+ microservices across 3 regions. What tools and architecture would you suggest?
- Production app works fine for internal users but fails for external ones (403 error). How will you isolate the issue?
- How do you ensure secure and dynamic secret rotation in Azure DevOps pipelines?
- Explain how you’d use Azure Application Gateway with Web Application Firewall for a sensitive banking application.
- During an Azure deployment, you receive intermittent DNS resolution issues. What can be the causes?
- A user reports 10-second delays every 15 minutes in an app running on AKS. No code changes happened. How would you begin RCA?
- Jenkins jobs are randomly failing at the artifact upload step. What layers would you check?
- How would you set up an automated rollback strategy in Kubernetes for failed deployments?
- Design a cost-optimized cloud architecture for an internal reporting app that runs every night and stores logs for 3 years.
- How do you handle zero-downtime database migrations in a distributed application?
- What’s your approach to disaster recovery for stateful apps running on containers?
- An Azure function is being throttled. How will you detect and fix it?
- Define a plan for blue/green deployment with rollback on Azure using Terraform and pipelines.
- How would you monitor end-to-end SLA for services involved in a payments pipeline?
- Explain the difference in scaling strategies for compute-intensive vs I/O-intensive workloads in Azure.
- Suppose your production pipeline is blocked due to missing approvals and stakeholders are unreachable. What will you do?

### JPMorgan — DevOps SRE（Exp-5years，Role--Devops/SRE）（16 题）

- What would you say is your strongest skillset area in DevOps/SRE and which technologies do you want to focus on going forward?
- Your application is currently running on EC2 instances in a public subnet. How would you migrate it to a private subnet without any downtime? Explain the complete approach. if it doent work how would u rollback?
- You have two running pods in a Kubernetes cluster, but they are unable to communicate with each other. There are no errors in the logs or events, and both pods appear healthy. How would you troubleshoot and restore communication between them?
- If a pod’s liveness or readiness probe is failing, how would you troubleshoot the issue?
- Apart from  actuator health-check endpoints, what other checks can you perform using Kubernetes probes?
- If an application has only one replica and you perform a rolling restart, will there be downtime? Also what events occur during the pod restart can you explain the sequence step by step?
- You have an application with 2 replicas. During a rollout, the first pod is successfully replaced, but when the second pod is being replaced it enters a CrashLoopBackOff state. At that moment, which pod will the load balancer route traffic to the new pod, the old pod, or both? explain
- Just like we use code-quality and security checks (quality gates, OWASP) before building an image, how can we prevent insecure infrastructure changes from being pushed using terraform?
- For example, if someone modifies a security group in Terraform and opens it to 0.0.0.0/0, what mechanisms can we use in Terraform to stop such changes from being applied?
- How would you handle Terraform state management for a team? Specifically, how would you store the tfstate file securely, make sure only one person can modify it at a time, and ensure the state is not tampered with? give me answers for all 3 qns
- You’ve joined a company where a large production infrastructure was built manually and the previous engineers have left. How would you bring that existing infrastructure under Terraform management? Walk me through your plan
- Are you aware of the recent AWS and Azure outages? What were your key takeaways from those incidents?
- If an entire region goes down and even a multi-cloud setup (like AWS + Azure) experiences outages how would you ensure that your data is still safe and not lost? What strategies would you use to guarantee reliable backups and recovery?
- What components or agents are typically installed along with Prometheus, and what does each of them do?
- In an EFK/ELK stack, what does each component do and how does the overall pipeline work? Additionally, how do filtering and indexing work inside Elasticsearch?
- Do you have any questions you would like to ask me?

## Koerber Pharma（37 题）

### Koerber Pharma — DevOps Engineer（Exp --9 yrs Relevant (5 years)）（37 题）

- How to handle cost optimization in aws…how can we plan for cost optimization.
- If someone deleted a resource in terraform how can you identify it and recover it. how to detect some one deleted in tf how to rectifty
- How to desgin an web appl handle flucting low latency and how traffice flow in it
- How to achieve low latency routing? Which routing you will use?
- If your statefile is deleted..how can you recover without recreating resources.
- How are you connecting client's environment from your AWS environment.
- Suppose you found a malware in client's machine and now you want to get rid of it and set up a environment which will be free from malware attack. How to achieve it.
- Types of ec2 instance.
- What is spot, reserve instance, on-demand instances.
- How you are creating different environment in terraform.(dev,prod,test)
- terraform provisioner
- How will you connect your terraform environment from aws and implement CI/CD.
- What is terraform work space and how are you managing it.
- Whats are the strategy to deploy a application.
- Difference between observality and monitoring
- What are cloud watch, cloud trail, cloud matrix
- If some resource is deleted how can you identify which resource is deleted.
- security best pracices in aws
- how to manages certificate in aws. If the certificate expires how are you managing it and what's the action you are taking over here.
- Difference between NAT gateway and NAT instance.
- Difference between transit gateway and vpc peering.
- Suppose you joined to a organisation, how the access would be given to you.how to secure aws account as admin.
- Difference between roles and policies
- what's the strategy you are using for zero downtime..how to acheve it…explain it
- Difference between cmd and entrypoint
- Docker volume, docker prune
- Types of storages…difference between s3 and EBS.
- K8s architecture, services, if application pod fails how to troubleshoot
- how to shecedlue a pod in specifc node
- diff between statefull set and stateless app
- can we delete pause conatiner
- aws lambda where to use use case
- diff between monitoring and observality
- terraform uses real time issue we faced…what are the error u faced in terraform recently
- different plugins for ci/cd in jenkins using aws platform
- service to monitor spike in aws .application cpu usuage in cloud.
- how to do backup from ebs volume and attach in another server

## LTIMindtree（48 题）

### LTIMindtree — DevOps Engineer 1（8 题）

- Can we install docker inside a container.
- If we have created 3 instances using terraform script and the instance names are mentioned as a list
- Suppose we removed 2nd instance name from the list and applied script again then what will happen to the already 3 instances created before.
- If we have 5 stages in a jenkins pipeline and 5th stage having syntax error then what will happen if we run the pipeline.
- What are some main differences between scripted and declarative pipeline.
- Difference between code quality and code coverage.
- What is default qualitygate in sonar
- How to run a yaml manifest without a yaml manifest file created.

### LTIMindtree — DevOps Engineer 2（Exp---5yrs）（13 题）

- Day to day activities in current role
- Git rebase
- Git clone
- Aws code commit flow
- Deployment types
- Lambda functions
- How u secure Lambda
- K8s architecture
- git cherry-pick command
- appspec.yml usage
- Docker file
- how u do environmental variable in aws
- Ansible

### LTIMindtree — DevOps Engineer 3（Exp---5 year）（5 题）

- write terraform script for creating app service in azure or write terraform script to create lambda in aws
- create 3 different images and store it in ecr or acr, deploy to eks or aks - write kubernetes yml files
- explain branching strategy
- you have an application gateway, services which is in backend is good, you are getting 404 error ,how do you troubleshoot further
- what is the difference between firewall and nsg

### LTIMindtree — DevOps Engineer 4（Exp--->3 yrs）（8 题）

- How do you deploy python application on aws using jenkins pipeline
- How do your day starts and what activities you perform
- How do you upgrade your eks
- How do you handle when pod dies
- Your aws jenkins pipeline takes high time, how will you troubleshoot
- Create manifest for 2 nginx replicas
- Create a terrsform state file s3 bucket which expires within 30 days
- How do you provide security in docker

### LTIMindtree — DevOps Engineer L2（EXP 3-5 years. (L2)）（14 题）

- How do you design a fault-tolerant architecture in the cloud?
- How do you manage secrets securely in GitOps or deployment pipelines?
- How do you implement blue-green or canary deployments using container orchestration?
- How do you manage multiple environments using reusable infrastructure code?
- What is the purpose of backends in infrastructure-as-code and how do you implement remote state with locking?
- How do you implement rollback in an automated deployment pipeline?
- How do readiness and liveness probes work and why are they important in production environments?
- How do you troubleshoot a pod that is stuck in CrashLoopBackOff?
- How do you secure sensitive data like passwords or API keys in infrastructure setups?
- How does your GitOps tool detect drift and how do you manage it?
- Write a script to monitor a service and restart it if it fails, including proper logging.
- 12 .How do you handle parallel execution in CI/CD workflows?
- What’s the difference between using count and for_each in infrastructure code, and when should you use each?
- How do you monitor and alert on cloud resources effectively?

## L and T（24 题）

### L and T — DevOps Engineer（EXP-- 9years(4yrs in devops)）（24 题）

- What is cherry-pick
- what is git checkout
- Explain git branching startgey
- What is dockere compose
- explain k8 archtiecure
- What is docker file
- Diff between virulastion and conteraziation
- what is stragey to do conterzation of an application
- how your approach to do migration an app  from montholic to conterization
- What is loadbalancer in k8
- What is ingress controller
- Explain git branching startgey
- what is docker compose depends_on
- can we delete pod and multipilte container can run in
- what is git merge conflict
- Can conatiner can restart itself how explain?
- access control in k8
- what is kubeproxy
- how to get static ip of k8 how to manage
- How you are managing secrets in kubernetes
- what is ansible roles
- what is ansible vault
- and how to manage variables diff env in ansible
- how to run anisble playbook and diff options

## Marsh McLennan（17 题）

### Marsh McLennan — DevOps Engineer（YOE---> 3 yrs）（17 题）

- What is the difference between Git Merge and Git Rebase?
- Explain Git Merge and Git Rebase with an example using the main and feature (or master) branches.
- How do you reduce the size of a Docker image?
- What is a multi-stage Docker build? How does it help reduce image size?
- What is Docker image layer caching?
- How do you implement Docker image layer caching?
- Do you use any tool for Docker image layer caching? If yes, which one?
- In GitHub Actions, if one job depends on another job, which parameter do you use?
- How do you prevent concurrent executions in GitHub Actions?
- What is the difference between needs and concurrency in GitHub Actions?
- Walk me through the troubleshooting steps for a failed Helm deployment.
- If a Helm release is partially deployed and some resources are updated while others have failed, how do you perform a rollback?
- Where do you store application credentials in your CI/CD pipeline?
- How do you manage credentials in Jenkins?
- Have you used HashiCorp Vault for secret management?
- How do you store and retrieve secrets from HashiCorp Vault?
- What are the different authentication methods or injectors supported by HashiCorp Vault?

## Moodys（10 题）

### Moodys — MLOps Engineer（YOE---->3-4 yrs）（10 题）

- Can you briefly introduce yourself and explain your background relevant to DevOps/MLOps?
- How do you set up infrastructure for deploying ML models using Terraform?
- How do you manage and version Docker images stored in Amazon ECR?
- Apart from SageMaker, which AWS or open-source services have you used or are aware of for training ML models?
- If batch jobs are running for ML workloads, how do you handle deployments without impacting ongoing processing?
- How do you design and implement a complete CI/CD pipeline for ML models?
- How do you prevent misuse or unauthorized usage if someone attempts to spin up ML services in AWS?
- What strategies do you use to optimize and control AWS costs for ML workloads?
- How do you set up monitoring and observability for ML models in production?
- You are given a GitHub Actions workflow snippet. How would you identify incorrect steps and suggest improvements or missing steps for a robust CI/CD pipeline?

## Morgan Stanley（18 题）

### Morgan Stanley — Release Engineer（EXP-- 7 YOE - Release engineer）（18 题）

- Reverse proxy and forward proxy
- Ulimts
- You got an error like "Too many files are open" in your script, what will be the fix
- A and CNAME
- Date is behind the current date in VM, how to fix that
- Cross-Origin Resource Sharing
- /proc purpose of this directory in Linux
- Purpose of sed command
- Python code to find missing file
- Is it possible to add multiple alias to domain
- If I have two different domains, how to enable a communication between them
- Creating certs for multiple sub-domains
- Hardlink and Softlink
- Linux Command to create softlink
- Using sed command, how to remove first and last line of the file
- stdin, stdout, stderr in linux
- Ingress vs Egress
- How to fetch error from log files

## NPCI（10 题）

### NPCI — DevOps Engineer（Exp-----> 5yrs）（10 题）

- Docker:
- I can able to get access application from outside container but from inside getting packet loss. How do you trobleshoot.
- How do you get logs from docker level.
- Two containers are there. One with front end application and second container has db.Fisrt I want to start db then front end. What should you do?( 2tier application)
- Kubernetes:
- How do you call pod1 to pod2 without service.
- what is Container Network Interface
- what is CSI driver
- Static volume provisioning and dynamic volume provisioning. Explain in with use case.
- what is auto volume expansion.

## NUOS INFO Systems（18 题）

### NUOS INFO Systems — DevOps Engineer（Exp--4yrs）（18 题）

- Tech stack— mainly around Terraform, Azure, DevOps, Docker, and Git
- How do you scale a Terraform pipeline that takes 25+ mins?
- What happens to the Terraform state file if someone deletes resources from Azure?
- If the pipeline fails due to existing resources, how do you handle RIP (Remove, Import, Plan)?
- How do you export Azure resources into Terraform code?
- How do you enforce Azure Policies (like tag or location restrictions) using Terraform at scale?
- Best practices to structure repos and pipelines in a large DevOps project?
- Pipeline fails only on Tuesdays, no code changes — how do you debug?
- Logs are incomplete — how would you troubleshoot across AKS, Ingress, App, and Infra?
- How to monitor Azure VM memory and alert if it crosses 80%?
- How to write a multistage Dockerfile for a Node.js app — removing secrets and unnecessary layers?
- Recommended tools for CI/CD, artifact storage, vulnerability scanning, and container registry in a hybrid (on-prem + Azure) setup?
- How do you assess Azure DevOps migration readiness and plan the transition?
- How do you manage AWS + Azure using a single DevOps process with focus on security & cost?
- How would you use Azure DevOps REST API to apply a security policy to all repos programmatically?
- What’s the difference between Git Merge and Rebase?
- If someone force-pushed and lost the main branch, how do you recover it?
- How to push the recovered branch back to remote?

## NatWest Group（7 题）

### NatWest Group — DevOps Engineer（7 题）

- about Maven release
- about maven lifecycle
- about dependency management tag
- how did u manage Kubernetes pods it is on Linux right?
- what will happen with maven install
- what are the types of branching stratergy u r using
- in which directory or in which place ur pom.xml there

## Netcracker（22 题）

### Netcracker — DevOps Engineer（Exp- 7 Years - DevOps role）（22 题）

- Diff between mount and directories in Linux
- How will you restart http service from VM
- Disk I/O
- What is meant by CPU throttling
- Custom resource in k8s
- What is ingress
- Application is configured with Ingress but the webpage is not loading ? What are the steps will be checked
- How will you monitor the cluster through Prometheus
- Upgrading the worker nodes in K8s
- For junior team member, what are the roles will be provided in k8s
- Diff between Role and Role binding
- If I want to deploy my app in worker node2, what should I do ?
- Diff between Nodeselector, node affinity VS Taint, toleration
- While updating your worker node, you're trying to perform drain out the PODs  but some PODs are not removed from the node, what you will do
- What command will you give for view access for the cluster → READ in rolebinding.yaml file
- Storage classes in k8s
- NFS
- What's the purpose of using storage class in k8s
- I've two PODS in the same worker node, will they communicate with each other?
- I've two PODS in diff worker nodes, can they communicate ?
- How to restrict the communication between them ? → network policy
- What component should be added in network policy YAML file

## Nextturn（22 题）

### Nextturn — DevOps Engineer（YOE---）（22 题）

- Python – Write a script to check disk usage and send an alert if it exceeds a threshold.
- Explain Continuous Integration, Continuous Delivery, and Continuous Deployment.
- Explain an end-to-end CI/CD pipeline.
- Kubernetes – Troubleshoot a worker node that goes down.
- Kubernetes – Troubleshoot a Pod stuck in Pending, CrashLoopBackOff, or ImagePullBackOff.
- Terraform – Difference between terraform refresh and terraform plan.
- Terraform vs Ansible – When to use each and how they work together.
- Azure DevOps – Variable Groups, Environment Variables, and Secrets.
- Helm – Upgrade failed. How do you rollback and troubleshoot?
- Jenkins vs GitHub Actions.
- GitOps – Push-based vs Pull-based deployment.
- Jenkins – If the controller (master) node goes down, how will you troubleshoot and restore it?
- Difference between Continuous Delivery and Continuous Deployment.
- You have a Kubernetes cluster with 30 nodes. 29 nodes are Ready, but 1 node is NotReady. You have already checked kubectl logs, kubectl describe, and other basic commands. How will you troubleshoot the node further?
- What is your hands-on experience with Ansible? Explain a real project where you used it.
- In Terraform, how would you create multiple EC2 instances, each with different configurations (for example, different instance types, AMIs, tags, or volumes)?
- Explain Docker layer caching. During a Docker build, if layers 1–10 are already cached and you modify Layer 5, what happens to Layers 6–10? Will Docker reuse the cache or rebuild them? Explain why.
- You are able to launch an EC2 instance from the AWS Console, but you cannot SSH into the instance. How would you install tree package
- Explain the pre-build, build, and post-build stages in a CI/CD pipeline.
- In a Jenkins pipeline, at which stage would you publish or push artifacts/images to Nexus or Artifactory—pre-build, build, or post-build? Why?
- What are the common reasons for a Kubernetes node becoming NotReady, and how would you identify the root cause?
- Describe your approach to troubleshooting Kubernetes worker node issues beyond the basic kubectl commands.

## Nice（33 题）

### Nice — SRE 1（EXP--3yr）（14 题）

- Comapny - Nice
- Position - Cloud Site Reliability Engineer
- Explain your project .
- What is terraform how you configured your project ?
- What is modules in Terraform ?
- What is diffrence between CMD and Entrypoint in docker ?
- What is diffrence between ADD and Copy ?
- What is the deployment and statefullset ?
- What is the deployment ?
- what is the monitoring set up for your project ?
- Have you create the Dashboards in  Grafana ?
- How do you handle the HELM chart ?
- Explain CICD ?
- How you are maintaining ArgoCD for E1,E2,E3 env ?

### Nice — SRE 2（EXP--3yr）（19 题）

- Comapny - Nice
- Position - Cloud Site Reliability Engineer
- [ ] Can you brief through your profile?
- [ ] Is it client-based work or are you just in the middle of deployment?
- [ ] You mentioned improving CI/CD efficiency by 60%. Can you explain the specific optimizations you made for this?
- [ ] What is your approach to integrating automated testing in pipelines to ensure high code quality?
- [ ] How do you integrate tools like SonarQube into your pipelines?
- [ ] How do you design and manage a containerized environment to ensure scalability and high availability?
- [ ] In Kubernetes, how do you manage application deployment, scaling, and rollback? Can you walk through a specific scenario?
- [ ] What is the advantage of using a YAML file over classic build pipelines in Azure DevOps?
- [ ] Any other advantages of using YAML pipelines that you have experienced personally?
- [ ] Are you familiar with Terraform?
- [ ] Can you describe a real-time scenario where you used Terraform to provision a highly scalable infrastructure?
- [ ] What branching strategy do you follow for source code management in a large team with a complex application?
- [ ] Do you have experience using Azure Key Vault?
- [ ] Have you integrated Azure Key Vault into your pipelines or branches in any project?
- [ ] Did you create the Azure Key Vault access policies yourself, or did someone else do it for you?
- [ ] What is a recent challenge you faced while implementing a DevOps practice or pipeline in your team or organization?
- [ ] Other than Azure and AWS, are you familiar with any other cloud platforms or services?

## Nisum Technologies（14 题）

### Nisum Technologies — DevOps Engineer（14 题）

- explain CI/CD pipeline
- what is scrapper?
- can we deploy services on master node?
- Did you upgraded any services?
- what is deployment stratergy that you are following?
- what is differnece between COPY and ADD commands ?
- How do you fix security issues in Docker images?
- what is difference between content and tuple in terraform?
- Any experience on phython/shell scripting? can you explain one file?
- Any expercience on ansible?
- Expalin about fargate?
- If you pod is not running, how do you troubleshoot it?
- what is diffrence between list and string in terraform?
- Did you worked on helm charts?

## Nitor Infotech（25 题）

### Nitor Infotech — DevOps Engineer（YOE-->6 yr）（25 题）

- CI/CD setup in current project. How does the flow look like
- Gitops approach, ArgoCD, Flux
- Shared libraries in jenkins
- How is caching implemented in jenkins in your project
- Current jenkins version
- How have you implemented parallelism in your pipelines
- Statefulset, daemonset, Deployment
- Networking in kubernetes, how have you implemented
- Taints, tolerations, affinity
- How would you reduce the runtime of pipeline, multi stage build
- SCP
- VPC Endpoint, IGW, Transit Gateway, Virtual Gateway
- Need to provide user only EC2 start and stop access how would you do it
- User has the role with policy to access S3 bucket, but it still not able to access what may be the reason
- Terraform refresh command
- How do you handle infrastructure code for multiple environments using terraform
- State locking in terraform
- Create a Deployment named web-app with:
- Image: nginx:1.25
- Replicas: 3
- Container port: 80
- Labels: app=web
- Write a nodeport service to expose the application on port 8080 for the above deployment
- Write a script to count how many processes are running under the user ubuntu.
- How have you implemented RBAC in your EKS setup

## OPT IT（15 题）

### OPT IT — DevOps Engineer（Exp:2+yrs）（15 题）

- If dbs are in private subnets how do you deploy in kubernetes
- WHAT ARE THE BEST PRACTICES THAT YOU FOLLOW TO CREATE RESOURCES LIKE EC2,RDS,MANGODB
- HOW MANY TEAM MEMBERS
- HAVE YOU WRITTEN ANY KUBERNETES MANIFEST FILES,WHAT ARE THE KINDS YOU WROTE
- WORKSPACE CONCEPT,MODULES CONCEPT
- WHAT ARE THE MONITORING TOOLS U USED
- WHY USE PROMETHEUS AND WHERE YOU DEPLOYED
- PROJECT RELATED HOW MANY MICROSERVICES ARE THERE IN YOUR PROJECT NAME SOME
- WHICH MICROSERVICES YOU WORKED ON
- WHAT DID YOU LEARN IN YOUR PREVIOUS COMPANY
- HOW DO YOU CONTAINERIZE YOUR APPLICATION
- WRITE A DOCKER FILE FOR JAVA APPLICATION
- WHAT TOOL YOU WORKED ON FOR CI/CD
- WHAT TYPE OF PIPELINE YOU WORKED ON
- ANY QUESTIONS

## One2N（21 题）

### One2N — DevOps Engineer（YOE--->）（21 题）

- What is something you have implemented end to end in your project
- HPA implementation in detail
- Why would you deploy rabbitmq as stateful set why not deployment
- How would you get application level metrics
- How would HPA with stateful set work
- Deploying a 3 tier architecture
- Your approach (Set of tools you would pick up)
- Docker Swarm/Kubernetes
- What kind of database you would use
- How would you manage these microservices
- How would you expose the application
- Is load balancer required in this setup why?
- How would reverse proxy setup work here?
- How would you setup DNS here?
- How would you set up entire CI/CD setup for this application
- Is nginx required in this setup
- How would you manage SSL and TLS
- How would you update the image and deploy them
- Setup alerting for this setup
- Want to know how many users are affected ?
- Which metric will tell me regarding the application is up or down?

## Optum（9 题）

### Optum — DevOps Engineer（Exp--->5 Yrs）（9 题）

- What are the terraform lifecycle policies
- Why do we use workspace in terraform
- How do I transfer payloads between lambda function in 2 different AWS account
- How do you ensure the least privilege access to the IAM users
- What is terraform external command and when it should be used
- How do you ensure particular AMI image is present in AWS account using terraform
- What are terraform provisioners
- What are s3 bucket lifecycle policies?
- What is meta-arguments in terraform

## Oracle（21 题）

### Oracle — DevOps Engineer（Experience - 8 years's）（12 题）

- What's the purpose of using init containers in K8s
- Stateful vs deployment in k8s
- Configmap VS secrets
- Pod Distribution budget in k8s
- Explain me all the steps for multi stage docker image
- Cron expression to schedule a job in Linux
- What are the layer's you will get in Docker while building
- When you're trying to deploy a POD, it's  throwing an error, how will you investigate.
- How to deploy a POD into a certain NODE?
- Explain me all the components present under deployment.yaml file
- If TF statefile is corrupted, how to fix it ?
- TF Lifecycle (create / after destroy)

### Oracle — DevOps Engineer 2（Exp----7 YOE - DevOps Engineer）（9 题）

- How do you give access to the user for a namespace in kubernetes cluster
- What is ingress and why are you using istio ?
- Explain me the three tier architecture
- What are the types of services and explain each
- What is custom resource definition
- What are the kubernetes resources you know
- What is the role of container runtime and which runtime do you use and why?
- What is reverse proxy
- What is traffic mirroring in istio

## Orion Innovation（12 题）

### Orion Innovation — DevOps Engineer（Exp---- 5yr DevOps Engineer）（12 题）

- what is A record and what it will do in DNS
- what is the value of A record
- what is CName record in DNS
- what is MXRecord in DNS
- you want to store the secrets in Jenkins pipeline , how will you do it
- application gateway TLS certificate is expired, what steps you will follow to renew it
- in Kuberenets there are 10 worker nodes, I have to deploy tomcat on each pods , how will you achieve it
- I have an apache tomcat application running in k8 cluster, what are the manifests files you will be having inside in it
- application gateway is L7 or L4
- you have multiple VPC, how will you connect them in AWS
- an RDS is there in India region, I want to do read sync with RDS in London region, how will you implement it
- i have an local laptop, I want to access my hosted website, what service will be used in K8s

## Perfios（14 题）

### Perfios — DevOps Engineer（Exp-->4.7yrs）（14 题）

- What happens when an user hits "www.clarify.com" how the request pass through the network ?? write a diagram and explain it to me
- Explain amazon traffic architecture how it goes to private subnet? I write diagram and explained it
- Do you use pipeline for three different env or one for all? Explain how?write a groovy script using any ci cd took for build, test and deploy stages.
- Difference between cluster ip and node port?
- How does a three tier architecture looks like? Compare it with two tier
- What are ALB and NLB, and when should you use each one?
- Write a shell script to sum (1..100) and give me result
- Canary vs blue green
- How to achieve zero downtime application upgrade?
- Have you contributed any automation initiatives in your current company as a DevOps engineer?
- When you deploy from CI, you build a package and then need a platform to deploy the application. How do you build that platform, and if it requires human intervention, how do you eliminate that dependency?
- In GitHub, after a code commit, what validations do you perform? Do you validate before the commit or after the commit?
- Write a shell script that takes an integer N as input and prints numbers in a triangular pattern.
- Each row should contain consecutive numbers, but printed in reverse order, and the number of elements in each row should increase by one.

## Persistent Systems（58 题）

### Persistent Systems — DevOps Engineer 1（Exp---9YOE DevOps - 5YOE，K8s ---，GitHub Actions ---，AWS ---）（16 题）

- Explain your current project and your activities in it.
- K8s Architecture.
- How do you upgrage k8s cluster.
- Pod Affinity and Node Affinity.
- HPA & VPA.
- What is GitHub Actions Matrix strategy.
- How caching works in Github Actions.
- what is Stale branch.
- ACM
- CloudTrail
- CloudFront
- CloudFormation.
- Cloud watch & how do you create a custom metric in AWS CloudWatch.
- How do you login to the ec2 instance if you've lost the .pem key?
- Public and Private Subnet, what makes it public and private??
- Where does NATGateway reside.

### Persistent Systems — DevOps Engineer 2（Exp----13 YOE -rele- 5yr DevOps Engineer）（9 题）

- Design an high availability and redundancy three tier architecture in azure
- Suppose you are having an e-commerce application  and slowness is there how will you troubleshoot
- Design three architecture for front end and react js and backend as node js , which are the services you will use it in azure
- What are the steps involved in creating in azure devops pipeline
- What is github actions
- In azure monitor which metrics is used for monitoring kubernetes
- What is the module approach in terraform, explain on it
- Suppose there are 1000 of lines in terraform, as a period of time it grows, it becomes slow in future, how to approach this issue, please explain
- Have you worked on python ,

### Persistent Systems — DevOps Engineer 3（exp -----> 5 yrs）（22 题）

- Explain your last project
- What are the AWS resources you have used in your previous role?
- Can you write code in Python? (Provided some samples)
- What is terraform state mv?
- What are microservices?
- Explain flow of CI/CD pipeline
- Have u handled lambda? Explain your project
- How do you ensure POD to POD communication?
- What is hierarchy of Kubernetes?
- If you are given a project eg EC2 or EKS or anything else what are the things you would take into consideration from prerequisite till output?
- How would you decide on the type of environment required for deployment?
- Explain terraform statefile
- Explain terraform move command?
- What is subnet?
- If I have EC2 instance for which I don’t want to talk to internet but intra-communication can be possible, how to configure it?
- What is ECS & EKS and when would you choose either of it?
- If there is a vendor who provides VPN services for company A, his manager wants to view some dashboard but do not have AWS account. How would you help him?
- I have webapp in India and slowly users from abroad are also tyring to access it but there is latency. How would fix this issue, which service can help in reducing latency?
- What is AWS lambda and where have u used?
- What is Athena?
- What are the different type of S3 storages available?
- How do you scale EKS? What are the metrics considered and where do you add your inputs and How? Explain how you have done auto-scaling in your project

### Persistent Systems — DevOps Engineer 4（11 题）

- With respect to DevOps, to set the CI/CD pipeline, which tools and services have you used?
- Do you have experience with AWS DevOps services like CodeDeploy, CodeBuild, and CodePipeline? How would you set up a pipeline using them?
- Do you have experience with GitHub Actions? Suppose I want to build and test a Java Maven application and create an artifact, what steps would you include?
- Where do you keep the GitHub Actions workflow file, and how do you upload a JAR artifact?
- You said you configured SonarQube. What does SonarQube do?
- Which version of SonarQube have you used — Community, Developer, Enterprise, or SonarCloud?
- How did you integrate SonarQube with Jenkins?
- In your project, what was the application language you scanned with SonarQube?
- How do you set up quality gates in SonarQube?
- What things have you done in Jenkins?
- Can you write a Jenkinsfile for a Node.js application to build, push Docker image, and deploy to Kubernetes? Please also explain it in detail.

## Plansource ValueLabs（13 题）

### Plansource ValueLabs — DevOps Engineer（13 题）

- how many subnets you can add to a VPC
- how to stream logs from docker conatiner to s3 from specific path within conatiner
- How you manage varibles in pipeline for terraform for different enevironments(dev/live/feture)
- what happens when youe hit DNS from browser
- difference between http and https
- difference between  Service  and Task in ecs
- how Autocaling happens in aws ECS
- how you scale  your EKS cluster based metrics/logs
- difference between ALB and ELB and comes under which layer, when  to choose and why
- How to spead up s3 upload with files in large size,  and client uploaded 10 Gb file but failed  after uploading 5 gb how you confirm that 5 gb is uploaded to s3
- how do  you optimize S3 cost
- how do you make s3 secure  which is  have client sensitive  data
- how autoscaing happens with ALB

## Publicis Global Delivery（7 题）

### Publicis Global Delivery — DevOps Engineer（Exp--->）（7 题）

- Kubernetes cluster upgrade from one version to another version? What is the approach?
- What is PDP in Kubernetes?
- How do you extract all git commits from last 3 days?
- How does authentication happen in Jenkins pipeline to use aws with particular login, if you have 1 logout?
- What are access modes in PVC?
- You have mongoDB db dump, from that you need to clear some space out of it. How will you do that?
- You have one stateful application, that needs to be deployed specified node in k8s, how?

## Qburst（17 题）

### Qburst — DevOps Engineer（EXP-3-5 yrs）（17 题）

- Different types of services?
- what is nodeport what are the cases we can use it?
- what are loadbalancer used?
- K8s command to list the pods with specific nodes?
- How can you restrict public access to load balancers either standalone or gke?
- What is major vpc difference between aws & gcp vpcs?
- How can you can you migrate one node pool vms to another node pool in gcp?
- If vm deployed in private subent how can you do patch updates like apt update?
- Terraform provisioned resource should not delete by deleteing resource configuration in terraform code how can you do it?
- How can you handle terraform different environments?
- Is it possible to move terraform state file to remote configuration once created?
- What is IAP in gcp?
- What vpc connect?
- How can you reduce gcp storage buckets costs?
- what is difference between add and copy in docker file?
- How can you reduce the docker build size?
- I want pass a value while building a docker image how can it be done?

## Qentelli Solutions（13 题）

### Qentelli Solutions — DevOps Engineer（Exp-----> 5yrs）（13 题）

- create s3 bucket with terraform
- If developer sets private subnet to public, what should you do?
- KMS
- ELB inflow and outflow
- How you maanage resources in terraform
- write a shell script to backup logs last 7 days and remove older days.
- SG and NACL
- How do you secure your environments in aws
- soft link and hard link
- user not able to get ssh, what are troubleshooting steps to perfrom
- what are metrics in cloudwatch you should focus on.
- Your aws billing spikes, what should you check
- what are security options in aws

## Rapidsoft（12 题）

### Rapidsoft — DevOps Engineer（Exp-: 10.5 years work ex. Devops. 4 -5 years of devops experience）（12 题）

- What things have you worked and your experience in brief?
- Terraform has errors while provisioning infrastructure. How to do investigate those? Basically how do you validate the terraform file
- In ansible if you need to execute something as root user how do you that?
- Your CI/CD pipeline has failed in jenkins. How do you investigate?
- How do you store sensitive information like passwords in jenkins?
- You have a multi-cloud environment. How do you manage pipelines for all those cloud environments?
- How would you structure disaster recovery for your applciation?
- How would you perform database migration for your database application?
- You have a crashbackloop error. How would you fix this error?
- Difference between deployment and stateful sets?
- Explain terms in deployment.yml file in kubernetes
- How you worked on docker swarm before?

## RelevantZ（21 题）

### RelevantZ — DevOps Engineer（Exp--->5 years，Role ---> devops）（21 题）

- RelevantZ interview questions
- Have you ever migrated on-premesis db to cloud , especially postgres or any other (port no of postgres sql too pls if you remember)
- how do you login into pods using kubectl command
- you have two environments, I should not deploy anything on one environment and another environment infrastructure should deploy via terraform, what strategy you will use
- how do you build dc/dr setup and what is the purpose for DR
- what cost optimization methods you had used for reducing cost
- suppose there are 100 lines of code am writing in terraform, I want to avoid it, how do I achieve it
- what are the tools you had used in azure devops , where do you store the output of CI pipeline (azure artifact)
- what are the steps you create in azure pipeline
- how do you store secrets in azure devops
- have you ever automated .csr – .cer - .pfx certificate activity
- for what purpose do you use log analytics workspace
- suppose a DB is there in private subnet, I want to communicate only with specific people , how do achieve it
- suppose there are multiple persons executing terraform commands, what problem will happen
- have you used any monitoring tools
- suppose I want to communicate from subscription to another subscription, what are all the methods available to achieve it
- tell me some commands on kubernetes – how do you troubleshoot it
- what is terraform drift
- there is data in ADF, data will not be constant always, it will be dynamic how do you get the data and analyse it and present (it can be done through pipeline too)
- what do you do with azure recovery service vault
- how do you take backups and explain some strategies which you had used

## SAP（12 题）

### SAP — DevOps Engineer（Exp---8yrs  Devops）（12 题）

- Suppose a new deployment was implemented, suddenly all the PODs (new and old ones) crashed, what's the reason for this ? → New deployment exhausted the resource limit, so we need to use "limit" in our deployment.yaml file
- Which deployment is better cost wise.
- I want my deployment to be implemented to specific workloads or regions, that update shouldn't go to other parts. There is an option in argo CD
- How the auto scaling works, how things work in the back-end, from worker nodes to master nodes. Communication track behind that.
- Can we perform Blue Green deployment under the same namespace? If yes, how will you manage them?
- You did a deployment with Canary, when you will delete the old pods, what are the KPIs to cross check before deleting them.
- Once the blue green deployment is completed, how to check if the deployment is successful.
- You’re trying to schedule a new POD but the new PODs are not deploying properly, what checks will be done.
- Why do you want to use Argo CD over Jenkins?
- How will you maintain your base image, vulnerability free?
- How will you perform the patches regularly
- Git submodules, what is their purpose

## Sapient（25 题）

### Sapient — DevOps Engineer（EXP--->6yr）（25 题）

- Comapny - Sapient
- Position -
- In AWS, what all the services you have used?
- In Route 53, can you tell me the difference between A record and CNAME record (written as “ad code and symmetry code” in screenshot)?
- Purpose of DNS in your project.
- In your project, what was your domain name? How are you establishing connection between domain name and service?
- Have you created DNS record?
- Can you tell about your VPC structure and networking architecture used in your project?
- How many subnets are you having?
- In which subnet are you placing your EKS cluster and which networking components have you used?
- Why are you keeping your web application in a public subnet?
- Where Load Balancer will be there?
- How many AWS storage services does it have?
- EBS: Suppose you are maintaining data in EBS (sensitive data) — how are you securing those data?
- Iteration limit – what is it?
- What is the data block?
- What are modules in Terraform?
- How are you calling your modules?
- Have you worked on null resources?
- Explain Terraform state file –
- In which file you will define where Terraform state file should be generated and where it has to be maintained (which config file)?
- In which way are you managing your cluster — using kubectl commands or something else?
- If your cluster is in a private subnet, then outside kubectl will not be working, right? How are you accessing that?
- What is EBS and EFS in Kubernetes?
- I have an S3 bucket, and there is some file inside it — my pod wants to access that S3 bucket. How will it access it?

## Sigmoid（149 题）

### Sigmoid — DevOps Engineer 1（Exp---> 7 YOE DevOps Engineer）（7 题）

- Reverse the string using For loop
- Check if the palindrome using For loop
- "Hello World Hello" --> Check how many times hello got repeated
- Diff between replica set vs replication controller
- K8s backup policies
- How do you handle deployment failures
- What happens if master node fails suddenly

### Sigmoid — DevOps Engineer 2（Exp---> 7 YOE DevOps Engineer）（31 题）

- Terraform taint
- How to limit the resource usage in K8s
- asked me to write request and limit usage YAML file
- Write a deployment file for the below requirement
- *Create a Deployment named 'space-alien-welcome-message-generator' of image 'httpd:alpine' with one replica.
- *It should've a ReadinessProbe which executes the command 'stat /tmp/ready' . This means once the file exists the Pod should be ready.
- *The initialDelaySeconds should be 10 and periodSeconds should be 5
- If Liveness probe is healthy and readiness probe is failing, what will happen
- How will you find out the data loss while switching back to DBs
- Have you integrated Global LB with K8s cluster
- How to enable RBAC to Service accounts
- You created a resource through Terraform but it failed during provision, what will happen
- Purpose of using "null resource" in Terraform
- If some developer hardcoded password mistakenly in source code and pushed to repo, how to fix it in CI process
- If terraform deployment got failed, what will be the approach
- Write a script to capture the failures
- Input :
- 2025-05-23 10:00:01 ERROR: Connection failed to database
- 2025-05-23 10:01:02 INFO: Retrying connection
- 2025-05-23 10:01:30 ERROR: Connection failed to database
- 2025-05-23 10:02:10 ERROR: Connection failed to database
- 2025-05-23 10:03:55 ERROR: Connection failed to database
- 2025-05-23 10:06:00 INFO: Recovery attempt successful
- 2025-05-23 10:07:20 ERROR: Timeout while reading from API
- 2025-05-23 10:08:15 ERROR: Timeout while reading from API
- 2025-05-23 10:09:10 ERROR: Timeout while reading
- output :
- [ALERT] 'Connection failed to database' occurred more than 3 times
- [ALERT] 'Timeout while reading from API' occurred more than 3
- DNS Custom resolver
- Metrics used for monitoring

### Sigmoid — DevOps Engineer 3（Exp---> 7 YOE）（28 题）

- If LB is created in us-south and that region is down what will happen ?
- If RDS is hosted in us-west region and has read replicas spread across other region, due to some issue us-west region is down, how will you redirect your traffic. But having one more DB is expensive to the client
- Which deployment strategy is best, assuming that you have only one POD is running
- If you're going with Blue Green deployment, how will you change your configuration to reroute the traffic between blue and green, exactly which configuration needs to changed?
- New web deployment was done today, how will you make sure that particular application is behaving and we need to find out the issues before user's figures out
- Practical difficulties in having the infra in two different regions
- Write a shell script to delete the log files which is older than 30 days
- Failover mechanism in LB
- Is it possible to have ASG and LB in different regions ?
- How to create sub user while writing Docker file
- Creating custom images
- How to enable Debug logs in Terraform
- Create system design for three tier architecture with secuirty and avalability in place.
- Create a python script for this requirement
- #Given a string s, find the length of the longest substring without duplicate characters.
- #Example 1:
- #Input: s = "abcabcbb"
- #Output: 3
- #Explanation: The answer is "abc", with the length of 3.
- #Example 2:
- #Input: s = "bbbbb"
- #Output: 1
- #Explanation: The answer is "b", with the length of 1.
- #Example 3:
- #Input: s = "pwwkew"
- #Output: 3
- #Explanation: The answer is "wke", with the length of 3.
- #Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

### Sigmoid — DevOps Engineer 4（Exp---> 4-7 YOE）（83 题）

- Round 1 (F2F technical - whiteboard round):
- Give introduction
- The flow from dev to prod. What are the security checks that you follow within CI pipeline of your current project.
- What is the branching strategy that you follow in your org. Why did you follow this approach over other strategies.
- There is a new requirement from platform team to design a 3 tier architecture, with frontend , backend and database with all the security best practices , high availability , low latency. (AWS)
- As a Devops engineer , you have to make a decision according to best and optimized solution for each component that you decide, like - should the db be run as statefullset or RDS/any cloud db managed solution is better, how do we deploy frontend-whether as pod or S3+cloudfront etc.
- During the explanation of architecture there were many counter and followup questions -
- How can you tell a subnet is pubic or private, what things needs to be in place.
- How is an end user able to access the app which is running inside pods of private subnet nodes.
- What is route53, how does the traffic actually flow in order, if a user requests or submits or posts anything from the UI.
- Explain each component in your architecture which is involved from a user requesting from the UI to the request reaching the backend pod, and how they are connecting with each other to ensure inbound and outbound flow(including the firewall, NACl, security groups, route tables etc).
- If you used a service with type: LoadBalancer and as you told its in private subnet , then how its able to launch a loadbalancer in public subnet, how its getting access to do it from within    private subnet. Which component of the control plane takes care of it.
- Why did you choose eks cluster over ecs.
- How are you managing the cluster nodes.
- For your specific architecture setup, how many ip addressess for all the components do you think will be sufficient enough from all the available IP's of both subnets within your VPC.
- Tell me how you handle the situation, if there is a DDoS attack in your cluster nodes or the cluster services, which is consuming all resources at 100% . What steps do you take in order to regain the condition back and what steps do you take to prevent this in future.
- How are you handling HA in your cluster , explain the reason why you use a specific feature over the other similar functionalities.
- What is the requirement of NAT gateway in your cluster, where should it placed to make it work as intended.
- Write a script to find a particular name in a file and replace it with another word.(can use bash or python) - they asked to execute as well
- Write a script to just find the first occurance of a pattern in the given file , and then extract the full line of the found pattern.(can use bash or python) - they asked to execute as well
- Write a script to find all the files in current directory and all subdirs,which are modified more than 5 hours ago, but not beyond today.
- Round 2(F2F technical round with cloud devops architect):
- Write python script to reverse string without using loop , without slicing shortcut, without in-built functions/libraries.
- Write a python script to take an integer input(input should handle only for atleast 2 digits), check divisibility by only 3 or by only 5 or by both 5 and 3 with proper handling, like if its divisible by both then it should not return the single divisibility, it should only return divisibility by both. If divisible by none of 3 or 5, check if its a prime number, if not a prime as well, then find all the numbers by which its divisible excluding itself and 1 and return the list of them.
- Explain and draw the architecture diagram of your current project flow end to end, while also explaining the measures you have taken for ensuring the security and best practicies to comply with SLA.
- In your current project , how are you handling the CI integration for multiple environments like dev/test/qa/staing/prod.
- Which branching strategy are you following and how did you apply this strategy to integrate within your CI pipeline to deploy the pushed code to the right env cluster. Where exactly in your CI code you handled deploying to dev , and to QA and so on till its ready for production. How did you handled the PR checks and approvals in your CI pipeline.
- What are the activities that happen after deploying to each env of CI pipeline and before its ready for next environment.
- Did you use AWS accounts? How did you handle the segregation of various environments within AWS.
- How is data block different from resource block in terraform. Explain a scenario in which both of them are used in conjunction.
- There is a requirement as part of some new integration in terraform managed resources, where couple of resources needs to be completely out of terraform lifecycle and they completely need to be handled manually. Come up with a solution to approach this without causing disruption to those resources, so that they are untouched and are not destroyed while also making it independant resource.
- What is taint in terraform, give a scenario where you need to use taint , explain how it works.
- Explain what are terraform workspaces, what is the main requirement to use them.
- There was an issue last time with some config changes in TF resource which had lead to slight downtime of the AWS resource during apply. What might have caused this downtime, how do you handle this in terraform for futurue config changes, for ensuring least possible downtime and maximum possible availability. Write a terraform code to handle this situation.
- Explain the S3 lifecycle. What are classess in S3.
- Did you work on cloudfront. How did you leveraged this for exposing frontend static code to serve the UI of the app.
- What is k8s API. Can you connect to a k8s API using REST api calls directly from any external app, like how kubectl connects to the API endpoints exposed on the kube API server?
- If there was an issue introduced in recent deployment , then how do we rollback the deployment , is it just the kubectl rollout undo command , how does it know which image it should revert to,does it take from the image repo or somewhere else?
- Round 3 (F2F managerial + technical round):
- Explain the use of below linux commands:
- finger,comm, netstat, jq, yq, at, atq, shuf, lsblk, less, last, nc, mtr, iftop, lsof, blkid, mkfs, nice
- Write a python script which takes a user input with any alphabet in capital (the user inp should be strictly alphabet and shouldn't be small letters).Then, from a given file, find min, max, sum from the corresponding numbers of the input alphabet. After printing the above details, delete all those matched lines from the file.
- eg:
- file.txt
- C,23
- A,41
- A,67
- Q,44
- C,29
- B,88
- A,12
- If input=A, then min = 12, max = 67 , sum = 120
- If input=B, then min = 88, max = 88 , sum = 88
- We have an app log updating in realtime, which contains multiple IP addresses who attempted connecting to it. Can you write a python script to return all the unique IP addresses from the log along with total count of unique ip addresses?
- eg:
- app.log
- Connection established from : 145.11.21.78
- Connection established from : 189.22.99.19
- Connection established from : 145.11.21.78
- output should be: 145.11.21.78 , 189.22.99.19 , count=2
- Write a 3 stage Dockerfile with below scenario using pre-built images that they provided for each stage
- Set and copy the env config files , env variables , bash profiles like .bashrc , .bashprofile etc which already comes with image, to the 2nd stage
- Use the files from previous stage and perform some prerequisite tasks and build the code from the current directory
- Use the output from the previous stage and build image
- Explain how is the image creation happening ,what are layers, how are layers forming, what details will we have in the image which is created from the final stage.
- What steps/commands in the Dockerfile is creating intermediate images. Once the final image is created , are these intermediate images still being utilized ?
- What is the difference between CMD and ENTRYPOINT. Explain with a scenario, how and why we use both of them in conjunction.
- What if we have multiple CMD's and ENTRYPOINT's in a single Dockerfile, would we get issues/errors during the docker build? If there is no issue in build , then how does docker takes care of these multiple CMD and ENTRYPOINT lines in Dockerfile while building it.
- What is publisher in Jenkins.
- What are executors in jenkins. Explain how they are working under the hood.
- Please explain how did you setup sonarqube in your CI jenkins pipeline, what are the quality gates and how did you set the threshold checks for code coverage leveraging the test reports created by developer.
- In Ansible playbook, how do you pass the output of one task to the next, especially when you're working with different blocks or stages in a playbook? For example, if you have multiple blocks, each with its own output, how can you transfer the results from one block to another—like from the first block to the second, or even from the 4th block to the tasks that come after?
- Why do we need extra load balancing capabilities like host based, path based routing etc to our pods, if services are anyways handling the traffic to route to right pod, what actuslly is the issue where just tradional standalone service cannot handle it. For example, if an end user is traversing accross various product details , how is frontend able to fetch details from the right pod (backend which in turn gets the actual product data from db), explain how the api calls to backend and to db is handled.
- If there is a real time application like a multiplayer game, or streaming app, how does it handle heavy concurrent user sessions at the same time without any latency and without too much delay.
- Consider a live production app which you are managing, and suddenly it started having latency issuues on the customer side where they are seeing slownes on each request to get processed and see the updates/response on UI back with lot of lag (lets say from 5 ms normal latency to suddenly ~5 mins). How would you go ahead with your troubleshooting, do a deep RCA to find out the exact source of issue, and you are given the task to resolve it in very short time as this is very critical app.
- Write a PromQL expression to alert if CPU usage is above 80% on any node.
- How will you alert if CPU usage stays above 90% for 5 minutes, but only if the number of running pods is below 5?
- Custom resource vs custom resource definitions
- Explain the end to end setup of ELK stack in the cluster that you are working on, in your current ongoing project.
- How is kibana connecting to Elasticsearch, write a yaml snippet  where this connectivity is handled.
- What are operators in kubernetes. How is the Elasticsearch working , is there some Elastic operator involved?
- Consider there is a MySQl operator running in one of your pod in one of your node of a k8s cluster. How the Mysql database managed by this is different from the normal pod that is started with a mysql image from deployment/pod template? Apart from just handling the updates, version changes, lifecycle, vulnerabilitites , security issues, it provides lot more advantages, please explain the use cases by giving some scenarios.
- If there is a requirement to run fixed 1 Mysql database accross each one of the nodes, how can you set this up in your cluster, with the help of custom operators.

## Sonata Software（50 题）

### Sonata Software — DevOps Engineer 1（Exp---- 5yr DevOps Engineer）（16 题）

- what is the difference between application gateway and front door
- how do you protect your endpoints in AKS
- what is the networking you are using in AKS
- how do you do cost optimization in cloud
- how do you implement to block an particular domain in application gateway
- how will write terraform module
- how do you upgrade an module in terraform
- share your screen and write terraform structure please
- how do you monitor if pods goes down
- which metrics is being used when cpu or memory  goes beyond 75% in vm
- where do you store the application gateway (TLS/SSL certificate) ?
- what is the time you will take to write an IAC code and deploy to app service ?
- how do you build ci/cd pipeline in azure devops
- suppose you are using SQL db, there cpu goes beyond 75% how do you upgrade it
- have you ever used terraform cloud
- do you use helmchart for AKS deployements

### Sonata Software — DevOps Engineer 2（YOE: 6 +）（34 题）

- AWS Questions
- What are the AWS services that you have worked on?
- Can you tell me what is cold start in Lambda?
- Have you worked on API Gateway?
- Can you tell me the difference between REST APIs and WebSocket APIs in API Gateway?
- How do you protect an API Gateway?
- Can you tell me the difference between NAT Gateway and Internet Gateway?
- Say if you have both explicit deny and allow policy to a user in AWS IAM, what happens?
- Can you tell me the difference between managed policy and inline policy in IAM?
- How do you retrieve secrets from AWS Secrets Manager using Python?
- How do you protect the secrets in Secrets Manager?
- How do you encrypt secrets in AWS Secrets Manager?
- Say you need to configure EC2 instances automatically or replace themselves automatically when they fail. How do you implement this?
- Have you worked on AWS Auto Scaling?
- What is the use case of Auto Scaling?
- Will Auto Scaling automatically scale up? How do you set that up?
- Say you have EC2 instances running web servers and need deployment with minimal downtime during updates. How do you approach this?
- Can you tell me the difference between traditional RDS and Aurora?
- How does Aurora handle automatic backups?
- Have you worked on AppConfig?
- Terraform Questions
- Have you worked on Terraform?
- Say I created an S3 bucket using Terraform and want to modify the bucket name. Is it possible? How would you do this?
- Can you tell me what is Data Block in Terraform?
- How do you handle multiple environments in Terraform?
- What are modules in Terraform?
- GitLab / CI-CD Questions
- Have you worked on GitLab?
- Can you tell me what are rules in GitLab?
- Scripting / Programming Questions
- Which scripting language have you used?
- Can you tell me the difference between single ampersand (&) and double ampersand (&&) in shell scripting?
- What is search keyword in Python?
- What is the difference between shallow copy and deep copy in Python?

## Sony（31 题）

### Sony — DevOps Engineer（31 题）

- How would you respond to a production outage during peak hours?
- So how do you guarantee zero downtime deployments in Kubernetes.
- How do you decide to roll back or apply a hot‑fix when a production issue occurs?
- How would you design a system to survive if one AWS region goes down?
- How would you investigate a sudden three‑times increase in the AWS bill?
- How can you shorten a CI/CD pipeline that currently takes 45 minutes?
- How do you stop broken code from reaching production?
- How do you start troubleshooting when a Kubernetes cluster feels slow?
- How do you guarantee zero‑downtime deployments in Kubernetes?
- What steps do you take when monitoring metrics say the system is healthy but users are still complaining?
- How do you design alerting so that you avoid noisy or false alerts?
- How do you design alerting to avoid alert fatigue?
- I want jenkins run pipeline once n number of commits are pushed how will you do that.
- What are the vulnerability reports in your sonarqube.
- If I want to start an ec2 instance once the cpu is utilised 80% what terraform code will you write and it also should copy the image from S3.
- How will you secure your jenkins pipelines.
- How would you design a Kubernetes cluster that must survive a full AZ failure without data loss, while running stateful workloads at scale?
- (Storage, networking, controllers, quorum, recovery)
- Explain the complete request flow when using Gateway API with multiple GatewayClasses across regions. How do you prevent split-brain routing?
- How do you debug intermittent pod restarts when liveness probes pass, readiness passes, but the pod is still killed by the node?
- What happens internally when etcd latency spikes above 500ms? How does it impact the scheduler, controllers, and API server?
- Design a multi-tenant Kubernetes platform where teams must not affect each other’s resource usage, network traffic, or upgrade cycles.
- How would you implement zero-trust networking inside Kubernetes without using a service mesh?
- Describe a real production incident where a misconfigured HPA caused cascading failure. How would you redesign autoscaling to avoid this?
- How do you safely refactor a Terraform monorepo with hundredsgg of state files into a module-based architecture without downtime?
- Explain how Terraform handles dependency graphs internally. How can circular dependencies still appear in real projects?
- How would you manage Terraform when multiple teams deploy to the same AWS account but must not overwrite each other’s resources?
- Describe a production failure caused by terraform apply. What guardrails would you implement to prevent it permanently?
- Why does a container sometimes exit immediately even though the application works perfectly in local testing? Give 3 real production causes.
- How would you design container images for ultra-fast cold starts in serverless or autoscaled Kubernetes environments?
- How do you design GitOps for 1000+ clusters with environment drift detection, emergency hotfixes, and controlled manual overrides?

## SquareOps（268 题）

### SquareOps — DevOps Engineer（268 题）

- 🏗️ Infrastructure & Architecture
- Q1. Explain the infrastructure and application setup of your last project. How is the application hosted?
- Follow-ups:
- Where exactly is the frontend hosted?
- Where is the backend hosted?
- Where is the database stored?
- Is everything on AWS or multi-cloud?
- What part of the infra do you manage personally?
- What are the microservices doing?
- Why did you choose this architecture?
- ☁️ AWS Cloud Responsibilities
- Q2. What exactly do you do in AWS Cloud in this project?
- Follow-ups:
- Do you manage VPC/subnets/security groups?
- Do you create EC2/EKS/ECS resources?
- Do you manage S3 lifecycle policies?
- Do you handle IAM + RBAC in Kubernetes?
- Do you participate in cost-optimization?
- Q3. On which compute platform are the applications hosted? (Expected: EKS)
- Follow-ups:
- Why EKS over ECS?
- How do you manage worker nodes?
- How many replicas do you run?
- Do you use Cluster Autoscaler / Karpenter?
- ☸️ EKS & Kubernetes
- Q4. Have you created an EKS cluster? Explain the process.
- Follow-ups:
- Did you use console, CLI, or Terraform?
- Which VPC/subnet configuration did you use?
- How did you configure node groups?
- How do you bootstrap kubectl access?
- Q5. Have you upgraded an EKS cluster before? How?
- Follow-ups:
- What risks come with upgrading?
- How do you handle node draining?
- Do deployments get recreated?
- What checks do you perform post-upgrade?
- Q6. If your teammate also wants access to the same cluster through kubectl, what steps do you follow?
- Follow-ups:
- What IAM policy do you attach?
- What is aws-auth ConfigMap?
- Where is aws-auth stored?
- How do you map users and roles?
- Do you provide RoleBinding or ClusterRoleBinding?
- Q7. In which Kubernetes resource do you map IAM users/roles?
- → AWS Auth ConfigMap
- Follow-ups:
- What sections inside it? (mapUsers, mapRoles)
- What mistakes can break authentication?
- ⛵ Helm & Application Deployment
- Q8. Have you worked with Helm and Helm Charts?
- Follow-ups:
- Why use Helm instead of plain YAML?
- Show the folder structure of a Helm chart.
- What is the templates folder?
- What is values.yaml used for?
- How do you manage multiple environments?
- Q9. How do you securely inject sensitive data into Helm?
- Follow-ups:
- Do you use AWS Secrets Manager?
- Do you avoid committing secrets in values.yaml?
- What is Sealed Secrets?
- What is the purpose of --set and --set-file flags?
- Q10. Can a public Helm chart be customized?
- Follow-ups:
- Why is it not recommended to edit the chart directly?
- How do you update config safely?
- What happens during chart upgrades?
- How do you extend a chart with new templates?
- Q11. How do you add extra Kubernetes manifest files to a public Helm chart?
- Follow-ups:
- Where do you put extra YAML files?
- How do you reference new values?
- Can this break the original chart?
- 💾 Kubernetes Storage
- Q12. How to implement shared storage across multiple pods running on multiple nodes in EKS?
- Follow-ups:
- Why EFS over EBS?
- What is the EFS CSI driver?
- What are the access modes?
- How do you mount PVC in deployment?
- Q13. If there is one node but multiple pods, can we use EBS for shared storage?
- Follow-ups:
- What access mode does EBS support?
- Why can't EBS work across multiple nodes?
- When is EFS mandatory?
- 🧠 Kubernetes Reliability & Troubleshooting
- Q14. What is a Pod Disruption Budget (PDB)?
- Follow-ups:
- What is voluntary disruption?
- What is involuntary disruption?
- When do we use minAvailable vs maxUnavailable?
- Q15. What is your approach to debug a CrashLoopBackOff?
- Follow-ups:
- What logs do you check?
- How do you check events?
- How do you inspect liveness/readiness probes?
- How do you check resource limits?
- How do you inspect environment variables and config maps?
- Q16. During peak traffic, ingress controller is routing requests slowly. How do you debug it?
- Follow-ups:
- Check ingress controller logs?
- Check CPU/memory usage?
- Check pod replicas?
- Do you use autoscaling (HPA)?
- Load balancer throttling issues?
- Endpoint misconfigurations?
- Are readiness probes failing?
- Is target response latency high?
- Q17. Should we increase ingress controller replicas permanently or dynamically?
- Follow-ups:
- Why is static scaling bad?
- When to use HPA?
- When to use Cluster Autoscaler?
- ☁️ AWS & Cloud Concepts
- Q18. Why choose EFS over EBS?
- Follow-ups:
- Which one supports multi-node?
- Which one is cheaper?
- Which one is faster?
- Q19. Can EBS be attached to multiple nodes? Why not?
- Follow-ups:
- Explain RWO vs RWX
- Who enforces the mount restriction?
- 🔄 CI/CD
- Q20. What CI/CD tools have you worked with?
- Follow-ups:
- Explain your GitHub Actions pipeline.
- How do you run iOS build automation?
- How do you handle secrets in pipelines?
- How do you deploy to EKS through GitHub Actions?
- Q21. How do you handle multi-environment pipelines?
- Follow-ups:
- Dev → QA → Prod
- Promotion strategy (manual approvals?)
- Git branching strategy?
- Q22. How do you implement rolling deployments?
- Follow-ups:
- What happens to old pods?
- What is maxSurge, maxUnavailable?
- 🧱 Terraform
- Q23. Have you used Terraform?
- Follow-ups:
- Show module structure.
- Show provider file.
- How do you manage remote backend?
- How do you manage state locking?
- What is a data block?
- What is a module block?
- ☁️ AWS Hands-On Services (Round 2)
- Q1. Which AWS services do you have the most hands-on experience with?
- Follow-ups:
- EC2?
- IAM?
- VPC?
- S3?
- RDS?
- CloudWatch?
- Are you confident in these?
- Have you worked on cost optimization?
- 🔐 IAM & Policies
- Q2. Create an EC2 IAM role that allows access only to S3 + DynamoDB and denies access to all other services.
- Follow-ups:
- What is the logic behind a custom policy?
- What is "Explicit Deny"?
- How would you restrict everything except two services?
- Which policy pattern do you use (Allow + NotAction Deny)?
- 💰 Cost Optimization
- Q3. What exact cost optimization steps have you implemented?
- Follow-ups:
- What was the % saving?
- Have you used Reserved Instances or Savings Plans?
- Do you know cost of ALB vs private ALB?
- Which scenario costs more?
- 🔁 ALB Cross-Communication
- Q4. Two apps in same VPC → each behind a public ALB → if App A calls App B, how does traffic flow?
- Follow-ups:
- Does it go out to internet?
- Does it come back through IGW?
- Which option is costlier, public or private ALB?
- What stays inside VPC vs what leaves?
- 📈 Auto Scaling — Memory & Disk
- Q5. How do you create auto scaling policies based on memory & disk usage?
- Follow-ups:
- Are memory and disk metrics available by default?
- Why do we need CloudWatch Agent?
- How do you configure the agent?
- Where do you create CloudWatch alarms?
- Do you need to update Launch Template?
- 🪣 S3 — Lifecycle + Versioning
- Q6. In a versioned bucket, how do you delete objects + all older versions after 10 days?
- Follow-ups:
- What options appear in lifecycle rules?
- Do we explicitly delete previous versions?
- What is the difference between Current vs Previous versions?
- 🧮 RDS Troubleshooting
- Q7. App is slow → you suspect RDS. What do you check?
- Follow-ups:
- CPU? Memory? Latency? IOPS? Connections? Disk queue depth?
- Slow query logs? Error logs? Performance Insights?
- Q8. You found memory pressure on RDS. You cannot resize. What immediate action can you take without downtime?
- Follow-ups:
- Can you kill heavy queries?
- Remove idle connections?
- Create a read replica?
- Which action applies instantly?
- Which action causes 0 downtime?
- 🌐 VPC & Networking
- Q9. Request comes from Internet → enters VPC through IGW → what is the first security layer? NACL or SG?
- Follow-ups:
- Why NACL first?
- Which one is stateless?
- Which one is stateful?
- Which takes precedence if conflict?
- Q10. If NACL denies a CIDR, but SG allows same IP, can the IP access LB?
- Follow-ups:
- Why not?
- Which one checks traffic first?
- How many IPs does /32 allow?
- Does IP X fall in CIDR Y?
- Q11. Does IP 10.11.7.44 fall under 10.11.0.0/16?
- Q12. Does IP 10.11.44.76 fall under 10.1.0.0/16?
- Q13. What does /32 represent?
- Follow-ups:
- How many IPs in /32?
- Which exact IP?
- How to calculate whether an IP is inside a CIDR block?
- ⚙️ CI/CD — Branch-Based & Rollback
- Q14. Repo has 3 branches: dev, staging, prod. How do you ensure pushing to staging triggers only staging deployment?
- Follow-ups:
- Separate pipelines or single pipeline?
- Use of branch conditions?
- Environment variables?
- Webhooks?
- Should pipeline constantly “check” repo?
- What type of Jenkins job is best?
- Q15. Have you ever set up rollback in CI/CD?
- Follow-ups:
- How do you implement automatic rollback?
- What triggers a rollback?
- Is rollback handled by CI/CD or Kubernetes?
- Q16. Have you integrated SonarQube in your CI/CD pipeline?
- Follow-ups:
- How to get Sonar token?
- Where to store token?
- How to insert Sonar scanner stage?
- What is quality gate?
- Q17. If a Jenkins job starts but gets stuck, how do you debug?
- Follow-ups:
- Check console logs?
- Node resources?
- Agent logs?
- External API calls?
- When do you restart agent?
- 🧱 Terraform Advanced
- Q18. Terraform generated RDS password, you didn’t save it. Can you retrieve it?
- Follow-ups:
- Where does Terraform store generated values?
- Local state or remote backend?
- Why is storing secrets in plaintext dangerous?
- Q19. Do you know what a custom Terraform module is?
- Q20. What does a module contain?
- Q21. What is in main.tf?
- Follow-ups:
- variables.tf?
- outputs.tf?
- providers.tf?
- How do you call a module from root module?

## Syncortex（10 题）

### Syncortex — Release Engineer（Exp---5yrs  Release engineer）（10 题）

- Block, release_on in Ansible
- Ansible command to view log during execution
- If you have two different VMs,, how will you modify your playbook for diff requirement?
- Taint and Tolerations
- If you want your developers to use only authorized images, what can we do ?
- How will you investigate POD failure
- How will you implement multi region Terraform code
- What are the parameters are used for HPA in K8s?
- How will take a backup of K8s clusters regularly
- How will you make sure EC2 is not deleted while running destroy command.

## Synechron（56 题）

### Synechron — DevOps Engineer 1（Exp----13 YOE - 5yr DevOps Engineer）（16 题）

- What is azure board, what are the things inside it
- What is pom.xml in maven
- Share your screen - write the structure of azure pipeline
- Share your screen - write simple dockerfile
- How to troubleshoot if pod is failed in AKS, commands please
- What is terraform drift command
- What are the different types of azure storage
- How will you store credentials in azure pipelines
- What are the different types of subscriptions in azure
- How will you implement dc/dr in azure – which are the services you will be using it
- What are the all the issues you had faced in your project, please explain
- Will you register app service first or deploy it
- Have you used any scripting language for automation purpose
- What is azure artifact
- What is self hosted agent and Microsoft host agent
- Docker cmd and entrypoint difference, how to configure sonarqube with azure

### Synechron — DevOps Engineer 2（Exp---- 3yr DevOps Engineer）（21 题）

- Tell me the difference between Docker and Docker Compose ?
- Tell me about  Docker Compose and Kubernetes ?
- Tell me about the ADD and COPY commands ?
- Explain to me Terraform architecture ?
- What is backend ?
- What is the difference between Find and sed ?
- How to find the 10th word  in a file ?
- How to moitor the system performance?
- What is CICD?
- Any challenges have you faced in CI/CD in your team, Tell me about it. How did you overcome this?
- What is Blue Ocean in  Jenkin ?
- How to configure the Flask in Jenkin, tell me procedure ?
- Tell me the difference betweeen Cloud watch and CloudFormation ?
- How  will you create the Custom alerts, tell me the procedure.
- What is ACM and S3 ?
- What is Ansibler galaxy ?
- Tell me Kubernet architecture  ?
- What is SLI and SLO ?
- What is Monkey Patching?
- Have you worked on SRE ?
- Tell me the difference betweeen DEVOPS and SRE ?

### Synechron — DevOps Engineer 3（Exp--4 year）（19 题）

- Client -Morgan Stanley,
- All the questions are scenario-based and counter questions. - I have remembered these question , all the counter questions into CICD related and Kubernets.
- Can you explain what CI/CD is and describe how you have implemented CI/CD pipelines in one of your projects?
- How does an AWS CodePipeline differ from a Jenkins pipeline? Can you give an example of when you would choose one over the other?
- How do you configure your CI/CD pipelines? Can you walk me through the steps you followed to set up a pipeline in a recent project?
- If you need to deploy an application to both cloud environments and on-premises servers (hybrid environment), how would you design and configure your pipeline to handle this?
- Where and how do you manage environment variables for your applications in a CI/CD setup?  Can you explain how you write and use them securely?
- After an application is deployed, what post-deployment steps do you typically perform to ensure everything is running smoothly?
- Can you explain how you would deploy a Kubernetes application using Jenkins? What plugins or tools would you use?
- What is the difference between git pull and git clone?
- Can you describe the difference between git pull and git fetch? When would you use one instead of the other?
- What is git pull vs. git fetch? What is git merge?
- Suppose you have two commits. How would you check the differences between them?
- What are Prometheus and Grafana? Can you explain it ?
- How do you monitor the health and performance of your Kubernetes pods in a production environment?
- What is Helm, and why do you prefer to use it for managing Kubernetes applications instead of deploying them normally?
- Can you describe the main components of a Kubernetes cluster and explain the role each one plays?
- If you want to use the feature branch instead of the main branch, how will you design the CICD?
- If any issue occurred in PIPELINE, who handled the issues, and how do the troubleshoot?

## TCS（69 题）

### TCS — DevOps Engineer 1（Exp -9 yrs devops rel-4yrs）（13 题）

- What is jfrog artifactory
- what is ansible tower
- what is nagios , how to integerate jenknins in nagios
- what is ansible tower
- what is ansible roles
- what is jinja2 template
- what is jfrog xray
- what is jfrog uses cases
- how to find the mount point space of linux
- what are the ansible modules you have used
- diff between github repo and jfrog
- what is branching stargery
- what is differnet type repo in jfrog

### TCS — DevOps Engineer 2（Exp-- 4-5 yrs (DEVOPS)）（16 题）

- what is role in ansible
- how do you encrypt in ansible
- what is idempotent in ansible
- what is module in ansible
- what is libraries in python
- what are deployment group in azure devops
- how wl you set approvals in pipeline
- difference between microsoft hosted agent and self hosted agent
- what is the difference between monolithic and microservices
- explain did u done any automation in your project
- pls explain the flow how the pipeline will trigger across different environments
- if developer is working on a code, what are all the next steps he has to do for running the pipeline along wd dgoogle translate english to hindievops engineer
- what are all the deployment startgies you use in deployments in k8s , explain canary and blue green strategies
- what is devsecops  , did you use any tools for scanning image etc
- what is the difference between classic pipeline and yml
- tell me pipeline steps for angular or java or .net

### TCS — SRE 1（EXP--->）（28 题）

- What is an Ansible Playbook?
- What is an Ansible Role?
- What is Ansible Tower?
- What is the difference between PV and PVC in Kubernetes?
- What is ConfigMap and Scheduler in Kubernetes?
- Explain your current e-commerce project and its architecture.
- What types of nodes did you deploy on AWS?
- What is the difference between Interface Endpoint and Gateway Endpoint in AWS?
- What does idempotent mean in Ansible?
- How does Kubernetes work — how do the master and worker nodes communicate, and what runs inside them?
- What is CrashLoopBackOff, and how do you troubleshoot it?
- Why does a pod show a “Pending” status in Kubernetes?
- If a rollback fails, how will you handle it?
- What is the command for rolling back to a specific revision in Kubernetes?
- What is a PVC in Kubernetes?
- How does Ansible work?
- What is an Ansible Role, and how do you create it?
- When you run a module like yum or apt and get “command not found,” what’s the reason?
- What is a Terraform state file interpreter?
- What to do if a terraform apply takes too much time?
- How to assign and print a variable in Bash?
- What are Lists and Tuples in Python?
- How do you restrict access to AWS resources for a specific user?
- How do you restrict a user to only EC2 and RDS access?
- When you create a VPC, what default components are added?
- What is an Ansible Role, and how do you create it?
- Explain the AWS architecture shown in the diagram (CodePipeline, CodeBuild, CodeDeploy, CloudFormation, CloudWatch).
- Do you have experience with operating systems — Windows or Linux? What types of file permissions exist in Linux?

### TCS — SRE 2（EXP--->）（12 题）

- Gemini company interview questions
- What is Terraform drift?
- Difference between COPY and ADD commands in a Dockerfile.
- If a Docker image becomes very large with many layers, what steps would you take to reduce its size?
- If you have 10 layers in a Dockerfile and layer 6 fails, after fixing it, where will the rebuild start from and why?
- Difference between bind mounts and volumes in Docker.
- Why do we need a StatefulSet when we can attach a PVC to a Deployment and make it stateful?
- If a pod is created with a Deployment and another with a StatefulSet, will the StatefulSet pod always remain on the same node?
- If we can run MySQL with a Deployment and PVC, why do we need a StatefulSet?
- What happens if we scale a Deployment with one PVC from 1 to 3 replicas?
- What types of services exist in Kubernetes, apart from ClusterIP, NodePort, and LoadBalancer?
- Why does a pod created from a Deployment have two sets of random characters in its name?

## Techdome（7 题）

### Techdome — DevOps Engineer（7 题）

- Kubernetes architecture
- Deployment vs stateful set
- Explain Docker networking and types of network. What is the default network.
- Terraform provisioners.
- Terraform statefile
- Docker image vs container
- Docker bind mount vs volume

## Turning（9 题）

### Turning — Cloud Engineer（Exp---> Cloud Engineer）（9 题）

- Failover happend in DB, so connection is switched from A to B, during this time interval, if user is writing some data, how to manage that ?
- Lamdba cold start
- AWS CDK commands
- How to implement TF in CD pipeline
- 10 developers are checking in code in GIT, I want to remove the code checkin done by developer 10, how to do that ?
- If someone manually changed the EC2 config, which was created through TF, how to fix it ?
- I've payment gateway app running in Lambda, sometimes there was an issue with connecting to external API, how to cross check and fix it while performing the payment
- Purpose of Blue Green deployment and how will you switch back to diff deployments ?
- Write a script to check if the external API is reachable before starting the request.

## UST（14 题）

### UST — Cloud Platform Engineer（EXP-3-5 yrs）（14 题）

- If something is created on the cloud platform and it is not present in Terraform, how will you achieve it?
- Terraform apply is creating all the resources again. What can be the possible problem?
- How can AI assist us in cloud infrastructure monitoring?
- How can AI assist developers in increasing their productivity?
- If a Python program is failing due to memory issues, what can be the cause?
- If a CI pipeline is taking 45 minutes to run, how can you optimize it?
- Write Terraform code to create an AWS EC2 instance and include variables for instance_type and region.
- You need to create 50 instances in one go. How will you create them in Terraform?
- If somebody has deleted the Terraform state file locally, what can be done?
- If a production instance is failing, what can be the possible causes?
- In a disaster recovery scenario, what will you do if users are not able to access the application?
- If there is a sudden spike in traffic on the server, how will you troubleshoot it?
- If credentials are visible in CI/CD pipeline logs, what will you do?
- Explain Blue-Green deployment.

## Verizon（28 题）

### Verizon — DevOps Engineer（Exp---3 years）（28 题）

- what are the disadvantages of each deployment models in k8s
- In k8s architecture which component is not running as pod
- k8s QOS (quality of service)
- disadvantage of using ebs volumes in eks
- Any reason why we cannot place our app pods in master node by default
- requests and limits in k8s
- How will u ensure docker container security while writing docker file
- how many clusters u have in ur project and how many pods in nodes
- what version of k8s u used and did u perform any cluster upgrade
- how you switch between clusters tell me the command
- what is context in k8s
- Etcd is sql or no sql database and reason
- init container and sidecar container
- liveness and readiness probes
- what is OOM and how to resolve OOM issue
- linux - hardlink vs softlink
- linux-  Cronjob
- AWS secret manager vs parameter store
- docker run command -p represents port or publish
- linux is OS or kernel
- linux file hierarchy
- Other ways to connect EC2 without pem key
- Horizontal and vertical scaling RDS db steps
- Db RDS multiavailability vs read replicas
- how to delete old/untaged images in ECR
- Types of variables in linux
- linux - kill vs kill -9 and total number of signals in linux
- How to check linux process without use of ps or top command

## Virtusa（19 题）

### Virtusa — Tech Lead（Exp---> Tech lead）（19 题）

- difference between deployement and replicaset and daoemonset and statefulset (what key words you will be writing over the, for ex : deployement.yml – rolling update, canary)
- what is chart.yml file contains in K8
- what files will be present in helm chart
- what you will declare in values.yml etc
- what is node affinity and pod affinity  in K8
- what is taint and tolerations in K8
- what is the terraform command for unlock statefile
- what is module in terraform
- suppose there are multiple ec2 instances manually created via console, I have to update those ec2 instances via terraform, what is the command
- write python program for reverse a string
- what is list and tuple in python
- difference between entrypoint and cmd in docker
- what is the difference between copy and run command in docker
- suppose you are having an ecs task definition, I have an website , the developer is hitting the url or website, what will be the flow of traffic , fargate is a serverless – how do you achieve configuration DNS or website over there
- what is task definition in ecs
- image is there docker, I want to build an image, deploy to docker hub, tag it - commands in docker please
- am having some min max pods running, suppose on festival day traffic increases at that time I have to increase pods, when no traffic is there I have reduce the pods, how will you achieve it in K8
- difference between cloud formation and terraform
- what is the difference between ecs and fargate

## Volkswagen Group Digital（12 题）

### Volkswagen Group Digital — DevOps Engineer（YOE-->）（12 题）

- ==
- Looking for both DevOps (70%) and development (30%).
- How do you onboard a new project from code to release management with multiple environments like prod, QA, Dev.
- how do you automate all the steps in the CI and CD with lots of tools?
- how do you run security checks in docker image?
- what are all production issues that you faced in k8s?
- how do you write CI/CD pipelines?
- what was the recent script that you wrote?
- explain a CI/CD process that you worked on with all the steps?
- what all azure services do you use?
- what services  do you want to learn in azure DevOps apart from this?
- what is the rest API? (As it requires development knowledge as wel

## Wikreate Media（6 题）

### Wikreate Media — DevOps Engineer（6 题）

- Use of Route53
- Git stash
- Difference between S3 and EBS
- difference between git fetch and git pull
- What is the difference between vertical and horizontal scaling?
- What is the role of continuous integration?

## Wipro（76 题）

### Wipro — DevOps Engineer 1（13 题）

- What is your day to day activity
- If there is file which is being used by 2 customers, and need to deploy that file in k8s cluster and on prem as well, how to do that?
- What is the issue with using large file image in dockerfile
- How to deploy an app to k8s cluster in terms of app deploy only ( basically explain CD part)
- If secret is stored in vault inside a pod and that pod is down then how to tsg
- How azure key vault is integrated in cicd
- What to do if an application is down
- Scenario based includes 3 sub-questions
- a) If any service is down for more than 2 weeks and customer is asking for update, what will you tell to customer?
- b) How to troubleshoot the issue and what will be checked during the process
- c) what steps to take so that the issue will not happen in future
- Contents written inside docker file
- Contents written inside deployment.yaml or heml chart

### Wipro — DevOps Engineer 2（Exp--->7 years，Role ---> Devops）（18 题）

- Could you elaborate your experience with automating and optimizing the deployment over large infrastructure using AWS and other tools like Terraform and Ansible from your previous roles?
- How about your experience developing CI/CD pipeline and utilizing tools such as Docker, Grafana and Prometheous. Share a particular project where these skills were critical.
- When dealing with multi tenant applications, how do you enforce tenant isolation at the API layer?
- If clients reporting 504 Gateway Timeout errors. describe your approach to debugging the issue?
- how would you implement optimistic locking a RESTful update endpoint to avoid lost updates?
- if you were required to run pre-task checks, main tasks and post-task validation for patch automation, how would you structure your RedHat Automation & Virtulization scripts?
- Can you describe an approach to automating secure decommissioning of VMs, including data shredding.
- If you were required to maintain clarity in very large Ansible Inventories, what best practices should be followed when naming groups and hosts.
- Describe the structure and advantage of using an Ansible role to manage a three-tier web application. what do you mean by three-tier web application?
- if you have custom plugins that multiple roles depends on, how do you manage them in the context of Ansible Roles Management?
- What is Cloud-agnostic strategies? how do you leverage conditionals to make a role cloud-agnostic, particularly for environments like AWS, Azure and GCP.
- How do you mitigate the risk of misscommunication when there are multi-lingual stakeholders involved in email threads?
- How would you structure a multi-stage pipeline that builds, tests and deploys a containerized application to kubernetes using Github Actions.
- How would you parameterize a workflow so that downstream jobs know which environment to deploy to?
- Describe the security implications of using Kubernetes secret in etcd without encryption?
- How does Python's GIL affect multi-threaded web service performance and what alternatives exist to overcome it? what is Python's GIL affect multi-threaded web service?
- How would you implement feature toggles in Deployment pipelines?
- How would you schedule a task to run every 15 minutes in windows using powershell and linux with cron?

### Wipro — DevOps Engineer 3（Exp--->4 years，Role ---> Devops）（11 题）

- If you have a monolith application and need to convert it to microservices, what prerequisites would you ask from the development and tech teams before starting the work?
- When designing a microservices-oriented infrastructure, what technologies and components (like load balancer, service mesh, Kubernetes) would you bring in, and how would you design the estate?
- When you have many services in a service mesh, how do you decide the number of control planes and data planes needed?
- What security measures and policies should be put in place when using a service mesh?
- Since some features of service mesh are also available through other tools, is it worth adding the burden of installing Istio service mesh into the estate?
- How do you handle the service discovery phase when moving from a monolith to microservices?
- If you have a Kubernetes cluster with pods running, but when you hit the URL you get HTTP errors (403, 404, 503), what would be your troubleshooting steps?
- In your 4-year career, what is the biggest achievement you are most satisfied with?
- Do career achievements always need to be big and complex, or can they also be simple improvements?
- Is a service mesh always needed, or are alternative tools sometimes enough?
- MiscImp Qst -:

### Wipro — DevOps Engineer 4（YOE-->4 yr）（17 题）

- They were mainly looking for terraform and Aws experience
- What commands you know in terraform
- ⁠how do you manage state file
- ⁠explain the process how do you get request to create cloud resource s
- ⁠did you come across a scenario where you used terraform destroy
- ⁠explain you cicd pipeline
- ⁠explain your terraform modules
- ⁠what are policies you used for cicd pipeline
- ⁠diff between GitHub actions and Argo cd
- ⁠diff bet Nat gateway and igw
- ⁠explain your roles and responsibilities
- ⁠Types of alerts in dynatrace
- ⁠did you install one agent in your applications
- ⁠explain command to use s3 native lock
- ⁠different types of modules and why it’s used
- ⁠what is route table
- ⁠where does route table is placed (private subnet of private subnet)

### Wipro — DevOps Engineer 5（EXP-9 yrs）（17 题）

- Can you brief your self and your project and responsibilities
- Application on AWS EC2 behind the loadbalancer suddenly unavailable, how do you troubleshoot
- AWS billing increased suddenly, how do you identify the costs
- A developer asking Ec2 instance for his local deployment, how you will achieve and what type of instance you create and give it to them.
- In kubernetes a pod is going to crashloopbackoff, how do you troubleshoot.
- Kubernetes deployment done successfully but unable to access the application externally, how do you troubleshoot.
- When kubernetes node fails what will happen.
- In pod configuration what we should do from Production perspective
- What is Git and why we are using it and what is branching strategy
- How do you write in yaml to create a ci/cd pipeline from scratch to test and deploy from Dev to UAT
- what is maven and explain about repositories
- I have a senerio to deploy an application on 100 servers using Ansible, how do you perform it.
- Docker containers stopped suddenly after starting, how do you troubleshoot
- Jenkins pipeline deployment failed in production but working in Dev, how do you troubleshoot and fix the issues.
- What is argocd and why we are using it
- what is Gitops
- In AWS how do you configure subdomains (like godady/bigrock)

## ZS Associates（27 题）

### ZS Associates — DevOps Engineer（YOE-->6 yr）（27 题）

- Multi stage docker build. In which scenarios it would be useful. Is is suitable for compile based language?
- Layer caching, explain with an example
- Privileged mode in Docker. Explain with an example
- Design an architecture for the scenario: if I type www.application.com it should get resolved to the backend service
- Calico and VPC CNI plugin difference. Why one is preferred over other. How would they help in setting up networking for pod.
- How is an ip address allocate to a pod. Does CNI plugin use same CIDR range which is provided by VPC or different?
- Two pods which are part of same replica set are not able to communicate with each other what may be the reason
- How to handle the extra traffic coming onto pods? Which solution you can implement
- After implementing HPA also some pods are in pending state. What maybe the reason
- How would you provision karpenter. What all things are needed in configuration
- Can you deploy mongo db database in EKS cluster. If yes how and what all configuration things you would need to keep in mind
- There are 3 backend pods in 3 different region. If one pod goes down how would the request be managed
- Suppose we configured a load balancer but it’s not accepting HTTPS request what would you do?
- Without installing certificate how would you divert the traffic coming from http to https
- How would karpenter know which node to provision. How would it get to know about resource constraints
- Possible reasons for pod to be stuck in Crashloopbackoff
- A backend pod needs to interact with S3 and lambda. How would you achieve it
- How would the service account know which role to assume. What all things you would need to configure in the service account
- Ingress, Gateway API
- A replica set has 3 pods. One pod is not coming up. What maybe be the reason
- Argo CD. How do you manage CI/CD in your organisation. How many EKS clusters you manage, no of nodes
- How do you implement state locking in terraform
- For each in terraform. Explain with an example
- If you want to deploy EC2 instances in 3 different region what would the terraform code structure look like
- questions on modules
- I have made some changes in the module for one resource, the resource should get updated but it should not get destroyed and recreated again when we do terraform apply. How would you approach
- Want to create a module for EKS cluster. What would be the structure

## Zensar（19 题）

### Zensar — DevOps Engineer（Exp-:6+ years）（19 题）

- What is service connection/connection string
- How to set alerts in azure monitor (explain steps and configuration that u do)
- Types of vnet peering
- What is DR
- What types of pipeline you use. How many types of pipeline are there
- What is variable in pipeline
- If we have to run multiple jobs parallely using a single pipeline, can it be done? How?
- What is agent?
- Diff between replica set and deployment
- Diff between stateless and stateful application
- How configmap and secrets can be used in k8s
- If control plane goes down what will happen to worker plane?
- What is etcd and its use
- How to create app registration
- What is docker networking
- Why k8s is need if docker volume is there? (Dont remember exact Q framing but sounded like this)
- If 2 pod are in diff namespace then how can we make them communicate to each other securely?
- What is ingress
- In terms of Cost optimisation which one should we use, Az App gateway or network gateway?

## ZopSmart（22 题）

### ZopSmart — DevOps Engineer（EXP-- 2yrs in devop）（22 题）

- explain cicd pipeline,
- write declarative pipeline in jenkins server
- write docker file and explain those keywords
- what is the command to display running conatiners and stopped containers
- what is the command to use remove docker images and docker containers
- explain ansible and how it is works
- what is ansible playbook
- what do terraform init
- what are the commands do you know in terraform?
- what are the commands do you know in k8s ?
- what is IAM Role
- what is maven life cycle?
- what is VPC Peering?
- you are using jenkins server as open source s/w tool like in aws service which  service is available to implement CICD Pipeline
- what is the differance between EBS and EFS
- what do terraform Terraform plan?
- you are using K8S  Cluster as open source s/w tool like in aws service which  service is available to create K8S Cluster
- write ansible playbook for create docker in the nodes
- how to implement authentication in k8s cluster?
- what are the git commands used in daily task?
- what is the command to use change file permission  linux?
- what is git stash?

## Others（451 题）

### Others — Cloud Administrator senior（YOE-->6 yr）（18 题）

- Senior Cloud Administrator
- If you are implementing HPA for statefulsets if new pod comes the pvc would be empty? How would it be able to serve the request?
- When would prefer on-prem Kubernetes cluster over EKS and vice-versa
- ECR
- Kubernetes architecture in depth. Every component functioning. How would you join a new node to control plane?
- Like kubelet is there any similar agent used to manage the control plane side of things?
- When would you implement HPA and VPA. Give an example
- Node selector, taints tolerations
- Pod is in pending state. Reasons?
- How would you implement security for Kubernetes(both on container side and the infra side using native Kubernetes solutions)
- What is the controller used to manage the self managed worker nodes
- What is karpenter. On which metric does it scale up and down?
- EKS cluster upgrade entire process
- Helm commands, how would you deploy an application via helm. How do you integrate this entire process via CI/CD
- Project specific questions(How would you setup a new environment on AWS, Terraform code provisioning)
- How many clusters are you managing currently, No of addons you have deployed
- Why would you need an application to be deployed as stateful set
- How are you provisioning infra using terraform via CI/CD

### Others — Cloud Engineer（7 题）

- AWS Cloud Engineer role -:
- Explain OSI models
- How do you did cost optimization in AWS?
- Explain on Lambda, CFT, Data Storage, S3 ?
- How do you implement best security policies on AWS?
- What factor motivates you for this role?
- Explain how you did your cloud migration

### Others — DevOps Engineer 1（27 题）

- L1 Questions:
- In Git, explain the push and pull commands.
- What is the use of Git tags?
- What are the different types of branches in Git?
- How do you write an Ansible playbook, and what client requirements do you consider?
- In Python, what are lists and tuples, and how do they differ?
- In CloudWatch, what is the use of log groups and log trails?
- In Terraform, what is the purpose of init, plan, and apply commands?
- What happens if the Terraform state file is accidentally deleted?
- What is the purpose of creating S3 bucket policies?
- How do you maintain the lifecycle of an S3 bucket?
- In Airflow, if a job fails, how do you debug it?
- If you're facing performance issues on a server, how do you troubleshoot?
- 🔥 L2 Questions:
- What are Network ACLs and Security Groups, and how do they differ?
- Explain EC2 instances and handling multiple VPCs.
- How do you configure AWS RDS, and what factors do you consider (size, requirements, etc.)?
- How much data is stored in your RDS MySQL?
- How many masters and slaves are in RDS?
- How do you configure a Grafana dashboard?
- What kind of CI/CD pipelines are you familiar with?
- Explain Declarative vs. Scripting pipelines.
- In Kubernetes, if a pod is in a pending state, how do you troubleshoot?
- If Docker containers are consuming too much disk space, how do you fix it?
- In Linux, how do you attach and detach a filesystem?
- How do you print the last 15 lines of a file in Linux?
- How do you enable passwordless authentication between two servers?

### Others — DevOps Engineer 10（20 题）

- Devops interview questions
- What is docker file what is inside it
- Why K8 instead of docker swam
- Architecture of K8
- What is blue green deployment explain a project based on it
- Why canary and blue green differ
- What happens if etcd stops working
- What are the types of services
- Explain a project in which u used Docker K8 and CICD
- What ci/cd do u use tell us about it in detail
- What wil happen if the docker image has port 8080 and container/application has some port
- Why is load balancer used
- What iare ur git branching strategies
- terraform state file locking
- service vs deployment
- linux commands
- ansible file in writen
- CI-CD pipeline in details
- jenkinsfile stages
- VPC

### Others — DevOps Engineer 11（17 题）

- Self intro
- How to host an S3 static website without enabling public Access
- Difference between secret manager and parameter store
- Why to use Self hosted runner instead of default runner
- What CICD is using in your project for terraform infrastructure.
- Difference between Iam users.. GitHub Oidc role and terraform io role.. which is secured and when to use use GitHub Oidc and when to use terraform io role
- Write a simple docker file
- Write a terraform code to provision an Ec2
- You are having lambda function and role everything setup perfectly but logs are not coming up in the cw group how to troubleshoot?
- When to  use Ec2 and when to use Lambda.. give scenario based answers
- How DRS works.. explain the architecture
- How failover and failback happens in DRS
- How to create a user without an SSH access
- Difference between tf validate and format
- What are provisioners and how to use
- Hi Can anyone explain me best explanation on diffrenec between azure managed identity and service proncipal , how to explain this in tnterview
- how the alert is created with which metrics when cpu and memory goes high in vm, what is action group, how do you create an  alert explain step by step etc, some basic troubleshooting kql queries in log analytics workspace - check on those things, any automation done with scripting etc for monitoring..

### Others — DevOps Engineer 12（Round 1: Technical Discussion (Client, Virtual)，Round 2: Technical Manager Round (Internal, F2F)，Round 3: Technical Round (Client, F2F)，Round 4: Client Reporting Manager (Client, Virtual)）（57 题）

- Total  - 4 Technical Round, 2F2F and 2 Virtual Round.
- Tell me about yourself ?
- What was your roles and responsibilities in your project ?
- Can you explain how you used Python in your projects and what tasks you have done with it ?
- Can you write a Python program to reverse a string ?
- Do you know slicing in Python? If yes, can you slice a string from 0 to 4 ?
- What is the difference between  list and  tuple in Python ?
- Have you ever created your own module in Python? If yes, can you create one own module and print "Hello, World"?
- Can you explain inheritance in Python ?
- Have you ever customized the operating system as per project requirements? If yes, how and  what you customised ?
- Can you write a shell script to take the names of files that are creating in a directory and store into a file ?
- What is the difference between ADD and COPY in a Dockerfile?
- What is the difference between CMD and ENTRYPOINT in a Dockerfile?
- How do you check the server system load ?
- What is the difference between git fetch and git pull?
- What is the difference between git rebase and git merge ?
- Write a shell script that compresses logs older than 30 days and deletes logs older than 90 days. Also, run it daily via cron ?
- What is DNS ?
- Some other questions related to BareMetal Server, Storage(HP, DELL) related.
- How would you optimize AWS resource costs? Can you explain the methods you would use ?
- Create Terraform S3 resources, and ensure that the resource is deleted automatically after 7 days ?
- What is a state file and how do you store it ?
- What is Terraform lifecycle management, and what does it does ?
- Write both Jenkins pipeline syntaxes with examples: Declarative and Scripted pipelines ?
- How you secure secrets and credentials in your CI/CD process ?
- Write an Ansible playbook and explain it ?
- Reverse the words from a given list using Python ?
- Remove the first duplicate element from a list using Python ?
- Can you explain the Kubernetes architecture and its components ?
- What is the difference between Pod and Deployment in Kubernetes ?
- What are the services in Kubernetes have ?
- What would you recommend: NodePort Service or LoadBalancer Service in Kubernetes and why?
- Have you worked on Salt ?
- How you used Ansible in your project and what task you have done ?
- What is ansible roles and can you explain it ?
- What is inventory file in ansible ?
- Have you worked on Ansible  Tower ?
- Can you write a Ansible playbook and explain it ?
- What are modules in Ansible ?, How many modules you have worked on, can you tell the module names ?
- What is the difference between Ansible and  Salt ?
- How do you group hosts in an inventory file, can you explain it ?
- How do you debugg Ansible Playbook ?
- Can you write a docker-file and explain it ?
- How would you expose your application in Docker?
- Suppose you have created a CI/CD process. After building the image, manual intervention is required. How would you configure it, and where ?
- What is IAM and how it works ?
- How did you migrate an application from an on-premise server to AWS?,  Can you explain the process and the method you followed ?
- How do you check the cpu details ?
- how do you check the network details and traffic flows on a system and which command you will use ?
- As you know C++, if you don’t want to store duplicate values, which one you use , list or set and Why ?
- What is Blue-Green Deployment, and what is Canary Deployment? Can you explain the difference between them ?
- How can you create a new copy of an existing Jenkins job ?
- You have a microservices application that needs to scale dynamically based on traffic. How would you design an architecture for this using AWS services ?
- Let's say, A critical production deployment failed and caused downtime. How would you handle the situation ?
- What is the difference between Liveness and Readiness Probes in Kubernetes ?
- What are the challenges you faced in your oranization and how did you overcome with it ?
- Rest questions are formal discussion about me and Reporting Manager ?

### Others — DevOps Engineer 13（44 题）

- What is the difference between import and include in Ansible?
- Can the same Terraform code be used for different cloud providers?
- What is the difference between a Deployment and a StatefulSet in Kubernetes?
- Give a command to find a process and kill it.
- What is MongoDB, and how does it work?
- How does high availability work in MongoDB (primary and secondary nodes)?
- What is artifact management, and which tool do you use in your organization?
- How do you reduce the size of a Docker image?
- Write a Bash script for log analysis.
- How do SSL and TLS certificates work?
- Explain the Maven lifecycle.
- What is the difference between Continuous Delivery and Continuous Deployment, and how do you implement them in Jenkins?
- Write a GitHub/GitLab pipeline to deploy a microservice with 3 services running in parallel.
- Write a Bash script or command to get the total number of lines in a file.
- In a log file, there is a keyword ERR. Give me the count of errors in the file.
- What is runs-on in a pipeline? Which type of runners are you using in your organization, and do you know how to configure self-hosted runners?
- How do you trigger a pipeline if:
- a. Code is pushed to a specific branch?
- b. Ignore if it is pushed to some other branch?
- c. Trigger if a PR is raised?
- What is a base image in a Dockerfile?
- Can we write a Dockerfile without a base image?
- What are decorators in Python?
- What is SonarQube, and why is it used?
- How do you set up a manual trigger in GitHub Actions?
- How do you set up GitHub runners for the application environment?
- Follow-up for Q23: If you are using GitHub Marketplace actions, which are third-party tools, how do you ensure security concerns regarding them?
- What is a matrix in GitHub Actions?
- What is the needs keyword in GitHub Actions?
- Briefly explain the architecture of your current project.
- Write the structure for building and pushing a Docker image for an application in GitHub Actions.
- Round 1: Technical Interview Questions
- See Thread ›
- There are no messages in this thread yet.
- Round 2: Techno-Managerial Interview Questions
- What type of GitHub branching strategy are you using? Please explain.
- How do you run jobs in parallel in GitHub Actions?
- How do you check the integrity of a Docker image or file?
- How do you handle secrets in your project?
- What steps are included in your GitHub Actions workflow file?
- How is static code analysis configured in your pipeline file?
- Which is the optimized method to run SonarQube: for every PR raised or every push?
- What are webhooks, and have you used them anywhere?
- How do you configure a pipeline with AWS or Docker?

### Others — DevOps Engineer 14（10 题）

- k8s node pending state how to debug
- pod is pending state, due to disk issue, how to resolve
- Have u done k8s cluster upgrade
- u r unable to evict the pods from node, how to resolve
- Tell me the flow of network packets starting from user hit the application url
- Suppose during upgrade storage plugin had issue, unable to upgrade, what u will do ? (couldn't answer properly)
- what is pullsecret in Openshift, there were 1 more but forgot
- what is kubernetes operator? If I need to run a shell script before any container to start how can i do it using operator ?
- how do u handle sev-1 issue
- What is the extra component/service present in Managed k8s cluster in cloud

### Others — DevOps Engineer 15（46 题）

- Pod is running fine, all the parameters looks good, but the traffic is not reaching the pod when the user is trying to access the application, what could be the possible reason ?
- Imagepullbackoff, why and when this usually occurs ?
- How do you debug inside the container ?
- if there are multiple pods, how do they identify each other ?
- How the helm charts work ?
- Do you actually use helm for the deployments ?
- Explain the rolling update ?
- If there a deployment failure what the next steps you perform ?
- How do you approach the debug on the deployment failure.
- If any sensitive data needs to passed in the deployment how do you pass it?
- what are secrets ? for what type of applications we may need them?
- your deployment is successful, but when u access the application it says 404 ?
- What are the api errors you have faced ? what is 504 ? 501 ?
- Explain what an api is ?
- some questions went around API and diff between authorization and authentication.
- They they started to evaluate the knowledge on docker
- basic questions like docker build docker file and so on.
- they it shifted towards the shell scripting - I dont really have enough knowledge on shell. My answers were blunt, and they moved on from it.
- Explain about observability stack
- New image has been deployed in production but it fails immediately what steps would you take ?
- Pod to pod communication
- Ingress vs ingress controllers
- Cost optimization strategies that you followed in your project
- Trunk based Branching strategy
- What errors you faced when you're working with k8s
- CMD vs entry point
- Pvc is in pending state how do you debug
- If app is responding slow how do you debug and what could be the issue
- How do you provide rds ready only access to developer
- What is NAT gateway?
- Prometheus memory is growing huge how do you debug this
- What if production rds is growing 95% how do you debug and how do you prevent this in future
- Any migration experience
- K8s architecture and argocd  architecture
- Do you have exp with helm?
- How did you manage secrets in your project?
- How can I map SSL certificates to the ingress file ?
- How does service mesh work and any experience?
- What if developer coming to you and saying that remove code quality from the pipeline as it is slow in scanning the code in this scenario what steps would you take?
- What if I have 10 FE micro services and 10 BE micro services how do you design the cicd pipeline using jenkins?
- How do you manage the state file in terraform and where do you store it?
- Write your jenkins pipeline,
- What is the purpose of agent, post-conditions and environment blocks in pipeline,
- How do you perform complete backup up of Jenkins including jobs/configurations/authentications,
- what are the ways to trigger the pipeline in Jenkins,
- I have 5 Jenkin jobs and how would you give view only access to other users.

### Others — DevOps Engineer 16（29 题）

- Difference between build artificats and pipeline artifacts and which one is better
- Elaborate the pipeline steps to move a file from azure blob to gcp cloud storage(automated way)
- Why Dynamic blocks are used in tf and write the skeleton for an azure resource using dynamic block
- How will you refer the output of vnet module based subnetid as an input to the VM module
- If a pipeline is deleted by one of your team member, how would you recreate and how would you prevent this scenario in future
- Difference between stakeholder and admin in azure devops
- How you will build single or minimal reusuable pipeline templates for 50 different applications
- What is the command or pipeline syntax used to refer the variable output of the previous stage in the current stage
- How sensitive data is managed in pipelines
- How the authentication and networking is established between azure devops pipeline and azure keyvault
- How will you provide access to only one pod/app to a storage account and restrict all the other pods within AKS
- Out of 32 GB memory AKS cluster, 30 GB is already utilized, Whether a new pod with request 500mb and resource limit of 4Gi can be scheduled in the same cluster using HPA/VPA
- Which App gateway setting is used to upload SSL certification and why
- What are the alternate ingress controllers you suggest as Nginx IGC is deprecated
- How pipeline logs are stored in azure devops
- he has asked to list the running instances from 5 accounts , I have written it  with sts
- then what you do if ec2 has comprised, I have given the answer of making the permissions as deny all then terminating ec2 if not needed
- what all the types of polices we have in iam
- how do you copy the jobs from one jenkins worker node to another worker node
- how do setup the communication between jenkins and kuberenetes
- how is the connectiivy from on prem to cloud
- how to access s3 from vpc securely
- then cloudformation and terraform differences
- least privileage in cft for the stacks and terraform
- linux"
- file system is 50% however its not able to write and df -ih is shoiwng full
- what is zombie process
- so list the usrs who  has not accessed the keys in iam for more than 90 days
- delete the inline policy for users where *  is mentioned in the iam users list

### Others — DevOps Engineer 2（12 题）

- Whats ur organisation current cicd process and tools
- How comfortable with AWS and how much rate urself out of 5?
- about IAM/Fargate/EC2/Lambda?
- Can u pls write a lambda file?
- About K8's Architecture and tell me the workflow?
- Can u pls write terraform file to provision the Ec2 instance in a public subnet in a VPC?
- R u using Dockerfile? u r build the dockerfile by codebuild?
- How many containers can run in a pod?
- in ur projects how many containers u ran? can u give me the use case where can run 4-5 containers in a pod?
- did u configure Prometheus and Grafana?
- What securities measures/tools u were taken in ur cicd pipeline?
- about RBAC

### Others — DevOps Engineer 3（14 题）

- ) How many NAT Gateways are needed for two public & two private subnets n a single VPC? Min & max?
- ) Explain TTL in DNS- how does it work, and when do we use it? Explain the Flow.
- ) How does weighted routing work in LB?
- ) How Docker is operable on a Linux machine? Explain the docker architecture components
- ) There are 1 Master & 3 Worker nodes- if the master fails, what happens? Will pods keep running or they will crash?
- ) In K8s, as etcd is a key-value store db, can write something manually on it?
- ) How to roll back a failed deployment in Docker & K8s?
- ) How does SSL work (Certbot, Let's Encrypt, AWS)? Explain the Flow.
- ) What are the top 5 infra attacks, and how do you mitigate them?
- ) If the tfstate file is lost, what do you do? With & without backup?
- ) In Linux systems there is the term Load Average? what does that mean? how it is being calculated? and in what format the load average output is?
- ) One of your worker nodes is not joining the cluster. How would you debug the issue?
- There were More Scenario Questions Related to "Load Balancers",
- "Route 53", and "EKS and DB Automation and Administration"

### Others — DevOps Engineer 4（36 题）

- how you ensure the best possible security for high availability architectures for 3 tier applications.
- Diff b/w SGs and NACLs.
- what is VPC peering.
- How do you scan the vulnerabilities specially for AWS instances.
- diff between IAM Users and Roles
- Can you avoid the specific port traffic using SGs?
- How you connect to private instances when the SSH connection is not working?
- where do you use firewalls, SGs and NACLs
- What are the best password security practices used by your organisation?
- What are the security parameters we must consider while we are creating an EC2 instance for production?
- How can you protect the data in an AWS instance?
- How can you connect from AWS to on-prem servers?
- Explain about the transit gateway and why do we use this?
- What are the provisioners available in Terraform and can you explain the use cases?
- I have created an EC2 instance named A, and I want to create another instance B. It should create an instance without deleting instance A. What can I do during this?
- I have created an EC2 instance through Terraform. I don't have a backup of the Terraform state file, it is not in the remote state and locally not available. Now when I do apply, what can I do?
- Suppose I have given one command in null resource, it should run every time. What is the behavior?
- What is the difference between a map of objects in Terraform and how can you write an example?
- Suppose in your DevOps team, new team members are added to your team. How can you provide AWS access to your new users, what is the behavior of login to the console?
- What is the difference between an EBS-backed instance and a non-EBS-backed instance?
- I have 3 nodes (small, medium, and large), and I want only data load to go to the large node. How can I do that?
- When I deploy the pods, it should be deployed on large and medium. Nodes, except small. How can I configure that?
- I am getting the following error, how can I debug that and what does the error mean?
- Pods fail to schedule
- 0/5 nodes are available: insufficient memory.
- What is the difference between scaling and autoscaling in Kubernetes?
- If I don't specify TargetPort in the service object, what is it going to do?
- What are the different types of secrets in Kubernetes?
- I have an Ingress object that is not routing the traffic to the Kubernetes cluster. What are the reasons and how do you troubleshoot that?
- I have created a service object that is not mapped to a deployment. What could be the reason and how do you debug it?
- What are the different ways to specify the probes in Kubernetes?
- What is the difference between git push --force-with-lease vs --force?
- If I select the restart policy as Never, what is it going to do?
- What is an init container and why do we need to use it?
- What is the difference between EKS vs ECS vs Fargate?
- How can you delete the last 2 git commits?

### Others — DevOps Engineer 5（18 题）

- What will happen if the k8 master node and worker node firewall gets broken? Will the existing deployments work or impact on any new deploymentsHow will you communicate to people
- How to use the secrets in kubernetes? What encryption methods do you use?
- How does the GSLB load balancer work?
- What is SLI, SLO, SLA
- How can you create the extensions in Grafana
- How does the ELK setup has been done and what type of agents have you collected
- Can you tell one scenario where you have done the RCA wrt linux
- You have the JSON data could you please let me know how would you ingest and collect the data in the keys format.
- Can you design the Istio Setup for your k8 cluster?
- AWS event bridge creation and setup via terraform
- What will be the command to add the annotation and the labels for the existing pod?
- Design the kubernetes cluster with Ingress.
- A sudden surge in traffic causes a web application to become unresponsive what will be the steps you will take to mitigate
- Design the deployment of the pod with replica set set as 3 and having apache httpd image running as a container.
- How do you reduce the size of Dockerfile
- Write a shell script to find and delete all files in a directory that are older than 30 days.
- Create a script to monitor the disk usage of a server. If usage exceeds 80%, log the details to a file and send an alert email.
- Write a script that renames all .txt files in a directory by appending the current date to the filename.

### Others — DevOps Engineer 6（21 题）

- What is the difference between NSG and Firewall.
- What is the difference between COPY and ADD command in Docker File.
- What is Taint/Tolerent.
- What is stateful set.
- Architecture of Kubernetes.
- Use case of Node-Port and Cluster IP service Type in Kubernetes.
- Explain GITHUB Action workflow file.
- Difference between entry point and CMD in Docker File.
- Can we connect two different VM that are in a different Vnet.
- Private Endpoints.
- Express route in Azure Cloud.
- What is PDB in Kubernetes.
- Difference between PV/PVC in Kubernetes.
- What is state file in Terraform.
- What is lock file in Terraform.
- Why Kube-let and Kube-proxy is used for in Kubernetes.
- How you can build an Image and push it to the ACR.
- How you can use the existing Image into the YAML file to deploy a POD.
- What is POD in Kubernetes.
- Types of Service in Kubernetes.
- Namespaces in Kubernetes.

### Others — DevOps Engineer 7（20 题）

- Introduction
- Whats ur organisation current cicd process and tools
- What do u know about Cyberark and what and how u r consuming that in ur pipeline
- Which scriting language u r aware? and how much confident on that?
- What are the services u were used in AWS
- If U want to design a infra for high scalablity, how did u do that?
- What are NACLs,SecurityGroups,NAT Gateway
- About Kubernetes architecture
- diff b/w Replicaset and Deployment
- About Ansible,Terraform
- About ConfigMaps,PV,PVCs
- write a Deployment file
- Write a Docker File
- About multistage Docker file
- Which type of Jenkins File u r using? Can u pls Write a Jenkins File?
- What is the toughest situation u r faced while implementing anything and what did u learnt from that?
- U handled any debug/troubleshoot for kubernetes?
- About Prometheus/Grafana
- About Fargate
- What is lambda functions? did u used any Lambda functions? what did u acheived from that?

### Others — DevOps Engineer 8（20 题）

- From one of the linkedin post >
- interview experience happened yesterday (08-02-2025).
- Write a Terraform code to create multiple S3 buckets
- How you managed statefile
- So how are you managing the conflict? State file conflicts
- what you did with Jenkins?
- How are you integrating the SonarQube with the Jenkins server?
- How were you authenticating Jenkins to push docker image to registery?
- Have you worked on the Kubernetes?So what deployment strategy are you following?
- So how are you implementing the blue green deployment?
- Do you know what is HPA?
- suppose you deploy one application okay and you found some issue, you wanted to roll back using the kubernetes how you roll back to the particular version, what is the command?
- What is the stateful set in the Kubernetes?
- Have you worked on the AWS, right?
- So how many types of policy, IAM policy are there? IAM policies?
- So what is the difference between the S3 bucket policies and acls?
- what is the dynamic auto scaling?
- What is the difference between Security groups and NACL?
- Two AWS accounts are there in same organisation. Account A has Ec2 instance and Account B has some tokens.  Need to access the tokens from Ec2 instance.
- How can achieve the requirement?

### Others — DevOps Engineer 9（12 题）

- /var partition is 90% full. What’s your immediate action?
- You’re locked out via SSH with no root access. How do you recover?
- Add 50GB to /opt using LVM without any downtime. What are the steps?
- Jenkins is failing to push a Docker image to the registry. How do you troubleshoot?
- Ansible playbook times out on one host out of twenty. What do you check?
- EC2 instance is unreachable, and it’s not a security group issue. What’s your next step?
- An S3 bucket was made public by mistake. How do you secure and audit it?
- RDS migration with minimal downtime – how would you approach it?
- CI/CD pipeline needs rollback capability. How would you implement it?
- Write a shell script that checks if a service is running, restarts it if not, and logs the event.
- Terraform script to provision an EC2 instance with a custom security group and user data script.
- Design a highly available backend on AWS – what services and architecture would you use?

### Others — DevOps Engineer behavioral（15 题）

- Tell me about a time you handled a failed deployment in production. How did you manage the team and stakeholders?,
- How do you ensure smooth collaboration between development and operations teams in a high-pressure situation?,
- Describe a scenario where you had to introduce a new DevOps tool or practice. How did you get team buy-in?,
- How do you prioritize and manage multiple critical issues in a CI/CD pipeline failure?,
- Tell me about a conflict you faced within your DevOps or cross-functional team. How did you resolve it?,
- Explain a situation where you were responsible for reducing deployment time. What approach did you take?,
- Have you ever dealt with a security vulnerability in your DevOps pipeline? How did you detect and respond to it?,
- Describe how you handled a rollback situation during a major release. What went wrong, and what did you learn?,
- How do you approach communicating technical issues to non-technical stakeholders or management?,
- Can you share an experience where your automation strategy failed or caused problems? What was your corrective action?,
- You are asked to reduce infrastructure cost without compromising performance. How do you approach this challenge?,
- How do you ensure accountability and ownership in a DevOps team, especially during failures?,
- Describe a time when you had to work under tight deadlines. How did you manage team workload and expectations?,
- How do you mentor or support junior DevOps engineers in your team while ensuring timely project delivery?,
- Tell me about a successful DevOps transformation project you were part of. What was your role, and how did you drive change?

### Others — SRE（8 题）

- SRE role -:
- Commands used for Kubernetes,Docker and Ansible..
- Explain Kubernetes Structure, Config Map and Schedular..
- How do you troubleshoot Imagepull backoff error ?
- Explain installation of prometheus and grafana..
- Explain how you build CICD pipeline..
- How we monitor cpu matrics in grafana?
- How do you grant access to user?

---

## 与 modules 的映射（按题目主题）

| 题目主题 | 对应 modules 模块 |
|---|---|
| Kubernetes（Pod / 探针 / 滚动更新 / 排障 / RBAC / 网络） | `kubernetes`（另见 `collections/k8s-web-archive.md`、`collections/k8s-local-library.md`） |
| Docker / 镜像构建 / 多阶段构建 | `kubernetes`（容器基础） |
| Terraform / Ansible / IaC 状态与安全门禁 | `cicd-iac` |
| Jenkins / GitHub Actions / Azure DevOps / GitLab CI 流水线 | `cicd-iac` |
| AWS / Azure / GCP（VPC / IAM / S3 / EKS / AKS / 多区域 / 成本） | `cloud-security` |
| Linux / Shell / Python 脚本题 | `linux` |
| 网络（子网 / NAT / DNS / 负载均衡 / TLS） | `network` |
| Prometheus / Grafana / ELK / EFK | `observability` |
| SLI / SLO / 事故复盘 / 值班 / 容量 | `sre-reliability` |
| 数据库 / Redis / Kafka / 消息队列 | `middleware` |
| 项目经历 / 冲突 / 优先级 / 自我介绍 | `behavior` |
| 系统设计题（三层架构 / 高可用 / 迁移方案） | `system-design` |
