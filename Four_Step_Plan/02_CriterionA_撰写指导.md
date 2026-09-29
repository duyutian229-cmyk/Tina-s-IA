# Criterion A 撰写指导 — Tina

> 阅读对象：老师 + Tina。
> 用法：**Tina 自己写英文终稿**。本文件只提供①中文骨架（写什么）②英文措辞提示（怎么写）③自查清单。
> 前置阅读：`IB/IA_Guide_2027/IA_Student_Handout.md` 第 1 节（评分要点），本文件不重复。

---

## 一、先把目标定死：3–4 分档要求三个动词全部到位

官方 3–4 分级描述原文拆成三个动作：

| # | 英文原文 | 中文 | Tina 现状 |
|---|---|---|---|
| 1 | **describes** the problem scenario in terms of its **measurable solution requirements** | 用**可衡量的求解需求**描述问题情境 | ⚠️ 描述了情境，但"可衡量需求"是隐含的，没有显性写出来 |
| 2 | **states appropriate** success criteria | 陈述**恰当**的成功标准 | ✅ 已有 7 条，基本可测（个别需改，见 §3） |
| 3 | **explains** the choice of **computational context** | **解释**为何选择该计算语境 | ❌ **完全缺失**——现有 "Computational Context" 段落写的是"方案是什么"，不是"为什么选计算方案" |

> **第 3 条是最容易补也最容易被忽略的提分点。** 现有稿件的 "Computational Context" 其实是一段方案描述（系统会取什么输入、返回什么输出）——批改人会判为"描述方案"而不是"解释语境"，这是 1–2 分档的做法。

**字数纪律：** A 的建议字数是 **300 词**（含成功标准条目）。现有稿件约 530 词，**超了 230 词**。全文上限 2000 词，A 多写 100 词等于从 D（12 分、1000 词）里偷 100 词。**必须砍。**

---

## 二、中文骨架（三段，共约 300 词）

### 第 1 段 · Problem scenario（约 110 词）

**写什么：**
1. 场景（保留现有稿件的优点）：新街口咖啡馆密集、菜单装修雷同、竞争激烈；顾客停留时间短（socializing + 拍照），咖啡馆是"short stopover"而非长时间场所。
2. **关键升级**：由此推出 3 条**可衡量的求解需求**，而不是继续抒情。现有稿件把需求写成"instant fun in a few minutes / personalized experience"——这是形容词，不可衡量。要改成带数量、时间、条件的句子。

**可衡量的需求（建议写这 3 条）：**
- 顾客从下单到收到音乐结果，**无需安装任何程序**，且等待时间与饮品制作时间重叠（不是额外等待）；
- 同一时刻店内**多位顾客的偏好必须被同时处理**，且每位顾客的等待时长可预期；
- 全过程**不增加店员的任何操作**（这是场景里已经提出的约束，但没被写成可测需求）。

### 第 2 段 · Computational context（约 90 词）★ 全新补写

**写什么：为什么用这套计算方案解决这个问题。** 至少回答 3 个"为什么选它，而不选替代方案"：

| 技术选择 | 要解释的对立方案 | 理由要点 |
|---|---|---|
| 客户端–服务端 Web 架构 | 手机原生 App | 无需安装、无需应用商店审核、顾客扫码即用；店家可直接控制服务端 |
| 关系型数据库（SQLite） | 内存变量 / 文本文件 | 订单与曲库需要**关联查询**（曲目标签 ↔ 情境 ↔ 反馈），且需要持久化供店家复盘 |
| 确定性打分 + 调度算法 | 纯随机 / 人工选曲 | 需求 2（多人并发 + 等待可预期）本质上是一个**调度问题**，必须由算法解决 |

⚠️ **反面教材（不要写）**：现有稿件的对应段落，以及讲义里 Sample C 的 "NetBeans is suitable for Android development"——泛泛的技术名词罗列不得分。

### 第 3 段 · Success criteria（约 140 词，8 条）

见 §3 的完整清单（已按确认的四个决定写好）。

---

## 三、成功标准清单（建议稿，约 140 词）

> 已按 2026-09-13 确认的四个决定重写：**店内扬声器公共播放 / 最小点单自制 / SL / 2027-01-18 终稿**。
> 每条都写成**可测试**的形式（含数值边界）。Tina 可以改措辞，但不要改"可测量"这个性质。

| # | 成功标准（英文建议稿） | 可测性说明 |
|---|---|---|
| 1 | The system must accept an order containing a drink item and an optional display nickname (max 20 characters), and must reject an empty or over-length nickname with a specific error message. | 边界输入可测：空、20 字符、21 字符 |
| 2 | The system must accept optional context inputs (weather, time of day, ambience preference) and must still generate a complete recommendation when all of them are absent. | 空值路径可测 |
| 3 | For an identical input set and an identical track library, the system must return the identical track, so that every recommendation is reproducible. | 同输入跑 2 次比对 |
| 4 | The system must select a track by scoring stored metadata tags against a weighted profile, and must return the ranked result **within 2 seconds** on the standard laptop. | 计时 |
| 5 | The system must maintain a queue of concurrent orders and schedule the shared speaker so that, in a queue of 5 customers, the gap between a customer's consecutive turns does not exceed **1.5 ×** the mean gap of the queue. | 公平性可量化（构造 5 人并发） |
| 6 | Every customer's phone page must display the currently playing track, the customer it was selected for, and the customer's own queue position, refreshed **within 3 seconds**. | 轮询间隔可测 |
| 7 | The system must record every session (timestamp, inputs, selected track, feedback) so the cafe can review usage patterns, and must allow a customer to delete their own session record. | 删除后可查库验证 |
| 8 | The system must only ever play tracks from the cafe's pre-approved ambience set, regardless of customer input. | 跑 100 组随机输入，断言输出全部落在允许集合内 |
| 9 | **（可裁剪）** The system must adjust its tag weights from customer feedback (skip / replay) such that, over 100 simulated sessions, the skip rate is measurably lower than the fixed-weight baseline. | 对照实验，可复现 |

### 关于第 9 条：为什么单独标"可裁剪"

- 这一条是 Criterion E 能写出**量化评价**的唯一来源（唯一能拿 E 满分的路子），所以值得放在 SC 里；
- 但它也是**技术上最容易做不出来的一条**。把它编在**最后一条**，万一 12 月发现做不完，直接删掉它并顺延编号即可，**不影响前面 8 条的编号和 B 的分解图**。
- ⚠️ **删除它必须在 2027-01-18 之前完成**，因为 1 月下旬起不允许大段文字改动。

---

## 四、英文措辞提示

### 4.1 可衡量的动词库

避免：`improve`、`enhance`、`make it easier`、`be user-friendly`、`be efficient`。

| 用途 | 可用措辞 |
|---|---|
| 输入校验 | `must reject ___ with a specific error message` / `must validate ___ against ___` |
| 时间约束 | `must return ___ within N seconds` |
| 数量约束 | `must support at least N concurrent ___` / `must not exceed N ___` |
| 可复现 | `must return the identical ___ for an identical input set` |
| 持久化 | `must record ___ so that ___` / `must allow the user to delete ___` |
| 公平性 | `the gap between ___ must not exceed N × the mean` |

### 4.2 句式模板（可直接改）

**问题情境段**
> In the centre of Nanjing Xinjiekou, cafes compete on near-identical menus and interiors, while customers typically stay for only a short period. This creates a measurable requirement that any solution must meet **without adding to the staff's workload**: ___.

**计算语境段（"解释为什么"的句式）**
> A client–server web architecture was selected **rather than** a native mobile application **because** ___.
> A relational database is **required rather than** in-memory storage **because** the track metadata, the order record and the feedback must be queried **in combination**.
> The problem is **inherently computational rather than clerical because** serving multiple concurrent customers from a single shared speaker is a scheduling problem with a fairness constraint.

**成功标准段**
> The system must ___, and must ___ when ___.
> For an identical input set, the system must ___.

### 4.3 三条"不要写"

1. ❌ 不要写技术名词的**罗列**（"uses Python, Flask, SQLite and HTML"）——要写**为什么是它们**；
2. ❌ 不要用形容词充当需求（"personalized", "fun", "seamless"）——除非紧跟一个可测的数字或条件；
3. ❌ 不要描述**怎么做**（那是 Criterion C 的事）——A 只说**问题与目标**。

---

## 五、Tina 自查清单（写完逐条打勾）

- [ ] 问题情境里有至少 **3 条显性的、带数字或条件的**可衡量需求
- [ ] 计算语境回答了至少 **3 个"为什么选它而不是替代方案"**（不是罗列技术名词）
- [ ] 每条成功标准都能**照着做一次测试**（能说出：测什么、预期什么）
- [ ] 每条成功标准都能追溯到第 1 段的某条需求（**A 内部要闭环**）
- [ ] 全文 ≤ 350 词
- [ ] 没有描述"怎么做"（没有出现表名、函数名、页面布局）

---

## 六、待 Tina 确认的一个小冲突

**昵称是必填还是选填？**
- 现有稿件的 SC1 写"coffee type and nickname as **required** inputs"；
- 老师转述的设想是"用户的昵称（**选填**）"。

**建议**：改为**选填**（更符合隐私友好，也更好论证），SC1 相应改为"若填写则校验长度与字符，为空时使用默认称呼"。上表 SC1 已按此写。若 Tina 坚持必填，把 `optional` 去掉即可，其余不变。
