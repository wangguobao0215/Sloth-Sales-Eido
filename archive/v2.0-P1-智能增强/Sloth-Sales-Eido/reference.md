# B2B 销售智能助理 v2.0 - 数据模型参考

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
| qualification_tags | TEXT (JSON) | 资质标签 `{"专精特新": true, "规上企业": true}` |
| employee_count_range | TEXT | 人员规模区间 |
| revenue_last_3_years | TEXT (JSON) | 近三年营收（万元）`[5000, 6000, 7000]` |
| financial_status | TEXT | 良好/一般/预警 |
| procurement_category | TEXT | 采购品类 |
| current_solution | TEXT (JSON) | 当前方案（见下方结构） |
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
[{"name": "张三", "title": "IT总监", "phone": "138xxxx", "email": "zhang@co.com", "source": "官网"}]
```

#### decision_chain JSON 结构

```json
[{"name": "李总", "role_type": "经济决策者", "influence": 5, "attitude": "支持", "personal_focus": "预算控制"}]
```

- role_type：经济决策者 / 技术评估者 / 使用者 / 采购执行者 / 内线
- influence：1-5
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
| key_date | TEXT (JSON) | 关键日期数组（见下方） |
| priority | TEXT | 高/中/低 |
| owner | TEXT | 负责销售 |
| health_score | INTEGER | 健康分 0-100 |
| stuck_reason | TEXT | 卡顿原因 |
| created_at | TEXT | 创建时间 |
| updated_at | TEXT | 更新时间 |

#### key_date JSON 结构【v2.0 重点字段】

```json
[
  {"date": "2025-06-30", "event": "报价有效期截止", "status": "待处理"},
  {"date": "2025-07-15", "event": "投标文件递交截止", "status": "待处理"}
]
```

用于存储从跟进活动中自动提取的关键日期。

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
| summary | TEXT | 内容摘要 |
| result | TEXT | 达成结果 |
| relationship_score | INTEGER | 关系温度 1-10 |
| next_stage_suggestion | TEXT | 建议推进阶段 |
| tags | TEXT | 话术标签（逗号分隔） |
| key_extracted_info | TEXT (JSON) | 结构化提取信息 |

### user_preferences 用户偏好表

| 字段 | 类型 | 说明 |
|------|------|------|
| pref_key | TEXT PK | 偏好键（role/product_type/methodology/initialized） |
| pref_value | TEXT | 偏好值 |

## 拜访准备简报模板【v2.0 新增】

当用户触发"准备拜访【客户名】"时，按以下模板生成：

```
## 客户拜访简报：[公司名]
日期：[今日日期]

### 1. 公司概况
- 行业/规模/营收趋势
- 近期动态（联网搜索）

### 2. 当前方案与痛点
- 在用方案：[current_solution]
- 推测痛点：[基于方案年限/满意度推断]

### 3. 决策链
- [按角色展示已知决策人]
- 建议切入点：[基于态度和关注点]

### 4. 提问清单（[方法论]框架）
- Q1: [情境/预算/指标问题]
- Q2: [难点/权限/经济买家问题]
- Q3: [暗示/需求/决策标准问题]
- Q4: [效益/时间/支持者问题]

### 5. 参考案例
- [行业+规模相似的成功案例]
```

## 会议纪要处理规则【v2.0 新增】

从用户提供的会议内容中，自动提取并更新：

| 识别信号 | 更新目标 |
|----------|----------|
| 提到具体系统名称/版本 | 更新 current_solution |
| 提到竞品名称 | 记入 key_extracted_info |
| 提到预算/金额 | 更新 estimated_deal_value |
| 提到时间节点 | 存入 key_date |
| 决策人态度变化 | 更新 decision_chain.attitude |
| 明确需求/认可产品 | 建议推进漏斗阶段 |

识别到积极信号时，在回应中给予正向反馈。
