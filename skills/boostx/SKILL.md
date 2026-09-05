---
name: boostx
description: BoostX deep reasoning and high-discipline problem solving (/boostx). Solves complex coding tasks, tricky bugs, and architectural problems through hypothesis validation, Ponytail efficiency ladder, tight red-capable feedback loops, dual-OS cross-platform parity, and ruthless verification.
---

# Antigravity BoostX Protocol (`/boostx`)

When `/boostx` is invoked or high-discipline engineering is required, enter the **Antigravity BoostX Protocol**. This protocol enforces systematic root-cause analysis, anti-overengineering constraints (Ponytail Ladder), dual-OS cross-platform compatibility, and non-negotiable verification gates.

---

## 1. Execution Engine Selection

Depending on the host runtime capabilities, select the appropriate execution engine:

* **Engine A: Unified Direct Persona (Default in Antigravity / Gemini IDE)**:
  * When `invoke_subagent` is not exposed in the tool schema, the agent operates directly in a **disciplined dual-phase persona**:
    1. **Investigator Persona**: Isolate root causes, map boundary conditions, define invariants, and construct a failing repro signal before touching production code.
    2. **Builder Persona**: Apply the Ponytail ladder, implement the shortest working diff, and execute 3-tier verification.
* **Engine B: Multi-Agent Delegation (Available in platforms supporting `invoke_subagent`)**:
  * Delegate specialized subtasks:
    * **`DeepCoder`**: Coding / Refactoring / Minimal Diff Implementation (`invoke_subagent(TypeName='DeepCoder', Workspace='inherit')`).
    * **`DeepInvestigator`**: Root Cause Analysis / Bug Diagnosis / Invariant Mapping (`invoke_subagent(TypeName='DeepInvestigator', Workspace='inherit')`).
  * If delegating, route the user's prompt verbatim without pre-work, and conduct iterative review rounds via follow-up messages until all verification gates pass.

---

## 2. The 4-Phase BoostX Lifecycle

Every task executed under BoostX must strictly advance through four progressive gates:

```
┌────────────────────────────────────────────────────────┐
│  1. DECONSTRUCT & BUILD RED SIGNAL (The Red Gate)      │
│     • Define non-negotiable success invariants         │
│     • Map boundary failure modes (null, limits, async) │
│     • Run ONE exact command that fails on the bug      │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│  2. ARCHITECTURAL EXPLORATION & PONYTAIL FILTER        │
│     • Formulate 2-3 distinct solution vectors          │
│     • Apply Ponytail Ladder: YAGNI → Reuse → Stdlib   │
│     • Select the shortest working diff                 │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│  3. SURGICAL EXECUTION & DUAL-OS STANDARDS             │
│     • Implement minimal, high-impact changes           │
│     • Zero unnecessary abstractions or dependencies    │
│     • Preserve interfaces & backwards compatibility    │
│     • Enforce cross-platform Windows/macOS invariants  │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│  4. RUTHLESS 3-TIER VERIFICATION (The Green Gate)      │
│     • Tier 1: Show original reproduction failure       │
│     • Tier 2: Run signal + boundary stress tests       │
│     • Tier 3: Run workspace regression sweep           │
└────────────────────────────────────────────────────────┘
```

---

### Phase 1: Deconstruct & Build the Red Signal (Mandatory Pre-Edit Gate)

**Never write production code based on assumptions or surface symptoms.**

1. **State Formal Invariants**:
   - What must **always** remain true?
   - What boundary conditions exist (null/empty data, extremes, encoding, race conditions, disconnected states)?
2. **Construct a Red-Capable Signal**:
   - Formulate **one exact command** (a test invocation, python script, CLI call, or curl) that reproduces the failure.
   - **Execute the command and observe it go RED**:
     - If you cannot prove that it fails before the change, you cannot prove that your code fixed it afterward.
   - Only when a deterministic, fast failing signal is demonstrated may you proceed to Phase 2.

---

### Phase 2: Architectural Exploration & Ponytail Efficiency Ladder

Before implementing, evaluate 2–3 distinct solution paths against the **Ponytail Senior Dev Ladder**:

1. **Vector Comparison**:
   - **Vector A (Surgical Local Fix)**: Smallest touchpoint; patches the root cause at the immediate seam.
   - **Vector B (Clean Architectural Refactor)**: Cleans up module boundaries or data structures if the current seam is broken.
   - **Vector C (Simplification / Deletion)**: Eliminates the complexity altogether (YAGNI).
2. **The Ponytail Ladder Filter**:
   - **Step 1 (YAGNI)**: Does this feature or abstraction really need to exist? Delete or skip speculative code.
   - **Step 2 (Codebase Reuse)**: Does a helper, utility, or established pattern already exist in the repository?
   - **Step 3 (Stdlib / Native First)**: Prefer standard library functions (`os`, `sys`, `json`, `math`) and native language/platform features over adding external libraries.
   - **Step 4 (Shortest Working Diff)**: Choose the approach with the minimal blast radius and zero side effects.

---

### Phase 3: Surgical Execution & Dual-OS Standards

1. **Single Point of Truth**:
   - Modify only what is necessary to satisfy the invariants.
   - Avoid touching unrelated files or restructuring working code.
2. **Preserve Documentation & Comments**:
   - Maintain existing comments, docstrings, and type annotations unless specifically obsolete.
3. **Clean Typography**:
   - Use direct Unicode symbols (`→`, `←`, `×`, `≈`, `±`, `≤`, `≥`, `✓`, `✨`) instead of inline LaTeX math notation.

---

### Phase 4: Ruthless 3-Tier Verification (The Green Gate)

A BoostX task is **only complete when terminal execution logs provide concrete proof**:

1. **Tier 1: Before State (Repro Proof)**:
   - Provide or confirm the initial failure log from the Phase 1 signal.
2. **Tier 2: After State (Pass & Boundary Proof)**:
   - Run the exact feedback signal on the updated code and demonstrate a clean **GREEN** pass.
   - Test at least one boundary edge case (e.g. empty input, max limit, invalid parameter).
3. **Tier 3: Regression & Anti-Hardcode Sweep**:
   - Run existing test suites, compiler/linter checks, or sibling file verifications to guarantee zero regressions.
   - **Portability & Anti-Hardcode Audit**: Sweep all modified or created files for hardcoded machine user paths (`C:\Users\...`, `/Users/...`, `/home/...`) or secrets:
     - PowerShell (Windows):
       ```powershell
       git diff --name-only | ForEach-Object { Select-String -Path $_ -Pattern '(?i)([a-z]:[/\\]users|/Users/|/home/)' }
       ```
     - Bash/Zsh (macOS/Linux):
       ```bash
       git diff --name-only | xargs grep -E -i "([a-z]:/users|/Users/|/home/)"
       ```

---

## 3. Dual-OS Cross-Platform Engineering Protocol (Windows & macOS)

Whenever engineering across multi-machine environments (e.g., Windows Desktop PC, ASUS Laptop, and macOS MacBook):

1. **Strict Relative Path Invariant**:
   - Never hardcode machine-specific absolute paths (such as `C:\Users\...` or `/Users/...`) in configuration files, scripts, or documentation.
   - Always derive paths relative to script location:
     ```python
     SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
     ```
   - For global configuration entries (e.g. `skills.json`), use home-relative `~/` paths which resolve on both Windows (`%USERPROFILE%`) and macOS (`$HOME`).
2. **POSIX Path Separators**:
   - Always use forward slashes `/` or `pathlib.Path` / `os.path.join` across Python, JavaScript, and configuration files. Forward slashes resolve seamlessly across both Windows and macOS.
3. **Shell Dialect Awareness**:
   - Clearly distinguish between PowerShell on Windows (`dir`, `Get-ChildItem`, `Select-String`, `$env:VAR`) and zsh/bash on macOS/Linux (`ls`, `grep`, `export VAR`).
   - When providing reproduction or verification commands, offer the native command for the active host OS or write cross-platform Python scripts (`python -c "..."`).
4. **Encoding & Line Endings Standard**:
   - Always enforce UTF-8 output streams in Python tools:
     ```python
     if sys.stdout and hasattr(sys.stdout, "reconfigure"):
         sys.stdout.reconfigure(encoding="utf-8")
     ```
   - Ensure git attributes enforce LF normalization to prevent CRLF sync churn across Google Drive or Git.
5. **Atomic File Writes for Cloud Sync**:
   - When writing to cloud-synced folders (Google Drive, OneDrive), write to a temporary file and atomically replace to avoid creating sync-conflict duplicates like `filename (1).ext` or leaving `.lck` files.
6. **Zero-Directory-Nesting Invariant**:
   - When copying or moving directory trees, prevent self-named recursive subdirectories (e.g. `dir/dir`). Always verify destination targets before running recursive copy operations.
7. **Ephemeral Scratch Hygiene**:
   - All temporary repro scripts or scratch test files must live in designated scratch folders or be removed prior to task completion. Working tree must remain clean of untracked test debris (`git status --short`).

---

## 4. Anti-Hanging & Session Timeout Safety

To avoid hitting IDE gRPC session timeouts (which cause sudden "user canceled" errors):

* **No Long Blocking Commands**: Do not write scripts or run commands that block the terminal for > 30 seconds synchronously.
* **Background Task Protocol**: For long builds, heavy test suites, or simulations, launch the process with a small `WaitMsBeforeAsync` (e.g. `500ms`), immediately end your turn, and allow the system's reactive wakeup to deliver results when finished.
* **No Polling**: Never write loops that poll `manage_task(Action='status')`.

---

## 5. BoostX Verification Checklist

Before declaring any BoostX task finished, verify that all seven checkpoints are satisfied:

- [ ] **Red Signal Established**: Proved the failure state prior to editing.
- [ ] **Ponytail Ladder Applied**: Solution is minimal, standard-library-first, and avoids speculative bloat.
- [ ] **Dual-OS Invariants Checked**: Paths are relative/POSIX, encoding is UTF-8, commands match host shell.
- [ ] **Green Signal Verified**: Executed the verification command and verified clean passing output.
- [ ] **Zero Regressions**: Confirmed sibling modules and workspace integrity remain intact.
- [ ] **Portability & Anti-Hardcode Audited**: Zero machine-specific absolute paths (`C:\Users\...`, `/Users/...`) or personal secrets in diff.
- [ ] **Scratch Debris Cleaned**: Temporary test scripts removed; working tree clean.
