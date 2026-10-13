from pathlib import Path
from typing import Any

import yaml

DATA_DIRECTORY = Path(__file__).resolve().parents[1] / "data"


def load_yaml(filename: str) -> dict[str, Any]:
    path = DATA_DIRECTORY / filename
    if not path.exists():
        raise FileNotFoundError(f"Required data file is missing: {path}")
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Expected a mapping in {path}")
    return data


def load_profile() -> dict[str, Any]:
    return load_yaml("profile.yaml")


def load_projects() -> list[dict[str, Any]]:
    return load_yaml("projects.yaml").get("projects", [])


def load_applications() -> list[dict[str, Any]]:
    return load_yaml("applications.yaml").get("applications", [])


def load_capabilities() -> list[dict[str, Any]]:
    return load_yaml("capabilities.yaml").get("capabilities", [])


def load_decisions() -> list[dict[str, Any]]:
    return load_yaml("decisions.yaml").get("decisions", [])
