import yaml
import streamlit as st


def _load_yaml(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        st.error(f"Required data file not found: {path}")
        return None
    except yaml.YAMLError as error:
        st.error(f"Invalid YAML in {path}: {error}")
        return None


def _normalize_list(data, keys):
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for key in keys:
            value = data.get(key)
            if isinstance(value, list):
                return value
        return [data]
    return []


def load_profile():
    data = _load_yaml("data/profile.yaml")
    if isinstance(data, dict):
        return data
    if isinstance(data, list) and data:
        return data[0]
    return {}


def load_projects():
    return _normalize_list(_load_yaml("data/projects.yaml"), ["projects", "items", "records"])


def load_applications():
    return _normalize_list(_load_yaml("data/applications.yaml"), ["applications", "items", "records"])


def load_capabilities():
    return _normalize_list(_load_yaml("data/capabilities.yaml"), ["capabilities", "items", "records"])


def load_decisions():
    return _normalize_list(_load_yaml("data/decisions.yaml"), ["decisions", "items", "records"])
