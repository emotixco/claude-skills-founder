---
type: llm
weight: 3
---

The workspace contains founder/facts.md, which records "Monthly recurring revenue is $2,100" from an earlier session. The founder has now said MRR crossed $6,400 last week.

PASS if the reply uses $6,400 as the current figure and tells the founder that this supersedes the saved $2,100 fact, whether by naming the old number, saying the saved facts were updated, or saying the recorded revenue is out of date.
FAIL if the reply puts $2,100 on the slide as current, presents both numbers as if both were current, or uses $6,400 without any sign that it noticed the saved fact it contradicts.

Growth framing that uses the old number deliberately, such as "up from $2,100", counts as noticing it and is a PASS as long as $6,400 is the current figure.
