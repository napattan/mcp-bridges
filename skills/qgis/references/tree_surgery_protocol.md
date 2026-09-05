# QGIS Advanced PyQGIS, Layer Tree Surgery & Crash Prevention Protocol

Detailed reference documentation for [`../SKILL.md`](../SKILL.md) regarding low-level PyQGIS quirks, C++ pointer safety, and layer tree manipulation in QGIS 3.28–3.40.

---

## 1. SIP Symbol Clone Crash Mechanics (QGIS 3.40, SIP/C++ Renderers)

Python-constructed `QgsSymbol` / `QgsSymbolLayer` / `Qgs*Renderer` objects hold transient pointers that SIP can prematurely garbage collect or corrupt. Any subsequent C++ `clone()` or serialization causes an instant segmentation fault (`SIGSEGV` at `sipQgsFillSymbol::clone`).

### Observed Kill Sites:
* `QgsVectorTileBasicRenderer.setStyles`
* `QgsCategorizedSymbolRenderer(field, list)`
* `QgsLayerTreeGroup.addLayer` / `insertLayer`
* `QgsProject.write`

### Safe Sequence:
1. MCP-add the layer (uses default C++ renderer).
2. Place it into its destination group using `create_layer_group` or the tree-move protocol below.
3. Style via `.qml` file on disk + `apply_style_qml`, or by editing `.qgz` XML directly on disk.
4. Call `save_project` ONLY after verifying that `len(proj.mapLayers())` is unchanged.

### Safe In-Place Mutation:
* Only mutate existing C++ symbols in-place after the layer is already placed in the tree:
  ```python
  layer.renderer().symbol().setColor(QColor(15, 23, 42))
  layer.triggerRepaint()
  ```
* **NEVER** build `QgsFillSymbol`, `QgsLineSymbol`, `QgsSingleSymbolRenderer`, or `QgsCategorizedSymbolRenderer` from scratch inside Python `execute_code`.

---

## 2. Layer-Tree Surgery & Project Wipe Prevention

In QGIS, removing a layer's **last** legend node in the tree automatically cascades and purges the layer from the project registry (`QgsLayerTreeRegistryBridge`). Calling `QgsLayerTreeGroup.clone()` followed by `removeChildNode(original)` can wipe an entire `.qgz` project to 0 layers.

### Safe Cross-Group Move Protocol:
```python
bridge = proj.layerTreeRegistryBridge()
bridge.setEnabled(False)
# 1. Add to destination group (layer now has 2 nodes)
dest_group.addLayer(layer)
# 2. Remove ONLY the old node from source group
source_group.removeChildNode(old_node)
# 3. Re-enable bridge
bridge.setEnabled(True)
```

### Critical Safeguards:
* Always verify layer count before saving:
  ```python
  assert len(proj.mapLayers()) > 0, "PROJECT CORRUPTED: Layer count dropped to 0!"
  ```
* Do not call MCP `load_project` (it may hang). Ask the user to reload via QGIS GUI or relaunch with `open -a QGIS-LTR` (macOS) / Windows shortcut.

---

## 3. Broken Datasource & Staging Directory Recovery Protocol

If layers under `Planning · Statutory Zoning & Land Use` report `isValid() == False` (`[!]` warning icon):

1. **Verify Physical File Existence**:
   * `01_site_analysis/01_macro_scale/05_db_e_buildings/04_osm_context/data/raw/bma_dpt/lup_polygon/lup_polygon_2013_zoning.geojson` (607 features)
   * `01_site_analysis/01_macro_scale/05_db_e_buildings/04_osm_context/data/raw/ldd_observed_landuse_2023/การใช้ที่ดิน/LU_BKK_2566.shp` (11,179 features)
   * `01_site_analysis/01_macro_scale/05_db_e_buildings/04_osm_context/qgis_bma_landuse/สมุทรปราการ2567/การใช้ที่ดิน/LU_SPK_2567.shp` (8,819 features)
2. **Re-stage and Reload**:
   * If paths were broken due to file movement, restore files to relative paths rather than changing layer IDs.
   * Call `lyr.dataProvider().reloadData()` or `lyr.setDataSource(...)`.
   * Verify with the Zero-Invalid Invariant:
     ```python
     assert len([l for l in QgsProject.instance().mapLayers().values() if not l.isValid()]) == 0
     ```
