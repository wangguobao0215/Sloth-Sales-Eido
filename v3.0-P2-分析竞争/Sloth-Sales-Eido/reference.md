# B2B 销售智能助理 v3.0 - 数据模型参考

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
| qualification_tags | TEXT (JSON) | 资质标签 |
| employee_count_range | TEXT | 人员规模区间 |
| revenue_last_3_years | TEXT (JSON) | 近三年营收（万元） |
| financial_status | TEXT | 良好/一般/预警 |
| procurement_category | TEXT | 采购品类 |
| current_solution | TEXT (JSON) | 当前方案 |
| key_contacts | TEXT (JSON) | 联系人数组 |
| decision_chain | TEXT (JSON) | 决策链数组 |
| data_source | TEXT | 数据来源 |
| monitor_flag | INTEGER | 0=普通 1=监控 |
| created_at | TEXT | 创建时间 |
| updated_at | TEXT | 更新时间 |

#### current_solution JSON 结构

```json
{"category":"","provider":"","product_name":"","adoption_year":2020,"satisfaction":"","contract_expiry":"2025-06","notes":""}
```

#### decision_chain JSON 结构

```json
[{"name":"","role_type":"经济决策者","influence":5,"attitude":"支持","personal_focus":"预算控制"}]
```

- role_type：经济决策者/技术评估者/使用者/采购执行者/内线
- influence：1-5，attitude：支持/中立/反对/未知

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
[{"date":"2025-06-30","event":"报价有效期截止","status":"待处理"}]
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

### case_library 案例库表【v3.0 新增】

| 字段 | 类型 | 说明 |
|------|------|------|
| case_id | INTEGER PK | 自增主键 |
| industry | TEXT | 客户行业 |
| scale | TEXT | 客户规模 |
| procurement_category | TEXT | 采购品类 |
| original_solution | TEXT | 原有方案 |
| pain_point | TEXT | 核心痛点 |
| solution | TEXT | 我方方案 |
| quantifiable_benefit | TEXT | 量化收益 |
| customer_quote | TEXT | 客户评价引用 |

### user_preferences 用户偏好表

| pref_key | 说明 | 可选值 |
|----------|------|--------|
| role | 角色 | 一线销售/销售团队负责人 |
| product_type | 产品 | 软件/SaaS, 工业设备, 专业服务 |
| methodology | 方法论 | SPIN, BANT, MEDDIC |
| initialized | 已初始化 | true/false |

## 健康度评分详细规则【v3.0 新增】

基础分：70 分

**扣分项：**
| 条件 | 扣分 |
|------|------|
| 距上次跟进 >7天 | -15 |
| 距上次跟进 >14天 | -30（替代-15） |
| 无 next_action | -20 |
| relationship_score 近期下降 | -10 |
| stuck_reason 非空 | -5 |

**加分项：**
| 条件 | 加分 |
|------|------|
| current_solution 存在老旧系统（上线>5年） | +15 |
| 近期活动有预算信号 | +20 |
| 决策链中有"支持"态度者 | +10 |
| priority = "高" | +5 |

分数范围限制为 0-100。

## 阻力点诊断框架【v3.0 新增】

分析维度：

1. **活动停滞**：最近一次活动距今天数、活动频率趋势
2. **决策链阻力**：是否存在 attitude="反对" 且 influence>=3 的角色
3. **竞品威胁**：key_extracted_info 中是否提及竞品
4. **预算缺失**：是否缺少明确的预算信号
5. **方法论缺口**：基于选定方法论，哪些关键维度信息缺失

输出格式：
```
## 商机阻力诊断：[客户名]

### 可能卡点
1. [具体卡点描述]
2. [具体卡点描述]

### 突破建议
1. [具体可执行的行动建议]
2. [具体可执行的行动建议]
```

## 协作快照模板【v3.0 新增】

```
客户：[公司名]，[行业]，年营收约[X]万，[资质标签]
当前在用：[current_solution 摘要]
核心痛点：[推测痛点]
关键人：[决策链关键人]（[角色]，态度[X]）
当前阶段：[漏斗阶段]，预估[X]万，[下一步计划]
```

## 角色化沟通关注点【v3.0 新增】

| 角色 | 关注点 | 话术风格 |
|------|--------|----------|
| 经济决策者 | ROI、战略价值、风险控制 | 简洁、数据驱动、战略视角 |
| 技术评估者 | 性能、SLA、集成、安全 | 技术深度、对比数据 |
| 使用者 | 易用性、培训、日常效率 | 场景化、实操导向 |
| 采购执行者 | 价格、条款、交期、资质 | 商务规范、合规导向 |
