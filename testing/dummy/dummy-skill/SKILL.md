---
name: dummy-skill
description: Dummy skill used only to test that the platform can install a skill from GitHub. Use when the user asks to run the dummy skill or to verify skill installation.
---

# Dummy Skill

This skill exists only to verify that skill installation works.

## Steps

1. Read `references/notes.md` with the read file tool.
2. Run `bash scripts/hello.sh` with the command line tool and capture its output.
3. Reply with exactly this block, filling in the values:

```
DUMMY_SKILL_LOADED=true
REFERENCE_FILE_READ=<yes|no>
SCRIPT_OUTPUT=<output of hello.sh>
```

Do not do anything else.
