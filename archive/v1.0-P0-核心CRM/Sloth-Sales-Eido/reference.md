# B2B 销售智能助理 v1.0 - 数据模型参考

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
| qualification_tags | TEXT (JSON) | 资质标签，如 `{"专精特新": true, "规上企业": true, "高新技术": false}` |
| employee_count_range | TEXT | 人员规模区间，如 "100-500人" |
| revenue_last_3_years | TEXT (JSON) | 近三年营收（万元），如 `[5000, 6000, 7000]` |
| financial_status | TEXT | 财务状态：良好/一般/预警 |
| procurement_category | TEXT | 采购品类：工业设备/原材料/物流服务/专业咨询/MRO/软件 |
| current_solution | TEXT (JSON) | 当前使用的核心产品或服务方案 |
| key_contacts | TEXT (JSON) | 联系人数组 |
| decision_chain | TEXT (JSON) | 决策链数组 |
| data_source | TEXT | 数据采集来源 |
| monitor_flag | INTEGER | 0=普通 1=重点监控 |
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
  "notes": ""
}
```

#### key_contacts JSON 结构

```json
[
  {
    "name": "张三",
    "title": "IT总监",
    "phone": "138xxxx",
    "email": "zhang@company.com",
    "source": "官网/招标书"
  }
]
```

#### decision_chain JSON 结构

```json
[
  {
    "name": "李总",
    "role_type": "经济决策者",
    "influence": 5,
    "attitude": "支持",
    "personal_focus": "预算控制"
  }
]
```

role_type 可选值：经济决策者 / 技术评估者 / 使用者 / 采购执行者 / 内线

influence 范围：1-5（1最低，5最高）

attitude 可选值：支持 / 中立 / 反对 / 未知

### sales_funnel 销售漏斗表

| 字段 | 类型 | 说明 |
|------|------|------|
| funnel_id | INTEGER PK | 自增主键 |
| customer_id | INTEGER FK | 关联客户 |
| current_stage | TEXT | 线索/初步接触/需求确认/方案演示/商务谈判/赢单/输单 |
| probability | INTEGER | 赢单概率 % |
| estimated_deal_value | REAL | 预估金额（万元） |
| next_action | TEXT | 下一步计划 |
| next_contact_date | TEXT | 下次跟进日期（YYYY-MM-DD） |
| key_date | TEXT (JSON) | 关键日期数组 |
| priority | TEXT | 高/中/低 |
| owner | TEXT | 负责销售 |
| health_score | INTEGER | 健康分 0-100，默认 70 |
| stuck_reason | TEXT | 卡顿原因 |
| created_at | TEXT | 创建时间 |
| updated_at | TEXT | 更新时间 |

#### 漏斗阶段与默认概率

| 阶段 | 默认概率 |
|------|----------|
| 线索 | 10% |
| 初步接触 | 20% |
| 需求确认 | 40% |
| 方案演示 | 60% |
| 商务谈判 | 80% |
| 赢单 | 100% |
| 输单 | 0% |

### activity_log 跟进记录表

| 字段 | 类型 | 说明 |
|------|------|------|
| log_id | INTEGER PK | 自增主键 |
| customer_id | INTEGER FK | 关联客户 |
| activity_type | TEXT | 电话/拜访/会议/演示/邮件 |
| timestamp | TEXT | 发生时间 |
| summary | TEXT | 交流内容摘要 |
| result | TEXT | 达成结果 |
| relationship_score | INTEGER | 关系温度 1-10 |
| next_stage_suggestion | TEXT | 建议推进阶段 |
| tags | TEXT | 话术标签（逗号分隔） |
| key_extracted_info | TEXT (JSON) | 结构化提取信息 |

### user_preferences 用户偏好表

| 字段 | 类型 | 说明 |
|------|------|------|
| pref_key | TEXT PK | 偏好键 |
| pref_value | TEXT | 偏好值 |

常用偏好键：

| pref_key | 说明 | 可选值 |
|----------|------|--------|
| role | 用户角色 | 一线销售 / 销售团队负责人 |
| product_type | 产品类型 | 软件/SaaS, 工业设备, 专业服务, 其他 |
| methodology | 销售方法论 | SPIN, BANT, MEDDIC |
| initialized | 是否已初始化 | true / false |

## 一句话活动记录解析规则

用户输入示例："刚和云创王总通了电话，他们用友U8太老了，约下周三演示"

解析结果：
- activity_type: 电话
- summary: 与云创王总通话，了解到用友U8版本老旧
- result: 约定下周三演示
- next_stage_suggestion: 需求确认 → 方案演示
- key_extracted_info: `{"competitor_system": "用友U8", "next_meeting": "下周三"}`
