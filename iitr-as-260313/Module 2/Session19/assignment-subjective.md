# Assignment Subjective: Medium Difficulty Practical-Theory Task

## Task
You are the AI quality analyst for ShopKart support. Create a compact **Grounded Response Design Note** for one customer-support use case by comparing ungrounded vs grounded behavior and proposing a safe answer strategy.

### Scenario
Use this customer query:

**"I returned a COD order last week. When will my refund come, and where will it be credited?"**

### What your submission must contain
1. A 2-3 line ungrounded answer that sounds fluent but has at least one policy mistake.
2. A corrected grounded answer that is strictly evidence-backed and user-friendly.
3. A short "Evidence Mapping" section with:
   - Retrieved policy points used
   - Which sentence in grounded answer maps to which policy point
4. A "Risk if Ungrounded" section with at least 3 business/customer risks.
5. A mini checklist titled "Before Sending Reply" with at least 5 validation checks.

### Quality expectations
- Keep the language clear and professional.
- Avoid vague phrases like "usually" when exact policy values are available.
- Keep every factual claim traceable to policy text.
- Do not include external assumptions that are not policy-backed.

### Submission Instruction
- Type the complete answer in the answer box.

---

## Answer Explanation (Mandatory - Ideal Solution)

### 1) Example Ungrounded Answer (Intentionally flawed)
"Thanks for your patience. COD refunds are usually processed within 24-48 hours and are often credited back to the original payment route or wallet. You should see the money very soon."

**Why this is wrong:**  
- Mentions **24-48 hours**, which is not aligned with policy.  
- Uses vague wording ("usually", "often").  
- Introduces "wallet" credit path without policy support.

### 2) Correct Grounded Answer (Policy-backed)
"Thanks for reaching out. For ShopKart returns, refunds are credited within **5-7 business days** after the returned item passes **warehouse verification**. Since this was a **COD order**, the refund is credited only to your **original UPI ID or bank account**."

### 3) Evidence Mapping

| Policy point retrieved | Grounded answer sentence mapped |
|---|---|
| Refunds are credited within **5-7 business days** after warehouse verification. | "Refunds are credited within 5-7 business days after the returned item passes warehouse verification." |
| COD orders are refunded to original **UPI/bank account only**. | "Since this was a COD order, the refund is credited only to your original UPI ID or bank account." |

### 4) Risk if Ungrounded
- **Customer expectation mismatch:** customer expects money in 24-48 hours and loses trust when it does not arrive.
- **Support escalation load:** incorrect timelines increase repeat follow-ups and complaint tickets.
- **Compliance/policy risk:** agent communication diverges from official policy language.
- **Operational confusion:** wrong destination guidance (e.g., wallet) causes avoidable disputes.

### 5) Before Sending Reply (Validation Checklist)
- Is the refund timeline exactly policy-aligned (**5-7 business days**)?
- Is the warehouse verification dependency explicitly mentioned?
- Is COD refund destination correctly limited to **UPI/bank account**?
- Are all claims traceable to retrieved policy lines?
- Did we avoid unsupported words like "usually", "likely", or invented channels?
- Is the final message clear, concise, and user-friendly without adding extra assumptions?

### Alternative acceptable approach
Learners may present the same facts in different wording, but all critical constraints must remain unchanged:
- timeline = **5-7 business days**
- condition = **after warehouse verification**
- COD destination = **original UPI or bank account only**
