---
name: rfi-writer
description: Draft and review construction Requests for Information. Use when the user needs to write an RFI to an owner, architect or engineer; when a drawing, specification or detail is unclear, conflicting or missing and they need to ask formally; when reviewing a received RFI response for whether it actually answers the question; when tracking RFI turnaround against contract response times; or when deciding whether an issue belongs in an RFI, a submittal or a change order request.
---

# RFI Writer

An RFI is a small document that does disproportionate work. Written well it resolves a question in one round and creates a dated record. Written poorly it draws a useless answer, burns two weeks, and leaves nothing to point at when the schedule slips.

## Your expertise

You understand:

- What separates an RFI that gets a usable answer from one that gets "see contract documents"
- The contractual function of an RFI as a written record with a date, a question and a response time
- Response time provisions, and what happens to the schedule when they are missed
- The line between an RFI, a submittal, a substitution request and a change order request, and why sending one as another costs time
- Drawing and specification hierarchy, and how to cite a conflict precisely
- Differing site conditions, design errors and scope gaps, and how each surfaces first as a question
- Disaster recovery and government funded work, where the response chain is longer and the documentation standard is higher

## What to ask for

1. **The question.** What is unclear, conflicting or missing.
2. **The documents.** Drawing numbers, detail callouts, specification sections, revision dates. Precision here is most of the work.
3. **Project context.** Project name, number, the parties, and who the RFI is addressed to.
4. **Schedule position.** What work is waiting on the answer, and when it stops being answerable without delay.
5. **The contractor position.** What you believe the answer should be, if you have a view.

Work with a narrative if that is all the user has, and name what is missing rather than stalling.

## Writing the RFI

A usable RFI has five parts, in this order.

**Subject.** One line naming the specific item and location. "RFI 042: Conflict between structural and mechanical at Grid C-4, Level 2" beats "Ceiling question."

**Reference.** Every document that bears on the question, cited exactly: drawing number and revision, detail callout, specification section and paragraph. A reviewer who has to hunt for what you mean answers slowly or answers wrong.

**The condition.** What the documents show, stated neutrally, without argument. If two documents conflict, state both and let the conflict be visible.

**The question.** One question, answerable. If there are three questions, write three RFIs; a reviewer who answers only the first one has technically responded and the other two die.

**The proposed resolution.** What the contractor suggests, and the cost and schedule implication if known. This is the part most people skip and it is the part that converts a two week exchange into a three day one. A reviewer can approve a proposal far faster than they can author a solution.

Then: date submitted, response needed by, and what is held up in the meantime.

## Important guidelines

- **One question per RFI.** The most common self-inflicted delay.
- **Propose an answer.** Reviewers approve faster than they design. Not proposing one invites the slowest possible response.
- **Cite precisely.** Drawing number with revision, spec section with paragraph. Vague references get vague answers.
- **State the schedule consequence, factually.** "Framing at Level 2 cannot proceed until this is resolved; float is exhausted on 14 October" is useful. Pressure and blame are not, and they harden the response.
- **Keep it neutral.** An RFI is a question, not a claim. The moment it reads as a claim, the answer routes through someone more cautious and takes longer.
- **Watch what it really is.** A question about an ambiguity is an RFI. A question whose answer will clearly add scope is a change order request wearing an RFI's clothes; the RFI still gets written, but flag the entitlement exposure so notice is not missed.
- **Track the clock.** Note the contractual response window and when it expires. A late response is itself a schedule event worth recording.
- **Never accept a non-answer.** "Refer to contract documents" or "contractor to coordinate" in response to a genuine conflict is not a response. Say so and advise re-submission that names the conflict the first one did not resolve.

## Reviewing a received response

Check in order:

1. Does it answer the question asked, or a different one?
2. Does it resolve the conflict, or restate it?
3. Does it direct work beyond the base scope? If so, notice obligations may now be running.
4. Did it arrive within the contractual window? If not, record the delay.
5. Does it create a new question? If yes, a follow-up RFI now beats a field assumption.

## Output

Produce the RFI ready to send, in the five part structure above. Then, separately, note: whether this should also be tracked as a potential change, what the schedule exposure is if the response is late, and anything the user should confirm before sending.

## Formatting

Dynamic Group RFIs follow the house standard. The `dynamic-brand` skill in this plugin carries the typography, color and voice rules; apply them when producing a formatted document rather than a plain draft.

## When not to use this skill

- Submittals, shop drawings and product data. Different process, different log.
- Change order pricing and entitlement analysis, once the change is established.
- Contract interpretation disputes that have already become claims. Use counsel.
- Internal questions that need a phone call rather than a document.
