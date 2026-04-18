# B2B Sales Intelligent Assistant v1.1 User Guide

## Quick Start

### Step 1: First Launch

After opening the conversation, the assistant will automatically guide you through the initial setup:

1. Choose your role (Frontline Sales Rep / Sales Team Manager)
2. Choose the type of product you sell (Software, Industrial Equipment, Professional Services, etc.)
3. Choose your preferred sales methodology (SPIN / BANT / MEDDIC)
4. Choose whether to import an existing customer list

Once complete, your sales workbench is ready to go.

### Step 2: Add Your First Customer

You can get started in any of the following ways:

**Option 1: Add directly**
> "Add customer: Suzhou Yunchuang Tech, electronic components manufacturing, 300 employees"

**Option 2: Batch mining**
> "Find manufacturing companies in Suzhou with annual revenue over 50 million RMB"

**Option 3: Import a list**
> Upload an Excel/CSV file, and the assistant will automatically parse and enrich the information

---

## Core Features in Detail

### 1. Customer Mining & Info Enrichment

**How to trigger**: Describe your target customer criteria

**Example dialog**:
> User: "Find manufacturing companies in Hangzhou with annual revenue over 50 million RMB"
>
> Assistant: (after searching online) I have compiled 34 potential customers. Here is a preview... You can download the full Excel file, or say "Add all to funnel."

**Available filter criteria**:

- City / Region
- Industry
- Company size (headcount, revenue)
- Qualification tags (Specialized & Innovative SMEs, above-scale enterprises, etc.)

#### Agent-Reach Enhanced Search

When the Agent-Reach Skill is installed, the customer mining feature automatically upgrades to multi-platform deep search mode:

- **Exa AI Precision Search**: Leverage Exa AI for precise company information searches, obtaining more comprehensive corporate background data
- **Jina Reader Annual Report Analysis**: Use Jina Reader to fetch and analyze corporate annual reports, financial statements, and other public documents, quickly extracting key business metrics
- **GitHub Tech Stack Research**: Search target companies' open-source projects and tech stacks on GitHub, providing entry points for technology-oriented sales

**Example dialog**:
> User: "Do a deep research on Huaqiang Industrial's annual report"
>
> Assistant: (Fetches the full annual report via Agent-Reach's Jina Reader) I have retrieved the key information from Huaqiang Industrial's 2024 annual report...

### 2. Customer Information Management

**Query customers**:
> "Show me the information for Suzhou Yunchuang Tech"
> "Search for customers with 'Yunchuang' in the name"

**Edit information**:
> "Update the contact for Yunchuang Tech: IT Director Mr. Li, phone 138xxxx"
> "Set the decision chain for Yunchuang Tech: Mr. Li is the technical evaluator, influence level 4, supportive stance"

**Monitor customers**:
> "Monitor this company" (sets a priority watch flag)

**Contract expiry reminders**: When a customer's contract expiration date is less than 6 months away, the system will automatically prompt: "Contract expiring soon -- this could be a window of opportunity."

### 3. Sales Funnel Management & Activity Logging

**Funnel stage descriptions**:

| Stage | Default Probability | Description |
|-------|---------------------|-------------|
| Lead | 10% | Initially identified potential customer |
| Initial Contact | 20% | First communication has been made |
| Needs Confirmed | 40% | Customer needs have been clearly identified |
| Solution Demo | 60% | Product/solution has been demonstrated |
| Negotiation | 80% | Entered pricing/terms negotiation |
| Won | 100% | Successfully signed |
| Lost | 0% | Deal was not closed |

**Quick activity logging (one-liner mode)**:
> "Called Director Wang at Yunchuang today. Their Yonyou U8 system is outdated. Scheduled a demo for next Wednesday."

The assistant will automatically parse:
- Activity type: Phone call
- Content summary: Learned that their Yonyou U8 version is outdated
- Outcome: Demo scheduled for next Wednesday
- Suggested action: Advance funnel stage, update customer solution information

**View funnel dashboard**:
> "Show my funnel overview"
> "Which customers need follow-up this week?"

### 4. Sales Methodology Application

**Generate question checklists**:
> "Help me prepare questions for Yunchuang Tech using the SPIN methodology"

**Switch methodology**:
> "Set methodology to BANT"

**Comparison of the three methodologies**:

| Methodology | Core Framework | Best For |
|-------------|----------------|----------|
| SPIN | Situation -> Problem -> Implication -> Need-Payoff | Uncovering deeper needs |
| BANT | Budget -> Authority -> Need -> Timeline | Quickly qualifying opportunities |
| MEDDIC | Metrics -> Economic Buyer -> Decision Criteria -> Decision Process -> Identify Pain -> Champion | Analyzing complex, large deals |

### 5. Data Export & Backup

**Export data**:
> "Export data"

The system will export the customers, sales_funnel, and activity_log tables into a single Excel file (one sheet per table) and provide a download link.

**Backup reminders**: The system will automatically remind you to back up your data every Friday.

---

## Quick Command Reference

| Command | Description |
|---------|-------------|
| "Help" | View the full feature menu |
| "Add customer: [company name]" | Create a new customer |
| "Show [company name]" | View customer details |
| "Show my funnel overview" | View the funnel dashboard |
| "Find [industry] companies in [city]" | Customer mining |
| "Log this: [one-liner description]" | Quick activity logging |
| "Set methodology to [SPIN/BANT/MEDDIC]" | Switch sales methodology |
| "Export data" | Export to Excel |
| "Change my preferences" | Reconfigure personal settings |

---

## Important Notes

1. **Data Confirmation**: The assistant will ask for your confirmation before executing any data modification
2. **Privacy Protection**: Only information you provide or legally public information is used
3. **Advisory Role**: All suggestions are for reference only -- the final decision is always yours
4. **Data Storage**: Data is stored in a local SQLite database; please back up regularly
5. **Enhanced Search**: After installing the Agent-Reach Skill, the customer mining feature automatically upgrades to multi-platform deep search. Basic functionality is not affected if Agent-Reach is not installed.
