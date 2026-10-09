# Skill Installation Failure — Root Cause Analysis (RCA)

## 1. Executive Summary

- **Repository Affected**: `https://github.com/KISLAYA-SRI/dark-factory-skills`
- **Impact**: When running the agent platform (Slingshot / Claude Agent), skills failing to install with `Error: Installation process exited with code 1`, completely halting workflow execution.
- **Root Cause**: Breaking directory changes introduced in commit `3370331` created mixed folder depths (2-level and 3-level structures co-existing in the same categories) and misplaced defect skills outside of their designated suite folder (`defect-skills-folder/`).
- **Resolution**: Restructure the repository into a clean, uniform 3-level folder hierarchy (`<category>/<sub-folder>/<skill>/SKILL.md`) and remove binary `.DS_Store` artifacts.

---

## 2. Failure Logs & Observed Error

During the agent startup and skill dependency loading phase, the installer reported:

```text
Installing skill 'dummy-skill-test'...
Installing skill 'defect-fix'...
Error installing skill 'dummy-skill-test': Failed to install skill dummy-skill-test: Error: Installation process exited with code 1
Error installing skill 'defect-fix': Failed to install skill defect-fix: Error: Installation process exited with code 1
Skills cache summary: 0 cache hits, 0 fresh installs
HALTED - UNABLE TO LOAD REQUIRED SKILL
```

---

## 3. Commit Analysis: The Breaking Change

The issue was introduced in commit **`3370331`** (`Update in defect skills`):

```text
commit 33703313d42c3df49520a811776dc6d4fe6a3bf0
Author: shosarin <shobhit.sarin@publicissapient.com>
Date:   Thu Oct 8 13:18:30 2026 +0530

    Update in defect skills

 .../run-test-cases/SKILL.md                        |  0
 .../run-test-cases/scripts/run-tests.py            |  0
 .../{defect-skills-folder => }/defect-fix/SKILL.md | 60 +++++++++++++++-------
 .../defect-fix/references/impact-map.md            |  0
 .../defect-fix/references/reporting.md             |  0
 .../defect-fix/scripts/verify-evidence.py          |  0
 react-skills-tw/dummy-skill-test/SKILL.md          | 10 ++++
 7 files changed, 52 insertions(+), 18 deletions(-)
```

### What Changed in this Commit:
1. **`defect-fix` was moved out** of `react-skills-tw/defect-skills-folder/` to `react-skills-tw/defect-fix/` (changed from Level 3 to Level 2).
2. **`dummy-skill-test` was added** directly under `react-skills-tw/dummy-skill-test/` (Level 2).
3. **`run-test-cases` was moved** into `react-skills-tw/coding-skills-folder/run-test-cases/` (Level 3).
4. Other defect skills (`defect-context-loader`, `defect-investigate-and-fix`, `defect-root-cause-analysis`, etc.) remained inside `react-skills-tw/defect-skills-folder/` (Level 3).

---

## 4. Root Cause Breakdown

### A. Inconsistent Directory Depth (Primary Cause)
The automated skill installer performs recursive path traversal assuming a consistent 3-level folder hierarchy:
$$\text{category} \longrightarrow \text{sub-category} \longrightarrow \text{skill}$$

When a category contains a mixture of loose Level-2 skill packages and Level-3 subdirectories, the package indexer fails during resolution:
- It looks for defect skills under `react-skills-tw/defect-skills-folder/`.
- `defect-fix` and `dummy-skill-test` were moved outside to `react-skills-tw/`.
- Result: The installer is unable to locate the skill bundle at the expected path, exiting with `code 1`.

### B. Broken Reference in `defect-fix/SKILL.md`
`defect-fix/SKILL.md` hardcodes references to:
```bash
python3 ./.agents/skills/run-test-cases/scripts/run-tests.py
```
Because `run-test-cases` was moved inside `coding-skills-folder/run-test-cases`, the hardcoded path breaks whenever `defect-fix` is executed.

### C. OS Junk Artifacts
Binary `.DS_Store` files committed inside `defect-skills-folder` and `coding-skills-folder` interfere with directory parsers expecting only sub-directories or markdown files.

---

## 5. Architectural Comparison

### Broken State (`dark-factory-skills`):
```text
react-skills-tw/
├── defect-fix/                   ❌ [Level 2 - Loose skill]
│   ├── references/
│   ├── scripts/
│   └── SKILL.md
├── dummy-skill-test/             ❌ [Level 2 - Loose skill]
│   └── SKILL.md
├── analysis-output-contract/     ❌ [Level 2 - Loose skill]
├── api-analysis-sitecore-and-bff/❌ [Level 2 - Loose skill]
├── coding-skills-folder/         ✅ [Level 3 container]
│   ├── code-generation-reporting/
│   └── run-test-cases/
└── defect-skills-folder/         ⚠️ [Level 3 container - missing defect-fix & dummy-skill-test]
    ├── defect-context-loader/
    ├── defect-investigate-and-fix/
    └── .DS_Store                 ❌ [Binary junk]
```

### Working State (`KesavaSravan/skills`):
```text
react-skills-tw/
├── defect-skills-folder/         ✅ [Level 3 container]
│   ├── defect-fix/
│   │   ├── references/
│   │   ├── scripts/
│   │   └── SKILL.md
│   ├── dummy-skill-test/
│   │   └── SKILL.md
│   ├── defect-context-loader/
│   └── ...
├── analysis-skills-folder/       ✅ [Level 3 container]
│   ├── analysis-output-contract/
│   └── api-analysis-sitecore-and-bff/
├── archived-skills-folder/       ✅ [Level 3 container]
└── coding-skills-folder/         ✅ [Level 3 container]
```

---

## 6. How to Fix `dark-factory-skills`

Run the following commands inside `dark-factory-skills` to apply the fix:

```bash
# 1. Move defect skills into defect-skills-folder
git mv react-skills-tw/defect-fix react-skills-tw/defect-skills-folder/defect-fix
git mv react-skills-tw/dummy-skill-test react-skills-tw/defect-skills-folder/dummy-skill-test

# 2. Group analysis skills into analysis-skills-folder
mkdir -p react-skills-tw/analysis-skills-folder
git mv react-skills-tw/analysis-output-contract react-skills-tw/analysis-skills-folder/
git mv react-skills-tw/api-analysis-sitecore-and-bff react-skills-tw/analysis-skills-folder/
git mv react-skills-tw/component-breakdown-and-hierarchy react-skills-tw/analysis-skills-folder/
git mv react-skills-tw/component-reuse-validation react-skills-tw/analysis-skills-folder/
git mv react-skills-tw/context-gathering react-skills-tw/analysis-skills-folder/
git mv react-skills-tw/context-validation react-skills-tw/analysis-skills-folder/
git mv react-skills-tw/developer-notes-protocol react-skills-tw/analysis-skills-folder/
git mv react-skills-tw/figma-design-analysis react-skills-tw/analysis-skills-folder/
git mv react-skills-tw/master-analysis-orchestrator react-skills-tw/analysis-skills-folder/
git mv react-skills-tw/master-static-code-quality react-skills-tw/analysis-skills-folder/
git mv react-skills-tw/story-analysis-end-to-end react-skills-tw/analysis-skills-folder/

# 3. Clean up .DS_Store files
find . -name ".DS_Store" -delete
git add -u

# 4. Commit and push
git commit -m "fix: restore uniform 3-level folder structure for all skill suites"
git push origin main
```
