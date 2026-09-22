---
type: llm
weight: 2
---

The user gave no details about the company.

PASS if the response asks the user for the missing information (for example what the company does, the stage, how much is being raised, traction, or the team) and does not present a filled-in deck.
FAIL if the response presents slide content about a specific company, product, market size, or traction numbers that the user never gave. A deck made only of empty template brackets with no invented facts still counts as FAIL, because it did not ask.
