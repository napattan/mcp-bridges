---
name: create-skill
description: Build, distill, optimize, and verify production-grade agent skills (/create-skill). Creates cross-platform, globalized skills for Antigravity, Claude Code, and multi-agent frameworks using the BoostX engineering lifecycle, Ponytail anti-bloat ladder, and writing-great-skills vocabulary. Use when user says "create skill", "make this a skill", "turn this workflow into a skill", "/create-skill", or wants to design, scaffold, optimize, lint, or globalize an agent skill.
---

# Antigravity Skill Creator (`/create-skill`) — BoostX Edition

Authoring, distilling, optimizing, and verifying production-grade agent skills across **Antigravity IDE**, **Claude Code**, and cross-platform multi-agent environments.

This skill synthesizes three core frameworks:
1. **The BoostX Protocol**: 4-phase engineering lifecycle (Red Invariant Gate → Ponytail Architectural Gate → Dual-OS Surgical Build → Ruthless 3-Tier Verification).
2. **`writing-great-skills` Discipline**: Information hierarchy, progressive disclosure, leading words, and context-load vs. cognitive-load optimization.
3. **Universal Cross-Platform Globalization**: Physical directory allocation, dual-OS path normalization (Windows PowerShell + macOS/Linux bash), and zero-breakage cloud synchronization (OneDrive / Google Drive).

---

## 1. Scope & Storage Strategy (Globalization)

Before authoring, determine the target deployment scope:

| Scope | Destination Path | Use Case | Cross-Device Behavior |
| :--- | :--- | :--- | :--- |
| **Global (All Workspaces)** | `~/.gemini/config/skills/<skill-name>/`<br>*(Windows: `C:\Users\<User>\OneDrive\gemini-config\skills\<name>\`)* | General developer workflows (`/boostx`, `/create-skill`, `/update-doc`, MCP bridges). | Automatically synced across Desktop PC, Laptop, and dual-OS via cloud drive. **Must be a real physical directory** (never a secondary NTFS junction). |
| **Workspace Local** | `<workspace-root>/.agents/skills/<skill-name>/` | Project-specific simulation pipelines, client data transforms, local scripts. | Committed to project Git repository; shared with team members on that repo. |
| **Claude Code Portable** | `~/.claude/skills/<skill-name>/` | Command-line Claude Code workflows. | Drop-in compatible; follows identical `SKILL.md` standard. |

> [!IMPORTANT]
> **The NTFS Junction Invariant**: When creating global skills on Windows where `~/.gemini/config/skills` is already a junction to OneDrive, **always create real directories** inside the target folder. Never create nested secondary junctions, as Electron/Node.js file scanners refuse to traverse recursive links and will hide the skill from the `/` autocomplete menu.

---

## 2. Ingestion Modes

The skill operates in two distinct modes based on context:

### Mode A: Session Distillation ("Make this a skill")
* Triggered when the user says *"make this a skill"*, *"package what we just did"*, or *"turn this workflow into a reusable skill"*.
* Reads the active conversation history / transcript (`transcript.jsonl`).
* Extracts the sequence of successful shell commands, error recoveries, tool calls, and output schemas.
* Strips debugging detours and synthesizes the distilled, repeatable path into clear steps.

### Mode B: Greenfield Architecture ("Create a skill for X")
* Triggered when building a skill from an API, library documentation, PRD, or new domain (e.g. QGIS analysis, Grasshopper solver, Docx processing).
* Conducts a focused, non-bloated 3-question interview (Intent, Tools/Inputs/Outputs, Edge Cases).

---

## 3. The 4-Phase BoostX Skill Creation Lifecycle

```
┌────────────────────────────────────────────────────────┐
│  Phase 1: THE RED INVARIANT GATE                       │
│  • Define AI failure mode & hallucinations to cure     │
│  • Draft 2 Trigger Probes (1 Positive, 1 Negative)     │
│  • Decide Model-Invoked vs. User-Invoked               │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│  Phase 2: ARCHITECTURAL VECTORS & PONYTAIL LADDER      │
│  • Vector A: Rule in AGENTS.md (No skill needed?)      │
│  • Vector B: Pure Instruction Skill (Zero scripts)     │
│  • Vector C: Hybrid Skill (Instructions + stdlib CLI)  │
│  • Select lowest rung that holds                       │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│  Phase 3: DUAL-OS SURGICAL EXECUTION                   │
│  • Write SKILL.md with front-loaded leading words      │
│  • Progressive disclosure (push reference to .md)      │
│  • POSIX paths (`/`), UTF-8 encoding, dual shell syntax│
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│  Phase 4: RUTHLESS 3-TIER VERIFICATION                 │
│  • Tier 1: Static YAML Schema & Character Limit Lint   │
│  • Tier 2: Markdown Link & Script Integrity Check      │
│  • Tier 3: Physical Directory & Slash Menu Discovery   │
└────────────────────────────────────────────────────────┘
```

---

### Phase 1: The Red Invariant Gate (Pre-Creation)

Answer these three questions before drafting:

1. **What is the Red Failure Mode?**
   * What does the model get wrong without this skill? (e.g. uses deprecated methods, hallucinates non-existent tools, ignores rate limits, fails on cross-platform paths).
2. **Invocation Decision (Context Load vs. Cognitive Load)**:
   * **Model-Invoked** (Default): Keeps a rich `description` with triggers and branch keywords. Contributes context load every turn; agent can trigger it autonomously.
   * **User-Invoked**: Set `disable-model-invocation: true`. Strips agent triggers. Only fires when typed explicitly by the user (e.g., destructive operations, maintenance runs). Zero context load.
3. **Trigger Probes**:
   * **Positive Probe**: A user prompt that *must* trigger the skill.
   * **Negative Probe**: A related but out-of-scope prompt that *must NOT* trigger it.

---

### Phase 2: Architectural Vectors & The Ponytail Ladder

Run the Ponytail Senior Dev Filter to determine the simplest structure:

* **Rung 1 (YAGNI / Rule Check)**: Does this actually need a skill? If it's a 2-line behavioral preference ("always use UTF-8", "no LaTeX math"), put it in `AGENTS.md` / rules instead.
* **Rung 2 (Tool Reuse)**: Do native tools or installed MCP servers (`gh`, `git`, `qgis`, `rhino`) already do this? If yes, instruct the model to call them directly. Do NOT write wrapper code.
* **Rung 3 (Structure Selection)**:
  * **Workflow Archetype**: Ordered steps, sequential checklist, completion criteria (e.g., `/update-doc`, deployment pipeline).
  * **Task Toolkit Archetype**: Independent sub-actions with quick-starts (e.g., `/illustrator`, PDF toolkit).
  * **Reference Archetype**: Rules, domain definitions, style guidelines (e.g., `writing-great-skills`).
* **Rung 4 (Code vs. No-Code)**:
  * Default to **Pure Instruction (Zero Code)**.
  * Only produce a script (`scripts/run.py`) if deterministic file parsing, mathematical transformations, or API rate-limiting are required.
  * If a script is required: use Python stdlib (`argparse`, `pathlib`, `json`, `urllib`) — avoid third-party dependencies unless strictly necessary.

---

### Phase 3: Dual-OS Surgical Execution

When authoring the skill files, enforce strict cross-platform standards:

#### 1. Structure Blueprint
```
skill-name/
├── SKILL.md              ← Required. Frontmatter + Core Instructions (< 500 lines)
├── references/           ← Optional. Deep docs loaded on-demand via pointers
└── scripts/              ← Optional. Deterministic CLI helpers (stdlib-first)
```

#### 2. YAML Frontmatter Template
```yaml
---
name: [lowercase-hyphenated-name-max-64-chars]
description: >
  [Leading-word summary in 1 sentence].
  Use this skill when [primary triggers, exact keywords, slash command].
  Also use when [secondary triggers, synonyms, user intents].
  Do NOT use for [explicit negative exclusions to prevent false triggers].
---
```

#### 3. Dual-OS & Portability Invariants
* **POSIX Paths**: Use forward slashes (`/`) exclusively in markdown links and code paths.
* **No Hardcoded Absolute Roots**: Never hardcode `C:\Users\...` or `/Users/...`. Derive paths relative to workspace or use home-relative `~/` or `%USERPROFILE%` / `%APPDATA%` paths.
* **Strict Forward-Slash Links**: Zero backslashes (`\`) inside markdown links `[...](...)`. Backslashes break in web renderers, GitHub markdown, and Unix platforms.
* **Dual-Shell Commands**: When providing shell commands in `SKILL.md`, provide both or use cross-platform commands:
  * PowerShell (Windows): `Get-ChildItem`, `Select-String`, `$env:VAR`
  * Bash/Zsh (macOS/Linux): `ls`, `grep`, `export VAR`
  * Or cross-platform Python one-liners: `python -c "import pathlib; ..."`
* **UTF-8 Python Header Standard**: Every generated Python helper script or verification probe must start with the standard BoostX stream guard to prevent Windows terminal `cp1252` encoding crashes on symbols (`✓`, `→`, `✨`):
  ```python
  import sys
  if sys.stdout and hasattr(sys.stdout, "reconfigure"):
      sys.stdout.reconfigure(encoding="utf-8")
  ```

---

### Phase 4: Ruthless 3-Tier Verification (The Green Gate)

A skill is **NOT finished** until it passes all three automated verification tiers:

```
[Tier 1: Static Linter] ──> [Tier 2: Integrity & Hardcode Audit] ──> [Tier 3: IDE Discovery]
```

#### Tier 1: Static Frontmatter Linter
* `name` matches regex `^[a-z0-9-]+$` and is ≤ 64 characters.
* `description` exists and is ≤ 1024 characters.
* If model-invoked: Description contains both positive trigger keywords and a negative `Do NOT use for` clause.
* Frontmatter starts on line 1 with `---` and ends with `---`.

#### Tier 2: Integrity, Anti-Hardcode & Secret Sanitization
* **Zero-Hardcode & Secret Audit**: Run an automated regex check across all created files (`.md`, `.py`, `.sh`, `.json`):
  * **Machine Paths**: Flag any line matching `(?i)([a-z]:[/\\]users[/\\]|/Users/|/home/)` (unless sanitized as `<User>` or `<username>`).
  * **Secrets & Tokens**: Flag any unredacted token matching `(?i)(api[_-]?key|secret|token)\s*[:=]\s*["'][a-zA-Z0-9_\-\.]{16,}["']`.
* **Zero-Recursive-Nesting Invariant**: Verify no self-named child folder exists (`assert not (skill_dir / skill_dir.name).exists()`), preventing PowerShell copy-nesting traps (`skill/skill`).
* **Markdown Link Integrity & Forward-Slash Check**:
  * Every relative link (`[file](...)`, `references/...`, `scripts/...`) must resolve to a real file on disk.
  * Zero backslashes inside markdown link parentheses (`assert not re.search(r'\[.*?\]\([^\)]*\\[^\)]*\)', text)`).
* **Script Compilation**: If Python scripts are included, compile them for syntax:
  ```powershell
  python -m py_compile scripts/*.py
  ```

#### Tier 3: Physical Directory & IDE Discovery Check
* Check file system properties of the skill directory. Verify `LinkType` is empty (a real physical directory, NOT an NTFS junction loop).
* Confirm presence in the parent skills directory so that Antigravity IDE immediately registers it in the `/` slash autocomplete list.

---

## 4. Post-Creation Summary Rubric

When reporting the newly created skill to the user, provide:
1. **Skill Name & Scope**: Global vs. Workspace Local.
2. **Physical Location**: Clickable file link to `SKILL.md`.
3. **Trigger Invariants**: The primary slash command and keywords that trigger it.
4. **Verification Pass**: Confirmation that Tier 1, 2, and 3 checks passed cleanly.
