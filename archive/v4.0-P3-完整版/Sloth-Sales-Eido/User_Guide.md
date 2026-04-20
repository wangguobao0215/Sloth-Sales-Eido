# B2B Sales Intelligent Assistant v4.1 User Guide

## Quick Start

v4.1 is the Full Edition, containing all 22+ capabilities from v1.0 through v4.1.

### Step 1: First Launch

The assistant will guide you through a 4-step initialization:

1. **Role Selection**: Field Sales Rep / Sales Team Leader (selecting "Team Leader" activates 18 team management features)
2. **Product Type**: Software/SaaS, Industrial Equipment, Professional Services, Other
3. **Methodology Preference**: SPIN (default) / BANT / MEDDIC
4. **Data Import**: Upload an Excel list / Start from scratch

Once complete, your sales workbench is ready to go.

### Step 2: Add Your First Customer

You can get started in any of the following ways:

**Option 1: Direct Entry**
> "Add customer: Suzhou Yunchuang Tech, electronic components manufacturing, 300 employees"

**Option 2: Bulk Mining**
> "Find me manufacturing companies in Suzhou with revenue over 50 million RMB"

**Option 3: Import a List**
> Upload an Excel/CSV file, and the assistant will automatically parse and enrich the information

---

## Feature Details

### 1. Customer Mining & Info Enrichment (v1.0, v4.1 Agent-Reach Enhanced)

**How to Trigger**: Describe your target customer criteria

**Example Dialog**:
> User: "Find me manufacturing companies in the Hangzhou area with revenue over 50 million RMB"
>
> Assistant: (After web search) Found 34 potential customers. Here is a preview... You can download the full Excel, or say "Add all to funnel".

**Available Filters**:

- City/Region
- Industry
- Scale (headcount, revenue)
- Qualification tags (Specialized & Innovative SME, Above-Scale Enterprise, etc.)

**v4.1 Agent-Reach Omnichannel Enhancement**: With Agent-Reach installed, customer mining will automatically leverage Exa AI deep search, LinkedIn enterprise information, WeChat Official Account industry coverage, corporate website scraping, and other omnichannel data sources, significantly improving the richness and accuracy of search results.

### 2. Customer Information Management (v1.0)

**Query a Customer**:
> "View Suzhou Yunchuang Tech's information"
> "Search for customers with 'Yunchuang' in the name"

**Edit Information**:
> "Update Yunchuang Tech's contact: IT Director Mr. Li, phone 138xxxx"
> "Set Yunchuang Tech's decision chain: Mr. Li is a Technical Evaluator, influence level 4, attitude supportive"

**Watch a Customer**:
> "Monitor this company" (sets the watch-list flag)

**Contract Expiry Reminder**: When a customer's contract expiry date is within 6 months, the system automatically prompts "Contract expiring soon -- this may be an engagement window".

### 3. Sales Funnel Management & Activity Logging (v1.0)

**Funnel Stage Descriptions**:

| Stage | Default Probability | Description |
|-------|---------------------|-------------|
| Lead | 10% | Newly identified potential customer |
| Initial Contact | 20% | First communication completed |
| Needs Confirmed | 40% | Customer needs clarified |
| Solution Demo | 60% | Product/solution presented |
| Negotiation | 80% | Price/terms negotiation underway |
| Won | 100% | Contract signed |
| Lost | 0% | Deal not closed |

**Quick Activity Logging (One-Sentence Mode)**:
> "Called Mr. Wang at Yunchuang today. Their Yonyou U8 is too old. Scheduled a demo for next Wednesday."

The assistant will automatically parse:
- Activity type: Phone call
- Content summary: Learned Yonyou U8 version is outdated
- Outcome: Demo scheduled for next Wednesday
- Recommended action: Advance funnel stage, update customer solution info

**View Funnel Dashboard**:
> "My funnel overview"
> "Which customers need follow-up this week?"

### 4. Sales Methodology Application (v1.0)

**Generate a Question List**:
> "Help me prepare SPIN questions for Yunchuang Tech"

**Switch Methodology**:
> "Set methodology to BANT"

**Comparison of Three Methodologies**:

| Methodology | Core Framework | Best For |
|-------------|----------------|----------|
| SPIN | Situation -> Problem -> Implication -> Need-Payoff | Uncovering deep needs |
| BANT | Budget -> Authority -> Need -> Timeline | Quickly qualifying opportunities |
| MEDDIC | Metrics -> Economic Buyer -> Decision Criteria -> Decision Process -> Identify Pain -> Champion | Complex deal analysis |

### 5. Data Export & Backup (v1.0)

**Export Data**:
> "Export data"

The system will export the customers, sales_funnel, and activity_log tables into a single Excel file (one sheet per table) and provide a download link.

**Backup Reminder**: The system automatically reminds you to back up every Friday.

---

### 6. Intelligent Pre-Call Brief (v2.0)

**How to Trigger**:
> "Prepare visit Suzhou Yunchuang Tech"
> "Yunchuang Tech pre-call brief"

**Generated Content**:

The assistant automatically generates a one-page briefing with 5 sections:

**1. Company Overview & News**: Basic info (industry, scale, revenue) plus recent news gathered from web searches.

**2. Current Solution & Pain Points**: Inferred business pain points based on the recorded `current_solution` field. For example:
> "Currently using Yonyou U8 V13.0 (deployed in 2018, running for 8 years). Estimated pain points: multi-factory coordination difficulties, outdated version unable to meet new business requirements."

**3. Decision Chain Entry Points**: Displays known key decision-makers and their attitudes, with recommended engagement strategies.

**4. Structured Question List**: Auto-generated targeted questions based on your chosen methodology (SPIN/BANT/MEDDIC).

**5. Reference Cases**: At least one matched success case from the same industry and scale.

**Advanced Usage**:
> "Help me write a meeting invitation email to Yunchuang Tech"

The assistant can generate a meeting agenda email draft based on the pre-call brief content, ready for you to copy and send.

---

### 7. Personalized Value Proposition Generator (v2.0)

**How to Trigger**:
> "Generate value proposition Suzhou Yunchuang Tech"

**Output Format**:

The assistant generates 3 highly customized value points based on the customer's current solution, pain points, and industry characteristics. For example:

> For Suzhou Yunchuang Tech, currently using Yonyou U8 V13.0 (deployed in 2018):
> 1. "Resolve the bottleneck where U8 takes up to 7 days for financial closing across multiple factories."
> 2. "No need to replace the existing ERP -- achieve real-time data integration with MES through an integration layer."
> 3. "Local service team responds within 2 hours, avoiding delays from the original vendor's support."

**Use Cases**: Email subject lines, proposal summary pages, phone openers, demo introductions.

---

### 8. Smart Meeting Minutes Processing (v2.0)

**How to Trigger**: After a meeting, directly input the meeting content or key points.

**Example Dialog**:
> User: "Had a technical exchange meeting with Mr. Li from Yunchuang today. Mr. Li said their biggest problem with U8 is that data doesn't flow between factories, and monthly closing takes 7 days. They have IT budget for next year Q1, around 500K RMB. Mr. Li personally endorses our integration solution, but the CEO Mr. Wang hasn't expressed a position yet. They're also looking at Kingdee's solution."

**Assistant Processing Logic**:

| Detected Signal | Action |
|-----------------|--------|
| "U8 data doesn't flow between factories" | Update current_solution.notes |
| "Q1 next year IT budget, 500K" | Update estimated_deal_value, record budget signal |
| "Mr. Li endorses" | Update Mr. Li's attitude to "Supportive" in decision_chain |
| "Mr. Wang hasn't expressed a position" | Update or add Mr. Wang, attitude marked as "Unknown" |
| "Looking at Kingdee" | Record in key_extracted_info competitor field |

**Positive Feedback**: When positive signals are detected, the assistant provides encouragement:
> "This is a key milestone -- Mr. Li has explicitly endorsed the integration solution's technical capabilities, and the customer has a clear budget plan. Worth recording as a milestone."

**Output**: Structured meeting minutes (discussion points + conclusions + action items), automatically saved to activity_log.

---

### 9. Key Date & Compliance Reminders (v2.0)

**Auto-Extraction**: Dates mentioned when you log activities are automatically identified and stored.

> User: "Quote is valid until next Friday"
> Assistant: (Automatically stored in the key_date field)

**Daily Reminder**: During the first conversation each day, the assistant lists key dates within the next 7 days:

> Key dates in the next 7 days:
> - Suzhou Yunchuang Tech: Quote validity expires (April 23, Wednesday)
> - Hangzhou Zhizao: Bid document submission deadline (April 18, Friday 17:00)

**Supported Date Types**: Quote validity period, contract expiry date, bid deadline, demo/meeting schedule, payment milestones.

---

### 10. Opportunity Health Scoring & Alerts (v3.0)

**Auto-Trigger**: Automatically calculated and reported during the first conversation each day.

**Scoring Dimensions**:

| Dimension | Rule | Score Impact |
|-----------|------|--------------|
| Follow-up Interval | Over 7 days / Over 14 days | -15 / -30 |
| Action Plan | No next_action | -20 |
| Relationship Trend | relationship_score declining | -10 |
| Pain-Point Match | Customer has legacy system or explicit need | +15 |
| Budget Signal | Budget signal present | +20 |

Base score is 70, range 0--100.

**Output Example**:
> Opportunity Health Alerts (3 customers need attention):
> 1. Nanjing New Materials (35 pts): No follow-up in over 14 days, no next-step plan. Recommendation: Schedule a call to check on the customer's latest status.
> 2. Wuxi Precision (48 pts): Relationship score declining, competitor has engaged. Recommendation: Arrange a technical exchange to strengthen the relationship.

**Dormant Customers**: When next_contact_date is overdue by >7 days and health score <40, the assistant flags them separately:
> Dormant customers (2):
> - Suzhou Hengda: Last follow-up was 32 days ago. Recommendation: Send an industry case study to reactivate.
> - "Would you like me to help you generate a reactivation script?"

**Manual Trigger**:
> "Check opportunity health scores"
> "Which customers need urgent follow-up?"

---

### 11. Opportunity Bottleneck Diagnosis (v3.0)

**How to Trigger**:
> "Analyze why Suzhou Yunchuang Tech is stuck"
> "Where is Yunchuang Tech blocked?"

**Analysis Dimensions**:

1. **Activity Stagnation**: Recent activity frequency and interval trends
2. **Decision Chain Resistance**: Whether high-influence objectors exist
3. **Competitive Threat**: Whether competitors have been mentioned
4. **Budget Gap**: Whether budget signals are missing
5. **Methodology Gaps**: Which key dimensions are missing based on your selected methodology

**Output Example**:
> **Opportunity Bottleneck Diagnosis: Suzhou Yunchuang Tech**
>
> **Likely Bottlenecks:**
> 1. Technical Evaluator Director Li has an "Opposed" attitude, 4-star influence, did not respond positively in the last meeting.
> 2. Competitor Kingdee has engaged; the customer mentioned price comparisons.
> 3. Budget has not been explicitly released.
>
> **Breakthrough Recommendations:**
> 1. Arrange a targeted technical exchange focused on Director Li's pain points; invite an architect to participate.
> 2. Prepare a differentiation comparison with Kingdee, highlighting integration cost advantages.
> 3. In the next conversation, try to obtain budget timeline information.

---

### 12. Competitive Response & Script Generation (v3.0)

**How to Trigger**:
> "The customer says SAP is more stable -- how should I respond?"
> "Yunchuang Tech is comparing Kingdee. Help me prepare a response script."

**Script Structure** (Five-Step Method):

1. **Acknowledge**: First validate the customer's perspective
2. **Differentiate**: Highlight advantages in the context of the customer's specific situation
3. **Risk Alert**: Point out potential risks of the competitor in this scenario
4. **Case Evidence**: Reference success stories from customers in the same industry
5. **Call to Action**: Drive the next specific step forward

---

### 13. Collaboration Snapshot (v3.0)

**How to Trigger**:
> "Generate collaboration snapshot Suzhou Yunchuang Tech"

**Output Example** (within 200 words, ready to copy and forward):
> Customer: Suzhou Yunchuang Tech, electronic components manufacturing, ~80M RMB annual revenue, Specialized & Innovative SME
> Current solution: Yonyou U8 V13.0 (deployed 2018), no MES
> Core pain points: Multi-factory coordination difficulties, prolonged financial closing cycle
> Key contact: IT Director Mr. Li (leads technical evaluation, attitude neutral-to-supportive)
> Current stage: Solution Demo, estimated deal 350K RMB, demo next Wednesday

**Use Cases**: Forward to pre-sales consultants, technical experts, or senior management for quick customer background briefing.

---

### 14. Internal Help Request Script (v3.0)

**How to Trigger**:
> "Help me request pre-sales support for Suzhou Yunchuang Tech"
> "Help me request technical support for Yunchuang Tech"

**Output Example** (ready to paste into enterprise IM):
> @Zhang -- Need your pre-sales support:
> - Customer: Suzhou Yunchuang Tech, estimated deal 350K RMB, currently at Solution Demo stage
> - Pain point: Multi-factory coordination, U8 can't meet requirements
> - Demo audience: IT Director Mr. Li + 2 business leads
> - Time: Next Wednesday afternoon, approx. 2 hours
> - Key demo focus: Multi-organization coordination + data migration plan from existing U8
> Please confirm your availability when you get a chance. Thanks!

---

### 15. Role-Based Decision-Maker Communication (v3.0)

**How to Trigger**:
> "Write an email to the Technical Evaluator at Yunchuang Tech"
> "Help me write a pitch for Mr. Wang (Economic Decision Maker)"

**Role Focus Reference**:

| Role | Focus Areas | Language Style |
|------|-------------|----------------|
| Economic Decision Maker | ROI, strategic value, risk control | Concise, data-driven |
| Technical Evaluator | Performance, SLA, security, integration | Technical depth |
| End User | Ease of use, training, efficiency | Scenario-based |
| Procurement Executive | Price, terms, qualifications | Business-formal |

---

### 16. Personal Performance Dashboard & Behavioral Feedback (v3.0)

**How to Trigger**:
> "My performance"
> "Monthly summary"

**Output Example**:
> **This Month's Results (as of April 16)**
> - New leads: 12
> - Advanced to Demo stage: 4
> - Won: 2 (total amount 680K RMB)
> - Lost: 1
> - Total funnel estimated amount: 3.4M RMB
> - Month-over-month: Won amount +15%
>
> **Behavioral Insights**:
> 70% of your phone follow-ups this month did not include a specific next step. Consider adding an explicit invitation or scheduled action at the end of each conversation.

---

### 17. Win/Loss Review & Handover (v4.0 New)

#### Win Flow

When you mark an opportunity as "Won", the assistant proactively asks:

> "Congratulations on the win! Would you like to generate a customer handover checklist?"

**Handover Checklist Contents**:
- Feature commitments made before signing and the delivery timeline
- Key contacts' communication preferences (e.g., "Mr. Li prefers data reports, dislikes hearing technical details")
- Risk points requiring special attention during implementation
- Follow-up service recommendations

**Setting Fulfillment Milestones**: After a win, you can enter key milestone dates:
> "Set fulfillment milestones: first payment May 1, kickoff meeting May 15, estimated acceptance August 30"

These dates will appear in daily reminders.

#### Loss Flow

When you mark an opportunity as "Lost", the assistant proactively asks two questions:

> 1. "Which competitor was ultimately chosen?" (Yonyou/SAP/Kingdee/Other)
> 2. "What was the primary reason?" (Price/Product features/Brand/Relationship/Commercial terms/Delivery timeline/Service)

Answers are stored in the log in JSON format for future analysis:

```json
{"lost_to": "Yonyou", "reason": "Price"}
```

**Value**: After accumulating data over time, you can view trend distributions via "Loss Reason Analysis".

---

### 18. Customer News & Sentiment Monitoring (v4.0 New, v4.1 Agent-Reach Enhanced)

**How to Trigger**:
> "Show me updates on my watched customers"
> "News scan"

**Prerequisite**: You must first set the monitor flag for customers of interest:
> "Monitor Suzhou Yunchuang Tech"

**v4.1 Agent-Reach Omnichannel Search**: Leverages Agent-Reach omnichannel search: Exa AI enterprise news, LinkedIn key contact job changes, WeChat Official Account articles, Twitter/Weibo brand sentiment, and full-text reading of industry media articles.

**Scan Results & Action Recommendations**:

| Discovery Type | Assistant Prompt |
|----------------|------------------|
| Executive change (new CIO appointed) | "This could be a window to introduce a new system. Recommend reaching out soon." |
| Financing/IPO | "Budget may be released. Recommend learning about their latest IT plans." |
| New factory/expansion | "Business expansion may create system upgrade needs." |
| Negative news (litigation/tax issues) | "Payment risk alert. Recommend reviewing payment terms." |

**Output Format**: One-line briefing + action recommendation, keeping reading burden minimal.

---

### 19. Benchmark Case Smart Matching (v4.0 New)

**How to Trigger**:
> "Find a case similar to Suzhou Yunchuang Tech"
> "Any cases of manufacturing customers switching from Yonyou?"

**Matching Dimensions**: Industry, scale, procurement category, existing solution

**Output Contents**:
- 1--2 best-matching cases
- Customer-specific scenario description (not generic case text)
- Directly quotable customer testimonial (if available)
- Recommended storytelling approach

**When the Case Library Is Empty**: The assistant will suggest you can build the library via "Add case" or by uploading a CSV.

---

### 20. Industry Policy & Incentive Alerts (v4.0 New)

**Auto-Trigger**: When preparing a pre-call brief or viewing a customer in specific industries (manufacturing, high-tech, etc.), the assistant automatically searches the web for local industry subsidy policies.

**Example**:
> Policy incentive alert: Suzhou's 2026 "Smart Manufacturing Transformation" special fund is now open for applications. Manufacturing enterprises' IT projects can receive up to 500K RMB in subsidies. This can serve as an additional value point when communicating with the customer.

**Manual Trigger**:
> "Search for IT-related policy subsidies for Suzhou manufacturing"

---

### 21. Case Library Management (v4.0 New)

**Add a Single Case**:
> "Add case"

The assistant will guide you through step-by-step input: industry, scale, existing solution, core pain points, our solution, quantifiable benefits, customer testimonial.

**Bulk Import**:
> "Import cases" (upload a CSV file)

CSV fields: industry, scale, procurement_category, original_solution, pain_point, solution, quantifiable_benefit, customer_quote

---

### 22. Sales Team Leader Functions (v4.0 New)

The following features are activated only when the role is set to "Sales Team Leader".

#### Data Aggregation Method

1. Each sales rep periodically exports their personal data as Excel
2. The team leader uploads all Excel files to the assistant
3. The assistant automatically merges, deduplicates, and generates team dashboards

#### 18 Team Management Capabilities

**Dashboards & Statistics**:

| Command | Description |
|---------|-------------|
| "Team Funnel Dashboard" | Overall stage distribution, ranking by sales rep, health score alerts |
| "Team Performance Dashboard" | This month's won amount, win rate, average deal size, month-over-month comparison |
| "Activity Volume Audit" | New customers, activity count, and follow-up interval comparison per sales rep |
| "Sales Forecast Grading" | Categorize the funnel into Commit / Best Case / Pipeline |

**Alerts & Detection**:

| Command | Description |
|---------|-------------|
| "Duplicate Account Detection" | Fuzzy matching for duplicate customer coverage, with ownership recommendations |
| "Stagnant Opportunity Alert" | Opportunities overdue >14 days, grouped by sales rep |
| "Renewal/Upsell Alert" | Won customers with contracts expiring soon or long periods of inactivity |
| "Sales Workload Monitor" | Flag sales reps with >15 concurrent opportunities and <5 weekly activities |

**Analysis & Diagnosis**:

| Command | Description |
|---------|-------------|
| "Loss Reason Analysis" | Distribution statistics for lost_to and reason |
| "Pipeline Bottleneck Diagnosis" | Conversion rate analysis per stage, identifying common bottlenecks |
| "Sales Capability Benchmarking" | Five-dimension scoring (acquisition/advancement/closing/activity volume/relationships) |
| "Pre-Sales Resource ROI Ranking" | Sorted by "deal amount x probability" |

**Intelligence & Collaboration**:

| Command | Description |
|---------|-------------|
| "External intelligence scan" | Agent-Reach omnichannel search for industry bids/policies and match against the customer base |
| "Set rule: Alert me when XX happens" | Custom alert rules |
| "Generate sales feedback [rep name]" | Structured feedback with recognition and suggestions |
| "Generate team weekly report" | Integrates funnel, updates, risks, and next-week priorities |
| "Export team summary spreadsheet" | Merged data exported as Excel |

---

## Recommended Daily/Weekly Workflow

### Field Sales Rep

| Timing | Action | Corresponding Feature |
|--------|--------|-----------------------|
| Start of each day | Review follow-ups + key dates + dormant customers | Auto reminders |
| Before a visit | "Prepare visit [customer name]" | Pre-Call Brief |
| After a visit | Input meeting key points | Smart Meeting Minutes Processing |
| Before sending email | "Generate value proposition" / "Write email to [role]" | Value Proposition / Role-Based Communication |
| Facing a competitor | "The customer says [competitor] is better" | Competitive Response Script |
| Opportunity stuck | "Analyze why it's stuck" | Bottleneck Diagnosis |
| Need support | "Help me request pre-sales support" | Internal Help Request Script |
| Win/Loss | Mark the result | Auto-guided review |
| Friday | "My performance" + "Export data" | Performance Summary + Backup |

### Sales Team Leader

| Timing | Action | Corresponding Feature |
|--------|--------|-----------------------|
| Monday | Merge team data + review team funnel | Data Import + Team Dashboard |
| Midweek | Duplicate Account Detection + Stagnant Opportunity Alert + Workload Monitor | Team Alerts |
| Friday | Team performance + Loss analysis + Generate weekly report | Team Statistics |
| End of month | Sales forecast + Capability benchmarking + Pipeline diagnosis | Deep Analysis |

---

## Quick Command Reference

### Basic Operations (v1.0)

| Command | Description |
|---------|-------------|
| "Help" | Feature menu overview |
| "Add customer: [company name]" | Create a new customer |
| "View [company name]" | Query customer details |
| "My funnel overview" | Funnel dashboard |
| "Find me [industry] companies in [city]" | Customer mining |
| "Log this: [one sentence]" | Quick activity logging |
| "Set methodology to [XX]" | Switch methodology |
| "Monitor [company name]" | Set watch-list flag |
| "Export data" | Export to Excel |
| "Change my preferences" | Modify settings |

### Intelligent Enhancement (v2.0)

| Command | Description |
|---------|-------------|
| "Prepare visit [customer name]" | Pre-Call Brief |
| "Generate value proposition [customer name]" | Customized value points |
| "Write a meeting invitation email to [customer name]" | Email draft |
| (Directly input meeting content) | Smart Meeting Minutes Processing |

### Analysis & Competition (v3.0)

| Command | Description |
|---------|-------------|
| "Analyze why [customer name] is stuck" | Bottleneck Diagnosis |
| "Check opportunity health scores" | Health Scoring |
| "My performance" / "Monthly summary" | Performance Dashboard |
| "Generate collaboration snapshot [customer name]" | Internal forwarding summary |
| "Help me request pre-sales support [customer name]" | IM help request script |
| "Write email to [role] at [customer name]" | Role-Based Communication |
| "The customer says [competitor] is better" | Competitive Response Script |

### Knowledge Capture (v4.0)

| Command | Description |
|---------|-------------|
| "Find a case similar to [customer name]" | Case Matching |
| "Add case" | Enter a case |
| "Import cases" | Bulk CSV import |
| "Show me updates on my watched customers" | News Scan |
| "Search for [region] [industry] policy subsidies" | Industry Policy Search |

### Team Management (Team Leader only, v4.0)

| Command | Description |
|---------|-------------|
| "Team Funnel Dashboard" | Team funnel |
| "Team Performance Dashboard" | Team statistics |
| "Duplicate Account Detection" | Duplicate customer check |
| "Stagnant Opportunity Alert" | Overdue opportunities |
| "Loss Reason Analysis" | Competitor loss statistics |
| "Sales Forecast Grading" | Commit / Best Case / Pipeline |
| "Sales Capability Benchmarking" | Five-dimension scoring |
| "Generate team weekly report" | Weekly report summary |
| "Export team summary spreadsheet" | Team Excel export |

---

## Automatic Reminder Schedule

| Timing | Auto-Generated Output |
|--------|------------------------|
| First conversation each day | Key dates in the next 7 days + dormant customers |
| Monday morning each week | This week's follow-up list + health score alerts |
| Friday afternoon each week | This week's performance summary + behavioral feedback |
| 6 months before customer contract expiry | Engagement-window reminder |
| Every Friday | Data backup reminder |

---

## Data Security & Privacy

1. **Local Storage**: All data is stored in a local SQLite database and is never uploaded to the cloud
2. **Regular Backups**: Weekly Excel exports are recommended; the system reminds you every Friday
3. **Privacy Compliance**: The assistant only uses information you provide or legally public enterprise information
4. **Data Portability**: Data can be migrated to other CRM systems via Excel export

---

## Important Notes

1. **Data Confirmation**: The assistant will ask for your confirmation before executing any data modification
2. **Privacy Protection**: Only information you provide or legally public information is used
3. **Advisory Role**: All suggestions are for reference only; final decisions are always yours
4. **Data Storage**: Data is stored in a local SQLite database; please back up regularly
5. **Pre-call brief quality depends on recorded customer data**: The more complete fields like decision chain and current solution are, the more accurate the briefing
6. **Confirm after meeting minutes processing**: The assistant will list the fields to be updated; please confirm before execution
7. **Verify key dates**: Dates extracted from natural language may have inaccuracies; please confirm before relying on them
8. **Health scores are based on recorded data**: The more complete the data, the more accurate the scoring
9. **Bottleneck diagnosis requires sufficient activity records**: At least 3 follow-up records are recommended before use
10. **Competitive response scripts are for reference only**: Please adjust based on actual circumstances and your company's official messaging
11. **Performance statistics are based on database records**: Ensure Won/Lost statuses are updated promptly for accurate data

> **v4.1 Recommendation**: Installing the Agent-Reach Skill is strongly recommended for the best experience. Agent-Reach covers 17 platform channels (search engines, social media, professional networking, developer platforms, web & articles, video platforms). Once installed, customer mining, sentiment monitoring, and external intelligence scanning features will automatically leverage omnichannel search capabilities, significantly improving information coverage and timeliness.

---

## FAQ

**Q: How do I upgrade from an older version?**
A: Overwrite the old files with the new version and run init_db.py. All existing data is fully preserved.

**Q: How does the Sales Team Leader function aggregate multi-person data?**
A: Each sales rep periodically exports their Excel; the team leader uploads and merges them. Future versions may integrate with enterprise CRM systems.

**Q: How do I build the case library?**
A: Say "Add case" to enter cases one by one, or prepare a CSV for bulk import. It is recommended to start by entering your won customer cases.

**Q: How do I switch roles?**
A: Say "Change my preferences" and reselect your role.
