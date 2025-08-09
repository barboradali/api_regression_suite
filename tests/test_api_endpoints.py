import json
import os
import time
import random
import requests
import pytest
from jsonschema import validate

BASE_URL = "https://api.openweathermap.org/data/2.5"

# ---- load cases
data_file = os.path.join(os.path.dirname(__file__), "test_data.json")
with open(data_file) as f:
    raw_cases = json.load(f)

# turn raw cases into pytest.param, applying marks if present
cases = []
ids = []
for c in raw_cases:
    mark = c.get("mark")
    reason = c.get("reason", "")
    param = pytest.param(c, marks=(), id=c["name"])
    if mark == "xfail":
        param = pytest.param(c, marks=pytest.mark.xfail(strict=True, reason=reason), id=c["name"])
    elif mark == "skip":
        param = pytest.param(c, marks=pytest.mark.skip(reason=reason), id=c["name"])
    cases.append(param)
    ids.append(c["name"])

@pytest.mark.parametrize("case", cases, ids=ids)
def test_api(case):
    url = f"{BASE_URL}{case['endpoint']}"
    start = time.time()
    resp = requests.request(case["method"], url)
    elapsed = resp.elapsed.total_seconds() if resp.elapsed else (time.time() - start)

    # status code check
    assert resp.status_code == case["expected_status"], f"Expected {case['expected_status']}, got {resp.status_code}"

    # schema validation (if provided)
    schema_name = case.get("schema")
    if schema_name:
        schema_path = os.path.join(os.path.dirname(__file__), "schemas", schema_name)
        with open(schema_path) as sf:
            schema = json.load(sf)
        validate(instance=resp.json(), schema=schema)

# ---- ERROR demo: this test raises an exception before assertions -> recorded as ERROR
def test_program_error_demo():
    raise RuntimeError("Intentional error to demonstrate 'ERROR' outcome in report")

# ---- RERUN demo: first try fails, second try passes (requires pytest-rerunfailures)
_attempts = {"flaky": 0}

@pytest.mark.flaky(reruns=1, reruns_delay=0.5)
def test_flaky_rerun_demo():
    _attempts["flaky"] += 1
    # fail on first attempt, pass on rerun
    assert _attempts["flaky"] > 1, "Flaky failure on first run; should pass on rerun"

