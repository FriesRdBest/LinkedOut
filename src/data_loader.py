import yaml
import streamlit as st


def _load_yaml(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file) or []
    except FileNotFoundError:
        st.error(f"Required data file not found: {path}")
        return []
    except yaml.YAMLError as error:
        st.error(f"Invalid YAML in {path}: {error}")
        return []


def load_profile():
    return _load_yaml("data/profile.yaml") or {}


def load_projects():
    return _load_yaml("data/projects.yaml") or []


def load_applications():
    return _load_yaml("data/applications.yaml") or []


def load_capabilities():
    return _load_yaml("data/capabilities.yaml") or []


def load_decisions():
    return _load_yaml("data/decisions.yaml") or []
