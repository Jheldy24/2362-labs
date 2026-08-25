import streamlit as st
from aida2362_app.catalogue import LABS
from aida2362_app.db import load_live_catalogue
from aida2362_app.ui import render_connection_help

st.title("AIDA 2362 lab catalogue")
st.write("These course-local contracts are authoritative and remain available offline.")
for n, lab in LABS.items():
    st.markdown(f"**Lab {n:02d}: {lab['title']}**  \n{lab['build']}")

st.subheader("Optional live package details")
st.write("If configured, enrich the catalogue with reviewed, read-only Apex metadata for this course.")
if st.button("Load live catalogue details"):
    try:
        live_catalogue = load_live_catalogue()
    except Exception:
        render_connection_help()
    else:
        st.dataframe(live_catalogue, hide_index=True, use_container_width=True)
        st.caption("Live metadata is course-filtered, limited to ten rows, and cached for five minutes.")
