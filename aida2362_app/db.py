import pandas as pd
import streamlit as st
from aida2362_app.config import READ_TTL

EXPLORER_VIEWS = {
    "Facility profiles": "SELECT * FROM shared_facilities.v_facility_profile ORDER BY facility_id LIMIT 250",
    "Service routes": "SELECT * FROM shared_spatial.v_service_route_summary ORDER BY service_visit_id DESC LIMIT 250",
}
OFFLINE_METADATA = pd.DataFrame(
    [
        {"layer": "fictional_facilities", "geometry": "Point", "declared_crs": "EPSG:4326", "scale_note": "orientation only", "privacy": "synthetic"},
        {"layer": "fictional_service_routes", "geometry": "LineString", "declared_crs": "EPSG:4326", "scale_note": "orientation only", "privacy": "synthetic"},
    ]
)


def apex_connection():
    return st.connection("apex", type="sql")


def check_connection_and_workspace(schema):
    return apex_connection().query(
        """
        SELECT current_database() AS database_name,
               current_user AS database_user,
               %(workspace)s AS workspace_schema,
               has_schema_privilege(current_user, %(workspace)s, 'USAGE') AS can_use_workspace,
               has_schema_privilege(current_user, %(workspace)s, 'CREATE') AS can_create_in_workspace,
               has_schema_privilege(current_user, 'shared_facilities', 'USAGE') AS can_use_shared_data
        """,
        params={"workspace": schema},
        ttl=0,
    )


def explore_view(label):
    if label not in EXPLORER_VIEWS:
        raise ValueError("That view is not approved.")
    return apex_connection().query(EXPLORER_VIEWS[label], ttl=READ_TTL)


def load_live_catalogue():
    """Optionally load bounded, course-scoped package metadata."""
    return apex_connection().query(
        """
        SELECT lab_number, package_code, package_title, package_version,
               release_status, learning_purpose, dataset_count, dataset_codes,
               source_types, licence_names, contains_personal_information
        FROM shared_research.v_lab_data_package_catalog
        WHERE course_code = 'AIDA 2362'
        ORDER BY lab_number
        LIMIT 10
        """,
        ttl=READ_TTL,
        show_spinner="Loading optional live catalogue details...",
    )
