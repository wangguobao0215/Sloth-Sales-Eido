# B2B Sales Intelligent Assistant v2.1 User Guide

## Quick Start

### Step 1: First Launch

After opening the conversation, the assistant will automatically guide you through the initial setup:

1. Select your role (Frontline Sales / Sales Team Lead)
2. Select the product type you sell (Software, Industrial Equipment, Professional Services, etc.)
3. Choose your preferred sales methodology (SPIN / BANT / MEDDIC)
4. Choose whether to import an existing customer list

Once complete, your sales workstation is ready to go.

### Step 2: Add Your First Customer

You can get started using any of the following methods:

**Method 1: Direct Entry**
> "Add customer: Suzhou Yunchuang Tech, electronic components manufacturing, 300 employees"

**Method 2: Batch Mining**
> "Find me manufacturing companies in Suzhou with revenue above 50 million RMB"

**Method 3: Import a List**
> Upload an Excel/CSV file, and the assistant will automatically parse and enrich the information

---

## Feature Details

### 1. Customer Mining & Info Enrichment (v1.0)

**Trigger**: Describe your target customer criteria

**Example Dialog**:
> User: "Find me manufacturing companies in Hangzhou with revenue above 50 million RMB"
>
> Assistant: (after online search) I've compiled 34 potential customers. Here's a preview... You can download the full Excel file, or say "Add all to funnel."

**Supported Filter Criteria**:

- City/Region
- Industry
- Scale (headcount, revenue)
- Qualification tags (e.g., Specialized & Innovative SMEs, above-scale enterprises, etc.)

> When the Agent-Reach Skill is installed, customer mining leverages multi-platform online search (e.g., Exa AI) to retrieve richer, more accurate enterprise information, significantly improving mining depth and data quality.

### 2. Customer Information Management (v1.0)

**Query Customers**:
> "View Suzhou Yunchuang Tech's information"
> "Search for customers with 'Yunchuang' in the name"

**Edit Information**:
> "Update Yunchuang Tech's contact: IT Director Mr. Li, phone 138xxxx"
> "Set Yunchuang Tech's decision chain: Mr. Li is the technical evaluator, influence level 4, attitude supportive"

**Monitor Customers**:
> "Monitor this company" (sets the priority watch flag)

**Contract Expiration Alert**: When a customer's contract expiration date is less than 6 months away, the system will automatically prompt "Contract expiring soon — this may be an engagement window."

### 3. Sales Funnel Management & Activity Logging (v1.0)

**Funnel Stage Descriptions**:

| Stage | Default Probability | Description |
|-------|---------------------|-------------|
| Lead | 10% | Newly identified potential customer |
| Initial Contact | 20% | First communication completed |
| Needs Confirmed | 40% | Customer needs clearly identified |
| Solution Demo | 60% | Product solution presented |
| Negotiation | 80% | Entered price/terms negotiation |
| Won | 100% | Successfully signed |
| Lost | 0% | Deal did not close |

**Quick Activity Logging (One-Sentence Mode)**:
> "Called Mr. Wang at Yunchuang today — their Yonyou U8 is too old, scheduled a demo for next Wednesday"

The assistant will automatically parse:
- Activity type: Phone call
- Content summary: Learned that their Yonyou U8 version is outdated
- Outcome: Demo scheduled for next Wednesday
- Suggested action: Advance funnel stage, update customer solution information

**View Funnel Dashboard**:
> "Show my funnel overview"
> "Which customers need follow-up this week?"

### 4. Sales Methodology Application (v1.0)

**Generate Question List**:
> "Prepare SPIN methodology questions for Yunchuang Tech"

**Switch Methodology**:
> "Set methodology to BANT"

**Methodology Comparison**:

| Methodology | Core Framework | Use Case |
|-------------|----------------|----------|
| SPIN | Situation -> Problem -> Implication -> Need-Payoff | Uncovering deep needs |
| BANT | Budget -> Authority -> Need -> Timeline | Quickly qualifying opportunities |
| MEDDIC | Metrics -> Economic Buyer -> Decision Criteria -> Decision Process -> Identify Pain -> Champion | Complex enterprise deal analysis |

### 5. Data Export & Backup (v1.0)

**Export Data**:
> "Export data"

The system will export the customers, sales_funnel, and activity_log tables into a single Excel file (one sheet per table) and provide it for download.

**Backup Reminders**: The system automatically reminds you to back up your data every Friday.

---

### 6. Intelligent Pre-Call Brief (New in v2.0)

**Trigger**:
> "Prepare visit for Suzhou Yunchuang Tech"
> "Yunchuang Tech visit preparation"

**Generated Content**:

The assistant will automatically generate a one-page briefing containing 5 sections:

**1. Company Overview & Updates**: Basic information (industry, scale, revenue) and recent news from online search.

> With Agent-Reach's Exa AI search, the "Company Overview & Updates" section of the briefing will include the latest corporate news, funding updates, and industry policy changes.

**2. Current Solution & Pain Points**: Inferred business pain points based on the recorded `current_solution` field. For example:
> "Currently using Yonyou U8 V13.0 (deployed in 2018, running for 8 years). Inferred pain points: difficulty in multi-plant coordination, outdated version unable to meet new business requirements."

**3. Decision Chain Entry Points**: Displays known key decision-makers and their attitudes, with recommended engagement strategies.

**4. Structured Question List**: Automatically generated targeted questions based on your selected methodology (SPIN/BANT/MEDDIC).

**5. Reference Cases**: At least one matched success story from the same industry and similar scale for reference.

**Advanced Usage**:
> "Help me draft a meeting invitation email for Yunchuang Tech"

The assistant can generate a meeting agenda email draft based on the pre-call brief content, ready for you to copy and send.

---

### 7. Personalized Value Proposition Generator (New in v2.0)

**Trigger**:
> "Generate value proposition for Suzhou Yunchuang Tech"

**Output Format**:

The assistant will generate 3 highly customized value points based on the customer's current solution, pain points, and industry characteristics. For example:

> For Suzhou Yunchuang Tech, currently using Yonyou U8 V13.0 (deployed in 2018):
> 1. "Resolve the bottleneck where U8's multi-plant coordination causes month-end closing cycles of up to 7 days."
> 2. "No need to replace the existing ERP — achieve real-time data integration with MES through an integration layer."
> 3. "Local service team responds within 2 hours, avoiding delays from the original vendor's support."

**Use Cases**: Email subject lines, proposal summary pages, phone call openers, demo introductions.

---

### 8. Smart Meeting Minutes Processing (New in v2.0)

**Trigger**: After a meeting, directly input the meeting content or key points.

**Example Dialog**:
> User: "Had a technical exchange meeting with Mr. Li at Yunchuang today. Mr. Li said their biggest issue with U8 is that data doesn't sync across plants, and month-end closing takes 7 days. They have IT budget for next year Q1, around 500K RMB. Mr. Li personally endorses our integration solution, but the boss Mr. Wang hasn't expressed an opinion yet. They're also looking at Kingdee's solution."

**Assistant Processing Logic**:

| Detected Signal | Action |
|-----------------|--------|
| "U8 data doesn't sync across plants" | Update current_solution.notes |
| "Next year Q1 IT budget, 500K" | Update estimated_deal_value, record budget signal |
| "Mr. Li endorses" | Update Mr. Li's attitude to "Supportive" in decision_chain |
| "Mr. Wang hasn't expressed opinion" | Update or add Mr. Wang, attitude marked as "Unknown" |
| "Looking at Kingdee" | Record in key_extracted_info competitor field |

**Positive Feedback**: When positive signals are detected, the assistant provides encouragement:
> "This is a key milestone — Mr. Li has clearly endorsed the integration solution's technical capabilities, and the customer has a concrete budget plan. This is worth recording as a milestone."

**Output**: Structured meeting minutes (discussion points + conclusions + action items), automatically saved to activity_log.

---

### 9. Key Date & Compliance Reminders (New in v2.0)

**Automatic Extraction**: Dates mentioned in your activity logs are automatically identified and stored.

> User: "Quote is valid until next Friday"
> Assistant: (automatically stored in the key_date field)

**Daily Reminders**: At the first conversation each day, the assistant will list key dates for the upcoming 7 days:

> Key dates in the next 7 days:
> - Suzhou Yunchuang Tech: Quote validity expires (April 23, Wednesday)
> - Hangzhou Zhizao: Bid submission deadline (April 18, Friday 17:00)

**Supported Date Types**: Quote validity periods, contract expiration dates, bid submission deadlines, demo/meeting schedules, payment milestones.

---

## Recommended Daily Workflow

| Time | Action | Corresponding Feature |
|------|--------|----------------------|
| Start of day | Review customers to follow up and key dates | Automatically displayed at first daily conversation |
| Before a visit | "Prepare visit for [Customer Name]" | Intelligent Pre-Call Brief |
| After a visit | Input meeting content and key points | Smart Meeting Minutes Processing |
| Before sending emails | "Generate value proposition for [Customer Name]" | Personalized Value Proposition Generator |
| Anytime | One-sentence follow-up logging | Quick Activity Logging |
| Friday | "Export data" | Data Backup |

---

## Complete Command Reference

### Basic Operations (v1.0)

| Command | Description |
|---------|-------------|
| "Help" | View the full feature menu |
| "Add customer: [Company Name]" | Create a new customer |
| "View [Company Name]" | Query customer details |
| "Show my funnel overview" | View funnel dashboard |
| "Find me [Industry] companies in [City]" | Customer mining |
| "Log this: [one-sentence description]" | Quick activity logging |
| "Set methodology to [SPIN/BANT/MEDDIC]" | Switch methodology |
| "Export data" | Export to Excel |
| "Update my preferences" | Reconfigure personal settings |

### Smart Enhancement (New in v2.0)

| Command | Description |
|---------|-------------|
| "Prepare visit for [Customer Name]" | Generate pre-call briefing |
| "Generate value proposition for [Customer Name]" | Output 3 customized value points |
| "Help me draft a meeting invitation email for [Customer Name]" | Generate email draft |
| (Directly input meeting content) | Automatically process meeting minutes |

---

## Important Notes

1. **Data Confirmation**: The assistant will ask for your confirmation before executing any data modification
2. **Privacy Protection**: Only information you provide or legally public information is used
3. **Advisory Role**: All suggestions are for reference only — the final decision is always yours
4. **Data Storage**: Data is stored in a local SQLite database — please back up regularly
5. **Pre-call brief quality depends on the completeness of recorded customer data**: The more complete the decision chain, current solution, and other fields are, the more accurate the briefing will be
6. **Please confirm after meeting minutes processing**: The assistant will list the fields to be updated — please confirm before execution
7. **Please verify key dates**: Dates extracted from natural language may have deviations — please confirm before relying on them
8. **Agent-Reach is an optional dependency** (recommended): Installing the Agent-Reach Skill enhances customer mining and pre-call briefings with multi-platform online search, providing more comprehensive and timely information. All features work normally without it
