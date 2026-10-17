# Ambiguity audit result

Paste the complete output from the one required LLM audit here.

Do not edit the model output in this file. Put your true-positive and false-positive adjudication in the report.


# Requirements-reviewer audit — INT-01

Reviewer pass over the interview transcript for ambiguity, incompleteness, and direct contradictions that could lead an implementation team or coding agent to invent product behavior. Findings only; nothing is resolved here.

| # | Label | Paragraph(s) | Excerpt | Defect type | Unsafe decision |
| --- | --- | --- | --- | --- | --- |
| 1 | Grace-period value disagrees | P06, P12 | P06: "current policy is 15 minutes"; P12: "The desk's rule is 20 minutes." | Direct contradiction | Configuring or displaying one grace number is unsafe while staff and students assert different values, so any release-timing behavior built on it may be wrong. |
| 2 | "A little late" has no threshold | P07 | "If someone is only a little late, we try not to give the kit away." | Ambiguity (vague quantity) | Encoding when informal discretion suspends a release is unsafe because "a little late" names no measurable boundary or trigger. |
| 3 | Pre-waitlist message undefined | P10 | "They should get a message before it goes to the waitlist." | Ambiguity (unclear referent and scope) | Building the notification is unsafe when who "they" are, the triggering event, the timing, and the channel are all unstated. |
| 4 | Technician "ready" signal missing | P09, P17, P19, P21 | P19: "cannot tell you what screen or workflow"; P17: "do not know what signal the technicians use." | Incompleteness (undefined workflow / unconsulted stakeholder) | Deciding how a kit becomes "ready" for the waitlist is unsafe because that step lives only in the technicians' process, which was never elicited. |
| 5 | Hold-expiry behavior missing | P04, P19 | P04: "hold until 2:25"; P19: "a temporary hold and until when." | Incompleteness (missing behavior) | What the system does when a hold's end time passes with no check-in — auto-release, extend, or wait for staff — is unstated, so the post-hold transition would be invented. |
| 6 | "Checked in" is undefined | P02, P17, P19 | P02: "mark the reservation picked up"; P17: "already checked in at the desk." | Ambiguity (undefined event) | Which action sets the protected checked-in state — arrival, ID check, or completed pickup — is unspecified, so the rule that keeps a reservation active can't be placed safely. |
| 7 | "Contact" and extension scope open | P21 | "Staff sometimes extend a reservation after a student contacts us." | Incompleteness (missing criteria) | What counts as contact, how long an extension runs, and who may grant it are unspecified, so the conditions that create a valid hold would be guessed. |
| 8 | Waitlist order and claim unspecified | P02, P09, P13 | P09: "the waitlist person may already be at the counter"; P13: "A waitlisted student was there." | Incompleteness (missing model) | How the next waitlist person is selected, offered a kit, and given time to claim it is never described, so the waitlist mechanics would be invented. |

**Spread:** 1 direct contradiction (#1), 3 ambiguity (#2, #3, #6), 4 incompleteness (#4, #5, #7, #8).

Note: this transcript also contains a compliment (P14) and a future-use prediction (P15). They are not listed here because they are not ambiguity, incompleteness, or contradiction — they are items a reviewer should exclude from evidence, not defects that would cause invented behavior.