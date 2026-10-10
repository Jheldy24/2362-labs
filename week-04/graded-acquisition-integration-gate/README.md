# AIDA 2362 Week 4 — Graded Lab 1

## Acquisition, licence, metadata, and integration gate

**Value:** 5% of the course grade

- Part A checkpoint: 3%
- Part B production extension: 2%
- One lab folder and one GitHub/D2L submission

This is an **independent graded lab**. The practice lab in the Practical Lab
Examples repository demonstrates the workflow, but it is not an answer to this
lab. Use your own wording, decisions, QGIS evidence, and changed-variable test.

## Your decision task

You are advising a facilities-maintenance team. Decide whether the supplied
spatial data are ready for a limited integration and planning check.

Your decision must be exactly one of:

- `ready`
- `conditional`
- `quarantine`
- `reject`

Do not make a real operational decision. The data are fictional and supplied
only for learning.

## What you must use

- QGIS is the primary tool.
- Use the supplied `facilities.geojson`, `service_zones.geojson`, and
  `source_inventory.csv`.
- Read `metadata.json` before analysis.
- The supplied records are fictional. Do not add real personal information or
  real sensitive locations.
- The supplied files are all you need; no additional online account or external
  service is required.

## Part 1 — Copy the starter to your private repository

1. Download this folder from the instructor repository.
2. Extract the ZIP if it was downloaded as a ZIP.
3. Open your assigned private AIDA 2362 repository in VS Code.
4. Create or open the folder `week-04`.
5. Copy the complete folder `graded-acquisition-integration-gate` into it.
6. Open that copied folder in VS Code.
7. Do all graded work inside this copied folder.
8. Do not push work to the instructor `AIDA_2362_Graded_Labs` repository.

## Part 2 — Read the supplied files

Open each file before making a decision:

1. `metadata.json` — source, CRS, licence, privacy, governance, and
   accessibility information.
2. `source_inventory.csv` — the documented facility source and the legacy
   source that requires a gate decision.
3. `facilities.geojson` — facility point data.
4. `service_zones.geojson` — service-zone polygons.
5. `qgis-project.qgz` — prepared QGIS project.

Do not overwrite the supplied files.

## Part 3 — Create your working notes

Create a file named `README-your-name.md` in the lab folder. Answer these
questions in complete sentences:

1. Who is the decision-maker?
2. What action could the decision-maker take?
3. What spatial unit is being analysed?
4. What is the geographic extent?
5. What scale is appropriate for this result?
6. What is the time or retrieval limitation?
7. What decision did you make: ready, conditional, quarantine, or reject?
8. Why is that decision limited to this fictional teaching example?

## Part 4 — Open the QGIS project

1. Open QGIS.
2. Select **Project → Open**.
3. Open `qgis-project.qgz`.
4. Confirm that the facility and service-zone layers appear.
5. If a layer is not visible, right-click it and choose **Zoom to Layer**.
6. Confirm that the layer paths point to files in this lab folder.
7. Record the project and layer CRS in your notes.

## Part 5 — Complete the source and metadata audit

For each source in `source_inventory.csv`, record:

1. publisher;
2. retrieval date;
3. licence;
4. CRS;
5. geometry type;
6. feature count;
7. field names;
8. stable ID field;
9. duplicate IDs;
10. missing geometry;
11. missing required attributes;
12. extent;
13. temporal fitness;
14. scale or resolution;
15. privacy limit;
16. community or Indigenous data-authority requirement;
17. integration decision.

Create `source-audit.csv` with one row per source and clear column names.

## Part 6 — Check the facility layer in QGIS

1. Open the facility attribute table.
2. Count the features.
3. Identify the stable ID field.
4. Check for duplicate IDs.
5. Check for blank IDs.
6. Check the geometry type.
7. Check the layer CRS.
8. Record the result in `README-your-name.md`.

## Part 7 — Check the service-zone layer in QGIS

1. Open the service-zone attribute table.
2. Count the polygons.
3. Identify the stable zone ID field.
4. Check for duplicate zone IDs.
5. Check for blank zone names.
6. Run **Vector → Geometry Tools → Check Validity**.
7. Save the validity result as a new derived output.
8. Record invalid feature IDs, if any.
9. Do not delete or overwrite source features.

## Part 8 — Record CRS, units, and area of use

1. Record the storage CRS.
2. State whether it uses degrees or metres.
3. State the analysis CRS you selected, if a projected copy is needed.
4. State the units of the analysis CRS.
5. Explain why the CRS area of use matters.
6. Save any projected layer as a new file.
7. Keep the original input layer unchanged.

## Part 9 — Produce one reproducible QGIS result

Create one QGIS result that supports your decision. Examples include:

- a facility-to-zone spatial relationship;
- a clean/invalid geometry result;
- a documented integration selection;
- a source-ready or source-quarantine layer.

Your result must include:

1. the operation name;
2. the input layers;
3. the important parameters;
4. the output path;
5. the feature counts;
6. the affected IDs;
7. the date or run context;
8. a saved QGIS Processing history, model, or equivalent written record.

Save the result in a folder named `outputs`.

## Part 10 — Run one changed-variable comparison

Change one consequential variable only. Examples:

- `within` versus `intersects`;
- original CRS versus projected working copy;
- inclusion versus quarantine of unsupported records;
- one documented threshold or extent choice.

Create `outputs/changed-variable-comparison.csv` with these columns:

```text
baseline_setting,changed_setting,baseline_count,changed_count,affected_ids,decision_effect
```

Explain the result in `README-your-name.md`. Do not change multiple variables
at the same time.

## Part 11 — Create an accessible result

Create one map or QGIS layout in `outputs`. It must include:

- a descriptive title;
- a legend or key;
- CRS or unit context;
- a scale or extent cue;
- meaning that does not depend on colour alone;
- no unnecessary sensitive location detail.

Create an exact text/table equivalent named
`outputs/text-table-equivalent.md`. The text/table must communicate the same
claim as the map. A reader should be able to understand the result without
opening QGIS.

## Part 12 — Complete the peer review

Use `peer-review-questionnaire.md`.

1. Ask a classmate to review the repository locally.
2. Do not give the reviewer permission to edit your files.
3. Ask the reviewer to cite evidence paths.
4. Save the completed questionnaire as `peer-review-response.md`.
5. State whether you accepted, rejected, or deferred each useful observation.

## Part 13 — Complete the retrospective and declarations

Complete these files using the supplied templates:

- `retrospective.md` using `retrospective-template.md`;
- `manifest.json` using `manifest-template.json`;
- `ai-declaration.md` using `ai-declaration-template.md`;
- `environment-record.md` using `environment-record-template.md`.

Your retrospective must explain what changed between Part A and Part B, which
assumption most affected the result, what could still be wrong, and what would
be needed before operational use.

## Required final folder

Your completed lab folder must contain at least:

```text
graded-acquisition-integration-gate/
├── README-your-name.md
├── facilities.geojson
├── service_zones.geojson
├── source_inventory.csv
├── metadata.json
├── qgis-project.qgz
├── source-audit.csv
├── peer-review-questionnaire.md
├── peer-review-response.md
├── retrospective.md
├── manifest.json
├── ai-declaration.md
├── environment-record.md
└── outputs/
    ├── saved QGIS result
    ├── changed-variable-comparison.csv
    └── text-table-equivalent.md
```

Do not submit screenshots alone. Screenshots may support your evidence, but
your QGIS project, saved outputs, notes, and tables must also be present.

## Git and D2L submission — one submission only

1. Save all files in the one `graded-acquisition-integration-gate` folder.
2. Open the terminal in your private repository.
3. Check your files:

```powershell
git status
```

4. Add the lab folder:

```powershell
git add week-04/graded-acquisition-integration-gate
```

5. Create a meaningful commit:

```powershell
git commit -m "Complete AIDA 2362 Week 4 graded lab"
```

6. Push to your private repository:

```powershell
git push
```

7. Open GitHub and confirm that the commit and lab folder are visible.
8. Copy your private repository URL.
9. Submit that one URL in the Week 4 D2L submission link.

This lab has one GitHub/D2L submission worth 5%. Part A and Part B are marking
components inside the same folder. Do not create two separate submissions.

## Academic and responsible-use rules

- Use your own analysis and wording.
- Cite or document any outside source.
- Declare AI assistance and verify every material suggestion.
- Do not include passwords, API keys, personal addresses, or real sensitive
  locations.
- State who may benefit, who may be harmed, and what authority is required for
  community or Indigenous data. OCAP® is First Nations-specific.
