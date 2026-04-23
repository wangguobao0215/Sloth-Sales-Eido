# 深耕 · 销售管理 v5.0 - 数据模型参考

## 数据库路径

`~/.qoderwork/data/Sloth-Sales-Eido/sales_crm.db`

## 表结构

### customers 客户信息表

| 字段 | 类型 | 说明 |
|------|------|------|
| customer_id | INTEGER PK | 自增主键 |
| company_name | TEXT NOT NULL | 公司全称 |
| city | TEXT | 所在城市 |
| country | TEXT | 国家（v5.0新增，东南亚模式必填） |
| market | TEXT | 所属市场：中国大陆 / ASEAN / 其他 |
| industry | TEXT | 所属行业 |
| qualification_tags | TEXT (JSON) | 资质标签 `{"专精特新":true,"规上企业":true,"高新技术":false}` |
| company_type | TEXT | 企业类型：上市公司/国企/民企/外企/家族企业（v5.0新增） |
| employee_count_range | TEXT | 人员规模区间 |
| revenue_last_3_years | TEXT (JSON) | 近三年营收（万元）`[5000,6000,7000]` |
| financial_status | TEXT | 良好/一般/预警 |
| procurement_category | TEXT | 采购品类：工业设备/原材料/物流服务/专业咨询/MRO/软件 |
| current_solution | TEXT (JSON) | 当前方案（见下方） |
| key_contacts | TEXT (JSON) | 联系人数组 |
| decision_chain | TEXT (JSON) | 决策链数组（v5.0增强，见下方） |
| competitor_intelligence | TEXT (JSON) | 竞品情报（v5.0新增，见下方） |
| data_source | TEXT | 数据来源 |
| monitor_flag | INTEGER | 0=普通 1=监控 |
| created_at | TEXT | 创建时间 |
| updated_at | TEXT | 更新时间 |

#### current_solution JSON 结构

```json
{
  "category": "工业设备",
  "provider": "西门子",
  "product_name": "XX型号",
  "adoption_year": 2020,
  "satisfaction": "一般",
  "contract_expiry": "2025-06",
  "notes": "多工厂协同困难"
}
```

#### key_contacts JSON 结构

```json
[{"name":"张三","title":"IT总监","phone":"138xxxx","email":"zhang@co.com","source":"官网"}]
```

#### decision_chain JSON 结构【v5.0 增强】

```json
[{
  "name": "李总",
  "role_type": "经济决策者",
  "influence": 5,
  "attitude": "支持",
  "personal_focus": "预算控制",
  "political_position": "上升期",
  "personal_agenda": "推动数字化转型出成绩以竞争VP",
  "relationship_with_competitor": "与用友区域经理是校友",
  "internal_ally": "与CTO王总关系密切",
  "relationship_score": 6,
  "last_touchpoint": "2026-04-10",
  "family_role": null
}]
```

字段说明：
- role_type：经济决策者 / 技术评估者 / 使用者 / 采购执行者 / 内线 / **家族成员**（v5.0）/ **Trusted Advisor**（v5.0，东南亚家族企业）
- influence：1-5（1最低5最高）
- attitude：支持 / 中立 / 反对 / 未知
- political_position（v5.0）：上升期 / 稳定 / 边缘化 / 未知
- personal_agenda（v5.0）：该人的职业诉求/个人动机
- relationship_with_competitor（v5.0）：与竞品销售/公司的已知关系
- internal_ally（v5.0）：在客户内部的盟友关系
- relationship_score（v5.0）：我方与此人的关系温度 1-10
- last_touchpoint（v5.0）：最近一次接触日期
- family_role（v5.0）：仅东南亚家族企业模式——Patriarch / Next-Gen / Trusted Advisor / Professional Manager / null

#### competitor_intelligence JSON 结构【v5.0 新增】

```json
{
  "competitor_name": "用友",
  "stage_in_account": "报价中",
  "competitor_rep": "张经理（区域总监级别）",
  "pricing_intel": "比我方低约15%，但实施费另算",
  "implementation_capacity": "该区域有3人实施团队",
  "relationship_depth": "与客户IT总监有5年合作关系",
  "strengths": "本地化服务、价格",
  "weaknesses": "产品老化、二次开发成本高",
  "updated_at": "2026-04-15"
}
```

### sales_funnel 销售漏斗表【v5.0 增强】

| 字段 | 类型 | 说明 |
|------|------|------|
| funnel_id | INTEGER PK | 自增主键 |
| customer_id | INTEGER FK | 关联客户 |
| current_stage | TEXT | 线索/初步接触/需求确认/方案演示/商务谈判/赢单/输单 |
| is_stalled | INTEGER | 0=正常 1=悬停（v5.0新增） |
| stalled_since | TEXT | 进入悬停的日期（v5.0新增） |
| stage_history | TEXT (JSON) | 阶段变更历史（v5.0新增，见下方） |
| probability | INTEGER | 赢单概率 % |
| estimated_deal_value | REAL | 预估金额（万元） |
| deal_currency | TEXT | 币种，默认CNY（v5.0新增，ASEAN模式用） |
| payment_terms | TEXT | 付款条件（v5.0新增，如 TT/LC/OA） |
| next_action | TEXT | 下一步计划 |
| next_contact_date | TEXT | 下次跟进日期 |
| key_date | TEXT (JSON) | 关键日期数组 |
| priority | TEXT | 高/中/低 |
| owner | TEXT | 负责销售 |
| health_score | INTEGER | 健康分 0-100 |
| stuck_reason | TEXT | 卡顿原因 |
| created_at | TEXT | 创建时间 |
| updated_at | TEXT | 更新时间 |

#### stage_history JSON 结构【v5.0 新增】

```json
[
  {"from": "线索", "to": "初步接触", "date": "2026-03-01", "direction": "forward"},
  {"from": "初步接触", "to": "需求确认", "date": "2026-03-15", "direction": "forward"},
  {"from": "需求确认", "to": "方案演示", "date": "2026-03-28", "direction": "forward"},
  {"from": "方案演示", "to": "需求确认", "date": "2026-04-10", "direction": "backward", "reason": "客户说领导还要再评估，竞品也介入了"}
]
```

#### Stalled 基准周期

| 阶段 | 基准停留天数 | 超过即标记 Stalled |
|------|-------------|-------------------|
| 线索 | 14 天 | 是 |
| 初步接触 | 10 天 | 是 |
| 需求确认 | 14 天 | 是 |
| 方案演示 | 10 天 | 是 |
| 商务谈判 | 21 天 | 是 |

#### 漏斗阶段与默认概率

| 阶段 | 概率 | 阶段 | 概率 |
|------|------|------|------|
| 线索 | 10% | 方案演示 | 60% |
| 初步接触 | 20% | 商务谈判 | 80% |
| 需求确认 | 40% | 赢单/输单 | 100%/0% |

### activity_log 跟进记录表【v5.0 增强】

| 字段 | 类型 | 说明 |
|------|------|------|
| log_id | INTEGER PK | 自增主键 |
| customer_id | INTEGER FK | 关联客户 |
| activity_type | TEXT | 电话/拜访/会议/演示/邮件/**关系投资**（v5.0新增） |
| relationship_investment_type | TEXT | 仅关系投资时填写：用餐/节日问候/资讯分享/引荐/帮忙/礼品/其他（v5.0新增） |
| target_contact | TEXT | 关系投资的目标联系人（v5.0新增） |
| timestamp | TEXT | 发生时间 |
| summary | TEXT | 内容摘要 |
| result | TEXT | 达成结果 |
| relationship_score | INTEGER | 关系温度 1-10 |
| next_stage_suggestion | TEXT | 建议推进阶段 |
| tags | TEXT | 话术标签（逗号分隔） |
| key_extracted_info | TEXT (JSON) | 结构化提取信息 |

#### key_extracted_info 常见结构【v5.0 增强】

```json
// 输单记录（v5.0：多因归因+权重）
{
  "lost_to": "用友",
  "reasons": [
    {"factor": "价格", "weight": 50},
    {"factor": "客户关系", "weight": 30},
    {"factor": "客户内部政治", "weight": 20}
  ],
  "reflection": "应更早引入TCO对比，关系投资不足"
}

// 竞品提及
{"competitor": "SAP", "competitor_advantage": "品牌知名度"}

// 预算信号
{"budget_signal": "明年Q1有预算", "estimated_budget": 50}

// 阶段回退（v5.0新增）
{"stage_regression": true, "from": "方案演示", "to": "需求确认", "reason": "竞品介入重新选型"}
```

### case_library 案例库表【v5.0 增强】

| 字段 | 类型 | 说明 |
|------|------|------|
| case_id | INTEGER PK | 自增主键 |
| case_type | TEXT | **成功** / **失败**（v5.0新增） |
| industry | TEXT | 客户行业 |
| scale | TEXT | 客户规模（如"500-1000人"） |
| procurement_category | TEXT | 采购品类 |
| original_solution | TEXT | 原有方案（如"用友U8 V13.0"） |
| pain_point | TEXT | 核心痛点 |
| solution | TEXT | 我方方案（成功案例）/ 竞品方案（失败案例） |
| quantifiable_benefit | TEXT | 量化收益（成功案例）/ 输单教训（失败案例） |
| customer_quote | TEXT | 客户评价引用 |
| lost_to | TEXT | 仅失败案例：输给了谁（v5.0新增） |
| lesson_learned | TEXT | 仅失败案例：核心教训总结（v5.0新增） |

### user_preferences 用户偏好表【v5.0 增强】

| pref_key | 说明 | 可选值 |
|----------|------|--------|
| language | 交互语言（v5.0新增） | zh / en |
| role | 角色 | 一线销售/销售团队负责人 |
| target_market | 目标市场（v5.0新增） | 中国大陆 / ASEAN / 两者都有 |
| product_type | 产品 | 软件/SaaS, 工业设备, 专业服务, 其他 |
| methodology | 方法论 | SPIN, BANT, MEDDIC |
| initialized | 已初始化 | true/false |

## 健康度评分规则【v5.0 权重模型】

v5.0 改用加权模型，核心维度按重要性分配权重：

| 维度 | 权重 | 评分规则 |
|------|------|----------|
| **预算信号** | 25% | 有明确预算=100，有信号但未确认=60，无信号=20 |
| **决策链通畅度** | 25% | 有支持者(influence≥4)=100，有中立高层=60，有反对者(influence≥3)=30，无决策链信息=10 |
| **跟进活跃度** | 20% | ≤3天=100，4-7天=70，8-14天=40，>14天=10 |
| **关系投资** | 15% | 近30天有关系投资=100，仅业务活动=50，无活动=10 |
| **竞品压力** | 15% | 无竞品=100，竞品在早期=70，竞品在报价/锁定=30 |

**附加调节：**
- Stalled 标记：总分 × 0.7
- 阶段回退 ≥2次：总分 × 0.6
- 合同到期 <3个月且阶段在"需求确认"之前：总分 × 0.8（窗口关闭预警）

范围限制：0-100

## 阻力点诊断框架【v5.0 增强】

分析维度：
1. 活动停滞（频率/间隔/活动类型单一化）
2. 决策链阻力（反对者 influence≥3、关键人关系温度低）
3. 竞品威胁（competitor_intelligence 分析）
4. 预算缺失
5. 方法论缺口
6. **关系投资不足**（v5.0新增）
7. **客户内部政治**（v5.0新增：关键人 political_position 变化）
8. **阶段回退模式**（v5.0新增：是否存在反复回退的结构性问题）

## 协作快照模板

```
客户：[公司名]，[行业]，年营收约[X]万，[资质标签]
当前在用：[current_solution 摘要]
核心痛点：[推测痛点]
关键人：[决策链关键人]（[角色]，态度[X]，关系温度[X]/10）
竞品：[竞品名] [竞品阶段]
当前阶段：[漏斗阶段]，预估[X]万，[下一步计划]
```

## 角色化沟通关注点

| 角色 | 关注点 | 话术风格 |
|------|--------|----------|
| 经济决策者 | ROI、战略价值、风险控制 | 简洁、数据驱动 |
| 技术评估者 | 性能、SLA、集成、安全 | 技术深度 |
| 使用者 | 易用性、培训、日常效率 | 场景化 |
| 采购执行者 | 价格、条款、交期、资质 | 商务规范 |
| Patriarch/家族掌门（ASEAN） | 信任、长期承诺、风险最小化 | 关系导向、尊重层级 |
| Next-Gen Leader（ASEAN） | 创新、效率、现代化 | 技术+战略结合 |

## 团队负责人功能参考

团队功能通过 Excel 导入实现多销售数据汇聚：
1. 各销售定期导出个人数据 Excel
2. 负责人上传至 Skill，执行"合并团队数据"
3. Skill 自动去重、合并、生成团队看板

**销售预测分级规则：**
- Commit（承诺）：商务谈判阶段 + 健康分>70
- Best Case（最佳情况）：方案演示阶段 + 健康分>50
- Pipeline（管道）：其余活跃商机

**销售能力五维度：**
- 获客能力：月新增线索数
- 推进能力：阶段推进次数/活跃商机数
- 关单能力：赢单率
- 活动量：月均活动记录数
- 关系维护：平均 relationship_score + 关系投资频次（v5.0增强）

## 每日聚焦算法参考【v5.0 新增】

紧迫度指数 = （预估金额 × 赢单概率 / 100）× 时间衰减系数 × 窗口系数

| 因子 | 条件 | 系数 |
|------|------|------|
| 时间衰减 | 距上次跟进 ≤7天 | 1.0 |
| 时间衰减 | 距上次跟进 8-14天 | 1.5 |
| 时间衰减 | 距上次跟进 >14天 | 2.0 |
| 窗口系数 | 合同到期 <3个月 | 2.0 |
| 窗口系数 | 关键日期 <7天 | 1.8 |
| 窗口系数 | 有预算信号 | 1.3 |
| 窗口系数 | Stalled 标记 | 1.5 |

取 Top 3 输出，附加1条关系投资提醒（从决策链中挑 relationship_score 最低但 influence ≥ 4 的人）。
