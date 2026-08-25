# AIDA 2362 Apex GIS companion

This self-contained local Streamlit shell complements the course's primary QGIS workflow. It supports reviewed Apex attributes, GeoPandas/Folium-compatible extensions, ten bounded lab pages, and a formative project area without assessed solutions.

Create and activate a Python 3.10+ environment, install `requirements.txt`, then run one command:

```powershell
streamlit run streamlit_app.py
```

The app launches without database secrets. QGIS and supplied GeoPackage/GeoJSON/raster files are the no-cost offline path; PostGIS is optional. If assigned database access, retain `verify-full`, read only shared data, and write only to `ws_aida2362_...`. Never commit secrets or sensitive locations. No personal capture, special hardware, or paid service is required. See [LOCAL-DEVELOPMENT.md](LOCAL-DEVELOPMENT.md).

## Student development workflow

Build every lab as a cumulative page in this application, commit and push the code to your private repository, and submit the validated evidence ZIP to D2L. Start with [STUDENT-WORKFLOW.md](STUDENT-WORKFLOW.md).
