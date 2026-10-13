import io

import pandas as pd
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

      .project-card {{
        background: {CARD};
        border: 1px solid {BORDER};
        border-radius: 20px;
        padding: 1.5rem 1.55rem;
        height: 100%;
        display: flex;
        flex-direction: column;
        gap: 0.75rem;
      }}

      .project-card h3 {{
        font-size: 1.18rem;
        font-weight: 780;
        letter-spacing: -0.02em;
        margin: 0;
      }}

      .project-card p {{
        color: #A9B7C4;
        font-size: 0.9rem;
        line-height: 1.6;
        margin: 0;
      }}

      .project-tags {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.4rem;
      }}

      .project-tag {{
        border: 1px solid {BORDER};
        background: rgba(255, 255, 255, 0.03);
        color: #C7D3DE;
        border-radius: 999px;
        padding: 0.22rem 0.6rem;
        font-size: 0.72rem;
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

      .stage-number {{
        color: {PRIMARY};
        font-size: 0.78rem;
        font-weight: 800;
        letter-spacing: 0.18em;
        text-transform: uppercase;
      }}

      .workflow-box {{
        border: 1px solid {BORDER};
        background: rgba(255, 255, 255, 0.03);
        border-radius: 12px;
        padding: 0.8rem 1rem;
        margin: 0.3rem 0;
        color: #C7D3DE;
        font-size: 0.88rem;
      }}

      .workflow-arrow {{
        color: {PRIMARY};
        text-align: center;
        font-size: 1.1rem;
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


def render_project_tags(values):
    tags = "".join(f'<span class="project-tag">{value}</span>' for value in values)
    st.markdown(f'<div class="project-tags">{tags}</div>', unsafe_allow_html=True)


def render_workflow(before, after):
    st.markdown(
        f"""
        <div class="workflow-box"><strong>Before</strong><br>{before}</div>
        <div class="workflow-arrow">↓</div>
        <div class="workflow-box"><strong>After</strong><br>{after}</div>
        """,
        unsafe_allow_html=True,
    )


def render_architecture(items):
    for item in items:
        st.markdown(f'<div class="workflow-box">{item}</div>', unsafe_allow_html=True)


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
    col1, col2, col3, col4 = st.columns(4)
    live_demos = sum(1 for p in projects if p.get("demo_url"))
    artifact_count = sum(1 for a in applications if a.get("artifact"))

    with col1:
        st.markdown(f"""<div class='metric-card'><div class='metric-value'>{metrics.get('public_repositories', len(projects))}</div><div class='metric-label'>Public repositories</div></div>""", unsafe_allow_html=True)
    with col2:
        flagship_count = sum(1 for p in projects if p.get("status") == "Flagship")
        st.markdown(f"""<div class='metric-card'><div class='metric-value'>{flagship_count}</div><div class='metric-label'>Flagship case studies</div></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown(f"""<div class='metric-card'><div class='metric-value'>{live_demos}</div><div class='metric-label'>Live demos</div></div>""", unsafe_allow_html=True)
    with col4:
        st.markdown(f"""<div class='metric-card'><div class='metric-value'>{artifact_count}</div><div class='metric-label'>Application artifacts</div></div>""", unsafe_allow_html=True)

    st.write("")
    st.markdown("### Primary actions")
    b1, b2, b3 = st.columns(3)
    with b1:
        if st.button("View Proof of Work", use_container_width=True):
            st.session_state["nav_override"] = "Proof of Work"
            st.rerun()
    with b2:
        if st.button("View Application Ledger", use_container_width=True):
            st.session_state["nav_override"] = "Application Ledger"
            st.rerun()
    with b3:
        if st.button("Contact me", use_container_width=True):
            st.session_state["nav_override"] = "Contact"
            st.rerun()

    st.write("")
    st.markdown("### Current focus")
    st.markdown(profile.get("current_focus", ""))

    st.markdown("### Work eligibility")
    st.markdown(profile.get("work_eligibility", "Authorized to work in the United States."))

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
        "A repeatable method for turning operational friction into working software. Every stage produces an observable output and connects to real proof of work.",
    )

    stages = [
        {
            "number": "Stage 1",
            "title": "Diagnose",
            "description": "Identify the operational bottleneck, understand the people involved, and define the decision the user needs to make.",
            "output": "A clear problem statement, target user, decision to support, and success measure.",
            "projects": ["Meeting Memory Hub", "Ghost Support Operations Engine"],
        },
        {
            "number": "Stage 2",
            "title": "Model",
            "description": "Map the workflow, data, roles, exceptions, dependencies, and measures of success.",
            "output": "A workflow model, data requirements, role map, exception handling approach, and success criteria.",
            "projects": ["Traceboard", "Pattern Library"],
        },
        {
            "number": "Stage 3",
            "title": "Prototype",
            "description": "Create a usable Python and Streamlit interface that makes the workflow visible and testable.",
            "output": "A working prototype with a clear interface, core workflow, and controlled sample data.",
            "projects": ["Providence", "Signal Field", "Plus Slop Stopper"],
        },
        {
            "number": "Stage 4",
            "title": "Validate",
            "description": "Test the solution against real scenarios, edge cases, stakeholder expectations, and operational constraints.",
            "output": "A validated prototype with documented assumptions, test scenarios, and required refinements.",
            "projects": ["Sash", "Providence"],
        },
        {
            "number": "Stage 5",
            "title": "Govern",
            "description": "Document assumptions, quality checks, accessibility, versioning, traceability, and limitations.",
            "output": "A governed solution with quality controls, accessibility considerations, and transparent limitations.",
            "projects": ["Traceboard", "Meeting Memory Hub"],
        },
        {
            "number": "Stage 6",
            "title": "Deploy and iterate",
            "description": "Package the solution, deploy it, collect feedback, and improve it through controlled iterations.",
            "output": "A deployed application with a feedback loop and a practical improvement path.",
            "projects": ["Sash", "Providence"],
        },
    ]

    for stage in stages:
        with st.expander(f"{stage['number']} · {stage['title']}"):
            st.markdown(stage["description"])
            st.markdown("**Output**")
            st.markdown(stage["output"])
            st.markdown("**Related proof of work**")
            st.markdown(", ".join(stage["projects"]))

    st.write("")
    st.markdown("## How artificial intelligence accelerates work")

    acceleration_columns = st.columns(3)
    acceleration_items = [
        ("Research and synthesis", "Artificial intelligence accelerates research, pattern recognition, documentation, and early interface exploration."),
        ("Prototype velocity", "It reduces the time required to move from an operational problem to a testable Python and Streamlit prototype."),
        ("Quality support", "It helps identify gaps, generate checks, and improve documentation, while human judgment remains accountable."),
    ]

    for column, item in zip(acceleration_columns, acceleration_items):
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

    st.write("")
    st.markdown("## Decisions that remain human owned")

    human_columns = st.columns(3)
    human_items = [
        ("Problem definition", "The operational problem, stakeholder needs, and definition of success must be understood and validated by people."),
        ("Business judgment", "Tradeoffs, priorities, risks, governance standards, and deployment decisions require accountable human judgment."),
        ("Validation and trust", "Artificial intelligence output must be tested against real scenarios before it can inform an operational decision."),
    ]

    for column, item in zip(human_columns, human_items):
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

    st.write("")
    st.markdown("## Working with me")

    collaboration_columns = st.columns(3)
    collaboration_items = [
        ("Clear communication", "I translate operational friction, technical constraints, and product decisions into language stakeholders can act on."),
        ("Evidence led feedback", "I welcome feedback, test assumptions, document decisions, and refine work based on observable results."),
        ("Reliable handoff", "I leave behind clear documentation, known limitations, decision records, and a practical path for continued improvement."),
    ]

    for column, item in zip(collaboration_columns, collaboration_items):
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


def ordered_projects():
    return sorted(
        projects,
        key=lambda project: 0 if project.get("status") == "Flagship" else 1,
    )


def render_project_card(project):
    summary = project.get("problem", "")
    if len(summary) > 180:
        summary = summary[:177].rstrip() + "..."

    st.markdown(
        f"""
        <div class="project-card">
          <div>
            <div class="eyebrow">{project.get('status', 'Project')}</div>
            <h3>{project.get('title', 'Project')}</h3>
          </div>
          <p>{summary}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_project_tags(project.get("stack", [])[:3])
    if st.button(
        "View case study",
        key=f"view_{project.get('title', '').lower().replace(' ', '_')}",
        use_container_width=True,
    ):
        st.session_state["selected_project"] = project.get("title")
        st.rerun()


def render_project_detail(project):
    if st.button("Back to all projects", key="back_to_projects"):
        st.session_state["selected_project"] = None
        st.rerun()

    st.write("")
    render_status_pill(project.get("status", "Project"))
    st.markdown(f"# {project.get('title', 'Project')}")
    st.markdown(project.get("problem", ""))

    st.write("")
    left, right = st.columns(2)

    with left:
        st.markdown("### User decision")
        st.markdown(project.get("user_decision", ""))
        st.markdown("### Solution")
        st.markdown(project.get("solution", ""))

    with right:
        st.markdown("### Artificial intelligence contribution")
        st.markdown(project.get("ai_contribution", ""))
        st.markdown("### Human contribution")
        st.markdown(project.get("human_contribution", ""))

    st.write("")
    st.markdown("### Before / after workflow")
    render_workflow(
        project.get("before_workflow", "Manual, fragmented process with limited visibility."),
        project.get("after_workflow", "Streamlined workflow with clear decisions and traceable outputs."),
    )

    st.markdown("### Architecture")
    render_architecture(project.get("architecture", ["Python and Streamlit interface", "Structured YAML data layer", "Controlled sample data"]))

    st.markdown("### Screenshot / diagram")
    screenshot = project.get("screenshot")
    if screenshot:
        st.image(screenshot)
    else:
        render_empty_state("Screenshot coming soon. The workflow diagram above illustrates the core transformation.")

    st.write("")
    st.markdown("### Business value")
    st.markdown(project.get("business_value", ""))

    st.markdown("### Limitations")
    st.markdown(project.get("limitations", ""))

    st.markdown("### Stack")
    render_project_tags(project.get("stack", []))

    st.markdown("### Relevant roles")
    render_project_tags(project.get("relevant_roles", []))

    st.write("")
    st.link_button("Open repository", project.get("repository", "#"))
    demo_url = project.get("demo_url")
    if demo_url:
        st.link_button("Open live demo", demo_url)


def proof_page():
    render_page_heading(
        "Evidence over claims",
        "Proof of Work",
        "Each project connects a real problem, user decision, solution, artificial intelligence contribution, human judgment, limitation, and business value.",
    )

    selected_title = st.session_state.get("selected_project")
    selected_project = next(
        (project for project in projects if project.get("title") == selected_title),
        None,
    )

    if selected_project:
        render_project_detail(selected_project)
        return

    status_filter = st.selectbox(
        "Project status",
        ["All projects", "Flagship", "Supporting"],
    )

    all_stacks = sorted(
        {stack for project in projects for stack in project.get("stack", [])}
    )
    all_roles = sorted(
        {role for project in projects for role in project.get("relevant_roles", [])}
    )

    stack_filter = st.multiselect("Filter by stack", all_stacks)
    role_filter = st.multiselect("Filter by relevant role", all_roles)

    visible_projects = ordered_projects()

    if status_filter != "All projects":
        visible_projects = [
            project for project in visible_projects if project.get("status") == status_filter
        ]

    if stack_filter:
        visible_projects = [
            project
            for project in visible_projects
            if set(stack_filter).issubset(set(project.get("stack", [])))
        ]

    if role_filter:
        visible_projects = [
            project
            for project in visible_projects
            if set(role_filter).issubset(set(project.get("relevant_roles", [])))
        ]

    if not visible_projects:
        render_empty_state("No projects match these filters yet.")
        return

    st.write("")
    for index in range(0, len(visible_projects), 3):
        columns = st.columns(3)
        for column, project in zip(columns, visible_projects[index : index + 3]):
            with column:
                render_project_card(project)


def ledger_page():
    render_page_heading(
        "The search as evidence",
        "Application Ledger",
        "A transparent record of roles pursued, custom artifacts created for each opportunity, application status, outcomes, and reusable learning.",
    )

    active_statuses = ["Submitted", "Screening", "Interview"]
    total_applications = len(applications)
    active_applications = sum(
        1 for application in applications if application.get("status") in active_statuses
    )
    interview_applications = sum(
        1 for application in applications if application.get("status") == "Interview"
    )
    artifact_count = sum(
        1 for application in applications if application.get("artifact")
    )

    first, second, third, fourth = st.columns(4)

    with first:
        st.markdown(
            f"""
            <div class="metric-card">
              <div class="metric-value">{total_applications}</div>
              <div class="metric-label">Applications recorded</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with second:
        st.markdown(
            f"""
            <div class="metric-card">
              <div class="metric-value">{active_applications}</div>
              <div class="metric-label">Active applications</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with third:
        st.markdown(
            f"""
            <div class="metric-card">
              <div class="metric-value">{interview_applications}</div>
              <div class="metric-label">Interview stage</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with fourth:
        st.markdown(
            f"""
            <div class="metric-card">
              <div class="metric-value">{artifact_count}</div>
              <div class="metric-label">Custom artifacts created</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    status_filter = st.selectbox(
        "Filter by status",
        [
            "All statuses",
            "Researching",
            "Submitted",
            "Screening",
            "Interview",
            "Offer",
            "Rejected",
            "Withdrawn",
        ],
    )

    hide_companies = st.toggle("Hide company names", value=False)

    visible_applications = applications
    if status_filter != "All statuses":
        visible_applications = [
            application
            for application in visible_applications
            if application.get("status") == status_filter
        ]

    if not visible_applications:
        render_empty_state("No applications match this filter yet.")
    else:
        for application in visible_applications:
            company = application.get("company", "Company")
            if hide_companies:
                company = "Private company"

            example_label = "Representative example" if application.get("example_record") else "Application"

            with st.expander(f"{application.get('role', 'Role')} · {company}"):
                render_status_pill(f"{application.get('status', 'Not recorded')} · {example_label}")
                st.write("")
                st.markdown(f"**Applied on**\n\n{application.get('date', 'Not recorded')}")
                st.markdown(f"**Source**\n\n{application.get('source', 'Not recorded')}")
                st.markdown(f"**Custom artifact**\n\n{application.get('artifact', 'Not recorded')}")

                left, right = st.columns(2)
                with left:
                    st.markdown("**Artificial intelligence contribution**")
                    st.markdown(application.get("ai_contribution", ""))
                with right:
                    st.markdown("**Human contribution**")
                    st.markdown(application.get("human_contribution", ""))

                st.markdown(f"**Time invested**\n\n{application.get('time_invested', 'Not recorded')}")
                st.markdown(f"**Outcome**\n\n{application.get('outcome', 'Pending')}")
                st.markdown(f"**Learning**\n\n{application.get('learning', 'Not recorded')}")
                st.markdown(f"**Reuse potential**\n\n{application.get('reuse_potential', 'Not recorded')}")

                artifact_url = application.get("artifact_url")
                if artifact_url:
                    st.link_button("Open application artifact", artifact_url)

    st.write("")
    if applications:
        ledger_frame = pd.DataFrame(applications)
        export_buffer = io.StringIO()
        ledger_frame.to_csv(export_buffer, index=False)
        st.download_button(
            "Download application ledger as CSV",
            data=export_buffer.getvalue(),
            file_name="linkedout_application_ledger.csv",
            mime="text/csv",
        )


def capability_page():
    render_page_heading(
        "Skills with evidence",
        "Capability Map",
        "Every capability connects to projects, demonstrations, and application artifacts rather than self assigned ratings.",
    )

    evidence_filter = st.selectbox(
        "Filter by evidence strength",
        ["All evidence", "Production oriented", "Repeated", "Demonstrated"],
    )

    all_roles = sorted(
        {role for capability in capabilities for role in capability.get("relevant_roles", [])}
    )
    role_filter = st.multiselect("Filter by relevant role", all_roles)

    visible_capabilities = capabilities

    if evidence_filter != "All evidence":
        visible_capabilities = [
            capability
            for capability in visible_capabilities
            if capability.get("evidence_strength") == evidence_filter
        ]

    if role_filter:
        visible_capabilities = [
            capability
            for capability in visible_capabilities
            if set(role_filter).issubset(set(capability.get("relevant_roles", [])))
        ]

    if not visible_capabilities:
        render_empty_state("No capabilities match these filters yet.")
        return

    for capability in visible_capabilities:
        with st.expander(capability.get("name", "Capability")):
            render_status_pill(capability.get("evidence_strength", "Demonstrated"))
            st.write("")
            st.markdown("**Evidence**")

            evidence_names = capability.get("evidence", [])
            for evidence_name in evidence_names:
                related_project = next(
                    (project for project in projects if project.get("title") == evidence_name),
                    None,
                )
                if related_project:
                    if st.button(
                        f"View {evidence_name} case study",
                        key=f"capability_{capability.get('name', '').lower().replace(' ', '_')}_{evidence_name.lower().replace(' ', '_')}",
                    ):
                        st.session_state["selected_project"] = evidence_name
                        st.session_state["return_to_capability"] = True
                        st.rerun()
                else:
                    st.markdown(evidence_name)

            st.markdown("**Relevant roles**")
            render_project_tags(capability.get("relevant_roles", []))


def decisions_page():
    render_page_heading(
        "Judgment in the open",
        "Decision Records",
        "These records explain the choices behind each project, including alternatives considered, tradeoffs accepted, risks identified, and improvements planned.",
    )

    project_filter = st.selectbox(
        "Filter by project",
        ["All projects"] + sorted({decision.get("project", "") for decision in decisions}),
    )

    decision_type_filter = st.selectbox(
        "Filter by decision type",
        ["All decision types", "Architecture", "Product", "Data", "Governance", "Artificial intelligence"],
    )

    visible_decisions = decisions

    if project_filter != "All projects":
        visible_decisions = [
            decision
            for decision in visible_decisions
            if decision.get("project") == project_filter
        ]

    if decision_type_filter != "All decision types":
        visible_decisions = [
            decision
            for decision in visible_decisions
            if decision.get("type") == decision_type_filter
        ]

    if not visible_decisions:
        render_empty_state("No decision records match these filters yet.")
        return

    for decision in visible_decisions:
        with st.expander(f"{decision.get('project', 'Project')} · {decision.get('title', 'Decision')}"):
            render_status_pill(decision.get("type", "Decision"))
            st.write("")
            st.markdown(f"**Decision**\n\n{decision.get('decision', '')}")
            st.markdown("**Alternatives considered**")
            st.markdown(", ".join(decision.get("alternatives_considered", [])))
            st.markdown(f"**Tradeoff**\n\n{decision.get('tradeoff', '')}")
            st.markdown(f"**Risk**\n\n{decision.get('risk', '')}")
            st.markdown(f"**Artificial intelligence limitation**\n\n{decision.get('ai_limitation', '')}")
            st.markdown(f"**Next improvement**\n\n{decision.get('next_improvement', '')}")

            related_project = next(
                (project for project in projects if project.get("title") == decision.get("project")),
                None,
            )
            if related_project:
                if st.button(
                    f"View {decision.get('project')} case study",
                    key=f"decision_{decision.get('project', '').lower().replace(' ', '_')}_{decision.get('title', '').lower().replace(' ', '_')}",
                ):
                    st.session_state["selected_project"] = decision.get("project")
                    st.session_state["return_to_decisions"] = True
                    st.rerun()


def lab_page():
    render_page_heading(
        "Working demonstrations",
        "Live Lab",
        "Explore working applications through controlled demonstrations, sample data policies, and clear instructions.",
    )

    demo_projects = ["Traceboard", "Providence", "Signal Field", "Plus Slop Stopper"]
    selected_title = st.selectbox("Select a demonstration", demo_projects)
    selected_project = next(
        (project for project in projects if project.get("title") == selected_title),
        None,
    )

    if not selected_project:
        render_empty_state("No demonstration selected.")
        return

    st.write("")
    render_status_pill(selected_project.get("status", "Project"))
    st.markdown(f"## {selected_project.get('title', 'Project')}")
    st.markdown(selected_project.get("problem", ""))

    st.write("")
    left, right = st.columns(2)

    with left:
        st.markdown("### What to explore")
        st.markdown(selected_project.get("demo_instructions", "Use the interface to follow the core workflow and observe how the solution supports the user decision."))

    with right:
        st.markdown("### Sample data policy")
        st.markdown(selected_project.get("sample_data_policy", "This demonstration uses controlled sample data only. No confidential, personal, or production data is included."))

    st.write("")
    demo_url = selected_project.get("demo_url")
    if demo_url:
        st.link_button("Open live demo", demo_url)
    else:
        render_empty_state("Demo coming soon. This project currently has a repository and case study available.")

    if st.button(
        f"View {selected_project.get('title')} case study",
        key=f"lab_{selected_title.lower().replace(' ', '_')}",
    ):
        st.session_state["selected_project"] = selected_title
        st.session_state["return_to_lab"] = True
        st.rerun()

    st.link_button("Open repository", selected_project.get("repository", "#"))


def contact_page():
    render_page_heading(
        "Start a conversation",
        "Contact",
        "Use this page to discuss AI product work, operational tooling, design systems, workflow automation, or a specific opportunity.",
    )

    left, right = st.columns(2)

    with left:
        st.markdown("### Send a message")
        name = st.text_input("Your name")
        email = st.text_input("Your email")
        topic = st.selectbox(
            "What would you like to discuss?",
            [
                "AI product work",
                "Operational tooling",
                "Design systems",
                "Workflow automation",
                "A specific opportunity",
            ],
        )
        message = st.text_area("Message")

        if st.button("Send message"):
            if name and email and message:
                st.success("Thank you. Your message has been recorded for this demonstration.")
            else:
                st.warning("Please complete your name, email, and message.")

    with right:
        st.markdown("### Direct contact")
        st.link_button("Email me", "mailto:sylvester.career@gmail.com")
        st.link_button("GitHub profile", "https://github.com/FriesRdBest")

        brief = f"""LinkedOut Brief\n\n{profile.get('career_identity', '')}\n{profile.get('location', '')}\n\nFocus: {profile.get('current_focus', '')}\n\nEmail: sylvester.career@gmail.com\nGitHub: https://github.com/FriesRdBest\n"""
        st.download_button(
            "Download one-page LinkedOut brief",
            data=brief,
            file_name="linkedout_brief.txt",
            mime="text/plain",
        )

        st.markdown("### What I'm looking for")
        st.markdown(", ".join(profile.get("current_exploration", [])))

        st.markdown("### Role presets")
        preset1, preset2 = st.columns(2)
        with preset1:
            if st.button("AI Solutions"):
                st.info("Discussing AI Solutions Engineering.")
            if st.button("Product Ops"):
                st.info("Discussing Product Operations.")
        with preset2:
            if st.button("Design Systems"):
                st.info("Discussing Design Systems.")
            if st.button("Internal Tools"):
                st.info("Discussing Internal Tools.")

        st.markdown("### Response expectations")
        st.markdown("I aim to respond within 1-2 business days. For time sensitive opportunities, mention the timeline in your message.")


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

    default_index = 0
    if st.session_state.get("nav_override") in PAGES:
        default_index = list(PAGES.keys()).index(st.session_state["nav_override"])
        st.session_state["nav_override"] = None

    selected_page = st.radio(
        "Navigate",
        list(PAGES.keys()),
        index=default_index,
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
