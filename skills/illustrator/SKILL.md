---
name: illustrator
description: >-
  Vector graphics authoring, artboard layout management, typographic hierarchy, color swatches, layer manipulation, and automated diagram/plate production via Adobe Illustrator MCP server.
  Use when the user asks to inspect, manipulate, create, style, or export Adobe Illustrator documents (.ai/.eps/.pdf/.svg), or mentions /illustrator, "illustrator", or ".ai master file".
  Do NOT use for general Artificial Intelligence discussions, 3D Rhino CAD modeling, or Figma-only UI designs.
---

# Adobe Illustrator Master Plate & Vector Design Workflow (/illustrator)

This skill enables direct AI agent interaction with active **Adobe Illustrator** desktop sessions via the **Adobe Illustrator MCP Server** (`illustrator-mcp-server` / COM automation & ExtendScript). It automates architectural presentation board layout, Swiss graphic design systems, multi-artboard management, precision vector diagramming, typographic hierarchy, and CAD/GIS vector post-processing for urban and landscape master planning.

---

## 1. Availability & Readiness Check

Before executing any Adobe Illustrator operation, perform the following verification steps:

1. **Verify MCP Server Configuration** (Dual-OS Support: macOS & Windows):
   - In `~/.gemini/config/mcp_config.json` (macOS/Linux) or `%USERPROFILE%/.gemini/config/mcp_config.json` (Windows):
     ```json
     "illustrator": {
       "command": "npx",
       "args": ["-y", "illustrator-mcp-server"]
     }
     ```
   - Grok CLI (both macOS & Windows):
     `grok mcp add illustrator -- npx -y illustrator-mcp-server`
2. **Verify Adobe Illustrator Desktop Session**:
   - Ensure Adobe Illustrator (CC 2024 / 2025 or Beta) is open on your desktop with the target document (e.g. `ON Illustrator 01.ai`).
   - **macOS Note**: On first launch on macOS, macOS will request **Automation** permissions under *System Settings → Privacy & Security → Automation* to allow the Node process to communicate with Adobe Illustrator.
   - If Illustrator is not open or the document is missing, prompt the user:
     > *"Please open Adobe Illustrator and load your project file (e.g. `ON Illustrator 01.ai`)."*
3. **Verify Document Color Mode & Raster Settings**:
   - **Color Mode**: 
     - **CMYK**: For physical A1 plotter prints, thesis juries, and printed booklets (**`File → Document Color Mode → CMYK Color`**).
     - **RGB**: For digital 16:9 slide decks, 4K screen reviews, and web exports (**`File → Document Color Mode → RGB Color`**).
   - **Document Raster Effects Settings (DRES)**:
     - Set to **`High (300 ppi)`** with **`Anti-alias: ON`** (**`Effect → Document Raster Effects Settings...`**) to guarantee crisp drop shadows and raster texture rendering.

---

## 2. Core Workflow Modes

### Mode A: Multi-Artboard Layout & Presentation Grid Systems
Use this mode to structure, arrange, and manage presentation artboards:
1. **Artboard Standards**:
   * **A1 Presentation Plates**: `841mm × 594mm` (Landscape) or `594mm × 841mm` (Portrait) at 300 DPI.
   * **A3 Technical Report / Booklet**: `420mm × 297mm`.
   * **16:9 Digital Widescreen Slides**: `1920pt × 1080pt` or `3840pt × 2160pt` (4K UHD).
2. **Artboard Operations**:
   * Inspect existing artboards, names, and coordinates (`get_artboards`, `get_document_info`).
   * Create, duplicate, reorder, or resize artboards (`manage_artboards`).
   * Align multi-artboard matrix layouts with standardized spacing (e.g. `40pt`–`60pt` gutters between slides).

---

### Mode B: Semantic Layer Architecture & Standards
Use this mode to maintain clean, professional layer hierarchies following the Swiss-Architectural protocol:

```text
📁 00_FRAME_TITLE        (#0f172a Ink Black) — Border frames, Swiss title blocks, project info, page tags
📁 01_DIAGRAMS_VECTOR    (#1d4ed8 Royal Blue) — Analytical diagrams, flow arrows, isochrones, network graphs
📁 02_TYPOGRAPHY_LABELS  (#0f172a Slate Dark) — Space Grotesk titles, Plus Jakarta Sans body, JetBrains Mono tags
📁 03_DESIGN_INTERVENTION(#059669 Deep Pine) — Master plan proposals, 161-Rai park parcels, berms, terraces
📁 04_BASE_MAP_GIS       (#64748b Slate Gray) — Ingested QGIS vectors (roads, canals, campus fence, contours)
📁 05_RASTERS_ORTHOS     (#475569 Muted Dark) — Satellite basemaps, 3D Rhino perspective renders, heatmaps
```

* **Layer Operations**:
  * Create, rename, lock, hide, reorder, and group layers via `manage_layers` and `move_to_layer`.
  * Ensure base GIS linework and aerial imagery remain locked on bottom layers while active annotations stay on top layers.

---

### Mode C: Swiss Graphic Design System & Token Styling
Align all vector graphics with the project's **Swiss-Architectural Design Language** ([`Graphic/slide_style_showcase_v2.html`](../../../Graphic/slide_style_showcase_v2.html) & [`docs/UI_THEME_PROTOCOL.md`](../../../docs/UI_THEME_PROTOCOL.md) Part II):

1. **Color Palette Tokens**:
   * **Swiss Royal Blue**: `#1d4ed8` (Primary brand, macro infrastructure, focal emphasis)
   * **Swiss Signal Amber**: `#d97706` (Existing On Nut waste facilities, conflict zones, warning metrics)
   * **Deep Pine**: `#059669` (161-Rai urban park conversion, ecology, phytoremediation)
   * **Canal Blue**: `#0284c7` (Khlong Prawet water network, retention wetlands, hydrology)
   * **Ink Black**: `#0f172a` (Primary typography, high-contrast structural borders)
   * **Canvas Pure White**: `#ffffff` (Card backgrounds, clean presentation plates)
   * **Muted Slate**: `#64748b` (Secondary labels, hairlines, contextual contours)

2. **Stroke Weights & Line Hierarchy**:
   * **Hairline / Context**: `0.25 pt` (GIS contours, secondary gridlines)
   * **Secondary / Roads**: `0.50 pt` (District roads, parcel dividers)
   * **Primary / Outlines**: `1.00 pt` (Card frames, diagram borders, master fences)
   * **Accent / Boundary**: `2.00 pt – 3.00 pt` (Campus perimeter, highlighted flow routes)
   * **Future Phasing**: `1.50 pt Dashed` (`strokeDashArray: [4, 4]`) for proposed 161-Rai concessions.

3. **3D Hard Drop Shadow Standard**:
   * Strict architectural 3D offset: **`4px offset, 315° angle (Bottom-Right), 0px blur`** with `#0f172a` (100% opacity or 20% tint).
   * Avoid generic soft blurry shadows.

---

### Mode D: Programmatic Vector Authoring & Geometry
Use this mode to construct and edit vector elements:
* **Primitives**: Generate rectangles, rounded cards (`cornerRadius: 8pt - 12pt`), circles, and polygons (`create_rectangle`, `create_ellipse`).
* **Path Authoring**: Construct complex bezier paths, flow arrows, and isochrones (`create_path`, `modify_object`).
* **Transformations**: Align, distribute, scale, rotate, and group vector components (`align_objects`, `group_objects`, `ungroup_objects`).

---

### Mode E: Typographic Hierarchy & Text Styling
Use this mode to maintain clean Swiss typography:
* **Font Family Stack**:
  * **Headers / Titles**: `Space Grotesk` (Bold / Semi-Bold, All-Caps or Title Case)
  * **Body Copy / Descriptions**: `Plus Jakarta Sans` / `Inter` (Regular / Medium, 1.4x line spacing)
  * **Metrics / Code / Scientific Pins**: `JetBrains Mono` (Bold / Monospace, uppercase badges)
  * **Thai Typography**: `Prompt` / `Sarabun` (Clean modern sans-serif Thai)
* **Text Frame Operations**:
  * Create point text or bounded paragraph text boxes (`create_text_frame`, `apply_text_style`).
  * Check typographic consistency, missing fonts, or text overflows (`check_text_consistency`, `list_fonts`).

---

### Mode F: QGIS & Rhino Vector Ingestion Bridge
Use this mode to assemble and polish vectors exported from computational and GIS engines:
1. **Ingesting QGIS Vectors (`.pdf` / `.svg` / `.dxf`)**:
   * Ingest exported vector layers from `QGIS/print/` or `QGIS/layers/`.
   * Remap raw GIS stroke widths into calibrated Swiss weights (0.25pt / 0.5pt / 1.0pt).
   * Assign semantic swatches matching the On Nut 14 official parcels.
2. **Ingesting Rhino 3D Vectors (`Make2D` / `.ai` / `.pdf`)**:
   * Ingest exploded axonometric linework from `Rhino/ON 01.3dm`.
   * Separate silhouette edges (1.5pt), profile creases (0.75pt), and internal surface hatches (0.25pt).

---

### Mode G: Batch Export & Deliverable Production
Use this mode to output presentation-ready assets:
* **Export Formats**:
  * **High-Res Slide Images**: 300 DPI `.png` or `.jpg` via `export` for digital presentation decks.
  * **Print-Ready PDF**: Multi-artboard `.pdf` via `export_pdf` for thesis jury submissions.
  * **Web SVG Assets**: Clean `.svg` for live web dashboards and HTML documentation.

---

## 3. Visual & Geometric Verification

After performing Illustrator operations:
1. **Inspect Object Bounds**: Verify coordinate positions and artboard alignment via `get_document_structure` or `get_selection`.
2. **Check Contrast & Legibility**: Verify WCAG AAA text contrast against white/tinted backgrounds using `check_contrast`.
3. **Preflight Check**: Run `preflight_check` to verify no missing font glyphs, broken image links, or RGB/CMYK color mismatches.
4. **Save Document**: Call `save_document` to commit changes to the `.ai` master file.

---

## 4. Safety & Best Practice Rules

1. **Illustrator Running**: Keep Adobe Illustrator open during all MCP operations.
2. **Strict Z-Index Order Preservation During Grouping**: 
   * When calling `group_objects` or restructuring containers, the UUID array **must strictly follow ascending z-order** (`[bottommost background paths/cards, intermediate graphics, topmost text/annotations]`).
   * **NEVER** pass unsorted or arbitrary UUID lists to `group_objects`, which inverts stacking order and causes solid background shapes to cover text frames and icons.
3. **Zero-Item Pre-Delete Verification Rule**:
   * **NEVER** call `manage_layers({ action: "delete" })` on any layer until `get_layers` explicitly confirms `item_count: 0`.
   * If items remain on a layer targeted for deletion, move them via `move_to_layer` first and run `get_layers` to verify the layer is completely empty before deleting.
4. **Pre/Post Item Count Audit Invariant**:
   * Before and after any layer collapsing or bulk restructuring, query `find_objects` and `list_text_frames` to audit total object count and text frame count.
   * If `count_after < count_before`, immediately alert or execute `undo` to restore state.
5. **Slide Deck Master Layer & Group Architecture**:
   * For multi-artboard presentation decks (16:9 slides), maintain a unified master layer (e.g. `01_Presentation_Deck`) with named parent Groups per slide (`Slide 01`, `Slide 02`, etc.).
   * This eliminates Illustrator's "Paste Remembers Layers" bug where copying objects between artboards traps them under lower layers.
6. **Non-Destructive Sublayering**: Always place newly generated diagram annotations on dedicated sublayers rather than overwriting base GIS linework.
7. **PDF Compatibility**: Always ensure **`Create PDF Compatible File`** is enabled when saving `.ai` documents to maintain seamless interoperability with Rhino, InDesign, and QGIS.
8. **Scale & Units**: Always verify document units (`Points`, `Millimeters`, or `Inches`) before issuing dimension-based commands.

