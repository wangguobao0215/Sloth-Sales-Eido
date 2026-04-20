# B2B Sales Intelligent Assistant v4.1 (Full Edition)

## Overview

The full edition of the B2B Sales Intelligent Assistant covers the complete sales process from lead mining to win/loss review, featuring 22+ core capabilities. Building on the Analysis & Competition edition, it adds Win/Loss Review & Handover, Customer News & Sentiment Monitoring, Benchmark Case Smart Matching, Industry Policy & Incentive Alerts, Case Library Management, and Sales Team Leader Functions.

## Version Information

| Item | Details |
|------|---------|
| Version | v4.1 |
| Codename | P3-Full Edition |
| Release Stage | General Availability |
| Skill Name | `Sloth-Sales-Eido` |
| Based On | v3.1 (fully inherited) |
| Total Features | 22+ |

## Feature List

### Core CRM Features (Inherited from v1.0, 5 items)

1. **Customer Mining & Info Enrichment** -- Search and enrich customer info by region/industry/scale (enhanced with Agent-Reach omnichannel capabilities)
2. **Customer Information Management** -- CRUD for customers, decision chains, and contacts
3. **Sales Funnel Management & Activity Logging** -- Stage management, one-sentence quick logging
4. **Sales Methodology Application** -- Supports SPIN/BANT/MEDDIC methodologies
5. **Data Export & Backup** -- One-click Excel export

### Intelligent Enhancement Features (Inherited from v2.0, 4 items)

6. **Intelligent Pre-Call Brief** -- One-page customer briefing
7. **Personalized Value Proposition Generator** -- 3 tailored value points based on customer pain points
8. **Smart Meeting Minutes Processing** -- Auto-extract key information and update the database
9. **Key Date & Compliance Reminders** -- Auto-detect and track important dates

### Analysis & Competition Features (Inherited from v3.0, 7 items)

10. **Opportunity Health Scoring & Alerts** -- Multi-dimensional health score + dormant customer flagging
11. **Opportunity Bottleneck Diagnosis** -- Comprehensive root-cause analysis with breakthrough recommendations
12. **Competitive Response & Script Generation** -- Structured response scripts based on customer context
13. **Collaboration Snapshot** -- 200-word summary for internal forwarding
14. **Internal Help Request Script** -- One-click IM script for @-mentioning colleagues
15. **Role-Based Decision-Maker Communication** -- Customized emails/scripts by stakeholder role
16. **Personal Performance Dashboard & Behavioral Feedback** -- Performance stats + behavioral insights

### v4.0 New Features (7 items)

17. **Win/Loss Review & Handover** -- Generate handover checklists on wins; capture competitive intel on losses
18. **Customer News & Sentiment Monitoring** -- News scanning for key watched customers via Agent-Reach omnichannel (LinkedIn/WeChat Official Accounts/Twitter/Weibo, etc.)
19. **Benchmark Case Smart Matching** -- Match best cases based on customer profile
20. **Industry Policy & Incentive Alerts** -- Web search for local industry subsidy policies
21. **Case Library Management** -- Single-entry and bulk CSV import of success cases
22. **Sales Team Leader Functions** -- 18 team management capabilities (Duplicate Account Detection, Team Funnel Dashboard, Sales Forecast Grading, etc.)

## File Structure

```
Sloth-Sales-Eido/
├── SKILL.md              # Main instruction file (178 lines)
├── reference.md          # Complete data model & rules reference
├── examples.md           # 7 full interaction examples
├── README.md             # Chinese README
├── README_EN.md          # This file (English)
├── 用户使用手册.md         # Detailed user guide (Chinese)
├── User_Guide.md         # Detailed user guide (English)
└── scripts/
    └── init_db.py        # Database initialization script (5 tables)
```

## Database Tables

| Table | Purpose | Introduced In |
|-------|---------|---------------|
| customers | Customer information | v1.0 |
| sales_funnel | Sales funnel | v1.0 |
| activity_log | Follow-up records | v1.0 |
| user_preferences | User preferences | v1.0 |
| case_library | Case library | v3.0 |

## Installation

Copy the entire `Sloth-Sales-Eido/` directory to `~/.qoderwork/skills/`.

```bash
cp -r Sloth-Sales-Eido ~/.qoderwork/skills/
```

To upgrade from any previous version: overwrite the files, then run `init_db.py` to automatically create any missing tables. Existing data is fully preserved.

On first use, the Skill will automatically guide you through initialization. You can also initialize manually:

```bash
python ~/.qoderwork/skills/Sloth-Sales-Eido/scripts/init_db.py
```

## Dependencies

- Python 3.8+ (for database operations and Excel generation)
- openpyxl (for Excel export; install via `pip install openpyxl`)
- Internet access (for customer mining, news scanning, and policy search)

## Optional Dependencies

- **Agent-Reach** (strongly recommended): An omnichannel internet access Skill covering 17 platform channels, providing comprehensive data sources for customer mining, sentiment monitoring, and external intelligence scanning. Supported channels include: search engines (Exa AI), social media (Xiaohongshu/Douyin/Weibo/Twitter/Bilibili/V2EX/Reddit), professional networking (LinkedIn), developer platforms (GitHub), web & articles (web scraping/WeChat Official Accounts/RSS), and video platforms (YouTube/Bilibili/Podcasts). Once Agent-Reach is installed, v4.1's customer mining, sentiment monitoring, and team intelligence scanning features will automatically leverage omnichannel search capabilities, significantly improving information coverage and timeliness.

## Two User Roles

v4.1 supports two roles, selected during the initial setup:

| Role | Available Features |
|------|--------------------|
| Field Sales Rep | All personal features (items 1--21) |
| Sales Team Leader | All personal features + 18 team management features |

## Detailed Feature Descriptions

### 1. Customer Mining & Info Enrichment (v1.0)

Search for potential customers by region, industry, scale, and other criteria. Results are structured after web searches and can be added to the funnel in bulk. Available filters include city/region, industry, scale (headcount/revenue), and qualification tags (e.g., Specialized & Innovative SME, Above-Scale Enterprise).

### 2. Customer Information Management (v1.0)

Create, read, update, and delete customer records. Manage decision chains (role, influence level, attitude), maintain contact information, and set watch-list flags. When a customer's contract expiry is within 6 months, the system automatically prompts an engagement-window alert.

### 3. Sales Funnel Management & Activity Logging (v1.0)

Manage sales funnel stages (Lead -> Initial Contact -> Needs Confirmed -> Solution Demo -> Negotiation -> Won/Lost). Supports one-sentence quick activity logging; the assistant auto-parses activity type, content summary, outcome, and recommended next action.

Funnel stages and default probabilities:

| Stage | Default Probability | Description |
|-------|---------------------|-------------|
| Lead | 10% | Newly identified potential customer |
| Initial Contact | 20% | First communication completed |
| Needs Confirmed | 40% | Customer needs clarified |
| Solution Demo | 60% | Product/solution presented |
| Negotiation | 80% | Price/terms negotiation underway |
| Won | 100% | Contract signed |
| Lost | 0% | Deal not closed |

### 4. Sales Methodology Application (v1.0)

Supports three mainstream B2B sales methodologies, switchable at any time:

| Methodology | Core Framework | Best For |
|-------------|----------------|----------|
| SPIN | Situation -> Problem -> Implication -> Need-Payoff | Uncovering deep needs |
| BANT | Budget -> Authority -> Need -> Timeline | Quickly qualifying opportunities |
| MEDDIC | Metrics -> Economic Buyer -> Decision Criteria -> Decision Process -> Identify Pain -> Champion | Complex deal analysis |

Can auto-generate structured question lists for a specific customer based on the selected methodology.

### 5. Data Export & Backup (v1.0)

One-click export of the customers, sales_funnel, and activity_log tables to an Excel file (one sheet per table). The system automatically reminds you to back up every Friday.

### 6. Intelligent Pre-Call Brief (v2.0)

Triggered by "Prepare visit [customer name]". Automatically generates a one-page briefing with 5 sections:

1. **Company Overview & News**: Basic info + recent news from web search
2. **Current Solution & Pain Points**: Inferred business pain points based on the current_solution field
3. **Decision Chain Entry Points**: Key decision-maker attitude analysis and engagement strategy recommendations
4. **Structured Question List**: Auto-generated targeted questions based on your chosen methodology
5. **Reference Cases**: Matched success cases from the same industry and scale

Advanced usage: generate a meeting invitation email draft based on the pre-call brief content.

### 7. Personalized Value Proposition Generator (v2.0)

Triggered by "Generate value proposition [customer name]". Outputs 3 highly customized, ready-to-use value points based on the customer's current solution pain points. Suitable for email subject lines, proposal summary pages, phone openers, and demo introductions.

### 8. Smart Meeting Minutes Processing (v2.0)

After a meeting, provide the meeting content and the assistant auto-extracts key information such as competitors, budget, and timelines. It updates database fields (current_solution, estimated_deal_value, decision_chain, key_extracted_info, etc.) and generates structured minutes (discussion points + conclusions + action items), automatically saving them to activity_log. When positive signals are detected, the assistant provides encouragement and milestone suggestions.

### 9. Key Date & Compliance Reminders (v2.0)

Automatically identifies key dates from follow-up records (quote validity period, contract expiry, bid deadline, demo schedule, payment milestones) and stores them in the key_date field. During the first conversation each day, a list of key dates within the next 7 days is displayed.

### 10. Opportunity Health Scoring & Alerts (v3.0)

Automatically calculates a 0--100 score (base score: 70) across five dimensions: follow-up interval, action plan, relationship trend, pain-point match, and budget signal. Customers scoring below 50 are flagged during the first daily conversation.

Scoring dimensions:

| Dimension | Rule | Score Impact |
|-----------|------|--------------|
| Follow-up Interval | Over 7 days / Over 14 days | -15 / -30 |
| Action Plan | No next_action | -20 |
| Relationship Trend | relationship_score declining | -10 |
| Pain-Point Match | Customer has legacy system or explicit need | +15 |
| Budget Signal | Budget signal present | +20 |

When next_contact_date is overdue by >7 days and health score <40, the customer is flagged as "Dormant -- Needs Reactivation".

### 11. Opportunity Bottleneck Diagnosis (v3.0)

Analyzes five dimensions -- activity logs, decision-chain objectors, competitor involvement, budget gaps, and methodology gaps -- to produce a structured bottleneck report with breakthrough recommendations. Trigger phrase: "Analyze why [customer name] is stuck".

### 12. Competitive Response & Script Generation (v3.0)

Generates response scripts following a five-step structure: "Acknowledge -> Differentiate -> Risk Alert -> Case Evidence -> Call to Action", tailored to the customer's specific situation. Trigger phrase: "The customer says [competitor] is better, how should I respond?"

### 13. Collaboration Snapshot (v3.0)

A structured customer summary within 200 words, covering basic info, current solution, core pain points, key contacts, and current stage. Can be directly copied and forwarded to pre-sales consultants, technical experts, or senior management.

### 14. Internal Help Request Script (v3.0)

One-click generation of an @-mention help request script ready to paste into enterprise IM, including customer background, pain points, demo audience, scheduling, and key demo highlights.

### 15. Role-Based Decision-Maker Communication (v3.0)

Automatically adjusts content focus and language style based on the recipient's role:

| Role | Focus Areas | Language Style |
|------|-------------|----------------|
| Economic Decision Maker | ROI, strategic value, risk control | Concise, data-driven |
| Technical Evaluator | Performance, SLA, security, integration | Technical depth |
| End User | Ease of use, training, efficiency | Scenario-based |
| Procurement Executive | Price, terms, qualifications | Business-formal |

### 16. Personal Performance Dashboard & Behavioral Feedback (v3.0)

Simply say "My performance" to see core metrics such as new leads, won deal amount, total funnel value, and month-over-month changes, along with behavioral diagnostic suggestions.

### 17. Win/Loss Review & Handover (v4.0 New)

**Won**: Automatically guides generation of a customer handover checklist (signed commitments, contact communication preferences, risk points, service recommendations). Supports setting fulfillment milestone dates (first payment, kickoff meeting, acceptance, etc.), which are included in daily reminders.

**Lost**: Automatically asks two follow-up questions (which competitor was chosen, primary reason). Answers are stored in the log in JSON format, and trends can be viewed later via "Loss Reason Analysis".

### 18. Customer News & Sentiment Monitoring (v4.0 New)

Performs web news scanning for customers with the "monitor" flag set. Identifies executive changes, financing/IPO events, new factories/expansion, and negative news. Outputs a one-line briefing + action recommendation. Trigger phrases: "Show me updates on my watched customers" or "News scan".

In v4.1, sentiment monitoring coverage is significantly enhanced through Agent-Reach omnichannel search, with the following supported channels:

- **Exa AI**: Deep search for enterprise news and industry trends
- **WeChat Official Accounts**: Corporate official account articles, industry media coverage
- **Twitter/Weibo**: Brand sentiment, executive social media activity
- **LinkedIn**: Key contact job changes, corporate HR announcements
- **Jina Reader**: Full-text reading and parsing of industry media articles

### 19. Benchmark Case Smart Matching (v4.0 New)

Matches the 1--2 most similar cases from the case library based on customer profile (industry, scale, procurement category, existing solution). Outputs a customer-specific scenario description and recommended storytelling approach. When the case library is empty, the assistant guides you to build it.

### 20. Industry Policy & Incentive Alerts (v4.0 New)

During pre-call briefs or customer reviews, the assistant automatically searches the web for local industry subsidy policies (e.g., "Smart Manufacturing Transformation" grants) as an additional value point for customer conversations. Manual search for specific industry policies is also supported.

### 21. Case Library Management (v4.0 New)

Supports two methods for building the case library: guided single-entry input (industry, scale, existing solution, core pain points, our solution, quantifiable benefits, customer testimonial) and bulk CSV import.

### 22. Sales Team Leader Functions (v4.0 New)

Activated only when the role is set to "Sales Team Leader". Data aggregation method: each sales rep periodically exports personal data as Excel; the team leader uploads them, and the assistant auto-merges, deduplicates, and generates team dashboards.

**18 Team Management Capabilities**:

Dashboards & Statistics: Team Funnel Dashboard, Team Performance Dashboard, Activity Volume Audit, Sales Forecast Grading (Commit/Best Case/Pipeline).

Alerts & Detection: Duplicate Account Detection (fuzzy matching for duplicate customer coverage), Stagnant Opportunity Alert (overdue >14 days, grouped by sales rep), Renewal/Upsell Alert, Sales Workload Monitor (flagging reps with >15 concurrent opportunities and <5 weekly activities).

Analysis & Diagnosis: Loss Reason Analysis (distribution of lost_to and reason), Pipeline Bottleneck Diagnosis (conversion rates per stage), Sales Capability Benchmarking (five-dimension scoring), Pre-Sales Resource ROI Ranking (sorted by "deal amount x probability").

Intelligence & Collaboration: External intelligence scanning (Agent-Reach omnichannel search for industry bids/policies matched to customer base), custom alert rules, generate sales feedback (structured recognition & suggestions), generate team weekly report (funnel + updates + risks + next-week priorities), export team summary spreadsheet.

## Automatic Time-Based Reminders

| Timing | Auto-Generated Content |
|--------|------------------------|
| First conversation each day | Key dates in the next 7 days + dormant customers |
| Monday morning each week | This week's follow-up list + health score alerts |
| Friday afternoon each week | This week's performance summary + behavioral feedback |
| 6 months before customer contract expiry | Engagement-window reminder |
| Every Friday | Data backup reminder |

## Version History

| Version | Codename | New Capabilities | Cumulative Capabilities |
|---------|----------|------------------|-------------------------|
| v1.0 | P0-Core CRM | 5 | 5 |
| v2.0 | P1-Intelligent Enhancement | 4 | 9 |
| v3.0 | P2-Analysis & Competition | 7 | 16 |
| v4.0 | P3-Full Edition | 7 | 22+ |
| v4.1 | P3-Full Edition (Agent-Reach Enhanced) | Agent-Reach omnichannel integration | 22+ |

## References

- Complete data model: [reference.md](reference.md)
- Interaction examples: [examples.md](examples.md)
- User guide: [User_Guide.md](User_Guide.md)
