from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass

import streamlit as st


@dataclass(frozen=True)
class FinalProjectContract:
    course_name: str
    project_name: str
    project_boundary: str
    selection_process: str
    data_evidence: Sequence[str]
    design_evidence: Sequence[str]
    validation_evidence: Sequence[str]
    responsibility_evidence: Sequence[str]
    final_deliverables: Sequence[str]


def _bullets(items: Sequence[str]) -> None:
    st.markdown("\n".join(f"- {item}" for item in items))


def render_final_project_workspace(
    contract: FinalProjectContract,
    render_student_solution: Callable[[], None],
) -> None:
    """Render the common 25% final-project workflow and editable solution area."""
    st.title(contract.project_name)
    st.caption(f"{contract.course_name} · individual alternate final examination · Apex Facilities Platform")

    weight, gates, submission = st.columns(3)
    weight.metric("Final grade", "25%")
    gates.metric("Formative gates", "6")
    submission.metric("Final delivery", "ZIP + demo + defence")

    st.info(
        "This is a student-selected project inside an approved facilities-maintenance boundary. "
        "Use the same private repository, local Apex database, and cumulative Streamlit application. "
        "Git records the development history; D2L remains the official submission and grading record."
    )

    brief, plan, data, design, build, evaluate, responsibility, deliver = st.tabs(
        [
            "1 · Brief",
            "2 · Plan",
            "3 · Data",
            "4 · Design",
            "5 · Build",
            "6 · Evaluate",
            "7 · Responsibility",
            "8 · Deliver",
        ]
    )

    with brief:
        overview, boundaries, workflow = st.tabs(["Overview", "Approval boundaries", "How the project works"])
        with overview:
            st.subheader("Project purpose")
            st.write(contract.project_boundary)
            st.subheader("Project-selection process")
            st.write(contract.selection_process)
        with boundaries:
            st.markdown(
                """
- Work individually and be prepared to explain every design and implementation decision.
- Use fictional, synthetic, supplied, or explicitly authorized data only.
- Keep shared Apex schemas read-only; write outputs only to your assigned course workspace.
- Do not place credentials, private host details, grades, or controlled information in Git.
- The official D2L project brief, rubric, and program-scheduled examination time remain authoritative.
"""
            )
        with workflow:
            st.markdown(
                """
1. Propose and obtain approval for a bounded decision problem.
2. Preserve evidence at each formative gate without treating a gate as a separate grade.
3. Build the solution cumulatively in this repository and commit meaningful checkpoints.
4. Validate the complete project from a clean setup.
5. Submit one final evidence package to D2L and complete the demonstration and individual defence.
"""
            )

    with plan:
        problem, stakeholders, criteria, portfolio = st.tabs(
            ["Problem & decision", "Stakeholders", "Success criteria", "Use-case portfolio"]
        )
        with problem:
            st.subheader("Decision question")
            st.info("State one precise facilities-maintenance decision that your project will support. Define what is in and out of scope.")
        with stakeholders:
            st.subheader("People and consequences")
            st.info("Identify the decision owner, affected groups, intended users, competing needs, and how the result will be used.")
        with criteria:
            st.subheader("Measurable success")
            st.info("Define acceptance measures, baseline evidence, failure conditions, and the practical threshold for a useful result.")
        with portfolio:
            st.subheader("Select the strongest project")
            st.info("Document the required candidate use cases, score them transparently, and justify the connected use cases and final implementation you selected.")

    with data:
        sources, provenance, quality, workspace = st.tabs(
            ["Sources", "Provenance & dictionary", "Quality & preparation", "Database workspace"]
        )
        with sources:
            st.subheader("Authorized inputs")
            _bullets(contract.data_evidence)
        with provenance:
            st.subheader("Traceable evidence")
            st.info("Record source, owner, licence or permission, retrieval/version date, fields, units, joins, intended use, and known limitations.")
        with quality:
            st.subheader("Preparation and fitness")
            st.info("Profile the inputs, define cleaning rules, preserve raw-to-derived traceability, test quality, and explain how defects affect the decision.")
        with workspace:
            st.subheader("Reproducible database work")
            st.info("Store only reproducible SQL and code in Git. Write student-created tables and outputs to your assigned workspace; never submit a database dump.")

    with design:
        architecture, method, baseline, risk = st.tabs(
            ["Architecture", "Method", "Baseline", "Risks & assumptions"]
        )
        with architecture:
            st.subheader("Solution design")
            _bullets(contract.design_evidence)
        with method:
            st.subheader("Why this approach")
            st.info("Connect every method, transformation, model, analysis, map, or visualization to the decision question and the course outcomes.")
        with baseline:
            st.subheader("Comparison point")
            st.info("Define a simple, defensible baseline or current-state comparison before claiming that the final solution adds value.")
        with risk:
            st.subheader("Assumptions and failure modes")
            st.info("List dependencies, assumptions, likely failure modes, compute or performance limits, and the evidence needed before operational use.")

    with build:
        implementation, outputs, git_history = st.tabs(
            ["Implementation workspace", "Outputs", "Git checkpoints"]
        )
        with implementation:
            st.subheader("Student solution")
            st.caption("Edit `render_student_solution()` in `views/final_project.py`. Replace the starter guidance with your tested project interface and logic.")
            render_student_solution()
        with outputs:
            st.subheader("Decision-ready product")
            st.info("Expose only useful, interpretable outputs. Label measures and uncertainty, provide safe empty/error states, and make the recommended action clear.")
        with git_history:
            st.subheader("Meaningful development history")
            st.info("Commit the approved scope, evidence plan, prototype, validation, release candidate, and final release as separate meaningful checkpoints.")

    with evaluate:
        tests, results, limitations, acceptance = st.tabs(
            ["Tests", "Results", "Limitations", "Acceptance evidence"]
        )
        with tests:
            st.subheader("Verification and validation")
            _bullets(contract.validation_evidence)
        with results:
            st.subheader("Interpretation")
            st.info("Explain what the evidence supports, what it does not support, why it matters to the stakeholder, and how it compares with the baseline.")
        with limitations:
            st.subheader("Honest boundaries")
            st.info("Document data, method, generalization, uncertainty, performance, accessibility, and operational limitations without hiding negative results.")
        with acceptance:
            st.subheader("Release decision")
            st.info("Show which success criteria passed, which failed, what remains conditional, and whether to release, revise, monitor, or stop the solution.")

    with responsibility:
        privacy, fairness, access, ai_use, operations = st.tabs(
            ["Privacy & security", "Bias & impact", "Accessibility", "AI declaration", "Monitoring & rollback"]
        )
        with privacy:
            st.subheader("Safe information handling")
            _bullets(contract.responsibility_evidence)
        with fairness:
            st.subheader("Bias and affected groups")
            st.info("Identify uneven error or impact, excluded groups, harmful proxies, and the human review required before a consequential decision.")
        with access:
            st.subheader("Accessible communication")
            st.info("Use readable text, clear labels, keyboard-friendly controls, non-colour-only cues, and explanations suitable for the intended audience.")
        with ai_use:
            st.subheader("Permitted AI use")
            st.info("Declare the tool, purpose, material prompts or assistance, verification performed, changes made, and what you personally understand and can defend.")
        with operations:
            st.subheader("Human oversight")
            st.info("Define monitoring signals, review ownership, escalation, stop conditions, rollback steps, and the evidence required for future changes.")

    with deliver:
        milestones, reproduce, package, demo = st.tabs(
            ["Six gates", "Reproduce", "Final package", "Demo & defence"]
        )
        with milestones:
            st.subheader("Formative project gates")
            st.markdown(
                """
1. **Week 6:** approved proposal and scope.
2. **Week 8:** evidence plan and initial design.
3. **Week 10:** working prototype.
4. **Week 12:** validation evidence.
5. **Week 14:** release candidate, peer/operational review, and revision.
6. **Week 15:** release readiness and documentation.
"""
            )
        with reproduce:
            st.subheader("Clean-run proof")
            st.info("Provide exact setup and run instructions, pinned dependencies, ordered SQL/code steps, test commands, expected outputs, and a clean-environment verification record.")
        with package:
            st.subheader("Required final evidence")
            _bullets(contract.final_deliverables)
            st.warning("Inspect the final ZIP before uploading it. It must contain no credentials, database dump, private host information, cache, or unrelated files.")
        with demo:
            st.subheader("Individual demonstration and defence")
            st.info("Demonstrate the working solution, trace one result from source to decision, explain a failure or limitation, justify a major design choice, and answer questions without relying on another person or AI tool.")
            st.caption("The exact final-examination date and time are published through the official program schedule and D2L.")
