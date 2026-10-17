# Evidence log schema

Use 8 to 10 entries. IDs must begin with E, A, or Q.

- E: real evidence from the interview transcript.
- A: an assumption that is not established by the interview.
- Q: an unresolved question that must be answered before the related decision is treated as settled.

Use this table shape:

| ID | Source | Claim | Status | Owner |
| --- | --- | --- | --- | --- |
| E-1 | OBS-02 | Rider waited 18 minutes for the next bus after a missed connection. | Observed | Student |

Status says how the claim is known: `Observed` for a specific past event someone described, `Stated` for a rule or fact a speaker asserted, `Assumption` for an A entry, and `Open` for a Q entry. Owner is the person or group who could confirm the claim or answer the question.

The worked row above is unrelated to the media-lab case. For this assignment, transcript sources must use the form `INT-01:Pxx`, for example `INT-01:P13`.

Do not cite `SYN-01` as real-user evidence. Synthetic-user material can generate a hypothesis, but it cannot establish actual user behavior, willingness, priorities, or requirements.

####

# Evidence log: INT-01 (media equipment late pickups)

| ID | Source | Claim | Status | Owner |
| --- | --- | --- | --- | --- |
| E-1 | INT-01:P04 | Yesterday a camera kit reserved for 2:00 was kept for a late student: the student called at 2:08, Jordan wrote "hold until 2:25" on the paper slip and told the other desk worker not to release it, and the student arrived at 2:22 and completed pickup. The phone call is what prevented a no-show release. | Observed | Jordan Lee (Media Lab checkout coordinator) |
| E-2 | INT-01:P13 | Last Thursday Priya's 3:00 lighting kit was released before she arrived. Her class ran to 3:11, the desk line was busy twice at 3:13, and she arrived at 3:16. A waitlisted student was at the counter while the kit was still behind the counter for a technician check of a light stand. Priya waited until 3:38 for a returned kit, and her interview started about 10 minutes late. The confirmation email, call history, and paper list each showed only part of what happened. | Observed | Priya Shah (student borrower) |
| E-3 | INT-01:P09, INT-01:P13 | Marking a reservation released does not mean the kit is ready for the next person. Technicians may need to move it from the pickup shelf, replace a missing battery, or confirm accessories, and the desk does not promise readiness until that check is finished. | Stated | Jordan Lee; equipment technicians |
| E-4 | INT-01:P06, INT-01:P17, INT-01:P21 | A reservation should not be released if the student has checked in or if staff recorded a hold. Staff sometimes extend a reservation after a student makes contact, and a checked-in reservation should stay active past the grace window. | Stated | Jordan Lee |
| E-5 | INT-01:P17, INT-01:P21 | The waitlist should only see equipment that is actually ready to hand out. The student would rather see "not yet ready" than have a waitlisted person sent to the desk during repacking. | Stated | Jordan Lee; Priya Shah |
| E-6 | INT-01:P06, INT-01:P21 | The grace value is set by the lab and has changed before. The software should use the configured value and should not invent policy. | Stated | Media Lab manager |
| E-7 | INT-01:P19 | If paper notes are replaced, the coordinator wants to keep: reservation start time, check-in status, whether a temporary hold was entered and until when, when the reservation became releasable, whether the kit is ready for the next checkout, and the reason for any manual hold. | Stated | Jordan Lee |
| Q-1 | INT-01:P06, INT-01:P12 | What grace period is actually in effect, and what are students told? Jordan says 15 minutes; Priya says the desk told her 20 minutes twice, including in March, and she does not know if it changed. The interview does not show whether the policy changed, whether desk staff give inconsistent information, or which number is correct. (The 3:16 release in P13 fits 15 minutes, but one case does not settle the policy.) | Open | Media Lab manager |
| Q-2 | INT-01:P09, INT-01:P17, INT-01:P19, INT-01:P21 | How do equipment technicians signal that a released kit is ready for the next checkout, and what screen or workflow would fit their work? Neither interviewee knows; Jordan says the technicians have not been asked. | Open | Equipment technicians |
| A-1 | INT-01:P14, INT-01:P15 | Students would use a self-service "running late" option instead of calling, and it would prevent releases. This rests on one student's hypothetical ("I would probably use it") and general enthusiasm for a dashboard. No one has used such a feature, and the interview does not say whether a student-reported delay should count as a staff hold. | Assumption | Student borrowers; Media Lab manager |

## Notes on uncertainty

- **Not resolved:** the 15- vs 20-minute grace period (Q-1) is recorded as a conflict, not picked. Any design decision should read the configured value (E-6) rather than hard-code either number.
- **Ambiguous statement not logged as a requirement:** in P10 Jordan says "They should get a message before it goes to the waitlist." It is unclear who "they" are (the late borrower, presumably), when the message is sent, or through what channel. Treat it as a follow-up for Jordan before using it.

