# dummy-skills

Test repo for checking skill installation on the platform.

Layout: each skill is a folder at the repo root containing a `SKILL.md`.

    dummy-skills/
      dummy-skill/
        SKILL.md
        references/notes.md
        scripts/hello.sh

## Add on the platform

- Repo URL: `https://github.com/<your-user>/dummy-skills`
- Skill name: `dummy-skill`
- Expected id: `https://github.com/<your-user>/dummy-skills/dummy-skill`

## Test prompt

    Load the skill `dummy-skill` with the skill tool and follow it.
    If it cannot be loaded, reply: HALTED - UNABLE TO LOAD REQUIRED SKILL
