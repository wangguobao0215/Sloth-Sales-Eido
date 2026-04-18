# B2B 销售智能助理 v4.0 - 数据模型参考

## 数据库路径

`~/.qoderwork/data/Sloth-Sales-Eido/sales_crm.db`

## 表结构

### customers 客户信息表

| 字段 | 类型 | 说明 |
|------|------|------|
| customer_id | INTEGER PK | 自增主键 |
| company_name | TEXT NOT NULL | 公司全称 |
| city | TEXT | 所在城市 |
| industry | TEXT | 所属行业 |
| qualification_tags | TEXT (JSON) | 资质标签 `{"专精特新":true,"规上企业":true,"高新技术":false}` |
| employee_count_range | TEXT | 人员规模区间 |
| revenue_last_3_years | TEXT (JSON) | 近三年营收（万元）`[5000,6000,7000]` |
| financial_status | TEXT | 良好/一般/预警 |
| procurement_category | TEXT | 采购品类：工业设备/原材料/物流服务/专业咨询/MRO/软件 |
| current_solution | TEXT (JSON) | 当前方案（见下方） |
| key_contacts | TEXT (JSON) | 联系人数组 |
| decision_chain | TEXT (JSON) | 决策链数组 |
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

#### decision_chain JSON 结构

```json
[{"name":"李总","role_type":"经济决策者","influence":5,"attitude":"支持","personal_focus":"预算控制"}]
```

- role_type：经济决策者 / 技术评估者 / 使用者 / 采购执行者 / 内线
- influence：1-5（1最低5最高）
- attitude：支持 / 中立 / 反对 / 未知

### sales_funnel 销售漏斗表

| 字段 | 类型 | 说明 |
|------|------|------|
| funnel_id | INTEGER PK | 自增主键 |
| customer_id | INTEGER FK | 关联客户 |
| current_stage | TEXT | 线索/初步接触/需求确认/方案演示/商务谈判/赢单/输单 |
| probability | INTEGER | 赢单概率 % |
| estimated_deal_value | REAL | 预估金额（万元） |
| next_action | TEXT | 下一步计划 |
| next_contact_date | TEXT | 下次跟进日期 |
| key_date | TEXT (JSON) | 关键日期数组 |
| priority | TEXT | 高/中/低 |
| owner | TEXT | 负责销售 |
| health_score | INTEGER | 健康分 0-100 |
| stuck_reason | TEXT | 卡顿原因 |
| created_at | TEXT | 创建时间 |
| updated_at | TEXT | 更新时间 |

#### key_date JSON 结构

```json
[
  {"date":"2025-06-30","event":"报价有效期截止","status":"待处理"},
  {"date":"2025-07-15","event":"投标文件递交截止","status":"待处理"},
  {"date":"2025-08-01","event":"首付款到期","status":"待处理"}
]
```

#### 漏斗阶段与默认概率

| 阶段 | 概率 | 阶段 | 概率 |
|------|------|------|------|
| 线索 | 10% | 方案演示 | 60% |
| 初步接触 | 20% | 商务谈判 | 80% |
| 需求确认 | 40% | 赢单/输单 | 100%/0% |

### activity_log 跟进记录表

| 字段 | 类型 | 说明 |
|------|------|------|
| log_id | INTEGER PK | 自增主键 |
| customer_id | INTEGER FK | 关联客户 |
| activity_type | TEXT | 电话/拜访/会议/演示/邮件 |
| timestamp | TEXT | 发生时间 |
| summary | TEXT | 内容摘要 |
| result | TEXT | 达成结果 |
| relationship_score | INTEGER | 关系温度 1-10 |
| next_stage_suggestion | TEXT | 建议推进阶段 |
| tags | TEXT | 话术标签（逗号分隔） |
| key_extracted_info | TEXT (JSON) | 结构化提取信息 |

#### key_extracted_info 常见结构

```json
// 输单记录
{"lost_to": "用友", "reason": "价格"}

// 竞品提及
{"competitor": "SAP", "competitor_advantage": "品牌知名度"}

// 预算信号
{"budget_signal": "明年Q1有预算", "estimated_budget": 50}
```

### case_library 案例库表

| 字段 | 类型 | 说明 |
|------|------|------|
| case_id | INTEGER PK | 自增主键 |
| industry | TEXT | 客户行业 |
| scale | TEXT | 客户规模（如"500-1000人"） |
| procurement_category | TEXT | 采购品类 |
| original_solution | TEXT | 原有方案（如"用友U8 V13.0"） |
| pain_point | TEXT | 核心痛点 |
| solution | TEXT | 我方方案 |
| quantifiable_benefit | TEXT | 量化收益（如"关账周期从7天缩短至2天"） |
| customer_quote | TEXT | 客户评价引用 |

### user_preferences 用户偏好表

| pref_key | 说明 | 可选值 |
|----------|------|--------|
| role | 角色 | 一线销售/销售团队负责人 |
| product_type | 产品 | 软件/SaaS, 工业设备, 专业服务, 其他 |
| methodology | 方法论 | SPIN, BANT, MEDDIC |
| initialized | 已初始化 | true/false |

## 健康度评分规则

基础分：70

| 条件 | 加/减分 |
|------|---------|
| 距上次跟进 >7天 | -15 |
| 距上次跟进 >14天 | -30（替代-15） |
| 无 next_action | -20 |
| relationship_score 下降 | -10 |
| stuck_reason 非空 | -5 |
| 老旧系统（上线>5年） | +15 |
| 有预算信号 | +20 |
| 决策链有"支持"者 | +10 |
| priority="高" | +5 |

范围限制：0-100

## 阻力点诊断框架

分析维度：活动停滞（频率/间隔）、决策链阻力（反对者 influence>=3）、竞品威胁、预算缺失、方法论缺口。

## 协作快照模板

```
客户：[公司名]，[行业]，年营收约[X]万，[资质标签]
当前在用：[current_solution 摘要]
核心痛点：[推测痛点]
关键人：[决策链关键人]（[角色]，态度[X]）
当前阶段：[漏斗阶段]，预估[X]万，[下一步计划]
```

## 角色化沟通关注点

| 角色 | 关注点 | 话术风格 |
|------|--------|----------|
| 经济决策者 | ROI、战略价值、风险控制 | 简洁、数据驱动 |
| 技术评估者 | 性能、SLA、集成、安全 | 技术深度 |
| 使用者 | 易用性、培训、日常效率 | 场景化 |
| 采购执行者 | 价格、条款、交期、资质 | 商务规范 |

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
- 关系维护：平均 relationship_score
