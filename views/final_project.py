import streamlit as st

from project_workspace import FinalProjectContract, render_final_project_workspace


CONTRACT = FinalProjectContract(
    course_name="Geographic Information Systems",
    project_name="Final Spatial Project",
    project_boundary=(
        "Select an approved Apex facilities-maintenance spatial decision and build a reproducible QGIS/Python "
        "workflow with validated spatial data and an accessible decision-support map or dashboard."
    ),
    selection_process=(
        "Compare spatial opportunities by stakeholder value, data fitness, CRS/scale requirements, feasibility, "
        "privacy/community impact, and the evidence needed for a defensible recommendation."
    ),
    data_evidence=(
        "Authorized spatial data, provenance, metadata, licence, geometry type, CRS, scale, and resolution.",
        "Validity, topology, completeness, positional uncertainty, joins, and transformation evidence.",
        "Relative-path, supplied-data, and non-specialized-hardware alternatives for reproducibility.",
    ),
    design_evidence=(
        "A reproducible QGIS-primary workflow with Python/PostGIS used only where appropriate.",
        "Justified query, join, overlay, buffer, raster, spatial-statistical, or introductory ML methods.",
        "Accessible cartography or dashboard design connected to the decision context and audience.",
    ),
    validation_evidence=(
        "CRS, geometry validity, topology, scale, extent, attribute, and output reconciliation.",
        "Sensitivity to distance, resolution, classification, missingness, and spatial assumptions.",
        "Map/output review against baseline evidence and the stated organizational decision.",
    ),
    responsibility_evidence=(
        "Location privacy, security, bias, uncertainty, accessibility, and community-impact analysis.",
        "Respectful treatment of Indigenous data sovereignty and any relevant community governance.",
        "Human review, monitoring, update ownership, stop conditions, and rollback plan.",
    ),
    final_deliverables=(
        "Decision context, authorized spatial data, provenance, metadata, CRS, and quality evidence.",
        "Reproducible QGIS/Python workflow, analysis outputs, and accessible map/dashboard.",
        "Uncertainty, scale, limitations, privacy/community evidence, and strategy recommendation.",
        "Validated final ZIP, relative paths, demonstration materials, and AI-use declaration.",
    ),
)


def render_student_solution() -> None:
    """Replace this starter panel with the approved, tested spatial product."""
    st.info(
        "STUDENT BUILD AREA — render the decision-support map, spatial indicators, or dashboard extension here. "
        "Keep the authoritative QGIS workflow and reproducible processing files in the repository."
    )


render_final_project_workspace(CONTRACT, render_student_solution)
