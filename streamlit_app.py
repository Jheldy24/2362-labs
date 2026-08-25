import streamlit as st
from aida2362_app.ui import configure_page, render_context_banner

configure_page()
render_context_banner()
pages = {
    "Apex GIS companion": [
        st.Page("views/home.py", title="Home", icon=":material/home:", default=True, url_path="home"),
        st.Page("views/connection_check.py", title="Connection & workspace", icon=":material/database:", url_path="connection"),
        st.Page("views/data_explorer.py", title="Reviewed spatial explorer", icon=":material/map:", url_path="explorer"),
        st.Page("views/lab_catalogue.py", title="Lab catalogue", icon=":material/menu_book:", url_path="labs"),
        st.Page("views/final_project.py", title="Final project extension", icon=":material/flag:", url_path="final-project"),
    ],
    "AIDA 2362 labs": [st.Page(f"labs/lab_{n:02d}.py", title=f"Lab {n:02d}", url_path=f"lab-{n:02d}") for n in range(1, 11)],
}
st.navigation(pages, position="sidebar", expanded=10).run()
