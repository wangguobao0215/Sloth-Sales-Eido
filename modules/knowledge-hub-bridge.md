# Sloth-Sales-Eido Knowledge Hub Bridge

> B2B 销售助手 × 中央知识库集成协议（v2.0.0 — 双树架构）
> 仅当 EXTEND.md 中 `knowledge_hub.enabled = true` 时生效。

---

## 知识结晶点（Skill → Hub）

当以下操作完成后，AI **应当**向用户展示预填好的萃取建议卡片，经用户确认后写入中央库。

> v1.0 阶段仅激活 `priority: high` 的结晶点。`medium`/`low` 级别为 opt-in，用户可在 EXTEND.md 中配置。

| 触发条件 | 产出 asset_type | 目标节点 | priority | 萃取要素 |
|---------|----------------|---------|----------|---------|
| 赢单复盘（Won Deal Review） | `case_study` | C2 + S*（视客户行业） | **high** | 客户背景、决策链、关键赢因、竞对情况、成交策略 |
| 丢单复盘（Lost Deal Review） | `lesson_learned` | C2 + S*（视客户行业） | **high** | 客户背景、丢单原因、竞对优势、改进建议 |
| 新打法验证成功 | `best_practice` | C2 | medium | 打法描述、适用场景、效果数据、可复制条件 |
| 客户异议处理成功 | `playbook` | C2 | medium | 异议类型、处理话术、客户反应、成功关键 |

### 萃取规则

> 工作流：AI 检测到结晶点 → 预填萃取卡片（含 title/summary/confidence） → 用户确认或微调 → 提交注册。用户可选择「跳过本次」但系统会在下次相同场景再次提示。

1. **赢单复盘 → case_study**：
   - `title`："{客户名} 赢单案例 - {产品/方案}"
   - `summary`：核心赢因和可复制策略
   - `industry`：从客户行业直接提取
   - `capability_node`：`C2`（销售方法论）
   - `scenario_nodes`：根据客户行业映射（如汽车制造客户 → `["S4"]`；涉及质量场景 → `["S4", "S5"]`）
   - `scope`：`L2`（具体案例，关联到场景子节点）
   - `sensitivity`：`internal`（含客户信息，默认内部）
   - `customer_type`：从客户画像提取
   - `confidence`：A（有完整成交数据）; B（部分信息缺失）
   - `content`：客户背景 → 需求痛点 → 竞争格局 → 我方策略 → 成交关键因素 → 可复制要素
   - `applicable_skills`：`[Sloth-PSC-Eido, Sloth-MGO-Eido, Sloth-DeliveryMatrix-Eido]`

2. **丢单复盘 → lesson_learned**：
   - `title`："{客户名} 丢单复盘 - {根因简述}"
   - `summary`：丢单根因和关键教训
   - `capability_node`：`C2`（销售方法论）
   - `scenario_nodes`：根据客户行业映射（如制造业客户 → `["S4"]`）
   - `scope`：`L2`
   - `sensitivity`：`internal`
   - `confidence`：B（含客户反馈）; C（纯内部推测）
   - `content`：丢单时间线 → 根因分析 → 竞对做对了什么 → 我们的改进空间
   - `applicable_skills`：`[Sloth-PSC-Eido, Sloth-HybridDev-Eido]`

3. **新打法 → best_practice**（medium）：
   - `title`："{打法名称} 销售最佳实践"
   - `summary`：打法核心要点和适用条件
   - `capability_node`：`C2`（销售方法论）
   - `scenario_nodes`：`[]`（通用销售方法，不绑定特定场景；若打法针对特定行业可按需填写）
   - `scope`：`L1`
   - `sensitivity`：`internal`
   - `tags`：`[sales-tactic, {适用阶段}]`

4. **异议处理 → playbook**（medium）：
   - `title`："{异议类型} 异议处理 Playbook"
   - `summary`：异议类型、关键话术和成功率
   - `capability_node`：`C2`（销售方法论）
   - `scenario_nodes`：`[]`（通用异议处理；若针对特定业务场景可按需填写）
   - `scope`：`L2`
   - `sensitivity`：`internal`
   - `tags`：`[objection-handling, {异议类别}]`

---

## 知识需求点（Hub → Skill）

当用户启动以下操作时，AI **应当**先查询中央库获取相关知识推荐。

| 触发条件 | 查询维度 | 上下文信号 |
|---------|---------|----------|
| 启动客户跟进 / 准备拜访 | `scenario_node` 按客户行业匹配（如制造业 → S4）获取同场景 case_study + competitive_intel；`capability_node = C2` 获取销售方法论 | 客户行业、客户规模、涉及竞对 |
| 启动商机推进（阶段变更） | `capability_node = C2` 查询 best_practice (sales tactics) + playbook | 当前漏斗阶段、卡点描述 |
| 录入新客户 | `scenario_node` 按客户行业匹配获取 case_study + product_brief | 客户行业 |
| 准备报价/方案 | `scenario_node` 按客户行业匹配获取 case_study (similar deal size) + competitive_intel；`capability_node = C2` 获取报价策略 | 竞对、客户规模 |

### 推荐展示规则

> 有匹配结果时展示推荐卡片（最多 3 条），用户可选择查看详情或直接继续。无匹配则静默跳过。
> query_registry 支持 `scenario_node` L1 前缀匹配（查询 S4 自动返回 S4 + S4.1 + S4.2 + S4.3 + S4.4 全部资产）。

1. **拜访准备**：优先按 `scenario_node` 推荐同行业场景的赢单案例和竞争情报，为销售提供话术弹药。
2. **商机推进**：按 `capability_node = C2` 推荐同阶段的最佳实践和异议处理 Playbook，帮助突破卡点。
3. **新客户**：按 `scenario_node` 推荐相关产品简报和同行业案例，加速破冰。
4. **报价准备**：组合 `scenario_node` + `capability_node` 推荐竞对定价情报和类似规模的成交案例作为定价参考。

---

## 反馈通道

当用户在本 Skill 中引用了 Hub 推荐的知识资产后，AI 应当在任务完成时询问："这条知识对你有帮助吗？（有用 / 过时 / 有误）"，并通过 `record_feedback.py` 记录反馈，驱动知识质量自动演化。
