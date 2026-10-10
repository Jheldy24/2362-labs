# Week 4 Part A checkpoint — 3%

- **Decision-maker, action, and audience:** The GIS data steward will decide
  whether the fictional facilities-maintenance team may use a limited,
  course-only planning check. The proposed action is to permit the
  `facility_points` source for that limited check while keeping
  `legacy_access_paths` quarantined. The audience is the GIS and maintenance
  planning team.
- **Spatial unit, extent, scale, and time:** Five facility points are examined
  against three service-zone polygons. The zone extent is approximately
  longitude -113.815 to -113.764 and latitude 52.235 to 52.262. The selected
  local map scale is approximately 1:25,000. The data are a deterministic
  synthetic snapshot generated 2026-08-13, not a live operational export.
- **Source, licence, metadata, and authority:** The inventory lists
  `facility_points` as AIDA 2362 course data under CC0-1.0. The
  `legacy_access_paths` publisher, retrieval date, and CRS are not provided;
  its licence is unknown and two geometries are reported missing, so it is
  quarantined. The supplied `service_zones` layer is absent from
  `source_inventory.csv`; its source-specific inventory record must be
  completed before integration. The metadata says the records are fictional
  and contain no real personal or sensitive locations. OCAP is
  First Nations-specific; CARE is a high-level complement. Any real
  community or Indigenous data would require the relevant authority and
  locally specific protocols.
- **Storage CRS, analysis CRS, units, and area of use:** EPSG:4326 is the
  storage CRS and uses angular coordinates in degrees. EPSG:32612 is the
  metadata's suggested analysis CRS in metres when metric distance or area is
  required. Its area of use must be checked before such measurements. The
  current point-in-polygon comparison uses no metric distance or area.
- **Geometry, attributes, stable IDs, duplicates, and missingness:** The
  `facilities` layer has five Point features with populated, unique
  `feature_id` values and no missing geometries observed. Its fields include
  `facility_name`, `facility_type`, `readiness`, and `incidents`. The
  `service_zones` layer has three Polygon features with populated, unique
  `feature_id` values and non-empty `zone_name` values. QGIS Check Validity
  using GEOS returned three valid and zero invalid zone geometries. The
  legacy source's fields, IDs, geometry type, and extent cannot be checked
  because its data file was not supplied.
- **First reproducible QGIS result and saved evidence path:** QGIS Processing
  Join attributes by location used `facilities` as input,
  `service_zones` as join layer, predicate `within`, and one-to-one
  first-match behavior. It returned five facilities with non-empty zone
  names. Evidence: `outputs/facility_zone_within.gpkg` and the run record in
  `README-Kiara.md`. The geometry-validity output is
  `outputs/service_zones_valid.gpkg`.
- **Changed variable and expected effect:** The baseline predicate is
  `within`; the single changed variable is `intersects`. Because the supplied
  points are inside the zones, the expected result was no assignment change.
  QGIS returned five records in both runs and the same assignments; no
  facility IDs were affected. The comparison is in
  `outputs/changed-variable-comparison.csv`.
- **Uncertainty and operational limit:** The legacy data are unavailable for
  inspection, their source details and licence are unknown, and two
  geometries are reported missing. The service-zone source is omitted from
  the supplied inventory. The synthetic snapshot is not current operational
  evidence. The result supports only the limited fictional course check.
- **Peer review:** Not performed; this step was intentionally omitted by the
  student. No reviewer evidence or response is claimed, and the peer-review
  rubric criterion remains incomplete.
