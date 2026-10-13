import streamlit as st

st.set_page_config(
    page_title="LinkedOut",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded",
)

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

      .coming-soon {{
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


def render_coming_soon(message):
    st.markdown(f'<div class="coming-soon">{message}</div>', unsafe_allow_html=True)


def signal_page():
    st.markdown(
        """
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
            """
            <div class="metric-card">
              <div class="metric-value">8</div>
              <div class="metric-label">Public repositories audited for this portfolio</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with middle:
        st.markdown(
            """
            <div class="metric-card">
              <div class="metric-value">4</div>
              <div class="metric-label">Flagship case studies planned for deep presentation</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right:
        st.markdown(
            """
            <div class="metric-card">
              <div class="metric-value">8</div>
              <div class="metric-label">Career sections designed around evidence and decisions</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    st.markdown("### Current focus")
    st.markdown(
        """
        Building AI enabled operational products that make work measurable, usable, and governable.

        The current focus includes Python, Streamlit, workflow automation, design governance,
        data quality, product operations, and proof of work applications.
        """
    )

    st.markdown("### Primary capabilities")
    capability_columns = st.columns(3)
    capabilities = [
        "Python and Streamlit",
        "Workflow automation",
        "AI product prototyping",
        "Design governance",
        "Data quality",
        "Operational dashboards",
    ]

    for column, capability in zip(capability_columns, capabilities):
        with column:
            st.markdown(
                f'<div class="section-card"><h3>{capability}</h3></div>',
                unsafe_allow_html=True,
            )

    st.write("")
    st.markdown(
        '<div class="status-pill">Phase 1 foundation complete</div>',
        unsafe_allow_html=True,
    )


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
        "This section will present repositories as complete case studies. Each case study will explain the problem, user decision, architecture, artificial intelligence contribution, human judgment, limitations, and business value.",
    )
    render_coming_soon("Proof of Work arrives in Phase 4.")


def ledger_page():
    render_page_heading(
        "The search as evidence",
        "Application Ledger",
        "This section will record roles pursued, custom artifacts created for each opportunity, application status, outcomes, and reusable learning.",
    )
    render_coming_soon("Application Ledger arrives in Phase 5.")


def capability_page():
    render_page_heading(
        "Skills with evidence",
        "Capability Map",
        "This section will connect every capability to repositories, demonstrations, screenshots, and application artifacts rather than self assigned ratings.",
    )
    render_coming_soon("Capability Map arrives in Phase 7.")


def decisions_page():
    render_page_heading(
        "Judgment in the open",
        "Decision Records",
        "This section will explain the choices behind each project, including alternatives considered, tradeoffs accepted, risks identified, and improvements planned.",
    )
    render_coming_soon("Decision Records arrive in Phase 8.")


def lab_page():
    render_page_heading(
        "Working demonstrations",
        "Live Lab",
        "This section will provide direct access to interactive demonstrations, sample data policies, and clear instructions for exploring each application.",
    )
    render_coming_soon("Live Lab arrives in Phase 9.")


def contact_page():
    render_page_heading(
        "Start a conversation",
        "Contact",
        "This section will provide a direct route to discuss AI product work, operational tooling, design systems, workflow automation, or a specific opportunity.",
    )
    render_coming_soon("Contact experience arrives in Phase 10.")


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
        """
        <div class="linkedout-subtitle">
          Built with Python and Streamlit.<br>
          Designed for evidence first career presentation.
        </div>
        """,
        unsafe_allow_html=True,
    )

PAGES[selected_page]()
