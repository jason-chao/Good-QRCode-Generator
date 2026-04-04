# Good QR Code Generator — Web

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../LICENSE)

A single-page HTML QR code generator that runs entirely in your browser — no server, no account, no tracking.

Open `index.html` directly from your file system (no web server needed) or serve it from any static host.

## Features

- Encode any URL or text into a standard, scanner-compatible QR code
- Choose foreground and background colours (named colours or hex codes) with a live colour picker
- Transparent background support with checkerboard preview
- Error correction level (L / M / Q / H)
- Adjustable module size and quiet-zone border
- Copy to clipboard or save as PNG — all locally in the browser
- Works offline; nothing leaves your device

## Usage

**Locally (no server required)**

Just open `index.html` in any modern browser:

```bash
# macOS / Linux
open web/index.html

# Windows
start web/index.html
```

Chromium-based browsers (Chrome, Edge, Brave) and Firefox both support loading local files this way.

**Dependencies**

The library [`qrcode-generator`](https://github.com/kazuhikoarase/qrcode-generator) is bundled locally in `libs/`. If the local copy is missing, the app falls back to jsDelivr CDN automatically.

## Project structure

```
web/
├── index.html        # The entire application (self-contained)
└── libs/
    └── qrcode-generator.min.js   # Bundled QR library (local-first)
```
