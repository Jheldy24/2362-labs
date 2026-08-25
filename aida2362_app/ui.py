import streamlit as st
from aida2362_app.config import COURSE_CODE, workspace_configuration_error, workspace_schema


def configure_page():
    st.set_page_config(page_title=f"{COURSE_CODE} | Apex", page_icon=":material/map:", layout="wide")


def render_context_banner():
    schema = workspace_schema()
    st.info(
        f"**Synthetic spatial learning data — {COURSE_CODE}**  \nQGIS is primary. Shared Apex data is read-only. Workspace: `{schema}`"
        if schema
        else f"**Synthetic spatial learning data — {COURSE_CODE}**  \nQGIS/local-file pathway is ready; no database workspace is configured."
    )


def render_connection_help():
    st.warning("The optional live Apex database is unavailable with the current settings.")
    st.write("Check private secrets, network, assigned hostname, and verify-full certificate settings.")
    st.info("Continue in QGIS or with supplied GeoPackage, GeoJSON, or raster files. Offline data cannot demonstrate live permissions, writes, transactions, or persistence.")


def workspace_status():
    error = workspace_configuration_error()
    if error:
        st.warning(error)
        return ""
    return workspace_schema()
