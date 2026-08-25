# Local development — AIDA 2362

1. Clone your private course repository and open it in VS Code. Install QGIS separately using the official course directions; QGIS is primary.
2. Run `python -m venv .venv`, activate it, and run `python -m pip install -r requirements.txt` for the optional Python/browser companion.
3. Optionally copy the secrets example, enter assigned values, retain `verify-full`, and never commit it. Direct PostGIS is never mandatory.
4. Run `streamlit run streamlit_app.py`; confirm it launches offline. Use supplied GeoPackage, GeoJSON, or raster data with relative paths.
5. Extend the current lab page and reuse `aida2362_app` helpers. Test missing/invalid CRS, empty/invalid geometry, scale/units, and offline behavior. Document privacy, uncertainty, accessibility, community impact, and Indigenous data governance.
6. Review Git status before committing; exclude secrets, sensitive locations, uncontrolled exports, grades, and personal data.

The static catalogue is authoritative and works offline. Its optional live enrichment reads at most ten reviewed `AIDA 2362` rows from `shared_research.v_lab_data_package_catalog`; unavailable connections return generic help without exposing connection details.
