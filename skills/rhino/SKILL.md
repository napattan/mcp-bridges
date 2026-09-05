---
name: rhino
description: >-
  3D geometry modeling, layer & object management, computational RhinoCommon C#/Python automation, viewport rendering, and CAD/GIS translation via Rhino MCP server (Rhino-MCP-Platform).
  Use when the user asks to inspect, manipulate, model, query, or script Rhino 3D geometry, or mentions /rhino or "rhino".
  Do NOT use for Grasshopper canvas wiring, component graphs, or data tree surgery (use /grasshopper instead), or 2D Adobe Illustrator plate layouts.
---

# Rhino 3D Computational Design & Automation Workflow (/rhino)

This skill enables direct AI agent interaction with active **Rhinoceros 3D** sessions via the official McNeel **Rhino MCP Platform** router (`Rhino-MCP-Platform`). It automates 3D CAD/NURBS modeling, layer architecture, programmatic RhinoCommon C#/Python execution, viewport image feedback, and CAD/GIS data exchange for urban and landscape master planning.

---

## 1. Availability & Readiness Check

Before executing any Rhino operation, verify the live connection:

1. **Verify MCP Server Configuration** (Dual-OS Support: macOS & Windows):
   - **macOS**: Router executable is installed via Rhino 8 `_PackageManager` (`Rhino-MCP-Platform`):
     - Path (Apple Silicon): `~/Library/Application Support/McNeel/Rhinoceros/packages/8.0/Rhino-MCP-Platform/<version>/router/osx-arm64/rhino-mcp-router`
     - Path (Intel): `~/Library/Application Support/McNeel/Rhinoceros/packages/8.0/Rhino-MCP-Platform/<version>/router/osx-x64/rhino-mcp-router`
     - In `~/.gemini/config/mcp_config.json`:
       ```json
       "rhino": {
         "command": "/Users/<user>/Library/Application Support/McNeel/Rhinoceros/packages/8.0/Rhino-MCP-Platform/<version>/router/osx-arm64/rhino-mcp-router",
         "args": []
       }
       ```
   - **Windows**: In `%USERPROFILE%/.gemini/config/mcp_config.json`:
     ```json
     "rhino": {
       "command": "%APPDATA%/McNeel/Rhinoceros/packages/8.0/Rhino-MCP-Platform/0.1.5/router/win-x64/rhino-mcp-router.exe",
       "args": []
     }
     ```
   - Grok CLI:
     - macOS: `grok mcp add rhino -- ~/Library/Application\ Support/McNeel/Rhinoceros/packages/8.0/Rhino-MCP-Platform/<version>/router/osx-arm64/rhino-mcp-router`
     - Windows: `grok mcp add rhino -- "%APPDATA%/McNeel/Rhinoceros/packages/8.0/Rhino-MCP-Platform/0.1.5/router/win-x64/rhino-mcp-router.exe"`
   - Tool check: Call `list_slots`. Expected payload: running slots (e.g. `slotId`, `port` `10501`, `version` `"8"`).

2. **Verify Rhino Desktop & MCP Listener**:
   - Ensure Rhino 8 is open with the target document (e.g. `On Nut 01.3dm`).
   - If `Rhino-MCP-Platform` is not yet installed on this machine: In Rhino 8, run `_PackageManager`, search for `Rhino-MCP-Platform`, and click **Install** (restart Rhino).
   - If `list_slots` is empty or unreachable, prompt the user:
     > *"Please ensure Rhino 8 is open and type `MCPStart` in Rhino's command bar (listening on `localhost:10501`)."*

3. **Check Document Units & Tolerance**:
   - Metric Standard: All master planning and site analysis operations must operate in **Meters** (`UnitSystem.Meters`).
   - Tolerance: Absolute tolerance should be set to `0.01` or `0.001` meters.
   - When converting units from mm to meters, always verify whether geometry needs ×0.001 scaling (*"Change unit system and maintain object sizes"*) or unit-label redefinition only.

---

## 2. Core Workflow Modes

### Mode A: Document Discovery & Geometry Inspection
Use this mode to query objects, layer structures, bounding boxes, and geometric integrity:
1. **Query Objects**:
   - Use `list_objects` with filters (`geometryType`, `layer`, `includeHidden`, `includeLocked`, `limit`).
   - Read bounding box extents, centroids, object IDs, and geometry types.
2. **Inspect Layer & Document Structure**:
   - Query layer hierarchy, parent-child relationships, and per-layer object counts using `run_python` on `__rhino_doc__`.
   - Inspect active selections via `get_selection` and set focus via `set_selection`.
3. **Analyze Spatial Extents**:
   - Calculate total model extents (`BoundingBox.Union`) to verify coordinate placement and scale against real-world dimensions.

---

### Mode B: Native Rhino Command Execution
Use this mode to trigger standard Rhino commands and interactive operations:
1. **Execute Commands**:
   - Use `run_command` with hyphen-prefixed command syntax for scriptable execution (e.g. `_-SelAll`, `_-Purge`, `_-Offset`, `_-BooleanUnion`, `_-Contour`).
   - Ensure commands are non-interactive and properly terminate arguments with `_Enter`.
2. **Batch Processing**:
   - Combine selections and transformations using chained commands (e.g. `_-SelLayer "00_CONTEXT" _-Hide`).

---

### Mode C: Programmatic RhinoCommon C# & Python Engine
Use this mode for high-performance geometric computation, custom algorithms, and data transformation:
1. **Python 3 Scripting (`run_python`)**:
   - Use `__rhino_doc__` as the primary document handle. (Do not rely on `scriptcontext.doc` or `rhinoscriptsyntax` in MCP context).
   - Use `System.Drawing.Color` and standard RhinoCommon types (`Rhino.Geometry.*`, `Rhino.DocObjects.*`).
   - Wrap enum lookups safely in Python 3 (e.g. `System.Enum.Parse(EnumClass, "Name")`).
2. **High-Performance C# Scripting (`run_csharp`)**:
   - Use `run_csharp` with `Parallel.For` and primitive array structures (`double[]`, `Point3d[]`) for massive point cloud processing, isochrone distance matrices, and voxel calculations.

---

### Mode D: Semantic Layer Hierarchy & Architectural Standards
Use this mode to maintain clean, professional layer organization following the Swiss-Architectural color palette:

1. **Standard 4-Tier Master Plan Hierarchy**:
   * **`00_CONTEXT`** *(Slate Gray `#64748b`)*: Site boundary, surrounding external buildings, roads, canals, and CAD topography.
   * **`01_ON_NUT_FACILITIES`** *(Warm Amber `#d97706`)*: Existing facility buildings, proposed/new buildings, and demolition/relocation phases.
   * **`02_LANDSCAPE_DESIGN`** *(Emerald Green `#059669`)*: Hardscape outlines, paving patterns, planting envelopes, shrub hatches, waterfront edges, and earthworks.
   * **`03_ANNOTATION`** *(Sky Blue `#0284c7`)*: Section/elevation outlines, spot levels, callout tags, and legend symbols.
2. **Safe Layer Purge Protocol**:
   - In Rhino, block definitions (`doc.InstanceDefinitions`) may contain entities referencing empty CAD layers (e.g. `18CONT`, `25CONT`, `CW-pipe`).
   - **Remap before Purge**: Re-assign internal block entity `LayerIndex` to `Layer0` via `idef.ModifyGeometry(...)` before calling `doc.Layers.Delete(idx, True)`.

---

### Mode E: Viewport Renders, Camera & Visual Feedback
Use this mode to capture visual verification images directly from the Rhino viewport:
1. **Camera Positioning**:
   - Adjust perspective, top, front, or isometric views using `set_camera` or `zoom_to_layer` / `zoom_to_object`.
2. **Image Capture**:
   - Capture viewport renders using `get_viewport_image` (`viewport`, `displayMode` e.g. `'Rendered'`, `'Shaded'`, `'Arctic'`, `width`, `height`).
   - Review captured images to verify modeling progress, material mapping, and spatial proportions.

---

### Mode F: GIS & CAD Interoperability Bridge
Use this mode to align Rhino geometry with QGIS (`EPSG:32647` UTM Zone 47N):
1. **Coordinate Alignment**:
   - Preserve real-world UTM coordinates or document origin offsets when importing GeoJSON / DXF vectors from QGIS.
2. **Attribute Baking**:
   - Store simulation metadata, MCDA scores, and Traffy complaint density values into `Rhino.DocObjects.ObjectAttributes.UserDictionary`.

---

## 3. Visual & Geometric Verification

After performing modeling or layer changes:
1. **Validate Geometry Integrity**:
   - Ensure Breps are solid/closed (`brep.IsSolid`), meshes are manifold and normals unified, and curves are closed planar loops where required.
2. **Check Layer Tree State**:
   - Verify that all active geometry resides under one of the standard parent categories and no orphan geometry is left on unmanaged root layers.
3. **Save Document**:
   - Call `save_doc` or `run_command("_-Save _Enter")` once critical milestones are verified.

---

## 4. Safety & Best Practice Rules

1. **Modal Dialogs**: Avoid triggering commands that open modal GUI popups (like interactive file choosers) without command-line suppression (`_-`).
2. **Block Definitions**: Never force-delete layers without checking `doc.InstanceDefinitions` first.
3. **Document Handle**: Always use `__rhino_doc__` in Python scripts.
4. **Units Invariant**: Never mix millimeters and meters in the same workspace pipeline. Master plans are strictly **Meters** (`m`).
5. **Non-Destructive Edits**: Prefer creating new sub-layers for algorithmic outputs (e.g. `02_LANDSCAPE_DESIGN::Pave_Offset_5m`) rather than overwriting original base geometry.
