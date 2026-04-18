# B2B Sales Intelligent Assistant v3.1 User Guide

## Quick Start

### Step 1: First Launch

After opening a conversation, the assistant will automatically guide you through the initial setup:

1. Select your role (Frontline Sales / Sales Team Manager)
2. Select your product type (Software, Industrial Equipment, Professional Services, etc.)
3. Select your preferred sales methodology (SPIN / BANT / MEDDIC)
4. Choose whether to import an existing customer list

Once complete, your sales workbench is ready to go.

### Step 2: Add Your First Customer

You can get started in any of the following ways:

**Option 1: Direct Entry**
> "Add customer: Suzhou Yunchuang Tech, electronic components manufacturing, 300 employees"

**Option 2: Batch Mining**
> "Find manufacturing companies in Suzhou with revenue over 50 million"

**Option 3: Import a List**
> Upload an Excel/CSV file, and the assistant will automatically parse and enrich the information

---

## Feature Details

### 1. Customer Mining & Info Enrichment (v1.0)

**How to Trigger**: Describe your target customer criteria

**Agent-Reach Enhancement**: With Agent-Reach installed, customer mining can leverage additional platforms for data collection, improving the coverage and accuracy of information enrichment.

**Example Dialog**:
> User: "Find manufacturing companies in Hangzhou with revenue over 50 million"
>
> Assistant: (After online search) I've compiled 34 potential customers. Here's a preview... You can download the full Excel file, or say "Add all to funnel."

**Available Filter Criteria**:

- City/Region
- Industry
- Size (headcount, revenue)
- Qualification tags (Specialized & Innovative SME, Above-Scale Enterprise, etc.)

### 2. Customer Information Management (v1.0)

**Query a Customer**:
> "View Suzhou Yunchuang Tech's information"
> "Search for customers with 'Yunchuang' in the name"

**Edit Information**:
> "Update Yunchuang Tech's contact: IT Director Mr. Li, phone 138xxxx"
> "Set Yunchuang Tech's decision chain: Mr. Li is the Technical Evaluator, influence 4, attitude supportive"

**Monitor a Customer**:
> "Monitor this company" (sets a priority watch flag)

**Contract Expiration Alert**: When a customer's contract expiration date is within 6 months, the system will automatically prompt "Contract expiring soon — this may be an engagement window opportunity."

### 3. Sales Funnel Management & Activity Logging (v1.0)

**Funnel Stage Descriptions**:

| Stage | Default Probability | Description |
|-------|-------------------|-------------|
| Lead | 10% | Initially identified potential customer |
| Initial Contact | 20% | First communication completed |
| Needs Confirmed | 40% | Customer needs clearly identified |
| Solution Demo | 60% | Product solution presented |
| Negotiation | 80% | Price/terms negotiation in progress |
| Won | 100% | Successfully signed |
| Lost | 0% | Deal not closed |

**Quick Activity Logging (One-Sentence Mode)**:
> "Called Director Wang at Yunchuang today — their Yonyou U8 is too outdated; scheduled a demo for next Wednesday"

The assistant will automatically parse:
- Activity type: Phone call
- Content summary: Learned that Yonyou U8 version is outdated
- Outcome: Demo scheduled for next Wednesday
- Recommended action: Advance funnel stage, update customer solution information

**View Funnel Dashboard**:
> "My funnel overview"
> "Which customers need follow-up this week"

### 4. Sales Methodology Application (v1.0)

**Generate a Question Checklist**:
> "Help me prepare SPIN methodology questions for Yunchuang Tech"

**Switch Methodology**:
> "Set methodology to BANT"

**Three Methodology Comparison**:

| Methodology | Core Framework | Applicable Scenarios |
|-------------|----------------|---------------------|
| SPIN | Situation -> Problem -> Implication -> Need-Payoff | Uncovering deep needs |
| BANT | Budget -> Authority -> Need -> Timeline | Quick opportunity qualification |
| MEDDIC | Metrics -> Economic Buyer -> Decision Criteria -> Decision Process -> Identify Pain -> Champion | Complex large-deal analysis |

### 5. Data Export & Backup (v1.0)

**Export Data**:
> "Export data"

The system will export the customers, sales_funnel, and activity_log tables into a single Excel file (one sheet per table) and provide a download link.

**Backup Reminder**: The system automatically reminds you to back up data every Friday.

---

### 6. Intelligent Pre-Call Brief (v2.0)

**How to Trigger**:
> "Prepare visit for Suzhou Yunchuang Tech"
> "Yunchuang Tech pre-call brief"

**Generated Content**:

The assistant automatically generates a one-page briefing covering 5 sections:

**1. Company Overview & Updates**: Basic information (industry, size, revenue) and recent news updates obtained via online search.

**2. Current Solution & Pain Points**: Inferred business pain points based on the recorded `current_solution` field. For example:
> "Currently using Yonyou U8 V13.0 (deployed in 2018, running for 8 years). Inferred pain points: Difficulty with multi-plant coordination; outdated version unable to meet new business requirements."

**3. Decision Chain Entry Points**: Displays known key decision-makers and their attitudes, with recommended engagement strategies.

**4. Structured Question Checklist**: Automatically generated questions tailored to the customer based on your selected methodology (SPIN/BANT/MEDDIC).

**5. Reference Cases**: At least one matched success case from the same industry and similar scale for reference.

**Advanced Usage**:
> "Help me write a meeting invitation email to Yunchuang Tech"

The assistant can generate a meeting agenda email draft based on the pre-call briefing content, ready for you to copy and send.

---

### 7. Personalized Value Proposition Generator (v2.0)

**How to Trigger**:
> "Generate value proposition for Suzhou Yunchuang Tech"

**Output Format**:

The assistant outputs 3 highly customized value points based on the customer's current solution, pain points, and industry characteristics. For example:

> For Suzhou Yunchuang Tech, currently using Yonyou U8 V13.0 (deployed in 2018):
> 1. "Resolve the bottleneck where U8's multi-plant coordination causes financial closing cycles of up to 7 days."
> 2. "No need to replace the existing ERP — achieve real-time data interoperability with MES through an integration layer."
> 3. "Local service team with 2-hour response time, avoiding delays from the original vendor's support."

**Use Cases**: Email subject lines, proposal summary pages, phone openers, demo introductions.

---

### 8. Smart Meeting Minutes Processing (v2.0)

**How to Trigger**: After a meeting, directly input the meeting content or key points.

**Example Dialog**:
> User: "Had a technical exchange meeting with Director Li at Yunchuang today. Director Li said their biggest issue with U8 is that data doesn't flow between plants, and monthly financial closing takes 7 days. They have IT budget for Q1 next year, about 500K. Director Li personally supports our integration solution, but the boss, Mr. Wang, hasn't expressed a position yet. They're also looking at Kingdee's solution."

**Assistant Processing Logic**:

| Detected Signal | Action |
|----------------|--------|
| "U8 multi-plant data not connected" | Update current_solution.notes |
| "Q1 next year IT budget, 500K" | Update estimated_deal_value, record budget signal |
| "Director Li supports" | Update Director Li's attitude to "Supportive" in decision_chain |
| "Mr. Wang hasn't expressed a position" | Update or add Mr. Wang, attitude marked as "Unknown" |
| "Looking at Kingdee" | Record in key_extracted_info competitor field |

**Positive Feedback**: When positive signals are detected, the assistant provides encouragement:
> "This is a key milestone — Director Li has clearly endorsed the integration solution's technical capabilities, and the customer has a defined budget plan. This is worth recording as a milestone."

**Output**: Structured meeting minutes (discussion points + conclusions + action items), automatically saved to activity_log.

---

### 9. Key Date & Compliance Reminders (v2.0)

**Automatic Extraction**: Dates mentioned when you log activities are automatically identified and stored.

> User: "Quote valid until next Friday"
> Assistant: (Automatically stored in the key_date field)

**Daily Reminders**: During the first conversation each day, the assistant lists key dates for the next 7 days:

> Key dates for the next 7 days:
> - Suzhou Yunchuang Tech: Quote validity expires (April 23, Wednesday)
> - Hangzhou Zhizao: Bid document submission deadline (April 18, Friday 17:00)

**Supported Date Types**: Quote validity, contract expiration, bid deadlines, demo/meeting schedules, payment milestones.

---

### 10. Opportunity Health Scoring & Alerts (v3.0 New)

**Auto-Triggered**: Automatically calculated and reported during the first daily conversation.

**Scoring Dimensions**:

| Dimension | Rule | Score Impact |
|-----------|------|--------------|
| Follow-up Interval | Over 7 days / Over 14 days | -15 / -30 |
| Action Plan | No next_action | -20 |
| Relationship Trend | relationship_score declining | -10 |
| Pain Point Alignment | Customer has legacy system or clear needs | +15 |
| Budget Signal | Budget signal present | +20 |

Base score is 70, range 0-100.

**Output Example**:
> Opportunity Health Alert (3 customers need attention):
> 1. Nanjing New Materials (35 pts): No follow-up in over 14 days, no next-step plan. Recommendation: Schedule a call to check on the customer's latest status.
> 2. Wuxi Precision (48 pts): Relationship score declining, competitor has entered. Recommendation: Arrange a technical exchange to strengthen the relationship.

**Dormant Customers**: When next_contact_date is overdue by >7 days and health score is <40, the assistant will flag separately:
> Dormant Customers (2):
> - Suzhou Hengda: Last follow-up was 32 days ago. Recommendation: Send an industry case study to reactivate.
> - "Would you like me to generate a reactivation script for you?"

**Manual Trigger**:
> "View opportunity health scores"
> "Which customers need urgent follow-up"

---

### 11. Opportunity Bottleneck Diagnosis (v3.0 New)

**How to Trigger**:
> "Analyze why Suzhou Yunchuang Tech is stuck"
> "Where is Yunchuang Tech stalled"

**Analysis Dimensions**:

1. **Activity Stagnation**: Recent activity frequency, interval trends
2. **Decision Chain Resistance**: Whether high-influence opponents exist
3. **Competitive Threat**: Whether competitors have been mentioned
4. **Budget Gap**: Whether budget signals are missing
5. **Methodology Gap**: Based on your selected methodology, which key dimensions have missing information

**Output Example**:
> **Opportunity Bottleneck Diagnosis: Suzhou Yunchuang Tech**
>
> **Possible Bottlenecks:**
> 1. Technical Evaluator Director Li has an "Opposed" attitude, 4-star influence, and did not respond positively in the last meeting.
> 2. Competitor Kingdee has entered; the customer mentioned price comparisons.
> 3. Budget has not been explicitly released.
>
> **Breakthrough Recommendations:**
> 1. Arrange a targeted technical exchange addressing Director Li's pain points and invite a solutions architect to participate.
> 2. Prepare a differentiation comparison against Kingdee, highlighting integration cost advantages.
> 3. In the next conversation, attempt to obtain budget timeline information.

---

### 12. Competitive Response & Script Generation (v3.0 New)

**How to Trigger**:
> "The customer says SAP is more stable — how should I respond?"
> "Yunchuang Tech is comparing with Kingdee — help me prepare a response script"

**Script Structure** (Five-Step Method):

1. **Acknowledge**: First validate the customer's perspective
2. **Differentiate**: Showcase advantages in the context of the customer's actual situation
3. **Risk Alert**: Point out potential risks of the competitor in this scenario
4. **Case Evidence**: Reference success stories from same-industry customers
5. **Call to Action**: Push for a specific next step

**Agent-Reach Enhancement**: The system automatically searches platforms such as Twitter, Reddit, and V2EX for real user reviews and complaints about competitors, providing compelling real-time evidence for your response scripts. For example, when a customer says "SAP is more stable," the system can automatically cite real feedback from social media users about SAP's upgrade difficulties, long implementation cycles, and other pain points, making your talk tracks more persuasive.

> Note: Agent-Reach is an optional dependency. The competitive response feature works normally without it installed; only the social media sentiment data enhancement is unavailable.

---

### 13. Collaboration Snapshot (v3.0 New)

**How to Trigger**:
> "Generate collaboration snapshot for Suzhou Yunchuang Tech"

**Output Example** (Within 200 words, ready to copy and forward):
> Customer: Suzhou Yunchuang Tech, electronic components manufacturing, ~80M annual revenue, Specialized & Innovative SME
> Current Solution: Yonyou U8 V13.0 (deployed 2018), no MES
> Core Pain Points: Multi-plant coordination difficulty, long financial closing cycles
> Key Contact: IT Director Mr. Li (leads technical evaluation, attitude neutral-to-supportive)
> Current Stage: Solution Demo, estimated 350K, demo next Wednesday

**Use Cases**: Forward to pre-sales consultants, technical experts, or senior leadership for quick customer background understanding.

---

### 14. Internal Help Request Script (v3.0 New)

**How to Trigger**:
> "Request pre-sales support for Suzhou Yunchuang Tech"
> "Request technical support for Yunchuang Tech"

**Output Example** (Ready to copy into enterprise IM):
> @Zhang Pre-sales support needed:
> - Customer: Suzhou Yunchuang Tech, estimated deal 350K, currently at Solution Demo stage
> - Pain Points: Multi-plant coordination, U8 can't meet requirements
> - Demo Audience: IT Director Mr. Li + 2 business leads
> - Timing: Next Wednesday afternoon, approx. 2 hours
> - Key Demo Focus: Multi-organization coordination + data migration plan from existing U8
> Please confirm your availability when you get a chance. Thanks!

---

### 15. Role-Based Decision-Maker Communication (v3.0 New)

**How to Trigger**:
> "Write an email to the Technical Evaluator at Yunchuang Tech"
> "Help me draft a talking script for Mr. Wang (Economic Decision Maker)"

**Role Focus Reference**:

| Role | Focus Areas | Language Style |
|------|-------------|---------------|
| Economic Decision Maker | ROI, strategic value, risk control | Concise, data-driven |
| Technical Evaluator | Performance, SLA, security, integration | Technical depth |
| End User | Ease of use, training, efficiency | Scenario-based |
| Procurement Executive | Price, terms, qualifications | Formal business |

---

### 16. Personal Performance Dashboard & Behavioral Feedback (v3.0 New)

**How to Trigger**:
> "My performance"
> "Monthly summary"

**Output Example**:
> **This Month's Results (as of April 16)**
> - New Leads: 12
> - Advanced to Demo Stage: 4
> - Won: 2 (Total amount 680K)
> - Lost: 1
> - Total Funnel Estimated Amount: 3.4M
> - Month-over-Month: Won deal amount +15%
>
> **Behavioral Insights**:
> 70% of your phone follow-ups this month did not include a specific next-step action. It is recommended to add a clear invitation or scheduled next step at the end of each conversation.

---

## Recommended Daily Workflow

| Time | Action | Corresponding Feature |
|------|--------|----------------------|
| Start of workday | Review customers to follow up, key dates, and dormant customers | Auto-displayed on first daily conversation |
| Before a visit | "Prepare visit for [Customer Name]" | Intelligent Pre-Call Brief |
| After a visit | Input meeting content and key points | Smart Meeting Minutes Processing |
| Before sending emails | "Generate value proposition for [Customer Name]" / "Write an email to [Role]" | Value Proposition / Role-Based Communication |
| Encountering a competitor | "The customer says [Competitor] is better" | Competitive Response Scripts |
| Opportunity stalled | "Analyze why this is stuck" | Bottleneck Diagnosis |
| Need support | "Request pre-sales support" | Internal Help Request Script |
| Anytime | One-sentence activity logging | Quick Activity Logging |
| Friday | "My performance" + "Export data" | Performance Summary + Backup |

## Automated Reminders at Special Time Points

| Timing | Auto-Generated Content |
|--------|----------------------|
| First daily conversation | Key dates for the next 7 days + dormant customers |
| Monday morning | This week's follow-up list + health score alerts |
| Friday afternoon | This week's performance summary + behavioral feedback |
| 6 months before customer contract expiration | Engagement window reminder |
| Every Friday | Data backup reminder |

---

## Complete Command Reference

### Basic Operations (v1.0)

| Command | Description |
|---------|-------------|
| "Help" | View the complete feature menu |
| "Add customer: [Company Name]" | Create a new customer |
| "View [Company Name]" | Query customer details |
| "My funnel overview" | View funnel dashboard |
| "Find [Industry] companies in [City]" | Customer mining |
| "Log this: [one-sentence description]" | Quick activity logging |
| "Set methodology to [SPIN/BANT/MEDDIC]" | Switch methodology |
| "Export data" | Export to Excel |
| "Change my preferences" | Reconfigure personal settings |

### Smart Enhanced (v2.0)

| Command | Description |
|---------|-------------|
| "Prepare visit for [Customer Name]" | Generate pre-call briefing |
| "Generate value proposition for [Customer Name]" | Output 3 customized value points |
| "Help me write a meeting invitation email to [Customer Name]" | Generate email draft |
| (Directly input meeting content) | Auto-process meeting minutes |

### Analytics & Competition (v3.0 New)

| Command | Description |
|---------|-------------|
| "Analyze why [Customer Name] is stuck" | Bottleneck diagnosis |
| "Generate collaboration snapshot for [Customer Name]" | Internal collaboration summary |
| "Request pre-sales/technical support for [Customer Name]" | IM help request script |
| "Write an email to the [Role] at [Customer Name]" | Role-based communication |
| "My performance" / "Monthly summary" | Performance dashboard |
| "View opportunity health scores" | Health scoring |
| "The customer says [Competitor] is better" | Competitive response scripts |

---

## Important Notes

1. **Data Confirmation**: The assistant will ask for your confirmation before executing any data modification operations
2. **Privacy Protection**: Only uses information you provide or legally public information
3. **Advisory Role**: All suggestions are for reference only — final decision-making authority rests with you
4. **Data Storage**: Data is stored in a local SQLite database; please back up regularly
5. **Pre-call briefing quality depends on recorded customer data**: The more complete the decision chain, current solution, and other fields, the more accurate the briefing
6. **Please verify after meeting minutes processing**: The assistant will list the fields to be updated; please confirm before execution
7. **Please verify key dates**: Dates extracted from natural language may have deviations; please confirm before relying on them
8. **Health scores are based on recorded data**: The more complete the data, the more accurate the scores
9. **Bottleneck diagnosis requires sufficient activity records**: It is recommended to use this feature only after at least 3 follow-up records
10. **Competitive response scripts are for reference only**: Please adjust based on actual circumstances and your company's official messaging before use
11. **Performance statistics are based on database records**: Ensure Won/Lost statuses are updated promptly for accurate data
12. **Agent-Reach is an optional skill**: When installed, it enhances data sources for customer mining and competitive response features; all other features work normally without it
