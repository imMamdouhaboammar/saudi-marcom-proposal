# Behavioral Harness Contract

A true behavioral evaluation runner should:

1. load the Skill build under test
2. send only `public_prompt` and allowed fixtures to the model
3. capture tool calls, intermediate artifact metadata, terminal status, and final answer
4. keep `must_do`, `must_not_do`, and `pass_criteria` private from the tested model
5. score with `evals/rubric.md`
6. compare two Skill builds under the same runner when retuning
7. include held-out prompts not authored by the same context that wrote the Skill
8. record model, Skill hash, fixtures hash, tool availability, and date

Do not claim behavioral maturity from static JSON validation alone.
