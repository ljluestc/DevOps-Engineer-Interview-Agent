# linux运维工程师面试题总结（崔亮 · 收录）

> **来源**：[崔亮的博客 - linux运维工程师面试题总结](https://www.cuiliangblog.cn/detail/article/1)
> **收录日期**：2026-08-05
> **背景**：作者 2020 年 11 月发布，面试 IBM、新浪、完美世界等公司，方向为 Linux、容器运维、自动化运维。
> **版权**：仅收录题目列表（公开网页文本），不含原作者答案。分组保留原文。
>
> ⚠️ **与 `cuiliang-mid-ops-interview-2020.md`（article/2）高度重合**：Linux、MySQL、NoSQL、Docker、K8s、Prometheus、ELK、运维开发、日常工作、开放性 10 个大类几乎完全重复。仅 **ELK 第 4 题（kibana 自定义图表）** 与 **运维开发第 9 题（flask hello world）** 为本篇独有。收录本篇主要为完整性存档，智能体出题时以 article/2（中级）为主。

---

## 一、linux（17题）

01. 系统启动流程
02. linux文件类型
03. centos6和7怎么添加程序开机自启动？
04. 如何升级内核，目前最新版本号多少？
05. nginx日志访问量前十的ip怎么统计？
06. 删除/var/log/下.log结尾的30天前的日志文件
07. ansible有哪些模块？功能是什么？
08. nginx性能为什么比apache高？
09. 四层负载和七层负载区别是什么？
10. lvs有哪些工作模式？哪个性能高？
11. lvs nginx haproxy keeplived区别，优缺点？
12. 如下url地址，各个部分的含义 https://www.baidu.com/s?word=123&ie=utf-8
13. tomcat各个目录含义，如何修改端口，如何修改内存数？
14. nginx反向代理时，如何使后端获取真正的访问来源ip？
15. nginx负载均衡算法有哪些？
16. 如何进行压力测试？
17. curl命令如何发送https请求？如何查看response头信息？如何发送get和post表单信息？

## 二、mysql（11题）

01. 索引的为什么使查询加快？有啥缺点？
02. sql语句左外连接 右外连接 内连接 全连接区别
03. mysql数据备份方式，如何恢复？你们的备份策略是什么？
04. 如何配置数据库主从同步，实际工作中是否遇到数据不一致问题？如何解决？
05. mysql约束有哪些？
06. 二进制日志（binlog）用途？
07. mysql数据引擎有哪些？
08. 如何查询mysql数据库存放路径？
09. mysql数据库文件后缀名有哪些？用途什么？
10. 如何修改数据库用户的密码？
11. 如何修改用户权限？如何查看？

## 三、nosql（5题）

1. redis数据持久化有哪些方式？
2. redis集群方案有哪些？
3. redis如何进行数据备份与恢复？
4. MongoDB如何进行数据备份？
5. kafka为何比redis rabbitmq快？

## 四、docker（11题）

01. dockerfile有哪些关键字？用途是什么？
02. 如何减小dockerfile生成镜像体积？
03. dockerfile中CMD与ENTRYPOINT区别是什么？
04. dockerfile中COPY和ADD区别是什么？
05. docker的cs架构组件有哪些？
06. docker网络类型有哪些？
07. 如何配置docker远程访问？
08. docker核心namespace CGroups 联合文件系统功能是什么？
09. 命令相关：导入导出镜像，进入容器，设置重启容器策略，查看镜像环境变量，查看容器占用资源
10. 构建镜像有哪些方式？
11. docker和vmware虚拟化区别？

## 五、kubernetes（17题）

01. k8s的集群组件有哪些？功能是什么？
02. kubectl命令相关：如何修改副本数，如何滚动更新和回滚，如何查看pod的详细信息，如何进入pod交互？
03. etcd数据如何备份？
04. k8s控制器有哪些？
05. 哪些是集群级别的资源？
06. pod状态有哪些？
07. pod创建过程是什么？
08. pod重启策略有哪些？
09. 资源探针有哪些？
10. requests和limits用途是什么？
11. kubeconfig文件包含什么内容，用途是什么？
12. RBAC中role和clusterrole区别，rolebinding和 clusterrolebinding区别？
13. ipvs为啥比iptables效率高？
14. sc pv pvc用途，容器挂载存储整个流程是什么？
15. nginx ingress的原理本质是什么？
16. 网络类型，描述不同node上的Pod之间的通信流程
17. k8s集群节点需要关机维护，需要怎么操作

## 六、prometheus（7题）

1. prometheus对比zabbix有哪些优势？
2. prometheus组件有哪些，功能是什么？
3. 指标类型有哪些？
4. 在应对上千节点监控时，如何保障性能
5. 简述从添加节点监控到grafana成图的整个流程
6. 在工作中用到了哪些exporter

## 七、ELK（5题）

1. Elasticsearch的数据如何备份与恢复？
2. 你们项目中使用的logstash过滤器插件是什么？实现哪些功能？
3. 是否用到了filebeat的内置module？用了哪些？
4. kibana如何自定义图表和仪表盘？  ← **本篇独有**
5. elasticsearch分片副本是什么？你们配置的参数是多少？

## 八、运维开发（11题）

01. 备份系统中所有镜像
02. 编写脚本，定时备份某个库，然后压缩，发送异机
03. 批量获取所有主机的系统信息
04. django的mtv模式流程
05. python如何导出、导入环境依赖包
06. python创建，进入，退出，查看虚拟环境
07. flask和django区别，应用场景
08. flask开发一个hello word页面流程  ← **本篇独有**
09. 列举常用的git命令
10. git gitlab jenkins的CICD流程如何配置

## 九、日常工作（5题）

1. 在日常工作中遇到了什么棘手的问题，如何排查
2. 日常故障处理流程
3. 修改线上业务配置文件流程
4. 业务pv多少？集群规模多少？怎么保障业务高可用？

## 十、开放性问题（2题）

1. 你认为初级运维工程师和高级运维工程师的区别？
2. 你认为未来运维发展方向
