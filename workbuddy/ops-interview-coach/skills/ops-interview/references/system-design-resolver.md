# 系统设计主题解析器（resolver）——候选人说什么都能接上

> **自动生成，请勿手改** —— 由 `scripts/build_system_design_catalog.py` 生成，`scripts/verify_system_design.py` 校验。配套目录见 [system-design-catalog.md](system-design-catalog.md)。
>
> 语料是长年累积的，同一个主题最多有 **7** 种拼法，还有几个目录本身是错别字。本文件把 **597** 个可出题目录折叠成 **455** 个主题，并给出 **181** 条别名（含 78 条中文）。

## 智能体解析顺序（照这个顺序做，不要跳步）

1. **别名表**：把候选人的说法（去掉「设计 / design / 一个 / a」等词、忽略大小写与连字符）在下面两张别名表里查——命中即得到规范主题目录。
2. **目录名精确匹配**：再到 [catalog](system-design-catalog.md) 里按目录名查；命中后用「重复主题」表把它折叠到规范目录（变体目录里的 `06-quiz.md` 也值得读，常有不同的追问）。
3. **关键词模糊匹配**：用标题与一句话摘要在 catalog 里搜关键词（英文 + 中文都试）。
4. **都没命中**：**照样开面**——用 `system-design-questions.md` 的 Q1–Q4 方法论驱动（需求澄清 → 估算 → 高层设计 → 深挖 → 权衡与可运维性），并**明确告诉候选人语料里没有这个主题**，不要假装在读某份文档。
5. **AWS 岗位**：若候选人面的是 AWS / 云岗，再叠加 [collections/aws-managed-services-only.md](../../collections/aws-managed-services-only.md)（195 题，其中 131–195 是 11 个经典题的 AWS-only 渲染）作为「同一道题只用托管服务怎么答」的追问层。

## 一、别名 → 规范主题（英文 / 品牌 / 口语说法）

| 候选人可能说 | 规范主题目录 |
|---|---|
| `adclick` | [`ad-click-aggregator`](../../system-design/ad-click-aggregator/) |
| `adsclick` | [`ad-click-aggregator`](../../system-design/ad-click-aggregator/) |
| `airbnb` | [`rental-search-ranking`](../../system-design/rental-search-ranking/) |
| `airtag` | [`airtag`](../../system-design/airtag/) |
| `alexa` | [`alexa`](../../system-design/alexa/) |
| `autocomplete` | [`typeahead`](../../system-design/typeahead/) |
| `bitly` | [`url-shortener`](../../system-design/url-shortener/) |
| `blobstore` | [`blob-store`](../../system-design/blob-store/) |
| `booking` | [`hotel-booking-system`](../../system-design/hotel-booking-system/) |
| `cdn` | [`cdn`](../../system-design/cdn/) |
| `chatgpt` | [`chatgpt`](../../system-design/chatgpt/) |
| `collaborativeeditor` | [`google-docs`](../../system-design/google-docs/) |
| `craigslist` | [`craigslist-system`](../../system-design/craigslist-system/) |
| `cronjob` | [`distributed-job-scheduler`](../../system-design/distributed-job-scheduler/) |
| `didi` | [`uber`](../../system-design/uber/) |
| `discord` | [`messaging-system`](../../system-design/messaging-system/) |
| `distributedlock` | [`distributed-locking`](../../system-design/distributed-locking/) |
| `dns` | [`dns`](../../system-design/dns/) |
| `doordash` | [`doordash`](../../system-design/doordash/) |
| `douyin` | [`tiktok`](../../system-design/tiktok/) |
| `dropbox` | [`dropbox`](../../system-design/dropbox/) |
| `facebook` | [`fb-news-feed`](../../system-design/fb-news-feed/) |
| `facebookmessenger` | [`facebook-messenger-system`](../../system-design/facebook-messenger-system/) |
| `featureflag` | [`app`](../../system-design/app/) |
| `figma` | [`google-docs`](../../system-design/google-docs/) |
| `flashsale` | [`ticketmaster`](../../system-design/ticketmaster/) |
| `gmail` | [`email-service`](../../system-design/email-service/) |
| `googledocs` | [`google-docs`](../../system-design/google-docs/) |
| `googledrive` | [`file-storage-service`](../../system-design/file-storage-service/) |
| `googlemaps` | [`google-maps`](../../system-design/google-maps/) |
| `idgenerator` | [`unique-id-generator`](../../system-design/unique-id-generator/) |
| `instagram` | [`instagram`](../../system-design/instagram/) |
| `jobscheduler` | [`distributed-job-scheduler`](../../system-design/distributed-job-scheduler/) |
| `kafka` | [`distributed-message-queue`](../../system-design/distributed-message-queue/) |
| `keyvaluestore` | [`key-value-store`](../../system-design/key-value-store/) |
| `kvstore` | [`key-value-store`](../../system-design/key-value-store/) |
| `leaderboard` | [`dream11-leaderboard`](../../system-design/dream11-leaderboard/) |
| `leetcode` | [`leetcode-online-judge`](../../system-design/leetcode-online-judge/) |
| `linkedin` | [`linkedin-feed-ranking`](../../system-design/linkedin-feed-ranking/) |
| `livecomments` | [`fb-live-comments`](../../system-design/fb-live-comments/) |
| `llmserving` | [`inference-optimization`](../../system-design/inference-optimization/) |
| `loadbalancer` | [`loadbalancer`](../../system-design/loadbalancer/) |
| `logsearch` | [`distributed-logging`](../../system-design/distributed-logging/) |
| `lyft` | [`uber`](../../system-design/uber/) |
| `maps` | [`google-maps`](../../system-design/google-maps/) |
| `meituan` | [`food-delivery`](../../system-design/food-delivery/) |
| `messagequeue` | [`distributed-message-queue`](../../system-design/distributed-message-queue/) |
| `messenger` | [`facebook-messenger-system`](../../system-design/facebook-messenger-system/) |
| `metrics` | [`metrics-monitoring-hello-interview`](../../system-design/metrics-monitoring-hello-interview/) |
| `monitor` | [`monitoring`](../../system-design/monitoring/) |
| `nearbyfriends` | [`yelp`](../../system-design/yelp/) |
| `netflix` | [`video-streaming`](../../system-design/video-streaming/) |
| `notion` | [`google-docs`](../../system-design/google-docs/) |
| `objectstore` | [`object-storage`](../../system-design/object-storage/) |
| `onedrive` | [`file-storage-service`](../../system-design/file-storage-service/) |
| `onlinejudge` | [`online-judge-system`](../../system-design/online-judge-system/) |
| `pastebin` | [`pastebin`](../../system-design/pastebin/) |
| `paypal` | [`payment`](../../system-design/payment/) |
| `proximityservice` | [`yelp`](../../system-design/yelp/) |
| `pubsub` | [`pubsub`](../../system-design/pubsub/) |
| `quora` | [`quora`](../../system-design/quora/) |
| `rag` | [`RAG`](../../system-design/RAG/) |
| `ratelimiter` | [`rate-limiter`](../../system-design/rate-limiter/) |
| `reddit` | [`newsfeed`](../../system-design/newsfeed/) |
| `robinhood` | [`robinhood`](../../system-design/robinhood/) |
| `s3` | [`s3-like-storage`](../../system-design/s3-like-storage/) |
| `searchautocomplete` | [`typeahead`](../../system-design/typeahead/) |
| `searchengine` | [`distributed-search`](../../system-design/distributed-search/) |
| `searchsuggestion` | [`typeahead`](../../system-design/typeahead/) |
| `seckill` | [`ticketmaster`](../../system-design/ticketmaster/) |
| `sequencer` | [`unique-id-generator`](../../system-design/unique-id-generator/) |
| `sessionstore` | [`session-management-system`](../../system-design/session-management-system/) |
| `shorturl` | [`url-shortener`](../../system-design/url-shortener/) |
| `slack` | [`messaging-system`](../../system-design/messaging-system/) |
| `snowflake` | [`unique-id-generator`](../../system-design/unique-id-generator/) |
| `spotify` | [`spotify`](../../system-design/spotify/) |
| `strava` | [`strava`](../../system-design/strava/) |
| `stripe` | [`payment`](../../system-design/payment/) |
| `taskscheduler` | [`distributed-job-scheduler`](../../system-design/distributed-job-scheduler/) |
| `telegram` | [`messaging-system`](../../system-design/messaging-system/) |
| `throttling` | [`rate-limiter`](../../system-design/rate-limiter/) |
| `ticketmaster` | [`ticketmaster`](../../system-design/ticketmaster/) |
| `tiktok` | [`tiktok`](../../system-design/tiktok/) |
| `timeseries` | [`time-series-database`](../../system-design/time-series-database/) |
| `tinder` | [`tinder`](../../system-design/tinder/) |
| `tinyurl` | [`url-shortener`](../../system-design/url-shortener/) |
| `topk` | [`topk`](../../system-design/topk/) |
| `tracing` | [`observability`](../../system-design/observability/) |
| `trending` | [`trending-topic-system`](../../system-design/trending-topic-system/) |
| `tsdb` | [`time-series-database`](../../system-design/time-series-database/) |
| `twitch` | [`twitch`](../../system-design/twitch/) |
| `twitter` | [`twitter`](../../system-design/twitter/) |
| `uber` | [`uber`](../../system-design/uber/) |
| `ubereats` | [`uber-eats-system`](../../system-design/uber-eats-system/) |
| `vectordb` | [`vectordb`](../../system-design/vectordb/) |
| `venmo` | [`payment`](../../system-design/payment/) |
| `videoconferencing` | [`live-streaming-platform`](../../system-design/live-streaming-platform/) |
| `webcrawler` | [`webcrawler`](../../system-design/webcrawler/) |
| `whatsapp` | [`whatsapp`](../../system-design/whatsapp/) |
| `x` | [`twitter`](../../system-design/twitter/) |
| `yelp` | [`yelp`](../../system-design/yelp/) |
| `youtube` | [`youtube`](../../system-design/youtube/) |
| `zoom` | [`live-streaming-platform`](../../system-design/live-streaming-platform/) |

## 二、别名 → 规范主题（中文）

> 中文候选人直接说中文题名；这张表让 `switch system-design 秒杀` 能用。

| 中文说法 | 规范主题目录 |
|---|---|
| 一致性 | [`consistency-models-guide`](../../system-design/consistency-models-guide/) |
| 云盘 | [`file-storage-service`](../../system-design/file-storage-service/) |
| 令牌桶 | [`rate-limiter`](../../system-design/rate-limiter/) |
| 任务调度 | [`distributed-job-scheduler`](../../system-design/distributed-job-scheduler/) |
| 会议室预订 | [`conference-room-booking`](../../system-design/conference-room-booking/) |
| 会话管理 | [`session-management-system`](../../system-design/session-management-system/) |
| 信息流 | [`newsfeed`](../../system-design/newsfeed/) |
| 分布式id | [`unique-id-generator`](../../system-design/unique-id-generator/) |
| 分布式缓存 | [`distributed-cache`](../../system-design/distributed-cache/) |
| 分布式锁 | [`distributed-locking`](../../system-design/distributed-locking/) |
| 协同文档 | [`google-docs`](../../system-design/google-docs/) |
| 即时通讯 | [`messaging-system`](../../system-design/messaging-system/) |
| 发号器 | [`unique-id-generator`](../../system-design/unique-id-generator/) |
| 发布订阅 | [`pubsub`](../../system-design/pubsub/) |
| 可观测性 | [`observability`](../../system-design/observability/) |
| 向量检索 | [`vectordb`](../../system-design/vectordb/) |
| 唯一id | [`unique-id-generator`](../../system-design/unique-id-generator/) |
| 在线文档 | [`google-docs`](../../system-design/google-docs/) |
| 地图 | [`google-maps`](../../system-design/google-maps/) |
| 外卖 | [`food-delivery`](../../system-design/food-delivery/) |
| 大模型推理 | [`inference-optimization`](../../system-design/inference-optimization/) |
| 定时任务 | [`distributed-job-scheduler`](../../system-design/distributed-job-scheduler/) |
| 容灾 | [`disaster-recovery-system`](../../system-design/disaster-recovery-system/) |
| 容量估算 | [`back-of-envelope`](../../system-design/back-of-envelope/) |
| 对象存储 | [`object-storage`](../../system-design/object-storage/) |
| 广告点击 | [`ad-click-aggregator`](../../system-design/ad-click-aggregator/) |
| 库存 | [`ticketmaster`](../../system-design/ticketmaster/) |
| 弹幕 | [`fb-live-comments`](../../system-design/fb-live-comments/) |
| 打车 | [`uber`](../../system-design/uber/) |
| 抢票 | [`ticketmaster`](../../system-design/ticketmaster/) |
| 排行榜 | [`dream11-leaderboard`](../../system-design/dream11-leaderboard/) |
| 推荐系统 | [`recommendation`](../../system-design/recommendation/) |
| 推送 | [`notification-system`](../../system-design/notification-system/) |
| 搜索 | [`distributed-search`](../../system-design/distributed-search/) |
| 搜索提示 | [`typeahead`](../../system-design/typeahead/) |
| 支付 | [`payment`](../../system-design/payment/) |
| 数仓 | [`big-data-pipeline`](../../system-design/big-data-pipeline/) |
| 数据管道 | [`data-pipeline`](../../system-design/data-pipeline/) |
| 文件同步 | [`file-storage-service`](../../system-design/file-storage-service/) |
| 新闻推荐 | [`news-feed-aggregator`](../../system-design/news-feed-aggregator/) |
| 日志 | [`distributed-logging`](../../system-design/distributed-logging/) |
| 时序数据库 | [`time-series-database`](../../system-design/time-series-database/) |
| 朋友圈 | [`newsfeed`](../../system-design/newsfeed/) |
| 权限 | [`rbac`](../../system-design/rbac/) |
| 消息队列 | [`distributed-message-queue`](../../system-design/distributed-message-queue/) |
| 灾备 | [`disaster-recovery-system`](../../system-design/disaster-recovery-system/) |
| 点赞评论 | [`fb-live-comments`](../../system-design/fb-live-comments/) |
| 热门话题 | [`trending-topic-system`](../../system-design/trending-topic-system/) |
| 爬虫 | [`webcrawler`](../../system-design/webcrawler/) |
| 电商 | [`e-commerce`](../../system-design/e-commerce/) |
| 监控 | [`monitoring`](../../system-design/monitoring/) |
| 直播 | [`live-streaming-platform`](../../system-design/live-streaming-platform/) |
| 短网址 | [`url-shortener`](../../system-design/url-shortener/) |
| 短视频 | [`tiktok`](../../system-design/tiktok/) |
| 短链 | [`url-shortener`](../../system-design/url-shortener/) |
| 短链接 | [`url-shortener`](../../system-design/url-shortener/) |
| 票务 | [`ticketmaster`](../../system-design/ticketmaster/) |
| 秒杀 | [`ticketmaster`](../../system-design/ticketmaster/) |
| 秒级估算 | [`back-of-envelope`](../../system-design/back-of-envelope/) |
| 缓存 | [`distributed-cache`](../../system-design/distributed-cache/) |
| 网关 | [`api-gateway`](../../system-design/api-gateway/) |
| 网盘 | [`file-storage-service`](../../system-design/file-storage-service/) |
| 网约车 | [`uber`](../../system-design/uber/) |
| 群聊 | [`messaging-system`](../../system-design/messaging-system/) |
| 聊天 | [`messaging-system`](../../system-design/messaging-system/) |
| 自动补全 | [`typeahead`](../../system-design/typeahead/) |
| 视频 | [`video-streaming`](../../system-design/video-streaming/) |
| 订单 | [`e-commerce`](../../system-design/e-commerce/) |
| 训练平台 | [`distributed-genai-training`](../../system-design/distributed-genai-training/) |
| 负载均衡 | [`loadbalancer`](../../system-design/loadbalancer/) |
| 通知 | [`notification-system`](../../system-design/notification-system/) |
| 配送 | [`food-delivery`](../../system-design/food-delivery/) |
| 酒店预订 | [`hotel-booking-system`](../../system-design/hotel-booking-system/) |
| 链路追踪 | [`observability`](../../system-design/observability/) |
| 键值存储 | [`key-value-store`](../../system-design/key-value-store/) |
| 附近的人 | [`yelp`](../../system-design/yelp/) |
| 限流 | [`rate-limiter`](../../system-design/rate-limiter/) |
| 限流器 | [`rate-limiter`](../../system-design/rate-limiter/) |

## 三、重复主题：82 组（同一题的多种拼法）

> 规范目录是文档最全的那个；变体目录**不要当成新题**，但可以借它们的 `06-quiz.md` 做追问。

| 规范主题 | 文档数 | 变体目录（同一题） |
|---|---|---|
| [`url-shortener`](../../system-design/url-shortener/) | 11/11 | `url-shorten` · `url-shortening` · `url-shortener-system` · `url-shortener-design` · `url_shortener` · `url-shortener-educative-tests` |
| [`distributed-cache`](../../system-design/distributed-cache/) | 11/11 | `distributed_cache` · `distributed-cache-system` · `distributed-cache-design` · `distributed-cache-grokking` · `distributed-cache-educative-tests` |
| [`distributed-message-queue`](../../system-design/distributed-message-queue/) | 11/11 | `distributed-messaging-queue` · `distributed-messaging-queue-design` · `distributed-messaging-queue-grokking` · `distributed-messaging-queue-complete` · `distributed-messaging-queue-educative-tests` |
| [`rate-limiter`](../../system-design/rate-limiter/) | 11/11 | `ratelimiter` · `rate-limiter-design` · `rate-limiter-system` · `rate-limiter-system-design` · `rate-limiter-educative-tests` |
| [`loadbalancer`](../../system-design/loadbalancer/) | 11/11 | `load-balancer` · `load-balancer-system` · `load-balancer-tests` · `load-balancer-system-design` |
| [`monitoring`](../../system-design/monitoring/) | 11/11 | `monitor` · `monitoring-system` · `monitoring_system` · `monitoring-system-complete` |
| [`webcrawler`](../../system-design/webcrawler/) | 11/11 | `webcrawlers` · `web-crawler-system` · `web-crawler-tests` · `web-crawler-system-design` |
| [`cdn`](../../system-design/cdn/) | 11/11 | `cdn-system` · `cdn_system` · `cdn-educative-tests` |
| [`chatgpt`](../../system-design/chatgpt/) | 11/11 | `chatgpt-system` · `chatgpt-system-design` · `chatpgt-system-design` |
| [`database`](../../system-design/database/) | 11/11 | `database-demo` · `database-system` · `database-system-design` |
| [`google-docs`](../../system-design/google-docs/) | 11/11 | `google-docs-system` · `google-docs-demo` · `google_docs` |
| [`instagram`](../../system-design/instagram/) | 11/11 | `instagram-system` · `instagram-tests` · `instagram-system-design` |
| [`newsfeed`](../../system-design/newsfeed/) | 11/11 | `newsfeed-system` · `newsfeed-tests` · `newsfeed_system` |
| [`pastebin`](../../system-design/pastebin/) | 11/11 | `paste-bin` · `pastebin-system` · `pastebin-system-design` |
| [`ticketmaster`](../../system-design/ticketmaster/) | 11/11 | `ticketmaster-system` · `ticketmaster-system-design` · `ticketmaster-educative-tests` |
| [`twitter`](../../system-design/twitter/) | 11/11 | `twitter-system` · `twitter-tests` · `twitter-educative-tests` |
| [`typeahead`](../../system-design/typeahead/) | 11/11 | `typehead` · `typeahead-system` · `typeahead-tests` |
| [`whatsapp`](../../system-design/whatsapp/) | 11/11 | `whatsapp-system` · `whatsapp-tests` · `whatsapp-system-design` |
| [`youtube`](../../system-design/youtube/) | 11/11 | `youtube-system` · `youtube-tests` · `youtube-system-design` |
| [`RAG`](../../system-design/RAG/) | 11/11 | `rag` · `rag-system` |
| [`cloud-infrastructure`](../../system-design/cloud-infrastructure/) | 11/11 | `cloud-infrastructure-system` · `cloud-infrastructure-design` |
| [`dns`](../../system-design/dns/) | 11/11 | `dns-system` · `dns_system` |
| [`google-maps`](../../system-design/google-maps/) | 11/11 | `google_maps` · `google-maps-tests` |
| [`interview-prep`](../../system-design/interview-prep/) | 11/11 | `interview-prep-systems` · `system-design-interview-prep` |
| [`key-value-store`](../../system-design/key-value-store/) | 11/11 | `key-value-store-tests` · `key-value-store-design` |
| [`leetcode`](../../system-design/leetcode/) | 11/11 | `design-leetcode` · `leetcode-system-design` |
| [`pubsub`](../../system-design/pubsub/) | 11/11 | `pub-sub-system-design` · `pub-sub-educative-tests` |
| [`quora`](../../system-design/quora/) | 11/11 | `quora-tests` · `quora-system-design` |
| [`spotify`](../../system-design/spotify/) | 11/11 | `spotify-tests` · `spotify-system-design` |
| [`ace-causal-inference`](../../system-design/ace-causal-inference/) | 11/11 | `ace_causal_inference` |
| [`ads-recommendation`](../../system-design/ads-recommendation/) | 11/11 | `ads-recommendation-system` |
| [`agentic-orchestration`](../../system-design/agentic-orchestration/) | 11/11 | `agentic-orchestration-system` |
| [`api`](../../system-design/api/) | 11/11 | `api-design` |
| [`blob-store`](../../system-design/blob-store/) | 11/11 | `blob-store-educative-tests` |
| [`book_subscription`](../../system-design/book_subscription/) | 11/11 | `book_subscription_system` |
| [`client_side_monitoring`](../../system-design/client_side_monitoring/) | 11/11 | `client-side-monitoring-educative-tests` |
| [`code-deployment`](../../system-design/code-deployment/) | 11/11 | `code-deployment-tests` |
| [`conference-room-booking`](../../system-design/conference-room-booking/) | 11/11 | `conference-room-booking-system` |
| [`container-orchestration-system`](../../system-design/container-orchestration-system/) | 11/11 | `container-orchestration-system-design` |
| [`disaster-recovery-system`](../../system-design/disaster-recovery-system/) | 11/11 | `disaster-recovery-system-design` |
| [`disk-scheduling-simulator`](../../system-design/disk-scheduling-simulator/) | 11/11 | `disk_scheduling_simulator` |
| [`distribute-logs`](../../system-design/distribute-logs/) | 11/11 | `distribute-logging` |
| [`distributed-job-scheduler`](../../system-design/distributed-job-scheduler/) | 11/11 | `distributed-job-scheduler-hub` |
| [`distributed-logging`](../../system-design/distributed-logging/) | 11/11 | `distributed-logging-educative-tests` |
| [`distributed-monitoring`](../../system-design/distributed-monitoring/) | 11/11 | `distributed-monitoring-system` |
| [`distributed-search`](../../system-design/distributed-search/) | 11/11 | `distributed-search-system` |
| [`distributed-task-scheduler`](../../system-design/distributed-task-scheduler/) | 11/11 | `distributed-task-scheduler-tests` |
| [`document-retrieval`](../../system-design/document-retrieval/) | 11/11 | `document-retrieval-prototype` |
| [`enterprise-monitoring`](../../system-design/enterprise-monitoring/) | 11/11 | `enterprise_monitoring` |
| [`fault-tolerance-system`](../../system-design/fault-tolerance-system/) | 11/11 | `fault-tolerance-system-design` |
| [`fb-live-comments`](../../system-design/fb-live-comments/) | 11/11 | `fb-live-comments-tests` |
| [`fb-news-feed`](../../system-design/fb-news-feed/) | 11/11 | `fb-news-feed-tests` |
| [`file-storage-system`](../../system-design/file-storage-system/) | 11/11 | `file-storage-system-design` |
| [`food-delivery`](../../system-design/food-delivery/) | 11/11 | `food-delivery-system` |
| [`food-delivery-service`](../../system-design/food-delivery-service/) | 11/11 | `food-delivery-service-v2` |
| [`health-monitoring-system`](../../system-design/health-monitoring-system/) | 11/11 | `health-monitoring-system-v2` |
| [`image-captioning`](../../system-design/image-captioning/) | 11/11 | `image-captioning-system` |
| [`job-recommendation-system`](../../system-design/job-recommendation-system/) | 11/11 | `job-recommender-system` |
| [`job-scheduler`](../../system-design/job-scheduler/) | 11/11 | `job-scheduler-system` |
| [`kubernetes`](../../system-design/kubernetes/) | 11/11 | `kuberentes` |
| [`live-streaming-platform`](../../system-design/live-streaming-platform/) | 11/11 | `live-streaming-platform-detailed` |
| [`live-streaming-system`](../../system-design/live-streaming-system/) | 11/11 | `live-streaming-system-design` |
| [`messaging-system`](../../system-design/messaging-system/) | 11/11 | `messaging_system` |
| [`meta-pe-interview`](../../system-design/meta-pe-interview/) | 11/11 | `meta_pe_interview` |
| [`ml-system`](../../system-design/ml-system/) | 11/11 | `ml-systems-design` |
| [`new-aggregator`](../../system-design/new-aggregator/) | 11/11 | `news-aggregator` |
| [`object-oriented-design`](../../system-design/object-oriented-design/) | 11/11 | `object-oriented-design-system` |
| [`payment`](../../system-design/payment/) | 11/11 | `payment-tests` |
| [`rental-search-ranking`](../../system-design/rental-search-ranking/) | 11/11 | `rental-search-ranking-system` |
| [`server-side-monitoring`](../../system-design/server-side-monitoring/) | 11/11 | `server-side-monitoring-educative-tests` |
| [`session-management-system`](../../system-design/session-management-system/) | 11/11 | `session-management-system-v2` |
| [`social-recommendation`](../../system-design/social-recommendation/) | 11/11 | `social-recommender` |
| [`socket-programming-linux`](../../system-design/socket-programming-linux/) | 11/11 | `socket_programming_linux` |
| [`tinyurl`](../../system-design/tinyurl/) | 11/11 | `tinyurl-system` |
| [`twitch`](../../system-design/twitch/) | 11/11 | `twitch-system` |
| [`uber`](../../system-design/uber/) | 11/11 | `uber-tests` |
| [`uber-eats-system`](../../system-design/uber-eats-system/) | 11/11 | `uber-eats` |
| [`unique-id`](../../system-design/unique-id/) | 11/11 | `unique-id-educative-tests` |
| [`unique-id-generator`](../../system-design/unique-id-generator/) | 11/11 | `unique_id_generator` |
| [`video-streaming`](../../system-design/video-streaming/) | 11/11 | `video_streaming` |
| [`web-analytics`](../../system-design/web-analytics/) | 11/11 | `web-analytics-system` |
| [`yelp`](../../system-design/yelp/) | 11/11 | `yelp-system` |

## 四、文档偏薄的主题：2 个（标准文档 <4 份**且** md 总数 <6）

> 这些主题**仍然可以面**，但不要假装有完整语料：先 `ls` 该目录读实际存在的 md，再用 Q1–Q4 方法论补齐流程，并按需从同类主题（同一分类下文档齐全的那个）借追问。

| 主题 | 分类 | 标准文档 | md 总数 | 有 quiz | 有 drills |
|---|---|---|---|---|---|
| [`alexa`](../../system-design/alexa/) | products | 1/11 | 1 | · | · |
| [`doordash`](../../system-design/doordash/) | products | 1/11 | 4 | · | · |

### 四之二、用了**非标准编号**的主题：21 个（别误判成薄）

> 这些目录缺少 `00-index.md` / `06-quiz.md` 这类标准名，但自带另一套编号（例如 `airtag/` 有 `01-clarify-problem.md`、`03-nfr-slos.md`、`13-security-privacy.md`）。**先 `ls` 目录，再决定读什么**；不要对候选人说「语料很薄」。

| 主题 | 分类 | 标准文档 | md 总数 |
|---|---|---|---|
| [`bq`](../../system-design/bq/) | hubs | 1/11 | 3392 |
| [`linux-commands-interview-hub`](../../system-design/linux-commands-interview-hub/) | hubs | 1/11 | 49 |
| [`end-to-end`](../../system-design/end-to-end/) | fundamentals | 1/11 | 35 |
| [`typeahead-box-search`](../../system-design/typeahead-box-search/) | building-blocks | 2/11 | 34 |
| [`alexa-emergency-break-in`](../../system-design/alexa-emergency-break-in/) | products | 2/11 | 29 |
| [`security-interview-comprehensive`](../../system-design/security-interview-comprehensive/) | hubs | 1/11 | 29 |
| [`airtag`](../../system-design/airtag/) | products | 1/11 | 27 |
| [`instagram-design-comprehensive-hub`](../../system-design/instagram-design-comprehensive-hub/) | products | 1/11 | 27 |
| [`instagram-interview-hub`](../../system-design/instagram-interview-hub/) | products | 2/11 | 27 |
| [`cyclist`](../../system-design/cyclist/) | products | 1/11 | 26 |
| [`ecommerce-recommendation-hub`](../../system-design/ecommerce-recommendation-hub/) | ai-ml | 1/11 | 26 |
| [`kindle`](../../system-design/kindle/) | products | 1/11 | 26 |
| [`os-linux`](../../system-design/os-linux/) | os-systems | 1/11 | 26 |
| [`ai-system-design`](../../system-design/ai-system-design/) | ai-ml | 1/11 | 25 |
| [`amazon-kindle-payment`](../../system-design/amazon-kindle-payment/) | products | 1/11 | 25 |
| [`amazon-storage`](../../system-design/amazon-storage/) | building-blocks | 1/11 | 25 |
| [`async-communication-web-service-hub`](../../system-design/async-communication-web-service-hub/) | ops-infra | 1/11 | 25 |
| [`review-abuse`](../../system-design/review-abuse/) | ai-ml | 1/11 | 24 |
| [`lru-cache`](../../system-design/lru-cache/) | building-blocks | 1/11 | 23 |
| [`linux-opensource-projects-interview-hub`](../../system-design/linux-opensource-projects-interview-hub/) | os-systems | 0/11 | 22 |
| [`bank-legacy-digitalization`](../../system-design/bank-legacy-digitalization/) | ops-infra | 3/11 | 10 |

