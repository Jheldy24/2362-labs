"""Check that the Week 4 graded starter is complete without solving it."""
from pathlib import Path
import json
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).parent
required = [
    "facilities.geojson", "service_zones.geojson", "source_inventory.csv",
    "metadata.json", "qgis-project.qgz", "README.md",
    "peer-review-questionnaire.md", "retrospective-template.md",
    "part-a-checkpoint-template.md", "rubric.md", "manifest-template.json",
    "ai-declaration-template.md", "environment-record-template.md"
]
missing = [name for name in required if not (ROOT / name).exists()]
assert not missing, f"Missing starter files: {missing}"
metadata = json.loads((ROOT / "metadata.json").read_text(encoding="utf-8"))
assert metadata["week"] == 4
with zipfile.ZipFile(ROOT / "qgis-project.qgz") as archive:
    root = ET.fromstring(archive.read("project.qgs"))
    assert root.findall(".//maplayer")
assert not (ROOT / "workflow.py").exists(), "Starter must not contain a completed workflow"
assert not (ROOT / "outputs").exists(), "Starter must not contain completed outputs"
print("PASS: Week 4 graded starter is complete and contains no completed solution")
