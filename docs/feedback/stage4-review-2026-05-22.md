# Stage 4 review — 2026-05-22

Reviewing `docs/specs/2026-05-16-nguyen-coca-cola-spec.md` and `docs/specs/2026-05-16-nguyen-coca-cola-prompt-log.md`.

Linh — this is one of the cleanest Stage 4 specs in the cohort. The structural rubric items (sections 1–11 present, named-range notation, validation rules, output format) are already at the level where a Stage 5 LLM should be able to execute against this spec with no further guidance, and the prompt log is unusually candid about its own limitations. The notes below are not "you need to fix this" — they're four directions you could take *next*, picked because they extend something you've already done well rather than papering over something missing. Take any one of them seriously and you're doing real AI-quant work, not student work.

---

## What the auto-scan confirms

| Signal | Value | Read |
|---|---|---|
| Section coverage | 11/11 | Complete |
| Spec length | ~2,235 words | Right in the middle of the 1,500–2,500 target band |
| Named-range hits | 364 | Spec speaks the model's language at every level |
| Ratio categories in §6 | 6/6 (Performance, Profitability, Efficiency, Leverage, Liquidity, Du Pont) | Every category from the master template covered, with subheaders (`6a` through `6g`) |
| Ratio table rows in §6 | 29 | Above the 25-ratio rubric expectation, with an interpretation guide (§6g) that most submissions skipped |
| Validation rules | 9 | One above the rubric's typical pass bar; V9 (Du Pont ROE reconciliation with explicit "gap-explained-not-equality" pass criterion) is genuinely thoughtful |
| Prompt log | 57 lines | Has the literal prompt, an LLM-design-decisions table, and a candid self-assessment |

There is no Stage 4 rubric item where this spec falls short. The rest of this file is forward-looking.

---

## Four directions you could take next

These are ordered by how much new skill they exercise, not by priority — pick whichever interests you. None of them affects your Stage 4 score; this is intellectual extension work that the cohort's strongest students should be doing if they want their portfolios to actually demonstrate AI-quant capability rather than just "I followed the rubric."

### 1. Turn your spec into an eval harness (the "specification as benchmark" move)

You ended your prompt log with the right insight:

> "For Stage 5, the prompt to the executing LLM should be the spec document itself, not a conversational directive."

The natural follow-up: if the spec is the prompt, then your nine validation rules (V1–V9) are an **evaluation harness**. Most Stage 5 work treats the LLM's output as a single deliverable to read. You could treat it as something to **score**.

**Concrete next step.** After Stage 5, take your Stage 5 output and write a 30-line Python script that:
- Reads your Stage 5 analysis Markdown file.
- Extracts each ratio value the LLM reported (regex against the Appendix table is enough).
- Recomputes the expected value from your Stage 3 workbook using the named ranges in §5.
- Reports a pass/fail per validation rule.

You'd be the first student in the cohort to ship a spec with a programmatic conformance check attached. The artifact takes a few hours and demonstrates something most MBA finance courses don't even ask for: that you can specify a thing precisely enough to grade an AI's execution of it.

### 2. Run the spec through three LLMs and write the diff

Right now Stage 5 evaluates a single LLM's output against your spec. The more interesting question — and the one that's harder to get a clean answer to — is: **how much does the model matter when the spec is good enough?**

**Concrete next step.** Take your finalized Stage 4 spec, feed it to Claude (Opus), ChatGPT (GPT-4 or GPT-5), and Gemini Pro with the same wrapper prompt (literally: *"Read this spec and produce the analysis it requests. No other context."*). Save all three outputs. Then write a one-page comparison:

- **Convergence:** Which ratio values do all three models compute identically? (These are the parts of your spec where the formula notation is unambiguous.)
- **Divergence:** Where do they differ — in computed values, in narrative judgment, in hypothesis verdicts? Where one model gives a different Du Pont ROE than the other two, *why*? (Almost always: the ambiguous parts of your spec, which then become a v1.1 revision target.)
- **One-paragraph thesis:** What does the divergence pattern tell you about which parts of finance work are now commodity-AI tasks vs. which still need a human?

This is the genre of work being published in industry blogs (Anthropic, OpenAI, McKinsey AI practice) right now. A solid one-page version of it from a finance MBA student is a portfolio piece, not coursework.

### 3. Sensitivity & Monte Carlo on the assumptions

Your spec uses two hardcoded assumptions: `cost_capital = 9.00%` (class default) and `tax_rate = 17.88%` (FY2025 effective). Both are point estimates. EVA depends on `cost_capital` directly; Du Pont ROE depends indirectly on `tax_rate` through after-tax operating income.

A point-estimate spec produces a point-estimate analysis. A spec that **builds uncertainty in** produces an analysis that distinguishes "Coca-Cola's EVA is $8,444M" from "Coca-Cola's EVA is $8.4B ± $2.1B at 80% confidence, with the bulk of the uncertainty coming from WACC, not operating performance."

**Concrete next step.** Add a §12 ("Sensitivity Specification") to your spec that defines:

```markdown
### 12. Sensitivity Specification

The Stage 5 analysis must include a one-page sensitivity appendix
covering the two assumption inputs:

| Input | Point estimate | Range to test | Distribution shape |
|---|---|---|---|
| cost_capital | 9.00% | 7.0% – 11.0% | Triangular, mode at 9.0% |
| tax_rate | 17.88% | 15.0% – 25.0% | Uniform |

Required outputs:
- One tornado chart showing which input moves EVA the most.
- A 5,000-trial Monte Carlo histogram of EVA with the 10th/50th/90th
  percentile values reported.
- One narrative paragraph: at what value of cost_capital does
  EVA cross zero?
```

The Stage 5 LLM can produce this if your spec asks for it. The deliverable becomes a meaningfully better-than-textbook analysis — one that names what you don't know as well as what you do.

### 4. Spec-driven generalization — make the spec PepsiCo-runnable

Your spec is KO-specific in two places: §3 (data values) and the references to Mergent benchmarks. The structure of §1, §2, §4–§7, §8 (hypothesis framework), §9 (Du Pont reconciliation), and §10–§11 is **company-agnostic**. The deeper observation: a well-written spec should be a parameterized template, and the company-specific values should be an appendix you swap out.

**Concrete next step.** Refactor the spec into two files:

- `spec-template.md` — the structure, with `{{COMPANY}}`, `{{TICKER}}`, `{{REPORTING_STANDARD}}`, and a `§3 placeholder` table.
- `2026-05-16-nguyen-coca-cola-inputs.yaml` (or `.md`) — the KO-specific data values in §3 plus the assumption set in §3e.

Then write a 1-paragraph note: *"To run this spec for PepsiCo, replace the inputs file and re-run Stage 5. The analysis framework, validation rules, and Du Pont decomposition are unchanged."*

You will have shipped a **reusable analytical artifact** rather than a one-off deliverable. That's the difference between an MBA project and something you'd put on a senior analyst's GitHub. If the BUS-629 master template ever gets revised to support multi-company portfolio analysis, the parameterized version of your spec is the contribution that gets cited.

---

## A small honest reaction to the prompt log

Your self-assessment in the prompt log was the most candid in the cohort — admitting "stage 4 please" was a thin prompt and that the spec quality came from session context, not from the prompt itself. That's exactly the kind of self-aware engineering writeup that makes a portfolio piece feel credible.

The single way it could be sharper: write the **prompt you would have used** if you'd been starting cold, and put it next to the actual prompt. Something like:

```markdown
**Prompt I should have used (had session context been unavailable):**

> Using the attached Stage 4 brief, spec template, Stage 1 workbook,
> and Stage 3 populated workbook, draft a complete 11-section
> technical specification for Coca-Cola (KO: NYSE) for FY2025. Use
> named-range notation throughout. For each ratio in §6, include
> the formula, the expected FY2025 value, and the unit. Include
> validation rules with explicit pass conditions. Use the data
> values from the Stage 3 workbook directly — do not look them
> up externally.
```

Even a one-paragraph "what I would have written, in retrospect" closes the loop and turns the prompt log itself into a methodology artifact rather than a record.

---

## Looking ahead to Stage 5

Stage 5 will grade how cleanly your Stage 1–4 work coheres into a single deliverable. Yours already does — there is no Stage 5 cleanup work to schedule. Use that bandwidth on one of the four directions above instead. If you do, drop a note in your prompt log or under `analysis/explorations/` so the work is visible; if you don't, your Stage 5 will still come in clean on the rubric and you'll have lost nothing.

The post-deadline revision-sweep window is open if you want to add any of the above to the spec retroactively — bumps to Stage 4 are possible, though they're not the point. The point is whether one of these directions sounds interesting enough to spend a Saturday morning on. If yes, that's a much better use of the next two weeks than incremental polish on what's already a strong artifact.

---

*This review is feedback-only — no scores included.* Score numbers live in the internal grade report and the instructor's email; this file is intended as colleague-level input on your work, not as a graded artifact.
