#!/usr/bin/env bash
# Computational Agent Skills — Universal Installer (macOS & Linux)
# Symlinks skills to Claude Code (~/.claude/skills) and Google Antigravity (~/.gemini/config/skills)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_SRC="$SCRIPT_DIR/skills"

echo "============================================================"
echo "  ⚡ Computational Agent Skills — Universal Installer"
echo "============================================================"
echo "Source: $SKILLS_SRC"

install_to() {
    local target_dir="$1"
    local name="$2"
    
    mkdir -p "$target_dir"
    echo ""
    echo "Installing into $name ($target_dir)..."
    
    for skill in "$SKILLS_SRC"/*; do
        if [ -d "$skill" ]; then
            local skill_name
            skill_name="$(basename "$skill")"
            local dest="$target_dir/$skill_name"
            
            if [ -L "$dest" ] || [ -d "$dest" ]; then
                rm -rf "$dest"
            fi
            ln -s "$skill" "$dest"
            echo "  ✓ Linked /$skill_name"
        fi
    done
}

# 1. Claude Code (~/.claude/skills)
if [ -d "$HOME/.claude" ] || [ "$1" == "--claude" ] || [ "$1" == "--all" ]; then
    install_to "$HOME/.claude/skills" "Claude Code"
fi

# 2. Google Antigravity (~/.gemini/config/skills)
if [ -d "$HOME/.gemini" ] || [ "$1" == "--antigravity" ] || [ "$1" == "--all" ]; then
    install_to "$HOME/.gemini/config/skills" "Google Antigravity"
fi

# 3. Target workspace if provided
if [ -n "$2" ] && [ -d "$2" ]; then
    install_to "$2/.agents/skills" "Workspace ($2)"
fi

echo ""
echo "============================================================"
echo "  ✓ Installation Complete! All skills ready to trigger."
echo "============================================================"
