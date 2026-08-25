import streamlit as st
from aida2362_app.db import EXPLORER_VIEWS, OFFLINE_METADATA, explore_view
from aida2362_app.ui import render_connection_help

st.title("Reviewed spatial explorer")
st.write(
    "Review layer grain, geometry, declared CRS/SRID, units, snapshot, provenance, and privacy before "
    "preview. QGIS remains the primary analysis environment; arbitrary SQL/layer names are not accepted."
)
st.dataframe(OFFLINE_METADATA, hide_index=True, use_container_width=True)
selection = st.selectbox("Optional shared view", list(EXPLORER_VIEWS))
if st.button("Load reviewed live attributes"):
    try:
        data = explore_view(selection)
    except Exception:
        render_connection_help()
    else:
        st.dataframe(data, hide_index=True, use_container_width=True)
        st.caption(f"Displayed {len(data):,} reviewed rows/features; maximum 250.")
st.caption("Orientation metadata is fictional and point-in-time. It is not a styled assessed map or a substitute for CRS/validity checks.")
