# ⚡ Computational Agent Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platforms](https://img.shields.io/badge/Platforms-Claude_Code_•_Google_Antigravity_•_Cursor_•_Codex-8A2BE2)](#-universal-installation)
[![Dual-OS](https://img.shields.io/badge/Dual--OS-Windows_•_macOS_•_Linux-success)](#-dual-os-cross-platform-architecture)
[![Verification](https://img.shields.io/badge/Protocol-BoostX_Verified_✓-emerald)](#-the-boostx-engineering-discipline)

> **Production-grade agent skills & MCP automation bridges for computational design, spatial analytics, and high-discipline engineering.**  
> Built for AI coding assistants to operate deterministically across CAD, GIS, graphic production, and multi-file codebases.

---

## 🚀 Universal Installation

Install the entire suite into your favorite AI tool with a single command:

### 1. Claude Code (CLI)
```bash
git clone https://github.com/napattan/computational-agent-skills.git ~/.claude/skills
```

### 2. Google Antigravity / Gemini Code Assist
```bash
# Windows PowerShell
git clone https://github.com/napattan/computational-agent-skills.git "$env:USERPROFILE\.gemini\config\skills"

# macOS / Linux
git clone https://github.com/napattan/computational-agent-skills.git ~/.gemini/config/skills
```

### 3. Workspace-Local (Any AI IDE: Cursor, Windsurf, Codex, Antigravity)
```bash
git clone https://github.com/napattan/computational-agent-skills.git .agents/skills
```

---

## 📦 The Skill Catalog

The suite is divided into two synergistic layers: **Developer Infrastructure** and **AEC & Creative MCP Bridges**.

```
computational-agent-skills/
├── Developer Infrastructure
│   ├── /boostx          ← High-discipline root-cause engineering protocol
│   ├── /create-skill     ← Agent skill compiler & automated linter
│   └── /update-doc       ← Multi-file SSOT cross-synchronization engine
│
└── AEC & Creative MCP Bridges
    ├── /qgis             ← Geospatial intelligence & PyQGIS automation
    ├── /rhino            ← 3D NURBS modeling & RhinoCommon C#/Python
    ├── /grasshopper      ← Parametric canvas wiring & data tree surgery
    ├── /illustrator      ← Swiss vector plates & typographic layout
    └── /figma            ← Bidirectional HTML/CSS & Figma MCP sync
```

### 🛠️ Developer Infrastructure & Reasoning Protocols

| Skill | Command | Description |
| :--- | :---: | :--- |
| **BoostX Protocol** | `/boostx` | **High-discipline engineering lifecycle**. Solves tricky bugs and architectural problems through formal invariant mapping, a failing red signal gate, the Ponytail anti-bloat ladder, and ruthless 3-tier verification. |
| **Skill Creator** | `/create-skill` | **Skill compiler & quality linter**. Scaffolds new skills from documentation or distills completed chat sessions into reusable skills. Enforces context budgets, regex trigger validation, zero-hardcode sanitization, and dual-OS parity. |
| **Doc Synchronizer** | `/update-doc` | **Cross-document synchronization protocol**. Sweeps codebases to update all affected markdown documentation, HTML presentations, and indices after code or algorithm changes—eliminating drift. |

### 🏛️ AEC & Spatial Computing MCP Bridges

| Skill | Command | Description | Supported Stack |
| :--- | :---: | :--- | :--- |
| **QGIS Bridge** | `/qgis` | Direct interaction with active **QGIS Desktop** sessions. Automates spatial joins, raster algebra, metric UTM buffers (`EPSG:32647`), cartographic QML styling, and SIP pointer crash-safe layer tree surgery. | `qgis-mcp-server` • PyQGIS |
| **Rhino Bridge** | `/rhino` | Direct interaction with active **Rhinoceros 3D** sessions via McNeel's router. Automates CAD/NURBS modeling, layer hierarchies, programmatic RhinoCommon C#/Python execution, and viewport render capture. | `Rhino-MCP-Platform` • RhinoCommon |
| **Grasshopper Bridge** | `/grasshopper` | Active **Grasshopper (GH1)** parametric canvas automation. Places and wires components, performs data tree surgery (*Flatten-before-Graft*, path alignment), diagnoses red/orange solver errors, and automates geometry baking. | `g1_*` tools • Elefront |
| **Illustrator Bridge** | `/illustrator` | Desktop **Adobe Illustrator** vector plate production. Automates Swiss architectural layout systems, typographic hierarchy (`Space Grotesk` / `Plus Jakarta Sans`), z-index-safe grouping, and print/digital export. | `illustrator-mcp-server` • ExtendScript |
| **Figma Bridge** | `/figma` | Bidirectional design-to-code synchronization. Pushes live HTML pages into Figma via Option B and extracts Auto-Layout specs, typography tokens, and CSS properties back into source code. | `figma-developer-mcp` • Local HTTP |

---

## 🛡️ The BoostX Engineering Discipline

Every skill in this repository is built to eliminate the common failure modes of AI tools (context bloat, undertriggering, hardcoded environment paths, and broken links):

```
┌────────────────────────────────────────────────────────┐
│  1. THE RED INVARIANT GATE                             │
│     • Explicit failure modes defined before creation   │
│     • Positive trigger keywords + negative exclusions  │
│     • Context budget: YAML description ≤ 1024 chars    │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│  2. PONYTAIL ANTI-BLOAT LADDER                         │
│     • Prefer Markdown instructions over custom scripts │
│     • Reuse existing MCP servers & shell utilities     │
│     • Shortest working instructions win                │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│  3. DUAL-OS PORTABILITY INVARIANTS                     │
│     • Zero machine-specific absolute paths (`C:\...`)  │
│     • Universal POSIX forward slashes (`/`) in links   │
│     • UTF-8 stream reconfigured for Windows terminals  │
└──────────────────────────┬─────────────────────────────┘
                           │
┌──────────────────────────▼─────────────────────────────┐
│  4. RUTHLESS 3-TIER VERIFICATION                       │
│     • Tier 1: Static YAML frontmatter & regex linting  │
│     • Tier 2: Link target existence & secret audit     │
│     • Tier 3: Physical directory & slash menu proof    │
└────────────────────────────────────────────────────────┘
```

---

## 📂 Repository Structure

```
computational-agent-skills/
├── README.md
├── LICENSE                               ← MIT License
├── .gitignore
├── skills/
│   ├── boostx/SKILL.md
│   ├── create-skill/SKILL.md
│   ├── update-doc/
│   │   ├── SKILL.md
│   │   └── scripts/audit_workspace_docs.py
│   ├── qgis/
│   │   ├── SKILL.md
│   │   └── references/tree_surgery_protocol.md
│   ├── rhino/SKILL.md
│   ├── grasshopper/SKILL.md
│   ├── illustrator/SKILL.md
│   └── figma/SKILL.md
└── scripts/
    ├── install.sh                        ← Universal installer for macOS / Linux
    └── install.ps1                       ← Universal installer for Windows PowerShell
```

---

## 👤 Author

**Napat Phasundhiae**  
*Computational Design Technologist | Spatial Analytics • Urban & Environmental Simulation • Workflow Automation*

* **GitHub**: [@napattan](https://github.com/napattan)
* **LinkedIn**: [Napat Phasundhiae](https://www.linkedin.com/in/napat-phasundhiae)
* **Portfolio**: [Thesis & Professional Work](https://github.com/napattan)

---

## 📄 License

This repository is open-source under the [MIT License](LICENSE).
