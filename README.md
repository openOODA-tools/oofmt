# oofmt: Sovereign Paragraph Reformer & Text Reflow Engine

<div align="center">

```
================================================================================
                                 oofmt
            Sovereign openOODA Paragraph Reformer & Reflow Engine
================================================================================
```

**Sovereign Paragraph Reformer & Text Reflow Engine**  
*Optimal text paragraph reformer keeping uniform margins and clean gutters without ambient authority.*  
*Two Faces, One Engine:* Modern POSIX terminal ergonomics • Streaming JSON-RPC 2.0 MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()
[![Release: v0.2.0](https://img.shields.io/badge/Release-v0.2.0-blue.svg)](https://github.com/openOODA-tools/oofmt/releases/tag/v0.2.0)

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oofmt/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oofmt-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oofmt/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oofmt/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oofmt-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oofmt/uninstall.sh | bash -s -- --uninstall
```

---

## 2. CLI Usage

```
usage: oofmt [options] [-w WIDTH] [FILE...]

Optimal text paragraph reformer keeping uniform margins and clean gutters.

POSIX & Formatting Options:
  -w, --width WIDTH     maximum line width (default: 75 columns, or -N shorthand)
  -g, --goal GOAL       target line width goal (default: width - 5)
  -s, --split-only      split lines longer than width without joining shorter lines
  -u, --uniform-spacing uniform spacing (1 space between words, 2 after sentences)
  -c, --crown-margin    preserve first line indent and use second line for rest
  -p, --prefix PREFIX   reformat only lines starting with prefix and preserve prefix
  -j, --json            output structured reflow metrics and formatted text as JSON
  -D, --demo            interactive multi-mode paragraph reformer showcase
      --test            execute internal subsystem verification suite
      --mcp             run as Model Context Protocol JSON-RPC stdio server
  -v, --version         output version information and exit
  -h, --help            display this help and exit
```

### Examples
```bash
# Reflow file to 60 columns
oofmt -w 60 document.txt

# Reflow with numeric shorthand (-50)
cat notes.txt | oofmt -50

# Reflow email / comment quotes preserving leading "> " prefix
oofmt -p "> " -w 65 discussion.eml

# Split-only mode: break lines longer than width without joining shorter lines
oofmt -s -w 72 source_file.txt

# Uniform spacing (2 spaces after '.', '?', '!')
oofmt -u -w 80 manuscript.txt

# Structured JSON metrics and reflowed text
oofmt -j -w 60 input.txt
```

---

## 3. Model Context Protocol (MCP)

When invoked with `--mcp`, `oofmt` runs a JSON-RPC 2.0 stdio server providing streaming structured tools for AI coding agents:

```bash
oofmt --mcp
```

### Registered Tools
| Tool Name | Parameters | Description |
|---|---|---|
| `fmt_format_text` | `text` (string), `width` (int), `goal` (int), `split_only` (bool), `uniform` (bool), `prefix` (string) | Reflows text with width, goal, split_only, uniform, and prefix options |
| `fmt_reflow_paragraph` | `text` (string), `width` (int), `crown` (bool), `prefix` (string) | Reflows a paragraph string and returns structured JSON with reflow metrics |
| `fmt_inspect_margins` | `text` (string), `width` (int) | Analyzes line lengths, margin adherence, and detected overflows in text |
| `fmt_strip_prefixes` | `text` (string), `prefix` (string) | Strips comment or quote prefixes from lines of text |
| `fmt_demo` | *(none)* | Runs interactive sovereign text reflow and paragraph reformer showcase |

---

## 4. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`, `&McpCap`). Physical absence of ambient disk or network leakage.
* **Negative-Trust Architecture:** Hermetic string and paragraph algorithms, zero shell execution, bounded memory quotas.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 5. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
