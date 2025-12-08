# Maya Dependency Graph Editor

Production tool for batch node operations in Maya. Handles expression-based creation, regex pattern matching, and procedural workflows for riggers and pipeline TDs.

More info visit: [My Website](https://leiwu.co/maya-dependency-graph-editor/)

![Version](https://img.shields.io/badge/version-0.1.1-blue)
![Maya](https://img.shields.io/badge/Maya-2020%2B-green)
![Python](https://img.shields.io/badge/Python-3.7%2B-yellow)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

---

## Features

### Node Operations
- **Expression-based creation**: DSL parser for `name:type` syntax batch node generation
- **Template processor**: Generate numbered sequences (`ctrl_{id}_geo` → `ctrl_0_geo`, `ctrl_1_geo`...)
- **Regex deletion**: Pattern matching for bulk node cleanup with preview

### Connection Management
- **Attribute wiring**: Regex-based source → destination connections
- **Matrix workflow**: Modern `worldMatrix` → `offsetParentMatrix` connections (Maya 2020+)
- **Batch snap**: Pattern-based transform alignment via `matchTransform()`
- **Smart disconnect**: Automatic fallback for matrix connection removal

### Renaming Tools
- **Prefix/Suffix**: Add affixes to hierarchical selections
- **Search & Replace**: String literal and regex replacement with capture groups
- **UID tracking**: Path-safe operations during batch renames

### System
- **Atomic undo**: All batch operations collapse to single undo step
- **Persistent settings**: JSON-backed auto-save for patterns and preferences
- **Hot-reload**: Module reload system for rapid development iteration

---

## Architecture

```
src/
├── main.py                         # CLI entry: imports dg_editor.show()
│
└── dg_editor/                      # Core package namespace
    ├── __init__.py                 # Package entry: exposes ui__main_window as show()
    ├── config.py                   # VERSION, PATH, DEBUG flag
    ├── reloader.py                 # Hot-reload orchestrator (DEBUG mode)
    │
    ├── ui__main_window.py          # UI:    QTabWidget container, Maya parent wrapping
    │
    ├── ui_nodes.py                 # UI:    Node tab: WidgetCreate, WidgetDelete
    ├── nodes_create.py             # Logic: DSL lexer/parser (name:type syntax)
    ├── ui_nodes_create_dialog.py   # UI:    Template UI (spinbox, linedit → expression)
    ├── nodes_create_dialog.py      # Logic: Template processor (placeholder → names)
    ├── ui_nodes_delete_dialog.py   # UI:    Regex input dialog
    ├── nodes_delete_dialog.py      # Logic: Scene-wide regex matcher
    │
    ├── ui_connect.py               # UI:    Connection tab: from/to attribute matchers
    ├── ui_connect_dialog.py        # UI:    Regex dialog for attributes
    ├── connect_dialog.py           # Logic: Attribute-level regex filtering
    │
    ├── ui_rename.py                # UI:    Rename tab: prefix/search-replace widgets
    ├── rename.py                   # Logic: UID-based rename logic (hierarchy-aware)
    │
    ├── ui_settings.py              # UI:    Settings tab: undo toggle, font size spinbox
    ├── settings.py                 # Logic: JSON persistence: bind_lineedit, bind_spinbox
    │
    ├── widgets/                    # Reusable UI component library
    │   ├── __init__.py             # Exposes BaseWidget, BaseDialog
    │   └── base.py                 # Abstract base classes with layout builders
    │
    └── utils.py                    # undo_block decorator
build.py                            # Build script: copies src/ to build/dg_editor_x.x.x/
install.mel                         # MEL installer: drag-drop shelf button creation
```

**Pattern**: UI modules (ui_*.py) instantiate widgets and handle Qt signals; Logic modules (*.py without ui_ prefix) contain backend Maya cmds operations and algorithms of the corresponding UI.

---

## Installation

1. **Download** the latest release
2. **Extract** to any location
3. **Drag** `install.mel` into Maya viewport

The installer injects the tool path into `sys.path` and creates a persistent shelf button.

---

## Quick Start

### Create 20 FK Joints
```
Expression: spine_FK_{id}_jnt: joint
Count: 20
Outliner Result: spine_FK_0_jnt through spine_FK_19_jnt
```

### Connect IK Controls to FK Joints (Matrix)
```
From: spine_IK_(\d+)_ctrl
To: spine_FK_\1_jnt
Operation: Matrix Connect
Result: 20 worldMatrix connections
```

### Batch Rename for Unreal Engine
```
Search: collision_hull_(\d+)
Replace: UCX_character_hull_\1
Result: collision_hull_05 → UCX_character_hull_05
```

---

## Requirements

- **Maya**: 2020+
- **Python**: 3.7+
- **Dependencies**: PySide2

---

## Changelog

### v0.1.1 (2024-12-08)
- Added Matrix Connect operation for Maya 2020+
- Added Snap operation for batch transform alignment
- Extended disconnect with matrix fallback logic
- Added suffix rename functionality

### v0.1.0 (2024-11-15)
- Initial release
- Expression-based node creation
- Regex pattern matching for connections
- UID-based rename operations
- JSON settings persistence
