# B2B Sales Intelligent Assistant v1.1 (Core CRM)

## Overview

The foundational version of the B2B Sales Intelligent Assistant, providing three core capabilities: Customer Information Management, Sales Funnel Management, and Follow-up Logging. It serves as the data backbone of the entire sales workbench.

## Version Information

| Item | Details |
|------|---------|
| Version | v1.1 |
| Code Name | P0-Core CRM |
| Release Stage | Base Edition |
| Skill Name | `Sloth-Sales-Eido` |

## Feature List

1. **Customer Mining & Info Enrichment (Agent-Reach Enhanced)** -- Search and enrich customer information by region/industry/company size, integrated with Agent-Reach multi-platform search
2. **Customer Information Management** -- Full CRUD operations for customers, decision chains, and contacts
3. **Sales Funnel Management & Activity Logging** -- Stage management and quick one-liner activity logging
4. **Sales Methodology Application** -- Supports SPIN/BANT/MEDDIC methodologies
5. **Data Export & Backup** -- One-click export to Excel

## File Structure

```
Sloth-Sales-Eido/
├── SKILL.md              # Main instruction file (97 lines)
├── reference.md          # Data model & field definitions
├── README.md             # This file
└── scripts/
    └── init_db.py        # Database initialization script (4 tables)
```

## Optional Dependencies

- **Agent-Reach Skill** (Recommended): Multi-platform online search capability that enhances customer mining depth. Installation: Search for `agent-reach` in the QoderWork Skill Store and install it.

## Database Tables

| Table Name | Purpose |
|------------|---------|
| customers | Customer information |
| sales_funnel | Sales funnel |
| activity_log | Follow-up activity records |
| user_preferences | User preferences |

## Installation

Copy the entire `Sloth-Sales-Eido/` directory to `~/.qoderwork/skills/`.

```bash
cp -r Sloth-Sales-Eido ~/.qoderwork/skills/
```

On first use, the Skill will automatically guide you through initialization. You can also run it manually:

```bash
python ~/.qoderwork/skills/Sloth-Sales-Eido/scripts/init_db.py
```

## Use Cases

- Getting started with the sales assistant and need to set up the data backbone first
- Team pilot phase to validate the core CRM workflow
- Sales reps who are not yet familiar with AI tools and need a simple, easy-to-use version

## Upgrade Path

v1.1 -> v2.1-P1-Smart Enhancement (adds visit preparation, meeting minutes, value proposition, and key date reminders)
