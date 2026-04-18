# B2B 销售智能助理 v1.1（核心CRM版）

## 概述

B2B 销售智能助理的基础版本，提供客户信息管理、销售漏斗推进和跟进记录三大核心能力，是整个销售工作台的数据底盘。

## 版本信息

| 项目 | 内容 |
|------|------|
| 版本号 | v1.1 |
| 代号 | P0-核心CRM |
| 发布阶段 | 基础版 |
| Skill 名称 | `Sloth-Sales-Eido` |

## 功能清单

1. **客户挖掘与信息补全（Agent-Reach增强）** — 按区域/行业/规模搜索并补全客户信息，集成Agent-Reach多平台搜索
2. **客户信息管理** — 增删改查客户、决策链、联系人
3. **销售漏斗推进与活动记录** — 阶段管理、一句话快速记录
4. **销售方法论应用** — 支持 SPIN/BANT/MEDDIC 三种方法论
5. **数据导出与备份** — 一键导出 Excel

## 文件结构

```
Sloth-Sales-Eido/
├── SKILL.md              # 主指令文件（97行）
├── reference.md          # 数据模型与字段定义
├── README.md             # 本文件
└── scripts/
    └── init_db.py        # 数据库初始化脚本（4张表）
```

## 可选依赖

- **Agent-Reach Skill**（推荐安装）：多平台联网搜索能力，增强客户挖掘深度。安装方法：在 QoderWork 技能商店搜索 `agent-reach` 并安装。

## 数据库表

| 表名 | 用途 |
|------|------|
| customers | 客户信息 |
| sales_funnel | 销售漏斗 |
| activity_log | 跟进记录 |
| user_preferences | 用户偏好 |

## 安装

将 `Sloth-Sales-Eido/` 整个目录复制到 `~/.qoderwork/skills/` 下即可。

```bash
cp -r Sloth-Sales-Eido ~/.qoderwork/skills/
```

首次使用时，Skill 会自动引导初始化。也可手动运行：

```bash
python ~/.qoderwork/skills/Sloth-Sales-Eido/scripts/init_db.py
```

## 适用场景

- 刚开始使用销售助理，需要先搭建数据底盘
- 团队试点阶段，验证核心 CRM 流程
- 销售人员对 AI 工具尚不熟悉，需要简单易上手的版本

## 升级路径

v1.1 → v2.1-P1-智能增强（新增拜访准备、会议纪要、价值主张、关键日期提醒）
