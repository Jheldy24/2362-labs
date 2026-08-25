import re
import streamlit as st

COURSE_CODE = "AIDA 2362"
READ_TTL = "5m"
WORKSPACE_PREFIX = "ws_aida2362_"
WORKSPACE_PATTERN = re.compile(r"^ws_aida2362_[a-z0-9]{8,24}$")


def workspace_schema():
    try:
        value = str(st.secrets["apex"]["workspace_schema"]).strip()
    except (FileNotFoundError, KeyError):
        return ""
    return value if WORKSPACE_PATTERN.fullmatch(value) else ""


def workspace_configuration_error():
    try:
        value = str(st.secrets["apex"]["workspace_schema"]).strip()
    except (FileNotFoundError, KeyError):
        return "No private workspace is configured. QGIS and supplied local spatial data remain available."
    if not WORKSPACE_PATTERN.fullmatch(value):
        return f"The workspace must begin with `{WORKSPACE_PREFIX}` followed by 8 to 24 lowercase letters or numbers."
    return None
