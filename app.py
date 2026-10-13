import streamlit as st

from src.data_loader import (
    load_applications,
    load_capabilities,
    load_decisions,
    load_profile,
    load_projects,
)

st.set_page_config(
    page_title="LinkedOut",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded",
)

profile = load_profile()
projects = load_projects()
applications = load_applications()
capabilities = load_capabilities()
decisions = load_decisions()

PRIMARY = "#37E0C8"
MUTED = "#93A4B5"
CARD = "#0E141B"
BORDER = "#1D2833"

st.markdown(
    f"""
    <style>
      .stApp {{
        background:
          radial-gradient(1100px 620px at 12% -8%, rgba(55, 224, 200, 0.10), transparent 60%),
          radial-gradient(900px 520px at 92% 4%, rgba(96, 140, 255, 0.08), transparent 62%),
          #070B10;
        color: #E8EEF4;
      }}

      section[data-testid="stSidebar"] {{
        background: #080D12;
        border-right: 1px solid {BORDER};
      }}

      .linkedout-brand {{
        font-size: 1.55rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        margin-bottom: 0.15rem;
      }}

      .linkedout-brand span {{
        color: {PRIMARY};
      }}

      .linkedout-subtitle {{
        color: {MUTED};
        font-size: 0.82rem;
        line-height: 1.45;
        margin-bottom: 1.5rem;
      }}

      .hero {{
        border: 1px solid {BORDER};
        background: linear-gradient(145deg, rgba(55, 224, 200, 0.08), rgba(14, 20, 27, 0.94));
        border-radius: 22px;
        padding: 2.2rem 2.4rem;
      }}

      .hero h1 {{
        font-size: 2.55rem;
        font-weight: 850;
        letter-spacing: -0.045em;
        line-height: 1.05;
        margin: 0 0 0.9rem 0;
      }}

      .hero p {{
        color: #B9C6D2;
        font-size: 1.03rem;
        line-height: 1.65;
        max-width: 760px;
        margin: 0;
      }}

      .eyebrow {{
        color: {PRIMARY};
        font-size: 0.74rem;
        font-weight: 750;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        margin-bottom: 0.7rem;
      }}

      .metric-card {{
        background: {CARD};
        border: 1px solid {BORDER};
        border-radius: 18px;
        padding: 1.25rem 1.35rem;
        height: 100%;
      }}

      .metric-value {{
        font-size: 1.9rem;
        font-weight: 800;
        letter-spacing: -0.03em;
      }}

      .metric-label {{
        color: {MUTED};
        font-size: 0.82rem;
        margin-top: 0.25rem;
      }}

      .section-card {{
        background: {CARD};
        border: 1px solid {BORDER};
        border-radius: 18px;
        padding: 1.5rem 1.6rem;
        height: 100%;
      }}

      .section-card h3 {{
        font-size: 1.08rem;
        font-weight: 750;
        margin: 0 0 0.55rem 0;
      }}

      .section-card p {{
        color: #A9B7C4;
        font-size: 0.92rem;
        line-height: 1.6;
        margin: 0;
      }}

      .status-pill {{
        display: inline-flex;
        align-items: center;
        border: 1px solid rgba(55, 224, 200, 0.35);
        background: rgba(55, 224, 200, 0.10);
        color: {PRIMARY};
        border-radius: 999px;
        padding: 0.3rem 0.75rem;
        font-size: 0.78rem;
        font-weight: 700;
      }}

      .page-heading {{
        font-size: 2rem;
        font-weight: 820;
        letter-spacing: -0.035em;
        margin-bottom: 0.4rem;
      }}

      .page-intro {{
        color: #A9B7C4;
        max-width: 780px;
        line-height: 1.65;
        margin-bottom: 1.8rem;
      }}

      .empty-state {{
        border: 1px dashed {BORDER};
        border-radius: 18px;
        padding: 2.2rem;
        text-align: center;
        color: {MUTED};
        background: rgba(14, 20, 27, 0.65);
      }}

      @media (max-width: 768px) {{
        .hero {{ padding: 1.6rem; }}
        .hero h1 {{ font-size: 1.9rem; }}
        .page-heading {{ font-size: 1.55rem; }}
      }}
    </style>
    """,
    unsafe_allow_html=True,
)


def render_page_heading(eyebrow, title, introduction):
    st.markdown(
        f"""
        <div class="page-heading">{title}</div>
        <div class="page-intro">{introduction}</div>
        <div class="eyebrow">{eyebrow}</div>
        """,
        unsafe_allow_html=True,
    )


def render_empty_state(message):
    st.markdown(f'<div class="empty-state">{message}</div>', unsafe_allow_html=True)


def render_status_pill(text):
    st.markdown(f'<div class="status-pill">{text}</div>', unsafe_allow_html=True)


def signal_page():
    metrics = profile.get("headline_metrics", {})

    st.markdown(
        f"""
        <div class="hero">
          <div class="eyebrow">Proof of work career application</div>
          <h1>LinkedOut</h1>
          <p>
            A working alternative to a conventional professional profile.
            LinkedOut presents evidence, working software, decision records, and a transparent
            record of the custom work created for real opportunities.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    left, middle, right = st.columns(3)

    with left:
        st.markdown(
            f"""
            <div class="metric-card">
              <div class="metric-value">{metrics.get('public_repositories', len(projects))}</div>
              <div class="metric-label">Public repositories represented in this portfolio</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with middle:
        flagship_count = sum(1 for project in projects if project.get("status") == "Flagship")
        st.markdown(
            f"""
            <div class="metric-card">
              <div class="metric-value">{flagship_count}</div>
              <div class="metric-label">Flagship case studies presented in depth</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.markdown(
            f"""
            <div class="metric-card">
              <div class="metric-value">{len(capabilities)}</div>
              <div class="metric-label">Capabilities connected to observable evidence</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    st.markdown("### Current focus")
    st.markdown(profile.get("current_focus", ""))

    st.markdown("### Primary skills")
    skills = profile.get("primary_skills", [])
    for index in range(0, len(skills), 3):
        columns = st.columns(3)
        for column, skill in zip(columns, skills[index : index + 3]):
            with column:
                st.markdown(
                    f'<div class="section-card"><h3>{skill}</h3></div>',
                    unsafe_allow_html=True,
                )

    st.write("")
    st.markdown("### Currently exploring")
    st.markdown(", ".join(profile.get("current_exploration", [])))

    st.write("")
    render_status_pill("Data driven career application")


def operating_model_page():
    render_page_heading(
        "How work happens",
        "Operating Model",
        "A repeatable method for turning operational friction into working software. Each stage connects discovery, design, validation, governance, and delivery.",
    )

    stages = [
        ("Diagnose", "Identify the operational bottleneck and define the decision the user needs to make."),
        ("Model", "Map the workflow, data, roles, exceptions, and measures of success."),
        ("Prototype", "Create a usable Python and Streamlit interface that makes the workflow visible."),
        ("Validate", "Test the solution against real scenarios, edge cases, and stakeholder expectations."),
        ("Govern", "Document assumptions, quality checks, accessibility, versioning, and limitations."),
        ("Deploy and iterate", "Package the solution, deploy it, collect feedback, and improve it."),
    ]

    for index in range(0, len(stages), 3):
        columns = st.columns(3)
        for column, item in zip(columns, stages[index : index + 3]):
            title, description = item
            with column:
                st.markdown(
                    f"""
                    <div class="section-card">
                      <h3>{title}</h3>
                      <p>{description}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


def proof_page():
    render_page_heading(
        "Evidence over claims",
        "Proof of Work",
        "Each project connects a real problem, user decision, solution, artificial intelligence contribution, human judgment, limitation, and business value.",
    )

    status_filter = st.selectbox(
        "Filter projects",
        ["All projects", "Flagship", "Supporting"],
    )

    visible_projects = projects
    if status_filter != "All projects":
        visible_projects = [project for project in projects if project.get("status") == status_filter]

    if not visible_projects:
        render_empty_state("No projects match this filter yet.")
        return

    for project in visible_projects:
        with st.expander(f"{project['title']} · {project.get('status', 'Project')}"):
            st.markdown(f"**Problem**\n\n{project.get('problem', '')}")
            st.markdown(f"**User decision**\n\n{project.get('user_decision', '')}")
            st.markdown(f"**Solution**\n\n{project.get('solution', '')}")

            left, right = st.columns(2)
            with left:
                st.markdown("**Artificial intelligence contribution**")
                st.markdown(project.get("ai_contribution", ""))
            with right:
                st.markdown("**Human contribution**")
                st.markdown(project.get("human_contribution", ""))

            st.markdown(f"**Limitations**\n\n{project.get('limitations', '')}")
            st.markdown(f"**Business value**\n\n{project.get('business_value', '')}")

            st.markdown("**Stack**")
            st.markdown(", ".join(project.get("stack", [])))

            st.markdown("**Relevant roles**")
            st.markdown(", ".join(project.get("relevant_roles", [])))

            st.link_button("Open repository", project.get("repository", "#"))


def ledger_page():
    render_page_heading(
        "The search as evidence",
        "Application Ledger",
        "This ledger records roles pursued, custom artifacts created for each opportunity, application status, outcomes, and reusable learning.",
    )

    if not applications:
        render_empty_state(
            "No applications have been recorded yet. Each future application can include a custom artifact, status, outcome, and reusable learning."
        )
        return

    for application in applications:
        with st.expander(f"{application.get('role', 'Role')} · {application.get('company', 'Company')}"):
            st.markdown(f"**Applied on**\n\n{application.get('date', 'Not recorded')}")
            st.markdown(f"**Source**\n\n{application.get('source', 'Not recorded')}")
            st.markdown(f"**Status**\n\n{application.get('status', 'Not recorded')}")
            st.markdown(f"**Artifact created**\n\n{application.get('artifact', 'Not recorded')}")
            st.markdown(f"**Outcome**\n\n{application.get('outcome', 'Pending')}")
            st.markdown(f"**Learning**\n\n{application.get('learning', 'Not recorded')}")

            artifact_url = application.get("artifact_url")
            if artifact_url:
                st.link_button("Open application artifact", artifact_url)


def capability_page():
    render_page_heading(
        "Skills with evidence",
        "Capability Map",
        "Every capability connects to projects, demonstrations, and application artifacts rather than self assigned ratings.",
    )

    for capability in capabilities:
        with st.expander(capability.get("name", "Capability")):
            render_status_pill(capability.get("evidence_strength", "Demonstrated"))
            st.write("")
            st.markdown("**Evidence**")
            st.markdown(", ".join(capability.get("evidence", [])))
            st.markdown("**Relevant roles**")
            st.markdown(", ".join(capability.get("relevant_roles", [])))


def decisions_page():
    render_page_heading(
        "Judgment in the open",
        "Decision Records",
        "These records explain the choices behind each project, including alternatives considered, tradeoffs accepted, risks identified, and improvements planned.",
    )

    for decision in decisions:
        with st.expander(f"{decision.get('project', 'Project')} · {decision.get('title', 'Decision')}"):
            st.markdown(f"**Decision**\n\n{decision.get('decision', '')}")
            st.markdown("**Alternatives considered**")
            st.markdown(", ".join(decision.get("alternatives_considered", [])))
            st.markdown(f"**Tradeoff**\n\n{decision.get('tradeoff', '')}")
            st.markdown(f"**Risk**\n\n{decision.get('risk', '')}")
            st.markdown(f"**Artificial intelligence limitation**\n\n{decision.get('ai_limitation', '')}")
            st.markdown(f"**Next improvement**\n\n{decision.get('next_improvement', '')}")


def lab_page():
    render_page_heading(
        "Working demonstrations",
        "Live Lab",
        "This section will provide direct access to interactive demonstrations, sample data policies, and clear instructions for exploring each application.",
    )
    render_empty_state("Live Lab arrives in Phase 9.")


def contact_page():
    render_page_heading(
        "Start a conversation",
        "Contact",
        "This section will provide a direct route to discuss AI product work, operational tooling, design systems, workflow automation, or a specific opportunity.",
    )
    render_empty_state("Contact experience arrives in Phase 10.")


PAGES = {
    "Signal": signal_page,
    "Operating Model": operating_model_page,
    "Proof of Work": proof_page,
    "Application Ledger": ledger_page,
    "Capability Map": capability_page,
    "Decision Records": decisions_page,
    "Live Lab": lab_page,
    "Contact": contact_page,
}

with st.sidebar:
    st.markdown(
        """
        <div class="linkedout-brand">Linked<span>Out</span></div>
        <div class="linkedout-subtitle">
          A proof of work career application.<br>
          Evidence, demonstrations, and decisions in one place.
        </div>
        """,
        unsafe_allow_html=True,
    )

    selected_page = st.radio(
        "Navigate",
        list(PAGES.keys()),
        label_visibility="collapsed",
    )

    st.write("")
    st.markdown(
        f"""
        <div class="linkedout-subtitle">
          {profile.get('career_identity', '')}<br>
          {profile.get('location', '')}
        </div>
        """,
        unsafe_allow_html=True,
    )

PAGES[selected_page]()
