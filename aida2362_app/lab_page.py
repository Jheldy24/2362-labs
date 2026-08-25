import streamlit as st
from aida2362_app.catalogue import LABS
from aida2362_app.config import workspace_schema


def render_lab_page(number):
    lab = LABS[number]
    st.title(f"Lab {number:02d}: {lab['title']}")
    st.write("This bounded extension contract is not an assessed solution. QGIS remains primary and the official lab brief/rubric remain authoritative.")
    st.subheader("Build one feature")
    st.write(lab["build"])
    st.subheader("Required evidence")
    st.write(lab["evidence"])
    st.write("Test normal, empty, invalid, CRS, and geometry-validity cases. Record scale, uncertainty, privacy/community impact, Part B changes, and permitted AI use.")
    st.subheader("Guardrails")
    st.warning(lab["guardrail"])
    schema = workspace_schema()
    st.caption(f"Write database outputs only to `{schema}`." if schema else "Use supplied local spatial data; no database, paid service, or special hardware is required.")
