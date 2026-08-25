import streamlit as st

st.title("Final project extension area")
st.write(
    "Plan your own approved spatial project. QGIS/workflow remains primary; this app may host a local "
    "output, map, or dashboard extension but does not supply completed analysis or a required PostGIS solution."
)
st.markdown("""
**Formative gates:** proposal/scope; evidence plan/design; working prototype; validation; release
candidate and map/metadata peer review; release readiness.

**Evidence to create:** decision context; authorized data, provenance, metadata and licence;
CRS/validity/scale checks; reproducible QGIS/Python workflow; spatial analysis; accessible
map/dashboard; uncertainty and limitations; privacy, bias, community and Indigenous-data
considerations; strategy recommendation; AI declaration.
""")
st.warning("The official project instructions and program-scheduled final-exam time remain authoritative.")
