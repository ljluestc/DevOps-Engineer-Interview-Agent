# 高级运维工程师面试题汇总（崔亮 · 收录）

> **来源**：[崔亮的博客 - 高级运维工程师面试题汇总](https://www.cuiliangblog.cn/detail/article/89)
> **收录日期**：2026-08-05
> **背景**：作者 2024 年 7 月初–8 月中旬，面试 20+ 家公司（字节、京东、百度、网易、蚂蚁金服、小米、滴滴、去哪儿、猎豹移动、商汤、旷视、智谱华章、马蜂窝、竞技世界、电信、联通、建行、中石化等），累计 50+ 场，考察面试题 200+ 道。
> **标注**：☆ = 多次出现的高频面试题。
> **版权**：仅收录题目列表（公开网页文本），不含原作者参考答案与付费内容。分组保留原文。

---

## Linux

01. grep sed awk cut组合使用☆
02. http错误码和原因
03. 长连接、短连接、WebSocket区别和使用场景
04. nginx性能优化有哪些方式☆
05. lvs、nginx、haproxy区别和使用场景☆
06. 僵尸进程是什么
07. 进程、线程、协程区别☆
08. 什么是nginx的异步非阻塞
09. linux网络丢包怎么排查☆
10. 常用的性能分析诊断命令☆
11. 什么是进程中断
12. 什么是软中断、硬中断
13. 什么是不可中断进程
14. 什么是栈内存和堆内存
15. top 命令里面可以看到进程哪些状态☆
16. Linux 系统中/proc是做什么的
17. load和cpu使用率区别
18. MAC地址IP地址如何转换
19. 常见的raid有哪些，使用场景是什么
20. lvm怎么划分
21. jvm内存如何查看
22. 如何管理和优化内核参数
23. 什么是进程最大数、最大线程数、进程打开的文件数，怎么调整☆
24. du和df统计不一致原因☆
25. buffers与cached的区别☆
26. lsof命令使用场景
27. Linux中的进程间通信的方式及其使用场景
28. Linux中的进程优先级与设置方法
29. 什么是内存分页和分段
30. 如何创建和管理自定义systemd服务
31. Linux内核模块的加载与卸载过程
32. ansible roles使用场景，现在有多台机器需要批量加入k8s集群，怎么实现☆

## Kubernetes

01. 谈谈你对k8s的理解☆
02. k8s集群架构是什么☆
03. 简述Pod创建过程☆
04. 简述删除一个Pod流程
05. 不同node上的Pod之间的通信过程☆
06. pod创建Pending状态的原因☆
07. deployment和statefulset区别☆
08. kube-proxy有什么作用☆
09. kube-proxy怎么修改ipvs规则
10. ipvs为什么比iptables效率高
11. pod之间访问不通怎么排查☆
12. k8s中Network Policy的实现原理
13. 探针有哪些？探测方法有哪些？
14. pod健康检查失败可能的原因和排查思路
15. k8s的Service是什么☆
16. metrics-server采集指标数据链路
17. k8s服务发现有哪些方式？
18. pod几种常用状态
19. Pod 生命周期的钩子函数
20. Calico和flannel区别☆
21. calico网络原理、组网方式
22. Network Policy使用场景
23. kubectl exec 实现的原理
24. cgroup中限制CPU的方式有哪些
25. kubeconfig存放内容
26. pod DNS解析流程☆
27. traefik对比nginx ingress优点
28. Harbor有哪些组件
29. Harbor高可用怎么实现
30. ETCD调优
31. 假设k8s集群规模上千，需要注意的问题有哪些？
32. 节点NotReady可能的原因？会导致哪些问题？☆
33. service和endpoints是如何关联的？
34. ReplicaSet、Deployment功能是怎么实现的？
35. scheduler调度流程
36. HPA怎么实现的☆
37. request limit底层是怎么限制的☆
38. helm工作原理是什么？
39. helm chart rollback实现过程是什么？
40. velero备份与恢复流程是什么
41. docker网络模式
42. docker和container区别☆
43. 如何减小dockerfile生成镜像体积？
44. k8s日志采集方案
45. Pause容器的用途☆
46. k8s证书过期怎么更新
47. K8S QoS等级☆
48. k8s节点维护注意事项
49. Headless Service和ClusterIP区别☆
50. Linux容器技术的基础原理
51. Kubernetes Pod的常见调度方式
52. kubernetes Ingress原理☆
53. Kubernetes各模块如何与API Server通信
54. kubelet监控worker节点如何实现
55. 容器时区不一致如何解决？

## Prometheus

01. Prometheus的工作流程
02. Metric的几种类型？分别是什么？☆
03. Prometheus有哪几种服务发现☆
04. Prometheus常用函数
05. thanos架构☆
06. thanos与VictoriaMetrics对比
07. thanos sidecar和receive区别☆
08. thanos rule组件和prometheus区别
09. Prometheus告警从触发到收到通知延迟在哪
10. 告警抑制怎么做☆
11. 告警架构高可用怎么做☆
12. Pod指标WSS和RSS区别☆
13. 监控四个黄金指标
14. 在大规模环境下，如何优化Prometheus性能
15. 如何实现告警的自动化响应☆
16. Prometheus数据压缩和持久化实现原理
17. kubectl top输出与Linux free命令不一致原因☆
18. 用到了哪些exporter，功能是什么
19. 是否自己开发过exporter☆
20. target down的情况如何进行故障排除？
21. Exporter 停止工作，如何监控？
22. Prometheus的拉取模式与zabbix推送模式有何区别？各有什么优缺点？
23. Prometheus operator怎么添加targets和告警规则
24. k8s集群外exporter怎么使用Prometheus监控

## ELK

01. ES写入索引原理
02. ES存储原理☆
03. 搜索文档（单个文档）流程
04. ES全文搜索流程
05. ES写入性能优化☆
06. ES查询性能优化☆
07. ES JVM使用过高如何排查
08. ES的Fleet server架构☆
09. Fleet server架构和elk架构使用场景☆
10. ClickHouse、loki、ES的优劣对比
11. ES架构☆
12. 业务类ES和日志类ES架构设计区别
13. ES Full Gc怎么排查处理
14. 全文检索和精确搜索区别☆
15. 集群变黄状态时，你会如何进行故障排除☆
16. 如何在集群中添加或移除节点
17. ES Young GC和old GC有什么区别
18. 怎么提高查询结果评分
19. ES的version是解决什么问题的
20. 查询数据慢如何排查优化☆
21. 是否对ES JVM做过调优
22. ES是否数据越多需要内存越大
23. ES集群数据备份如何实现☆
24. ES聚合有哪些方式
25. Filebeat如何保证连续发送日志
26. Logstash如何提升性能☆
27. 如何提高Filebeat性能
28. Filebeat如何收集容器日志

## Devops

01. gitlab runner做了哪些优化
02. 怎么实现多集群逐个发布
03. 蓝绿部署、灰度发布、金丝雀发布区别☆
04. 什么是测试左移？（Shift-Left testing）
05. 什么是GitOps
06. GitOps和DevOps区别☆
07. gitlab仓库代码如何备份
08. Jenkins 构建失败时，你如何排查问题☆
09. Jenkins用户权限管理怎么做的
10. Jenkins pipeline有几种模式，区别是什么？
11. 如何配置 Jenkins 实现高可用性
12. Jenkins Master和Slave是如何协同工作的
13. 如何设计和实现一个 Jenkins Pipeline，以支持多阶段构建、测试和部署流程
14. Argo Rollouts蓝绿部署和金丝雀发布原理☆
15. Argo CD中的 Application CRD是什么
16. Argo CD中自动同步（Auto-sync）和手动同步的区别与应用场景
17. Argo CD检测到应用状态异常，你会如何进行故障排除
18. Argo CD如何配置自定义的健康检查规则
19. Argo CD检测到配置与实际状态不一致时如何处理这些差异
20. CICD流程如何监控?
21. 平时开发项目时git开发功能分支标准流程是什么?
22. git分支冲突怎么解决?

## Python VUE

01. Python中的 GIL是什么？它如何影响多线程？☆
02. python装饰器☆
03. is 和 == 的区别☆
04. Python中的生成器和迭代器有什么区别
05. Python的垃圾回收机制是如何工作的
06. Python上下文管理器的概念及其用途。
07. dict的内部实现原理
08. python浅拷贝和深拷贝☆
09. lambda匿名函数使用场景举例
10. 常见设计模式
11. python单例模式
12. 面向对象中__new__和__init__区别☆
13. Python中的列表和字典是如何实现的？它们在时间复杂度上有何差异？
14. Python中的多线程模块的区别☆
15. asyncio编写异步代码
16. django请求的生命周期☆
17. JWT认证
18. 什么是wsgi，uwsgi
19. Django安全防护
20. drf继承过哪些视图类，他们之间的区别☆
21. 谈谈django flask fastapi各自的优劣和适用场景。
22. python定时任务解决方案☆
23. 在 Celery 中，如何确保任务的可靠性和持久性
24. 如何监控 Celery 任务的执行情况
25. 当 Celery 任务出现阻塞或延迟时，你如何进行故障排除？
26. VUE双向数据绑定
27. VUE实例的生命周期钩子函数有哪些☆
28. v-if与v-show区别☆
29. cookie和seesion区别☆
30. VUE父子组件如何通信
31. nextTick 使用场景
32. ref和reactive区别
33. 你有写过VUE自定义指令吗？
34. 排序算法☆
35. 查找算法☆
36. SSO单点登录实现原理☆

## 开放性问题

01. 谈谈你对SRE理念的理解☆
02. 什么是可观测性
03. 你们当前的业务规模☆
04. 运维过程中遇到的最大的故障是什么？怎么解决的？☆
05. 有没有人为误操作导致故障，如何处理的？☆
06. 平时怎么去学习新的技术☆
07. 最近工作中做过最有意义的事☆
08. 最近研究的技术方向是什么
09. 运维上线流程规范
10. 运维体系建设包含哪些方面☆
11. 故障事件管控怎么设计
12. 告警覆盖率和准确率怎么衡量☆
13. 如何建设运维保障体系
14. 运维给公司带来的价值是什么
15. 运维和其他团队的职能边界和合作模式是什么
16. 运维的发展方向是什么☆
17. 运维的工作重点是什么
18. 运维的工作效率如何提升
19. 是否做过故障总结，包含哪些内容
20. 如何看待自动化操作高效性和人工操作确认安全性的问题
21. 如何看待运维维稳和开发求新的问题☆
22. 如何看待追求更多的可靠性和成本的平衡问题
23. 如何看待追求稳定性和新技术方案实践的问题
24. 如何看待运维工作中的重复性、没有持续价值的工作☆
25. 如何避免告警通知频繁导致成为告警噪声☆
26. 是否关注过资源使用率，考虑降低成本☆
27. CMDB数据库怎么设计
28. SLO是多少，运维自动化率多少
29. 与上级意见不一致怎么办
30. 你的优点和缺点分别是什么？
31. 与其他候选人相比，你的核心竞争力是什么？
32. 部分用户访问服务首页白屏超时，分析服务请求过程和可能的原因
33. 线上一个服务响应很慢，你如何排查，排查流程是什么?
34. 你们的告警监控体系怎么设计的？
