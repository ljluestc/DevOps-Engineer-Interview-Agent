# 中级运维工程师面试题汇总（崔亮 · 收录）

> **来源**：[崔亮的博客 - 中级运维工程师面试题汇总(含答案)](https://www.cuiliangblog.cn/detail/article/2)
> **收录日期**：2026-08-05
> **背景**：作者 2020 年发布的中级运维面试题，含答案（但**仅收录题目列表**，不收录作者发布在原文中的详细答案）。
> **版权**：仅收录题目列表（公开网页文本），不含原作者答案。分组保留原文。

---

## Linux（19题）

1. linux系统启动流程
2. linux文件类型
3. centos6和7怎么将源码安装的程序添加到开机自启动？
4. 简述lvm，如何给使用lvm的/分区扩容？
5. 为何du和df统计结果不一致？
6. 如何升级内核？
7. nginx日志访问量前十的ip怎么统计？
8. 如何删除/var/log/下.log结尾的30天前的日志？
9. ansible有哪些模块？功能是什么？
10. nginx为什么比apache快？
11. 四层负载和七层负载区别是什么？
12. lvs有哪些工作模式？哪个性能高？
13. lvs nginx haproxy keeplived区别，优缺点？
14. 如下url地址，各个部分的含义
15. tomcat各个目录含义，如何修改端口，如何修改内存数？
16. nginx反向代理时，如何使后端获取真正的访问来源ip？
17. nginx负载均衡算法有哪些？
18. 如何进行压力测试？
19. curl命令如何发送https请求？如何查看response头信息？如何发送get和post表单信息？

## MySQL（11题）

1. 索引的为什么使查询加快？有啥缺点？
2. sql语句左外连接 右外连接 内连接 全连接区别
3. mysql数据备份方式，如何恢复？你们的备份策略是什么？
4. 如何配置数据库主从同步，实际工作中是否遇到数据不一致问题？如何解决？
5. mysql约束有哪些？
6. 二进制日志（binlog）用途？
7. mysql数据引擎有哪些？
8. 如何查询mysql数据库存放路径？
9. mysql数据库文件后缀名有哪些？用途什么？
10. 如何修改数据库用户的密码？
11. 如何修改用户权限？如何查看？

## NoSQL（5题）

1. redis数据持久化有哪些方式？
2. redis集群方案有哪些？
3. redis如何进行数据备份与恢复？
4. MongoDB如何进行数据备份？
5. kafka为何比redis rabbitmq快？

## Docker（11题）

1. dockerfile有哪些关键字？用途是什么？
2. 如何减小dockerfile生成镜像体积？
3. dockerfile中CMD与ENTRYPOINT区别是什么？
4. dockerfile中COPY和ADD区别是什么？
5. docker的cs架构组件有哪些？
6. docker网络类型有哪些？
7. 如何配置docker远程访问？
8. docker核心namespace CGroups 联合文件系统功能是什么？
9. 命令相关：导入导出镜像，进入容器，设置重启容器策略，查看镜像环境变量，查看容器占用资源
10. 构建镜像有哪些方式？
11. docker和vmware虚拟化区别？

## Kubernetes（18题）

1. k8s的集群组件有哪些？功能是什么？
2. kubectl命令相关：如何修改副本数，如何滚动更新和回滚，如何查看pod的详细信息，如何进入pod交互？
3. etcd数据如何备份？
4. k8s控制器有哪些？
5. 哪些是集群级别的资源？
6. pod状态有哪些？
7. pod创建过程是什么？
8. pod重启策略有哪些？
9. 资源探针有哪些？
10. requests和limits用途是什么？
11. kubeconfig文件包含什么内容，用途是什么？
12. RBAC中role和clusterrole区别，rolebinding和 clusterrolebinding区别？
13. ipvs为啥比iptables效率高？
14. sc pv pvc用途，容器挂载存储整个流程是什么？
15. nginx ingress的原理本质是什么？
16. 描述不同node上的Pod之间的通信流程
17. k8s集群节点需要关机维护，需要怎么操作
18. Calico和flannel区别

## Prometheus（6题）

1. prometheus对比zabbix有哪些优势？
2. prometheus组件有哪些，功能是什么？
3. 指标类型有哪些？
4. 在应对上千节点监控时，如何保障性能
5. 简述从添加节点监控到grafana成图的整个流程
6. 在工作中用到了哪些exporter

## ELK（4题）

1. Elasticsearch的数据如何备份与恢复？
2. 你们项目中使用的logstash过滤器插件是什么？实现哪些功能？
3. 是否用到了filebeat的内置module？用了哪些？
4. elasticsearch分片副本是什么？你们配置的参数是多少？

## 运维开发（9题）

1. 备份系统中所有容器镜像
2. 编写脚本，定时备份某个库，然后压缩，发送异机
3. 批量获取所有主机的系统信息
4. django的mtv模式流程
5. python如何导出、导入环境依赖包
6. python创建，进入，退出，查看虚拟环境
7. flask和django区别，应用场景
8. 列举常用的git命令
9. git gitlab jenkins的CICD流程如何配置

## 日常工作（4题）

1. 在日常工作中遇到了什么棘手的问题，如何排查
2. 日常故障处理流程
3. 修改线上业务配置文件流程
4. 业务pv多少？集群规模多少？怎么保障业务高可用？

## 开放性问题（2题）

1. 你认为初级运维工程师和高级运维工程师的区别？
2. 你认为未来运维发展方向
