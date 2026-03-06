#!/usr/bin/env bash
# Build script for macOS
# Run from the project root directory.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

VENV_DIR=".venv"

echo "=== QR Code Generator — macOS build ==="

# 1. Create / reuse virtual environment
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

source "$VENV_DIR/bin/activate"

# 2. Install / upgrade dependencies
echo "Installing dependencies..."
pip install --upgrade pip -q
pip install -r requirements.txt -q

# 3. Build with PyInstaller (produces both a folder and a .app bundle)
echo "Running PyInstaller..."
pyinstaller qrcode_gen.spec --clean --noconfirm

echo ""
echo "Build complete."
echo "  App bundle : dist/QRCodeGen.app"
echo "  Raw binary : dist/QRCodeGen/QRCodeGen"
