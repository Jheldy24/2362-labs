import pandas as pd
import streamlit as st

from aida2362_app.lab_workspace import render_lab_workspace


def render_student_extension(data: pd.DataFrame) -> None:
    """Build and explain your own Lab 02 work here."""
    # The selected frame may contain service_visits or another approved course view.
    # PART A TODO: implement and test the in-class checkpoint, then commit and push it.
    # PART B TODO: extend the preserved Part A work and document every later change.
    st.subheader("Your Lab 02 work")
    st.info(
        "Replace this guidance with your own tested analysis or application feature. "
        "Keep the page usable when data is empty or invalid."
    )
    if data.empty:
        st.write("Load a reviewed Apex view, or use the authorized fallback named in the lab brief.")
    else:
        st.write("Start from the loaded synthetic rows and show only evidence relevant to your decision question.")
        st.write(data.head(5))


render_lab_workspace(2, render_student_extension)