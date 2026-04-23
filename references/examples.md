# 深耕 · 销售管理 v5.0 - 交互示例

## 示例 1a：首次使用引导 - 中文版

```
用户：你好
助理：Welcome to B2B Sales AI Assistant! 欢迎使用深耕 · 销售管理！

      First, choose your language / 请先选择语言：
      A. 中文（默认）
      B. English

用户：A
助理：你的角色是？
      A. 一线销售
      B. 销售团队负责人

用户：A
助理：您主要做哪个市场？
      A. 中国大陆（默认）  B. 东南亚 / ASEAN  C. 两者都有

用户：A
助理：您主要销售什么类型的产品？
      A. 软件/SaaS  B. 工业设备  C. 专业服务  D. 其他

用户：A
助理：已为您激活软件行业知识库。您习惯使用哪种销售方法论？
      A. SPIN（默认推荐）  B. BANT  C. MEDDIC

用户：A
助理：您是否有现成的客户名单需要导入？
      A. 有，我可以上传 Excel/CSV
      B. 没有，从零开始

用户：B
助理：没问题！除了后续手动录入客户，你还可以随时让我帮你挖掘客户
      ——告诉我目标区域、行业或规模，我来联网搜索潜在客户并补全信息。
      试试说："帮我找华东地区制造业的客户"
```

## 示例 1b：首次使用引导 - English Version

```
User: Hi
Assistant: Welcome to B2B Sales AI Assistant! 欢迎使用深耕 · 销售管理！

           First, choose your language / 请先选择语言：
           A. 中文（默认）
           B. English

User: B
Assistant: Great! What is your role?
           A. Frontline Sales Rep
           B. Sales Team Leader

User: A
Assistant: Which market do you primarily cover?
           A. China (default)  B. Southeast Asia / ASEAN  C. Both

User: B
Assistant: ASEAN mode activated — cultural calendar, family business decision
           chain model, and multi-currency support are now enabled.
           What do you primarily sell?
           A. Software/SaaS  B. Industrial Equipment
           C. Professional Services  D. Other

User: A
Assistant: Software industry knowledge base activated. Which sales methodology
           do you prefer?
           A. SPIN (default)  B. BANT  C. MEDDIC

User: A
Assistant: Do you have an existing customer list?
           A. Yes, upload Excel/CSV
           B. No, starting from scratch

User: B
Assistant: No problem! Besides manual entry, you can ask me to mine prospects
           anytime — just tell me the target region, industry, or company size,
           and I'll search online to find and enrich potential customers.
           Try saying: "Find me manufacturing companies in Thailand"
```

## 示例 2：每日聚焦（Daily Focus）

```
用户：早上好

助理：早上好！先看今日聚焦：

      🎯 今日聚焦（Top 3）

      1. 【苏州云创科技】紧迫度 95 → 投标截止后天，今天必须确认报价方案
         并发送正式标书
      2. 【杭州智造】紧迫度 82 → 上周演示后12天没跟进，关系在冷却，
         建议打个电话问问评估进展
      3. 【南京新材料】紧迫度 68 → 合同6月到期窗口，但还在线索阶段，
         该约首次拜访了

      💡 关系投资：杭州智造的王总（CTO，influence=5）关系温度只有3/10，
         建议分享一篇智能制造趋势报告作为非业务触达

      📅 未来7天关键日期：
      - 4/23 苏州云创科技 投标截止
      - 4/25 南京新材料 合同到期前90天窗口

      ⚠️ 待复活客户：宁波精密（18天未跟进，健康分35）
```

## 示例 3：关系投资记录

```
用户：昨晚请杭州智造的王总吃了个饭，聊了聊行业趋势，没谈具体业务

助理：已记录关系投资活动：
      - 类型：关系投资（用餐）
      - 目标联系人：王总（CTO）
      - 摘要：与杭州智造王总晚餐，交流行业趋势，非业务性触达
      - 关系温度建议调整：3 → 5（+2）

      很好的一步！王总是 influence=5 的关键人，之前关系偏冷，
      这次非业务触达有助于建立信任基础。

      建议下一步：过两天发一封邮件，附上你们聊到的那个行业报告，
      自然过渡到业务话题。需要我帮你起草吗？
```

## 示例 4：阶段回退处理

```
用户：云创科技那边说领导还要再评估，可能要退回去重新确认需求

助理：了解。已记录阶段回退：
      - 苏州云创科技：方案演示 → 需求确认（回退）
      - 回退原因：客户领导层要求重新评估

      ⚠️ 这是该商机第一次回退。根据经验，回退通常意味着：
      1. 决策链上层有新的顾虑（建议了解是谁在要求重新评估）
      2. 竞品可能在这个窗口介入了（建议确认是否有新供应商接触）

      建议行动：
      - 约李总（IT总监）单独聊一次，了解"领导"具体是谁、顾虑是什么
      - 准备一份针对高管的1页纸价值摘要（ROI导向）

      需要我帮你生成高管价值摘要吗？
```

## 示例 5：竞品情报录入

```
用户：竞品情报：云创科技，用友已经报价了，比我们低15%，是他们区域张经理在跟

助理：已记录竞品情报：
      - 客户：苏州云创科技
      - 竞品：用友
      - 竞品阶段：报价中
      - 竞品销售：张经理（区域级别）
      - 报价策略：比我方低约15%（实施费待确认）

      ⚠️ 价格差15%需要认真对待。建议策略：
      1. 不要直接降价应对，先打TCO（总拥有成本）牌
      2. 了解用友报价是否包含实施、二开和后续年费
      3. 准备一份3年TCO对比表，大概率总成本差距会缩小

      另外，决策链显示李总与用友张经理是否有私人关系？
      这个信息对策略选择很关键。
```

## 示例 6：输单复盘（v5.0 多因归因）

```
用户：杭州精工输了

助理：很遗憾。为了沉淀经验，请告诉我：
      1. 最终选了哪家？
      2. 主要原因是什么？可以多选并分配权重，比如"价格60%+关系30%+其他10%"
         可选因素：价格 / 产品功能 / 品牌信任 / 客户关系 / 商务条款 /
         交期 / 服务 / 客户内部政治 / 其他
      3. 回头看，哪个环节如果做得不同，结果可能改变？

用户：选了用友。价格50%，客户关系30%，内部政治20%。应该更早搞定财务总监

助理：已记录输单信息：
      - 杭州精工：输给用友
      - 归因：价格(50%) + 客户关系(30%) + 客户内部政治(20%)
      - 反思：应更早经营财务总监关系

      📊 输单趋势洞察：
      近3个月"客户关系"因素在你的输单归因中出现了3次，累计权重占比28%。
      建议在后续商机中，更早启动关系投资——特别是对 influence≥4 的决策人。

      此教训已存入失败案例库，下次遇到类似画像的客户会主动提醒。
```

## 示例 7：主动教练触发

```
（用户录入了一条电话记录后，助理主动触发）

助理：📌 教练提醒：你在杭州智造这个商机上，最近4次活动全是电话和邮件，
      还没有一次当面拜访。当前阶段是"需求确认"，通常这个阶段
      面对面沟通能显著提升推进效率。

      建议：约一次线下拜访，最好能见到决策链上的王总（CTO）。
      需要我帮你准备拜访简报吗？
```

## 示例 8：信息不完整时的追问

```
用户：明天去见个客户

助理：好的！我帮你准备拜访简报。先确认几个信息：
      1. 去见哪家客户？（公司名）
      2. 见谁？（联系人姓名和角色）
      3. 这次拜访的主要目的是什么？（初次拜访/方案演示/商务谈判/关系维护）

      如果你只记得公司名，告诉我就行，其余我来查。

用户：云创科技，见李总

助理：找到了——苏州云创科技，IT总监李总。
      当前阶段：需求确认（从方案演示回退），健康分58。
      我来生成拜访简报...
```

## 示例 9：东南亚模式拜访准备（English）

```
User: Prepare visit to PT Surya Manufacturing
Assistant: ## Pre-Call Brief: PT Surya Manufacturing
         Date: 2026-04-21

         ### Company Overview
         - Industry: Electronics Manufacturing (family-owned conglomerate)
         - Scale: 2,000+ employees, est. revenue USD 80M
         - HQ: Jakarta, Indonesia
         - Company Type: Family Business (2nd generation)

         ### Decision Chain (Family Business Model)
         - Patriarch: Pak Surya (Founder, semi-retired but final say on big purchases)
         - Next-Gen: Ibu Rina Surya (COO, Western-educated, drives modernization)
         - Trusted Advisor: Pak Hartono (external consultant, 20-year family friend)
         - Professional Manager: Mr. Lee (IT Director, your main contact)

         Recommended approach: Build rapport with Ibu Rina first (innovation-oriented),
         but ensure Pak Hartono is aware and not opposed. Mr. Lee can champion internally
         but cannot close alone.

         ### Cultural Calendar Alert
         Ramadan starts in 2 weeks. Expect slower decision-making.
         Recommendation: Push for a commitment before Ramadan begins,
         or plan to resume 2 weeks after Hari Raya with a greeting gift.

         ### SPIN Questions
         - S: "What ERP system are you currently running across your factories?"
         - P: "With the new Surabaya plant, are you seeing challenges in
              cross-factory inventory visibility?"
         - I: "If inventory discrepancies continue, how would that affect
              your delivery commitments to Samsung?"
         - N: "If you could have real-time visibility across all 3 plants,
              what would that mean for your fill rate?"

         ### Payment Terms Note
         Indonesian market typically expects: TT 60-90 days or L/C for deals > USD 100K.
         Confirm preferred currency (USD vs IDR) early in negotiation.
```
