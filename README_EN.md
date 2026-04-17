# B2B Sales Intelligent Assistant v2.1 (Smart Enhancement)

## Overview

Building on the core CRM foundation, this version adds four major capabilities: Intelligent Pre-Call Brief, Smart Meeting Minutes Processing, Personalized Value Proposition Generator, and Key Date & Compliance Reminders — significantly boosting sales efficiency before and after client meetings.

## Version Information

| Item | Details |
|------|---------|
| Version | v2.1 |
| Codename | P1-Smart Enhancement |
| Release Phase | Enhanced Edition |
| Skill Name | `Sloth-Sales-Eido` |
| Based On | v1.1 (fully inherited) |
| Total Features | 9 |

## Feature List

### Core CRM Features (Inherited from v1.0, 5 items)

1. **Customer Mining & Info Enrichment** — Search and enrich customer information by region/industry/scale, with Agent-Reach enhanced multi-platform online mining
2. **Customer Information Management** — CRUD operations for customers, decision chains, and contacts
3. **Sales Funnel Management & Activity Logging** — Stage management with one-sentence quick logging
4. **Sales Methodology Application** — Supports SPIN/BANT/MEDDIC methodologies
5. **Data Export & Backup** — One-click Excel export

### v2.0 New Features (4 items)

6. **Intelligent Pre-Call Brief** — One-page customer briefing with Agent-Reach real-time news collection
7. **Personalized Value Proposition Generator** — 3 customized value points based on customer pain points
8. **Smart Meeting Minutes Processing** — Automatically extracts key information and updates the database
9. **Key Date & Compliance Reminders** — Automatically identifies and tracks important dates

## File Structure

```
Sloth-Sales-Eido/
├── SKILL.md              # Main instruction file (128 lines)
├── reference.md          # Data model & field definitions (includes pre-call brief template, meeting minutes processing rules)
├── README.md             # This file
└── scripts/
    └── init_db.py        # Database initialization script (4 tables)
```

## Database Tables

| Table Name | Purpose |
|------------|---------|
| customers | Customer information |
| sales_funnel | Sales funnel |
| activity_log | Follow-up records |
| user_preferences | User preferences |

v2.0 stores automatically extracted key dates by enhancing the `sales_funnel.key_date` (JSON) field — no new tables required.

## Installation

Copy the entire `Sloth-Sales-Eido/` directory to `~/.qoderwork/skills/`.

```bash
cp -r Sloth-Sales-Eido ~/.qoderwork/skills/
```

If v1.0 is already installed, simply overwrite — the database is compatible and requires no migration.

On first use, the Skill will automatically guide you through initialization. You can also run it manually:

```bash
python ~/.qoderwork/skills/Sloth-Sales-Eido/scripts/init_db.py
```

## Detailed Feature Descriptions

### 1. Customer Mining & Info Enrichment (v1.0)

Search for potential customers by region, industry, scale, and other criteria. After performing an online search, the results are organized into structured information and can be batch-added to the funnel. Supported filter criteria include city/region, industry, scale (headcount/revenue), and qualification tags (e.g., Specialized & Innovative SMEs, above-scale enterprises, etc.).

### 2. Customer Information Management (v1.0)

Create, read, update, and delete customer records; manage decision chains (roles, influence, attitudes); maintain contact information; and set priority watch flags. When a customer's contract expiration date is less than 6 months away, the system automatically suggests it as a potential engagement window.

### 3. Sales Funnel Management & Activity Logging (v1.0)

Manage sales funnel stages (Lead -> Initial Contact -> Needs Confirmed -> Solution Demo -> Negotiation -> Won/Lost). Supports one-sentence quick logging of follow-up activities — the assistant automatically parses activity type, content summary, outcome, and suggested next actions.

Funnel stages and default probabilities:

| Stage | Default Probability | Description |
|-------|---------------------|-------------|
| Lead | 10% | Newly identified potential customer |
| Initial Contact | 20% | First communication completed |
| Needs Confirmed | 40% | Customer needs clearly identified |
| Solution Demo | 60% | Product solution presented |
| Negotiation | 80% | Entered price/terms negotiation |
| Won | 100% | Successfully signed |
| Lost | 0% | Deal did not close |

### 4. Sales Methodology Application (v1.0)

Supports three mainstream B2B sales methodologies, switchable at any time:

| Methodology | Core Framework | Use Case |
|-------------|----------------|----------|
| SPIN | Situation -> Problem -> Implication -> Need-Payoff | Uncovering deep needs |
| BANT | Budget -> Authority -> Need -> Timeline | Quickly qualifying opportunities |
| MEDDIC | Metrics -> Economic Buyer -> Decision Criteria -> Decision Process -> Identify Pain -> Champion | Complex enterprise deal analysis |

Can automatically generate a structured question list for a specific customer based on the selected methodology.

### 5. Data Export & Backup (v1.0)

One-click export of the customers, sales_funnel, and activity_log tables into an Excel file (one sheet per table). The system automatically reminds you to back up every Friday.

### 6. Intelligent Pre-Call Brief (New in v2.0)

Triggered by "Prepare visit for [Customer Name]", this feature automatically generates a one-page briefing covering 5 sections:

1. **Company Overview & Updates**: Basic information + recent news from online search
2. **Current Solution & Pain Points**: Inferred business pain points based on the current_solution field
3. **Decision Chain Entry Points**: Analysis of key decision-makers' attitudes with engagement strategy recommendations
4. **Structured Question List**: Automatically generated targeted questions based on the selected methodology
5. **Reference Cases**: Matched success stories from the same industry and similar scale

> When the Agent-Reach Skill is installed, the "Company Overview & Updates" section leverages Agent-Reach-driven real-time news collection (e.g., Exa AI search) to retrieve the latest corporate news, funding updates, and industry policy changes, making the briefing more timely and accurate.

### 7. Personalized Value Proposition Generator (New in v2.0)

Triggered by "Generate value proposition for [Customer Name]", this outputs 3 highly customized, ready-to-use value points based on the customer's current solution pain points. Suitable for email subject lines, proposal summary pages, phone call openers, and demo introductions.

### 8. Smart Meeting Minutes Processing (New in v2.0)

After providing meeting content, the system automatically extracts key information such as competitors, budget, and timelines, then updates database fields (current_solution, estimated_deal_value, decision_chain, key_extracted_info, etc.) and generates structured meeting minutes (discussion points + conclusions + action items), which are automatically saved to activity_log. When positive signals are detected, the assistant provides encouragement and milestone suggestions.

### 9. Key Date & Compliance Reminders (New in v2.0)

Automatically identifies key dates from follow-up records (quote validity periods, contract expiration dates, bid submission deadlines, demo/meeting schedules, payment milestones) and stores them in the key_date field. At the first conversation each day, the system displays a list of key dates for the upcoming 7 days.

## Optional Dependencies

- **Agent-Reach Skill** (recommended): Multi-platform online search capabilities that enhance customer mining depth and real-time news collection for pre-call briefings.

## Applicable Scenarios

- Sales teams with an established data foundation looking to improve pre- and post-visit efficiency
- Sales professionals who frequently visit clients and need to quickly generate preparation materials
- Teams that need to automatically extract and archive key business information from meetings
- Professionals managing multiple opportunities who need automatic tracking of key dates

## Upgrade Path

v2.1 -> v3.1-P2-Competitive Analysis (adds 7 new capabilities including health scoring, blocker diagnosis, competitive talk tracks, performance dashboard, and more)
