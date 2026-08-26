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

    brief_tab, requirements_tab, data_tab, work_tab, validation_tab, git_tab, submission_tab = st.tabs(
        ["1 · Brief", "2 · Requirements", "3 · Data & DB", "4 · Build & results", "5 · Test & validate", "6 · Git & evidence", "7 · Submit"]
    )
    with brief_tab:
        st.subheader("Apex decision problem")
        st.write(build)
        st.subheader("Professional boundary")
        st.warning(guardrail)
        st.caption("The official D2L brief and rubric remain authoritative for assessed details and dates.")

    with requirements_tab:
        st.subheader("Definition of done")
        st.write(evidence)
        st.markdown("""
- **Part A:** frame the decision, state assumptions, build the first working checkpoint, test it, commit it, and preserve the evidence.
- **Part B:** extend the preserved checkpoint into a production-quality feature and document every change made after Part A.
- **Professional standard:** the page must explain its result, handle missing or invalid input safely, and avoid unsupported claims.
""")
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
        st.subheader("Student build workspace")
        st.caption("Edit this lab's `render_student_extension()` function. Show the feature, its results, and the decision it supports here.")
        frame = st.session_state.get(state_key, pd.DataFrame())
        render_student_work(frame.copy())

    with validation_tab:
        st.subheader("Validation gate")
        st.markdown("""
- Run the normal case and confirm the result answers the stated decision question.
- Test empty, missing, malformed, and out-of-range input where relevant.
- Verify database writes target only your assigned workspace schema.
- Record assumptions, limitations, uncertainty, and responsible-use concerns.
- Confirm the page starts from a clean environment without manual repair steps.
""")
        st.warning(guardrail)

    with git_tab:
        st.subheader("Git and evidence gate")
        st.markdown(f"""
1. Run `python tools/prepare_lab.py --lab {number}` once.
2. Complete the evidence files under `evidence/lab_{number:02d}/`.
3. Put reproducible workspace changes in `workspace_sql/lab_{number:02d}.sql`; never submit a database dump.
4. Commit and push the Part A checkpoint before starting Part B.
5. Preserve Part A, then record every Part B design change and final validation result.
""")

    with submission_tab:
        st.subheader("D2L submission gate")
        st.markdown(
            f"""
1. Confirm the app, code, database query, evidence, and Git status all pass.
2. Build Part A with `python tools/build_submission.py --lab {number} --part A`.
3. Build Part B with `python tools/build_submission.py --lab {number} --part B`.
4. Inspect the generated ZIP and submit that ZIP to the matching D2L assignment.
5. Keep the private repository as your development history; D2L remains the official grading record.
"""
        )
        st.caption("The submission builder rejects secrets, uncommitted work, and unfinished evidence templates.")
