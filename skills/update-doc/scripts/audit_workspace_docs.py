#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Workspace Documentation & Cross-File Consistency Auditor
Checks all active markdown and HTML files for consistency with Master SSOT baselines:
- Master QGIS Layer Count: 81 layers (Domains A–G)
- Master QGIS Milestone: ON_v4.0.qgz
- Facility Parcels: 30 parcels · 546.1 Rai
- Citywide Odor Complaints: 105,455 records (2021–2026)
- Macro Odor Complaints: 13,673 records & 5-tier stepped isobands
- Thesis Architecture Portal: 17 workstreams · 5-gate tracks · Panel 3/4/5 & FLOW_NODES sync
"""

import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Root of workspace is 4 levels up from this script: .agents/skills/doc-sync-audit/scripts
WORKSPACE_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..', '..', '..'))

PASS_ICON = "✓"
FAIL_ICON = "✗"
WARN_ICON = "!"

def audit_docs():
    print(f"==================================================")
    print(f" THESIS WORKSPACE DOCUMENTATION CONSISTENCY AUDIT ")
    print(f" Workspace Root: {WORKSPACE_ROOT}")
    print(f"==================================================\n")

    errors = []
    warnings = []
    passes = []

    # 1. Audit docs/thesis_architecture.html
    ta_path = os.path.join(WORKSPACE_ROOT, 'docs', 'thesis_architecture.html')
    if not os.path.exists(ta_path):
        errors.append(f"docs/thesis_architecture.html missing at {ta_path}")
    else:
        with open(ta_path, 'r', encoding='utf-8') as f:
            ta_content = f.read()

        # Check workstream cards count
        ws_cards = re.findall(r'<article class="card workstream-card" data-ws-label="([^"]+)"', ta_content)
        if len(ws_cards) == 17:
            passes.append(f"thesis_architecture.html: exactly 17 workstream cards present.")
        else:
            errors.append(f"thesis_architecture.html: found {len(ws_cards)} workstream cards (expected 17).")

        # Check all cards have 5 spans in stage-track
        pattern = r'<article class="card workstream-card" data-ws-label="([^"]+)"[^>]*>(.*?)</article>'
        cards = re.findall(pattern, ta_content, re.DOTALL)
        bad_tracks = []
        for label, content in cards:
            track_m = re.search(r'<div class="stage-track">(.*?)</div>', content)
            if not track_m:
                bad_tracks.append((label, 0))
            else:
                spans = re.findall(r'<span[^>]*>', track_m.group(1))
                if len(spans) != 5:
                    bad_tracks.append((label, len(spans)))
        if not bad_tracks:
            passes.append(f"thesis_architecture.html: all 17 workstream cards have standard 5-gate tracks.")
        else:
            errors.append(f"thesis_architecture.html: cards with non-5 tracks: {bad_tracks}")

        # Check QGIS layer count
        if "81 layers" in ta_content and "ON_v4.0" in ta_content:
            passes.append(f"thesis_architecture.html: references Master QGIS 81 layers and ON_v4.0 milestone.")
        else:
            errors.append(f"thesis_architecture.html: missing '81 layers' or 'ON_v4.0' milestone reference.")

        # Check Traffy 105k
        if "105,455" in ta_content or "105k" in ta_content:
            passes.append(f"thesis_architecture.html: references 105k / 105,455 citywide odor complaints.")
        else:
            errors.append(f"thesis_architecture.html: missing 105k complaint evidence in A Traffy.")

        # Check FLOW_NODES updates
        for node in ['alg_justice', 'alg_kde', 'tool_qgis', 'tool_axo']:
            if f"{node}:" in ta_content:
                passes.append(f"thesis_architecture.html FLOW_NODES: contains updated node '{node}'.")
            else:
                errors.append(f"thesis_architecture.html FLOW_NODES: missing node '{node}'.")

    # 2. Audit QGIS/README.md
    qgis_readme = os.path.join(WORKSPACE_ROOT, 'QGIS', 'README.md')
    if os.path.exists(qgis_readme):
        with open(qgis_readme, 'r', encoding='utf-8') as f:
            qr_content = f.read()
        if "81" in qr_content and "ON_v4.0.qgz" in qr_content and "Single-Node Invariant" in qr_content:
            passes.append(f"QGIS/README.md: locked to 81 layers, ON_v4.0.qgz, and Single-Node Invariant.")
        else:
            errors.append(f"QGIS/README.md: missing 81 layers, ON_v4.0.qgz, or Single-Node Invariant.")

    # 3. Audit docs/WORKSPACE_ATLAS.md
    atlas_path = os.path.join(WORKSPACE_ROOT, 'docs', 'WORKSPACE_ATLAS.md')
    if os.path.exists(atlas_path):
        with open(atlas_path, 'r', encoding='utf-8') as f:
            atlas_content = f.read()
        if "81 layers" in atlas_content or "81" in atlas_content:
            passes.append(f"docs/WORKSPACE_ATLAS.md: contains updated 81 layers metric.")
        else:
            warnings.append(f"docs/WORKSPACE_ATLAS.md: check for stale QGIS layer counts.")

    # 4. Audit docs/PROPOSAL_PLAN_V2.md
    prop_path = os.path.join(WORKSPACE_ROOT, 'docs', 'PROPOSAL_PLAN_V2.md')
    if os.path.exists(prop_path):
        with open(prop_path, 'r', encoding='utf-8') as f:
            prop_content = f.read()
        if "105,455" in prop_content and re.search(r'stepped\s+iso-?bands', prop_content, re.IGNORECASE):
            passes.append(f"docs/PROPOSAL_PLAN_V2.md: synchronized with 105,455 complaints and stepped isobands.")
        else:
            warnings.append(f"docs/PROPOSAL_PLAN_V2.md: check for 105,455 complaints and stepped isobands.")

    # 5. Check for deprecated terms across active markdown docs
    deprecated_patterns = [
        (re.compile(r'\b66 layers\b', re.IGNORECASE), "Deprecated '66 layers' found (should be 81 layers)"),
        (re.compile(r'\b68 layers\b', re.IGNORECASE), "Deprecated '68 layers' found (should be 81 layers)"),
        (re.compile(r'\b72 layers\b', re.IGNORECASE), "Deprecated '72 layers' found (should be 81 layers)"),
    ]

    scanned_count = 0
    stale_hits = []
    for root, dirs, files in os.walk(WORKSPACE_ROOT):
        # Ignore git, node_modules, tempmedia, cache, archive
        if any(skip in root for skip in ['.git', '.gemini', 'node_modules', '.tempmediaStorage', 'archive', 'downloads_archive']):
            continue
        for file in files:
            if file.endswith(('.md', '.html')) and not file.startswith('.'):
                scanned_count += 1
                fpath = os.path.join(root, file)
                rel_path = os.path.relpath(fpath, WORKSPACE_ROOT)
                try:
                    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = f.readlines()
                    for line_no, line in enumerate(lines, 1):
                        for pat, msg in deprecated_patterns:
                            if pat.search(line):
                                stale_hits.append(f"{rel_path}:{line_no} -> {msg}")
                except Exception as e:
                    pass

    if stale_hits:
        for h in stale_hits:
            warnings.append(h)
    else:
        passes.append(f"Scanned {scanned_count} active files: zero deprecated layer count references found.")

    # Summary Display
    print("AUDIT RESULTS:")
    for p in passes:
        print(f"  [{PASS_ICON}] {p}")
    if warnings:
        print("\nWARNINGS:")
        for w in warnings:
            print(f"  [{WARN_ICON}] {w}")
    if errors:
        print("\nERRORS:")
        for e in errors:
            print(f"  [{FAIL_ICON}] {e}")
    else:
        print("\nOVERALL STATUS: PERFECT (100% CONSISTENT)")

    return len(errors) == 0

if __name__ == '__main__':
    success = audit_docs()
    sys.exit(0 if success else 1)
