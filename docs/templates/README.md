# docs/templates/

Reusable document templates for BUS 629 written deliverables.

## Templates in use

| Template | Used for | Source |
|----------|----------|--------|
| Memo template | Stage 2 company selection memo | BUS 629 course repo |
| Spec template | Stage 4 technical specification | BUS 629 course repo |

## File naming convention

All memos and specs in this repo follow:

```
YYYY-MM-DD-{slug}.md
```

Lowercase slug, hyphen-separated, ISO date prefix so files sort chronologically.

**Examples:**
- `2026-05-10-nguyen-coca-cola-selection.md` — Stage 2 company selection memo
- `2026-06-01-nguyen-coca-cola-spec.md` — Stage 4 technical specification

## YAML frontmatter

Every document based on a template includes a YAML frontmatter block with `template`, `purpose`, `audience`, `stage`, `author`, and `date`. Keep the frontmatter intact when adapting templates — it documents analytical intent and is read by the LLM-spec workflow at Stage 4.

## Customizations

No templates have been modified from the course originals. All documents in `docs/decisions/` and `docs/specs/` link back to the canonical course template structure.
