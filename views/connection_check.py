import streamlit as st
from aida2362_app.db import check_connection_and_workspace
from aida2362_app.ui import render_connection_help, workspace_status

st.title("Connection & workspace check")
schema = workspace_status()
if not schema:
    st.success("The GIS companion is running locally without a live database. QGIS and supplied files remain available.")
elif st.button("Run fresh access check", type="primary"):
    try:
        row = check_connection_and_workspace(schema).iloc[0]
    except Exception:
        render_connection_help()
    else:
        for label, passed in {
            "Connected to apex_facilities": row["database_name"] == "apex_facilities",
            "Shared data is readable": bool(row["can_use_shared_data"]),
            "Assigned workspace is usable": bool(row["can_use_workspace"]),
            "Workspace allows creation": bool(row["can_create_in_workspace"]),
        }.items():
            st.success(f"Passed: {label}") if passed else st.error(f"Needs attention: {label}")
