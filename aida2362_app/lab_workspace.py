from __future__ import annotations

from collections.abc import Callable

import pandas as pd
import streamlit as st

from aida2362_app.catalogue import LABS
from aida2362_app.config import workspace_schema
from aida2362_app.db import EXPLORER_VIEWS, explore_view

COURSE_NAME = "Geographic Information Systems"


def _contract(number: int) -> tuple[str, str, str, str]:
    lab = LABS[number]
    if isinstance(lab, tuple):
        title, purpose = lab
        return title, purpose, "Runnable code, tests, evidence, and documented decisions.", "Shared data is read-only; write only to your course workspace."
    return lab["title"], lab["build"], lab["evidence"], lab["guardrail"]


def render_lab_workspace(
    number: int,
    render_student_work: Callable[[pd.DataFrame], None],
) -> None:
    """Render the common lab frame and the student's editable implementation area."""
    title, build, evidence, guardrail = _contract(number)
    lab_code = f"LAB{number:02d}"
    state_key = f"{lab_code}-source-data"

    st.title(f"Lab {number:02d}: {title}")
    st.caption(f"{COURSE_NAME} · cumulative Apex application page · synthetic data only")
    left, middle, right = st.columns(3)
    left.metric("Part A", "Git checkpoint")
    middle.metric("Part B", "Production extension")
    right.metric("Official submission", "D2L ZIP")

    st.info(
        "Build this lab inside the current page, commit the Part A checkpoint, extend it for "
        "Part B, push your code to your private repository, and submit the validated evidence "
        "ZIP to D2L. The repository is your working record; D2L is the grading record."
    )

    overview, data_tab, work_tab, evidence_tab = st.tabs(
        ["Lab contract", "Apex data", "Your implementation", "Evidence & submission"]
    )
    with overview:
        st.subheader("What you will build")
        st.write(build)
        st.subheader("Evidence to preserve")
        st.write(evidence)
        st.warning(guardrail)
        schema = workspace_schema()
        if schema:
            st.success(f"Writable workspace: `{schema}`")
        else:
            st.warning("Run the student setup before database work. No credential is stored in Git.")

    with data_tab:
        st.subheader("Select a reviewed shared view")
        label = st.selectbox("Apex data source", list(EXPLORER_VIEWS), key=f"{lab_code}-view")
        if st.button("Load reviewed data", key=f"{lab_code}-load", type="primary"):
            try:
                st.session_state[state_key] = explore_view(label)
            except Exception:
                st.session_state.pop(state_key, None)
                st.error(
                    "The reviewed data could not be loaded. Confirm PostgreSQL is running and "
                    "that Connection & workspace passes. Do not paste credentials into the page."
                )
        frame = st.session_state.get(state_key, pd.DataFrame())
        if frame.empty:
            st.write("No live rows are loaded. The page remains safe to edit and test.")
        else:
            st.dataframe(frame, use_container_width=True, hide_index=True)
            st.caption(f"Loaded {len(frame):,} synthetic rows through an approved bounded query.")

    with work_tab:
        frame = st.session_state.get(state_key, pd.DataFrame())
        render_student_work(frame.copy())

    with evidence_tab:
        st.subheader("Required workflow")
        st.markdown(
            f"""
1. Run `python tools/prepare_lab.py --lab {number}` once.
2. Complete the evidence files under `evidence/lab_{number:02d}/`.
3. Put reproducible workspace changes in `workspace_sql/lab_{number:02d}.sql`; never submit a database dump.
4. Test the app, notebook/code, database query, empty input, and invalid input.
5. Commit and push the Part A checkpoint before starting Part B.
6. Build the clean D2L file with `python tools/build_submission.py --lab {number} --part A` or `--part B`.
"""
        )
        st.caption("The submission builder rejects secrets, uncommitted work, and unfinished evidence templates.")