LABS = {
    1: {
        "title": "Vector validation",
        "build": "Add checks for CRS presence, geometry type, empty/invalid geometries, and duplicates.",
        "evidence": "Validation counts, retained originals, repair strategy, and verification.",
        "guardrail": "Do not repair source features invisibly.",
    },
    2: {
        "title": "CRS troubleshooting",
        "build": "Diagnose a supplied mismatch, perform an explicit transformation, and compare units/extents.",
        "evidence": "Source/target CRS, transformation check, projection fitness, and limitations.",
        "guardrail": "Do not preselect a universally correct CRS.",
    },
    3: {
        "title": "Acquisition and metadata",
        "build": "Build or validate a manifest with source, licence, version, checksum, CRS, scale, use, and privacy review.",
        "evidence": "Complete manifest, local supplied-data path, and quality decisions.",
        "guardrail": "Do not rely on unlicensed or personally captured location data.",
    },
    4: {
        "title": "Joins and overlays",
        "build": "Implement one attribute/spatial join or overlay with a chosen predicate.",
        "evidence": "Unmatched counts, validity checks, predicate rationale, and interpretation.",
        "guardrail": "Do not supply the finished assessed overlay.",
    },
    5: {
        "title": "Accessible cartography",
        "build": "Implement map hierarchy, symbology, legend, labels, colour, and a text alternative.",
        "evidence": "Audience, scale, uncertainty, accessibility, and design rationale.",
        "guardrail": "The student chooses the map design and message.",
    },
    6: {
        "title": "Raster and terrain",
        "build": "Load a supplied raster, inspect CRS/resolution/extent/NoData, and add one bounded operation.",
        "evidence": "Metadata checks, output validation, display, and limitations.",
        "guardrail": "No live imagery, personal capture, or special hardware dependency.",
    },
    7: {
        "title": "Decision-support spatial analysis",
        "build": "Implement criteria, thresholds, or weights and a spatial decision output with sensitivity.",
        "evidence": "Assumptions, sensitivity, uncertainty, strategy recommendation, and privacy review.",
        "guardrail": "Avoid personal locations and expose every weighting choice.",
    },
    8: {
        "title": "Geoprocessing or spatial statistics",
        "build": "Implement one bounded buffer, clip, dissolve, proximity, density, cluster, or statistic workflow.",
        "evidence": "Units, topology, edge/scale effects, validation, and uncertainty.",
        "guardrail": "Do not provide a canned result or ignore spatial dependence.",
    },
    9: {
        "title": "Reproducible web map",
        "build": "Implement Folium layers, popups, legend, accessibility, and a standalone local export.",
        "evidence": "Relative paths, generalization/suppression choices, test output, and limitations.",
        "guardrail": "Do not disclose sensitive locations or require a hosted service.",
    },
    10: {
        "title": "GeoPandas workflow",
        "build": "Implement load, validate, transform, analyze, and export with assertions and metadata.",
        "evidence": "Reproducible run, CRS/validity checks, GeoPackage/GeoJSON output, and limitations.",
        "guardrail": "PostGIS is optional; do not make it the only pathway.",
    },
}
