# -*- mode: python ; coding: utf-8 -*-
#
# PyInstaller spec file for QR Code Generator
#
# Usage (run from project root with venv active):
#   pyinstaller qrcode_gen.spec
#
# The spec file is cross-platform; PyInstaller adapts the output for the
# OS on which it runs.  Build once per target platform.

import sys
from pathlib import Path

block_cipher = None

# Include config.ini next to the executable so users can edit defaults
added_files = [
    ("config.ini", "."),
]

a = Analysis(
    ["qrcode_gen.py"],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[
        "PIL._tkinter_finder",
        "qrcode.image.pil",
        "qrcode.image.styledpil",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="QRCodeGen",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,          # No console window on Windows / macOS
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # icon="assets/icon.ico",  # Uncomment and supply icon file if desired
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="QRCodeGen",
)

# macOS: also produce a .app bundle
if sys.platform == "darwin":
    app = BUNDLE(
        coll,
        name="QRCodeGen.app",
        # icon="assets/icon.icns",  # Uncomment and supply .icns if desired
        bundle_identifier="com.example.qrcodegen",
        info_plist={
            "NSHighResolutionCapable": True,
            "CFBundleShortVersionString": "1.0.0",
        },
    )
