# B2B Sales Intelligent Assistant v3.1 (Analytics & Competition)

## Overview

Building on the Smart Enhanced edition, this version adds seven analytics and competition capabilities — Opportunity Health Scoring, Bottleneck Diagnosis, Competitive Response Scripts, Collaboration Snapshots, Internal Help Request Scripts, Role-Based Decision-Maker Communication, and Personal Performance Dashboard — evolving the sales workflow from "record-keeping" to "analytical."

## Version Information

| Item | Details |
|------|---------|
| Version | v3.1 |
| Codename | P2-Analytics & Competition |
| Release Tier | Advanced |
| Skill Name | `Sloth-Sales-Eido` |
| Based On | v2.1 (fully inherited) |
| Total Features | 16 |

## Feature List

### Core CRM Features (Inherited from v1.0, 5 items)

1. **Customer Mining & Info Enrichment** — Search and enrich customer information by region/industry/size (with Agent-Reach multi-platform data enhancement)
2. **Customer Information Management** — CRUD operations for customers, decision chains, and contacts
3. **Sales Funnel Management & Activity Logging** — Stage management and quick one-sentence activity logging
4. **Sales Methodology Application** — Supports SPIN/BANT/MEDDIC methodologies
5. **Data Export & Backup** — One-click export to Excel

### Smart Enhanced Features (Inherited from v2.0, 4 items)

6. **Intelligent Pre-Call Brief** — One-page customer briefing
7. **Personalized Value Proposition Generator** — 3 customized value points based on customer pain points
8. **Smart Meeting Minutes Processing** — Automatically extracts key information and updates the database
9. **Key Date & Compliance Reminders** — Automatically identifies and tracks important dates

### v3.0 New Features (7 items)

10. **Opportunity Health Scoring & Alerts** — Multi-dimensional health score calculation + dormant customer flagging
11. **Opportunity Bottleneck Diagnosis** — Comprehensive analysis of stall reasons with breakthrough recommendations
12. **Competitive Response & Script Generation** — Generates structured response scripts based on customer context (enhanced with Agent-Reach social media sentiment)
13. **Collaboration Snapshot** — 200-word summary for easy internal sharing
14. **Internal Help Request Script** — One-click generation of @colleague IM request scripts
15. **Role-Based Decision-Maker Communication** — Generates customized emails/scripts based on role-specific concerns
16. **Personal Performance Dashboard & Behavioral Feedback** — Performance statistics + behavioral diagnostics

## File Structure

```
Sloth-Sales-Eido/
├── SKILL.md              # Main instruction file (133 lines)
├── reference.md          # Data model (includes health scoring rules, diagnostic framework, role-based templates)
├── README.md             # This file
└── scripts/
    └── init_db.py        # Database initialization script (5 tables)
```

## Database Tables

| Table Name | Purpose | Introduced In |
|------------|---------|---------------|
| customers | Customer information | v1.0 |
| sales_funnel | Sales funnel | v1.0 |
| activity_log | Follow-up records | v1.0 |
| user_preferences | User preferences | v1.0 |
| **case_library** | **Case library** | **v3.0 New** |

## Installation

Copy the entire `Sloth-Sales-Eido/` directory to `~/.qoderwork/skills/`.

```bash
cp -r Sloth-Sales-Eido ~/.qoderwork/skills/
```

Upgrading from v1.0/v2.0: Simply overwrite the files and run `init_db.py` — it will automatically create the new `case_library` table without affecting existing data.

On first use, the Skill will automatically guide you through initialization. You can also run it manually:

```bash
python ~/.qoderwork/skills/Sloth-Sales-Eido/scripts/init_db.py
```

## Detailed Feature Descriptions

### 1. Customer Mining & Info Enrichment (v1.0)

Search for potential customers by region, industry, size, and other criteria. After online search, results are organized into structured information and support batch addition to the funnel. Available filter criteria include city/region, industry, size (headcount/revenue), and qualification tags (Specialized & Innovative SME, Above-Scale Enterprise, etc.).

### 2. Customer Information Management (v1.0)

CRUD operations for customer records, manage decision chains (role, influence, attitude), maintain contact information, and set priority watch flags. When a customer's contract expiration date is within 6 months, the system automatically prompts an engagement window opportunity.

### 3. Sales Funnel Management & Activity Logging (v1.0)

Manage sales funnel stages (Lead -> Initial Contact -> Needs Confirmed -> Solution Demo -> Negotiation -> Won/Lost). Supports quick one-sentence activity logging — the assistant automatically parses activity type, content summary, outcome, and recommended actions.

Funnel stages and default probabilities:

| Stage | Default Probability | Description |
|-------|-------------------|-------------|
| Lead | 10% | Initially identified potential customer |
| Initial Contact | 20% | First communication completed |
| Needs Confirmed | 40% | Customer needs clearly identified |
| Solution Demo | 60% | Product solution presented |
| Negotiation | 80% | Price/terms negotiation in progress |
| Won | 100% | Successfully signed |
| Lost | 0% | Deal not closed |

### 4. Sales Methodology Application (v1.0)

Supports three mainstream B2B sales methodologies, switchable at any time:

| Methodology | Core Framework | Applicable Scenarios |
|-------------|----------------|---------------------|
| SPIN | Situation -> Problem -> Implication -> Need-Payoff | Uncovering deep needs |
| BANT | Budget -> Authority -> Need -> Timeline | Quick opportunity qualification |
| MEDDIC | Metrics -> Economic Buyer -> Decision Criteria -> Decision Process -> Identify Pain -> Champion | Complex large-deal analysis |

Can automatically generate a structured question checklist for a specific customer based on the selected methodology.

### 5. Data Export & Backup (v1.0)

One-click export of the customers, sales_funnel, and activity_log tables to an Excel file (one sheet per table). The system automatically reminds you to back up every Friday.

### 6. Intelligent Pre-Call Brief (v2.0)

After the trigger phrase "Prepare visit for [Customer Name]," the system automatically generates a one-page briefing covering the following 5 sections:

1. **Company Overview & Updates**: Basic information + recent news from online search
2. **Current Solution & Pain Points**: Inferred business pain points based on the current_solution field
3. **Decision Chain Entry Points**: Key decision-maker attitude analysis and engagement strategy recommendations
4. **Structured Question Checklist**: Automatically generated targeted questions based on the selected methodology
5. **Reference Cases**: Matched success cases from the same industry and similar scale

Advanced usage: Generate a meeting invitation email draft based on the pre-call briefing content.

### 7. Personalized Value Proposition Generator (v2.0)

After the trigger phrase "Generate value proposition for [Customer Name]," the system outputs 3 highly customized value points based on the customer's current solution pain points. Suitable for email subject lines, proposal summary pages, phone openers, and demo introductions.

### 8. Smart Meeting Minutes Processing (v2.0)

After providing meeting content, the system automatically extracts key information such as competitors, budget, and timelines, updates database fields (current_solution, estimated_deal_value, decision_chain, key_extracted_info, etc.), and generates structured meeting minutes (discussion points + conclusions + action items), which are automatically saved to activity_log. When positive signals are detected, the assistant provides encouragement and milestone recommendations.

### 9. Key Date & Compliance Reminders (v2.0)

Automatically identifies key dates from follow-up records (quote validity, contract expiration, bid deadlines, demo schedules, payment milestones) and stores them in the key_date field. Each day during the first conversation, a list of key dates for the next 7 days is displayed.

### 10. Opportunity Health Scoring & Alerts (v3.0 New)

Automatically calculates a 0-100 score based on five dimensions — follow-up interval, action plan, relationship trend, pain point alignment, and budget signals — and alerts on customers scoring below 50 during the first daily conversation.

**Scoring Dimensions**:

| Dimension | Rule | Score Impact |
|-----------|------|--------------|
| Follow-up Interval | Over 7 days / Over 14 days | -15 / -30 |
| Action Plan | No next_action | -20 |
| Relationship Trend | relationship_score declining | -10 |
| Pain Point Alignment | Customer has legacy system or clear needs | +15 |
| Budget Signal | Budget signal present | +20 |

Base score is 70, range 0-100. When next_contact_date is overdue by >7 days and health score is <40, the customer is flagged as "Dormant — Needs Reactivation."

### 11. Opportunity Bottleneck Diagnosis (v3.0 New)

Analyzes five dimensions — activity logs, decision chain opponents, competitor involvement, budget gaps, and methodology gaps — to output a structured bottleneck report with breakthrough recommendations. Trigger phrase: "Analyze why [Customer Name] is stuck."

### 12. Competitive Response & Script Generation (v3.0 New)

Generates scripts following the five-step structure of "Acknowledge -> Differentiate -> Risk Alert -> Case Evidence -> Call to Action," combined with the customer's actual context. Trigger phrase: "The customer says [Competitor] is better, how should I respond?"

**Agent-Reach Social Media Sentiment Enhancement**: When the Agent-Reach skill is installed, the system automatically searches social media channels such as Twitter, Reddit, and V2EX for real-world user feedback and complaints about competitors. This real-time sentiment data serves as compelling evidence for the "Risk Alert" and "Case Evidence" steps of the response script, making competitive talk tracks significantly more persuasive.

### 13. Collaboration Snapshot (v3.0 New)

A structured customer summary within 200 words, covering basic information, current solution, core pain points, key contacts, and current stage. Can be directly copied and forwarded to pre-sales consultants, technical experts, or senior leadership.

### 14. Internal Help Request Script (v3.0 New)

One-click generation of @colleague help request scripts ready to copy into enterprise IM, including customer background, pain points, demo audience, scheduling, and key demo content.

### 15. Role-Based Decision-Maker Communication (v3.0 New)

Automatically adjusts content focus and language style based on the recipient's role:

| Role | Focus Areas | Language Style |
|------|-------------|---------------|
| Economic Decision Maker | ROI, strategic value, risk control | Concise, data-driven |
| Technical Evaluator | Performance, SLA, security, integration | Technical depth |
| End User | Ease of use, training, efficiency | Scenario-based |
| Procurement Executive | Price, terms, qualifications | Formal business |

### 16. Personal Performance Dashboard & Behavioral Feedback (v3.0 New)

Simply say "My performance" to see core metrics such as new leads, won deal amounts, and total funnel value with period-over-period changes, along with behavioral diagnostics (e.g., "70% of your phone follow-ups did not include a specific next-step action").

## Automated Reminders at Special Time Points

| Timing | Auto-Generated Content |
|--------|----------------------|
| First daily conversation | Key dates for the next 7 days + dormant customers |
| Monday morning | This week's follow-up list + health score alerts |
| Friday afternoon | This week's performance summary + behavioral feedback |
| 6 months before customer contract expiration | Engagement window reminder |
| Every Friday | Data backup reminder |

## Applicable Scenarios

- Already using core CRM and smart enhanced features, need deep analytics capabilities
- Facing complex opportunities that require bottleneck diagnosis
- Frequently encountering competitive situations, need structured response scripts
- Need internal collaboration and cross-role communication support
- Want to quantify personal sales performance and continuously improve

## Upgrade Path

v3.1 -> v4.1-P3-Complete Edition (adds 7 capabilities including Win/Loss Post-Mortem, News Monitoring, Case Matching, Team Management, and more)

## Optional Dependencies

- **Agent-Reach**: When installed, enhances customer mining and competitive response capabilities. In particular, Agent-Reach's social media intelligence channels (Twitter, Reddit, V2EX, etc.) provide real-time user feedback and sentiment data for competitive talk tracks, significantly improving their persuasiveness and timeliness. All features remain fully functional without Agent-Reach installed; only the social media sentiment enhancement is unavailable.
