import streamlit as st

st.title("AIDA 2362 Apex GIS companion")
st.write("QGIS is the primary workspace. Use this local-browser companion to inspect metadata and outputs, then validate CRS and geometry, analyze at a defensible scale, and communicate responsibly.")
st.markdown("""
1. Start with supplied local data—no personal location capture.
2. Inspect metadata, CRS, units, scale, and privacy classification.
3. Work primarily in QGIS; use GeoPandas/Folium where appropriate.
4. Check the optional Apex connection or remain offline.
5. Open the current lab contract and preserve reproducible relative paths.
""")
st.warning("Consider uncertainty, location privacy, community impact, accessibility, and Indigenous data sovereignty before publishing any map.")
