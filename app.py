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

      /* Visual Elevation Reset — Phase 1
         Only: active sidebar block + remove Streamlit top chrome. */

      

      [data-testid="stToolbar"] {{
        display: none;
      }}

      

      .block-container {{
        padding-top: 2.5rem;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] {{
        gap: 0.25rem;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] label {{
        position: relative;
        display: flex;
        width: 100%;
        min-height: 2.75rem;
        margin: 0;
        padding: 0.72rem 0.85rem;
        border: 0;
        border-radius: 0;
        background: transparent;
        color: #93A4B5;
        font-size: 0.9rem;
        font-weight: 620;
        line-height: 1.2;
        transition: background 160ms ease, color 160ms ease;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] label div:first-child {{
        display: none;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] label p {{
        margin: 0;
        color: inherit;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {{
        background: rgba(55, 224, 200, 0.10);
        color: #E8EEF4;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {{
        background: #37E0C8;
        color: #070B10;
        font-weight: 780;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] p {{
        color: #070B10;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"]:hover {{
        background: #37E0C8;
        color: #070B10;
      }}

      @media (max-width: 767px) {{
        .block-container {{
          padding-top: 1.5rem;
        }}

        section[data-testid="stSidebar"] div[role="radiogroup"] label {{
          min-height: 2.6rem;
          padding: 0.68rem 0.75rem;
        }}
      }}
      .stApp {{
        background:
          radial-gradient(1100px 620px at 12% -8%, rgba(55, 224, 200, 0.10), transparent 60%),
          radial-gradient(900px 520px at 92% 4%, rgba(96, 140, 255, 0.08), transparent 62%),
          #070B10;
        color: #E8EEF4;
      }}

      .block-container {{
        padding: 2.5rem 3rem 4rem 3rem;
        max-width: 1280px;
      }}

      section[data-testid="stSidebar"] {{
        background: transparent;
        border-right: 0;
      }}

      section[data-testid="stSidebar"] > div {{
        background: transparent;
      }}

      section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {{
        padding-top: 0.35rem;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] {{
        gap: 0.15rem;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] label {{
        width: 100%;
        margin: 0;
        padding: 0.62rem 0.75rem;
        border: 0;
        border-radius: 0;
        background: transparent;
        color: #93A4B5;
        font-size: 0.9rem;
        font-weight: 560;
        transition: color 160ms ease, background 160ms ease;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {{
        background: transparent;
        color: #E8EEF4;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {{
        background: transparent;
        color: #37E0C8;
        font-weight: 760;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] p {{
        color: #37E0C8;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] label div:first-child {{
        display: none;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] label p {{
        margin: 0;
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
        padding: 2.5rem 2.75rem;
      }}

      .hero h1 {{
        font-size: 2.75rem;
        font-weight: 850;
        letter-spacing: -0.045em;
        line-height: 1.05;
        margin: 0 0 0.9rem 0;
      }}

      .hero p {{
        color: #B9C6D2;
        font-size: 1.05rem;
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
        padding: 1.4rem 1.5rem;
        height: 100%;
      }}

      .metric-value {{
        font-size: 2rem;
        font-weight: 800;
        letter-spacing: -0.03em;
      }}

      .metric-label {{
        color: {MUTED};
        font-size: 0.84rem;
        margin-top: 0.3rem;
        line-height: 1.4;
      }}

      .section-card {{
        background: {CARD};
        border: 1px solid {BORDER};
        border-radius: 18px;
        padding: 1.6rem 1.7rem;
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
        padding: 1.6rem 1.65rem;
        height: 100%;
        display: flex;
        flex-direction: column;
        gap: 0.8rem;
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
        font-size: 2.1rem;
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
        padding: 0.9rem 1.1rem;
        margin: 0.3rem 0;
        color: #C7D3DE;
        font-size: 0.9rem;
        line-height: 1.55;
      }}

      .workflow-arrow {{
        color: {PRIMARY};
        text-align: center;
        font-size: 1.1rem;
      }}

      .water-stage {{
        position: relative;
        overflow: hidden;
        isolation: isolate;
      }}

      .water-stage::before {{
        content: "";
        position: absolute;
        inset: auto -8% -8% -8%;
        height: var(--water-height, 44%);
        z-index: -1;
        pointer-events: none;
        opacity: 0.72;
        background:
          radial-gradient(70% 35% at 22% 0%, rgba(55, 224, 200, 0.16), transparent 74%),
          radial-gradient(65% 38% at 76% 18%, rgba(81, 160, 255, 0.10), transparent 72%),
          linear-gradient(
            180deg,
            rgba(55, 224, 200, 0.035) 0%,
            rgba(55, 224, 200, 0.085) 48%,
            rgba(55, 224, 200, 0.13) 100%
          );
        border-top: 1px solid rgba(55, 224, 200, 0.17);
        border-radius: 48% 52% 0 0 / 4% 4% 0 0;
        transform-origin: center bottom;
        animation: water-drift 15s ease-in-out infinite alternate;
      }}

      .water-stage::after {{
        content: "";
        position: absolute;
        left: -10%;
        bottom: calc(var(--water-height, 44%) - 0.15rem);
        width: 120%;
        height: 1.35rem;
        z-index: -1;
        pointer-events: none;
        opacity: 0.72;
        background:
          radial-gradient(
            ellipse at 12% 50%,
            transparent 0 46%,
            rgba(55, 224, 200, 0.2) 48% 50%,
            transparent 52%
          ) 0 0 / 7.5rem 1.15rem repeat-x;
        animation: water-ripple 11s linear infinite;
      }}

      @keyframes water-drift {{
        0% {{
          transform: translate3d(-1.5%, 0.35rem, 0) scaleX(1.01);
        }}
        100% {{
          transform: translate3d(1.5%, -0.2rem, 0) scaleX(1.04);
        }}
      }}

      @keyframes water-ripple {{
        from {{
          transform: translateX(0);
        }}
        to {{
          transform: translateX(-7.5rem);
        }}
      }}

      @media (prefers-reduced-motion: reduce) {{
        .water-stage::before,
        .water-stage::after {{
          animation: none;
        }}
      }}

      @media (max-width: 1279px) {{
        .block-container {{
          padding: 2rem 2.25rem 3.5rem 2.25rem;
        }}
        .hero {{ padding: 2.2rem 2.4rem; }}
        .hero h1 {{ font-size: 2.4rem; }}
      }}

      @media (max-width: 767px) {{
        .block-container {{
          padding: 1.5rem 1.1rem 3rem 1.1rem;
        }}
        .hero {{ padding: 1.6rem 1.4rem; border-radius: 18px; }}
        .hero h1 {{ font-size: 1.85rem; }}
        .hero p {{ font-size: 0.98rem; }}
        .page-heading {{ font-size: 1.55rem; }}
        .metric-card {{ padding: 1.15rem 1.2rem; }}
        .metric-value {{ font-size: 1.6rem; }}
        .section-card {{ padding: 1.3rem 1.3rem; }}
        .project-card {{ padding: 1.3rem 1.3rem; }}
      }}

      @media (max-width: 400px) {{
        .block-container {{
          padding: 1.1rem 0.75rem 2.5rem 0.75rem;
        }}
        .hero {{ padding: 1.3rem 1rem; }}
        .hero h1 {{ font-size: 1.6rem; }}
      }}

      /* Visual Elevation Phase 4: editorial content system */

      h1, h2, h3 {{
        color: #F2F6F8;
        letter-spacing: -0.03em;
      }}

      h2 {{
        margin-top: 2.7rem;
        margin-bottom: 0.9rem;
        font-size: clamp(1.35rem, 1.8vw, 1.75rem);
        font-weight: 760;
      }}

      h3 {{
        margin-top: 1.8rem;
        margin-bottom: 0.65rem;
        font-size: clamp(1.02rem, 1.3vw, 1.18rem);
        font-weight: 730;
      }}

      .page-heading {{
        max-width: 880px;
        font-size: clamp(2rem, 3.1vw, 3rem);
        line-height: 1.06;
        margin-bottom: 0.55rem;
      }}

      .page-intro {{
        max-width: 720px;
        color: #AEBCC7;
        font-size: 1rem;
        line-height: 1.72;
        margin-bottom: 2.25rem;
      }}

      .hero {{
        position: relative;
        box-shadow: 0 22px 80px rgba(0, 0, 0, 0.16);
      }}

      .hero::after {{
        content: "";
        position: absolute;
        left: 2.75rem;
        right: 2.75rem;
        bottom: -1px;
        height: 1px;
        background: linear-gradient(
          90deg,
          transparent,
          rgba(55, 224, 200, 0.56),
          transparent
        );
      }}

      .metric-card,
      .section-card,
      .project-card {{
        box-shadow: 0 12px 34px rgba(0, 0, 0, 0.12);
        transition:
          transform 180ms ease,
          border-color 180ms ease,
          background 180ms ease;
      }}

      .metric-card:hover,
      .section-card:hover,
      .project-card:hover {{
        transform: translateY(-2px);
        border-color: rgba(55, 224, 200, 0.32);
        background: linear-gradient(
          145deg,
          rgba(55, 224, 200, 0.055),
          #0E141B 65%
        );
      }}

      .metric-card {{
        min-height: 8.35rem;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
      }}

      .metric-value {{
        color: #F2F6F8;
      }}

      .section-card {{
        min-height: 9rem;
      }}

      .project-card {{
        min-height: 15rem;
      }}

      .project-card h3 {{
        margin-top: 0;
      }}

      .project-tags {{
        margin: 0.7rem 0 0.9rem;
      }}

      .project-tag {{
        border-color: rgba(147, 164, 181, 0.2);
        color: #D5DFE7;
      }}

      .stButton > button,
      .stDownloadButton > button,
      .stLinkButton > a {{
        min-height: 2.7rem;
        border-radius: 10px;
        border: 1px solid rgba(55, 224, 200, 0.38);
        background: rgba(55, 224, 200, 0.075);
        color: #E8EEF4;
        font-weight: 680;
        letter-spacing: -0.01em;
        transition:
          background 160ms ease,
          border-color 160ms ease,
          transform 160ms ease;
      }}

      .stButton > button:hover,
      .stDownloadButton > button:hover,
      .stLinkButton > a:hover {{
        background: rgba(55, 224, 200, 0.14);
        border-color: rgba(55, 224, 200, 0.72);
        transform: translateY(-1px);
        color: #FFFFFF;
      }}

      .stButton > button:focus-visible,
      .stDownloadButton > button:focus-visible,
      .stLinkButton > a:focus-visible,
      input:focus-visible,
      textarea:focus-visible {{
        outline: 2px solid #37E0C8 !important;
        outline-offset: 3px;
      }}

      [data-testid="stExpander"] {{
        border: 1px solid #1D2833;
        border-radius: 14px;
        background: rgba(14, 20, 27, 0.76);
        overflow: hidden;
        margin-bottom: 0.65rem;
      }}

      [data-testid="stExpander"]:hover {{
        border-color: rgba(55, 224, 200, 0.28);
      }}

      [data-testid="stExpander"] summary {{
        padding: 0.25rem 0.15rem;
        font-weight: 680;
        color: #E8EEF4;
      }}

      [data-testid="stExpanderDetails"] {{
        border-top: 1px solid rgba(147, 164, 181, 0.12);
        padding-top: 0.25rem;
      }}

      [data-testid="stSelectbox"],
      [data-testid="stMultiSelect"],
      [data-testid="stTextInput"],
      [data-testid="stTextArea"] {{
        margin-bottom: 0.75rem;
      }}

      [data-testid="stSelectbox"] label,
      [data-testid="stMultiSelect"] label,
      [data-testid="stTextInput"] label,
      [data-testid="stTextArea"] label {{
        color: #B8C5CF;
        font-size: 0.84rem;
        font-weight: 650;
      }}

      div[data-baseweb="select"] > div,
      [data-testid="stTextInput"] input,
      [data-testid="stTextArea"] textarea {{
        border-color: #273540 !important;
        background: rgba(14, 20, 27, 0.82) !important;
        border-radius: 10px !important;
        color: #E8EEF4 !important;
      }}

      .water-stage {{
        padding-bottom: 1.25rem;
      }}

      @media (max-width: 767px) {{
        h2 {{
          margin-top: 2.15rem;
        }}

        .page-intro {{
          margin-bottom: 1.65rem;
          font-size: 0.95rem;
        }}

        .hero::after {{
          left: 1.4rem;
          right: 1.4rem;
        }}

        .metric-card {{
          min-height: 7.25rem;
        }}

        .section-card,
        .project-card {{
          min-height: auto;
        }}

        [data-testid="stExpander"] {{
          border-radius: 12px;
        }}
      }}

      @media (prefers-reduced-motion: reduce) {{
        .metric-card,
        .section-card,
        .project-card,
        .stButton > button,
        .stDownloadButton > button,
        .stLinkButton > a {{
          transition: none;
        }}

        .metric-card:hover,
        .section-card:hover,
        .project-card:hover,
        .stButton > button:hover,
        .stDownloadButton > button:hover,
        .stLinkButton > a:hover {{
          transform: none;
        }}
      }}

      /* Visual Elevation Phase 5: final interface polish */

      html {{
        scroll-behavior: smooth;
      }}

      ::selection {{
        background: rgba(55, 224, 200, 0.28);
        color: #FFFFFF;
      }}

      .stApp {{
        min-height: 100vh;
      }}

      .block-container {{
        animation: linkedout-enter 340ms ease-out both;
      }}

      @keyframes linkedout-enter {{
        from {{
          opacity: 0;
          transform: translateY(5px);
        }}
        to {{
          opacity: 1;
          transform: translateY(0);
        }}
      }}

      section[data-testid="stSidebar"] {{
        scrollbar-width: thin;
        scrollbar-color: rgba(55, 224, 200, 0.28) transparent;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] label {{
        position: relative;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"]::before {{
        content: "";
        position: absolute;
        left: -0.38rem;
        top: 50%;
        width: 0.18rem;
        height: 1.15rem;
        border-radius: 999px;
        background: #37E0C8;
        box-shadow: 0 0 18px rgba(55, 224, 200, 0.46);
        transform: translateY(-50%);
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] label:hover::after {{
        content: "";
        position: absolute;
        right: 0.1rem;
        top: 50%;
        width: 0.28rem;
        height: 0.28rem;
        border-radius: 50%;
        background: rgba(55, 224, 200, 0.58);
        transform: translateY(-50%);
      }}

      .linkedout-brand {{
        padding-bottom: 0.8rem;
        border-bottom: 1px solid rgba(147, 164, 181, 0.12);
      }}

      .linkedout-subtitle {{
        max-width: 15.5rem;
      }}

      .status-pill {{
        box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.06);
      }}

      .workflow-box {{
        position: relative;
        overflow: hidden;
      }}

      .workflow-box::before {{
        content: "";
        position: absolute;
        left: 0;
        top: 0.8rem;
        bottom: 0.8rem;
        width: 2px;
        border-radius: 99px;
        background: linear-gradient(
          180deg,
          rgba(55, 224, 200, 0.72),
          rgba(55, 224, 200, 0.08)
        );
      }}

      .workflow-box {{
        padding-left: 1.25rem;
      }}

      [data-testid="stExpander"] summary {{
        transition: color 160ms ease;
      }}

      [data-testid="stExpander"]:hover summary {{
        color: #37E0C8;
      }}

      [data-testid="stDataFrame"] {{
        border: 1px solid #1D2833;
        border-radius: 14px;
        overflow: hidden;
      }}

      hr {{
        border-color: rgba(147, 164, 181, 0.14);
        margin: 2.1rem 0;
      }}

      @media (max-width: 767px) {{
        .block-container {{
          animation-duration: 240ms;
        }}

        section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"]::before {{
          left: -0.18rem;
        }}

        .linkedout-brand {{
          padding-bottom: 0.6rem;
        }}

        .workflow-box::before {{
          top: 0.65rem;
          bottom: 0.65rem;
        }}
      }}

      @media (prefers-reduced-motion: reduce) {{
        html {{
          scroll-behavior: auto;
        }}

        .block-container {{
          animation: none;
        }}

        [data-testid="stExpander"] summary {{
          transition: none;
        }}
      }}

      /* LinkedOut Ocean Palette v1 */

      .stApp {{
        color: #EDF8FA;
        background: linear-gradient(
          180deg,
          #174956 0%,
          #123C49 42%,
          #174955 76%,
          #37636A 93%,
          #B8AC8E 98%,
          #D9C9A7 100%
        ) !important;
        background-attachment: fixed !important;
        min-height: 100dvh;
      }}

      section[data-testid="stSidebar"],
      section[data-testid="stSidebar"] > div,
      section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {{
        background: transparent !important;
        border-right: none !important;
      }}

      .linkedout-brand,
      h1, h2, h3,
      .page-heading,
      .metric-value {{
        color: #F1FBFC !important;
      }}

      .linkedout-brand span,
      .eyebrow {{
        color: #37E0C8 !important;
      }}

      .linkedout-subtitle {{
        color: #C4DDE2 !important;
      }}

      .linkedout-brand {{
        border-bottom-color: rgba(196, 221, 226, 0.2) !important;
      }}

      .hero {{
        background: linear-gradient(
          135deg,
          rgba(44, 111, 122, 0.96),
          rgba(27, 75, 89, 0.96)
        ) !important;
        border-color: rgba(180, 223, 229, 0.3) !important;
        box-shadow: 0 16px 48px rgba(5, 33, 41, 0.18) !important;
      }}

      .hero p,
      .page-intro,
      .section-card p,
      .project-card p,
      .metric-label {{
        color: #D3E8EC !important;
      }}

      .metric-card,
      .section-card,
      .project-card {{
        background: #205563 !important;
        border-color: rgba(176, 217, 225, 0.28) !important;
        box-shadow: 0 10px 28px rgba(5, 33, 41, 0.14) !important;
      }}

      .metric-card:hover,
      .section-card:hover,
      .project-card:hover {{
        background: #286571 !important;
        border-color: rgba(55, 224, 200, 0.65) !important;
      }}

      .workflow-box,
      [data-testid="stExpander"],
      .empty-state {{
        background: #1E5361 !important;
        border-color: rgba(176, 217, 225, 0.3) !important;
        color: #D8ECEF !important;
      }}

      .project-tag {{
        background: rgba(214, 234, 236, 0.09) !important;
        border-color: rgba(196, 221, 226, 0.35) !important;
        color: #E3F1F3 !important;
      }}

      .status-pill {{
        background: rgba(55, 224, 200, 0.12) !important;
        border-color: rgba(55, 224, 200, 0.55) !important;
        color: #9CF4E5 !important;
      }}

      .stButton > button,
      .stDownloadButton > button,
      .stLinkButton > a {{
        background: #23616B !important;
        border-color: rgba(121, 225, 211, 0.6) !important;
        color: #F2FCFC !important;
        box-shadow: none !important;
      }}

      .stButton > button:hover,
      .stDownloadButton > button:hover,
      .stLinkButton > a:hover {{
        background: #37E0C8 !important;
        border-color: #37E0C8 !important;
        color: #082F36 !important;
      }}

      .stButton > button:hover p,
      .stDownloadButton > button:hover p,
      .stLinkButton > a:hover p {{
        color: #082F36 !important;
      }}

      [data-testid="stSelectbox"] label,
      [data-testid="stMultiSelect"] label,
      [data-testid="stTextInput"] label,
      [data-testid="stTextArea"] label {{
        color: #D3E8EC !important;
      }}

      div[data-baseweb="select"] > div,
      [data-testid="stTextInput"] input,
      [data-testid="stTextArea"] textarea {{
        background: #194B59 !important;
        border-color: #729DA6 !important;
        color: #EFF9FB !important;
      }}

      input::placeholder,
      textarea::placeholder {{
        color: #B8D2D8 !important;
        opacity: 1;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] label {{
        box-sizing: border-box;
        background: transparent !important;
        color: #CEE5E9 !important;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] label p {{
        color: inherit !important;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {{
        background: rgba(55, 224, 200, 0.12) !important;
        color: #FFFFFF !important;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked),
      section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {{
        background: #37E0C8 !important;
        color: #082F36 !important;
        border-radius: 0 !important;
        font-weight: 780 !important;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p,
      section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] p {{
        color: #082F36 !important;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] label::before,
      section[data-testid="stSidebar"] div[role="radiogroup"] label::after {{
        display: none !important;
      }}

      section[data-testid="stSidebar"] div[role="radiogroup"] label:focus-within {{
        outline: 2px solid #F0DFBC;
        outline-offset: 3px;
      }}

      hr {{
        border-color: rgba(196, 221, 226, 0.25) !important;
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
          <div class="eyebrow">Robin Sylvester's Proof of work career application</div>
          <h1>Linked<span class="hero-brand-out">Out</span></h1>
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
    live_demos = sum(1 for p in projects if p.get("demo_url"))
    artifact_count = sum(1 for a in applications if a.get("artifact"))

    flagship_count = sum(
        1 for project in projects if project.get("status") == "Flagship"
    )

    st.markdown(
        f"""
        <div class="signal-metrics-grid">
            <div class="signal-metric-card">
                <div class="signal-metric-value">
                    {metrics.get('public_repositories', len(projects))}
                </div>
                <div class="signal-metric-label">Public repositories</div>
            </div>
            <div class="signal-metric-card">
                <div class="signal-metric-value">{flagship_count}</div>
                <div class="signal-metric-label">Flagship case studies</div>
            </div>
            <div class="signal-metric-card">
                <div class="signal-metric-value">{live_demos}</div>
                <div class="signal-metric-label">Live demos</div>
            </div>
            <div class="signal-metric-card">
                <div class="signal-metric-value">{artifact_count}</div>
                <div class="signal-metric-label">Application artifacts</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    st.markdown("### Primary actions")
    st.markdown('<div class="primary-actions-row">', unsafe_allow_html=True)

    b1, b2, b3 = st.columns(3, gap="large")

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

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    st.markdown("### Current focus")
    st.markdown(profile.get("current_focus", ""))

    st.markdown("### Work eligibility")
    st.markdown(profile.get("work_eligibility", "Authorized to work in the United States."))

    st.markdown("### Primary skills")
    skills = profile.get("primary_skills", [])

    preferred_skill_order = [
        "Python",
        "Streamlit",
        "SQL",
        "Power BI",
        "Workflow automation",
        "AI product prototyping",
        "Design Governance",
        "Data quality",
        "Product operations",
        "Accessibility",
    ]

    skill_lookup = {
        skill.casefold(): skill
        for skill in skills
    }

    ordered_skills = [
        skill_lookup[name.casefold()]
        for name in preferred_skill_order
        if name.casefold() in skill_lookup
    ]

    ordered_skills.extend(
        skill
        for skill in skills
        if skill.casefold() not in {
            item.casefold()
            for item in ordered_skills
        }
    )

    skill_layout = [
        [0, 1, 2],
        [3, None, 4],
        [5, None, 6],
        [7, 8, 9],
    ]

    for row in skill_layout:
        columns = st.columns(3, gap="large")

        for column, skill_index in zip(columns, row):
            if skill_index is None or skill_index >= len(ordered_skills):
                continue

            with column:
                skill = ordered_skills[skill_index]
                st.markdown(
                    f'<div class="primary-skill-card"><h3>{skill}</h3></div>',
                    unsafe_allow_html=True,
                )

    for skill in ordered_skills[10:]:
        st.markdown(
            f'<div class="primary-skill-card"><h3>{skill}</h3></div>',
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

    filters_active = (
        evidence_filter != "All evidence" or bool(role_filter)
    )

    if not filters_active and len(visible_capabilities) == 10:
        capability_rows = [
            visible_capabilities[0:3],
            visible_capabilities[3:5],
            visible_capabilities[5:7],
            visible_capabilities[7:10],
        ]
    else:
        capability_rows = [
            visible_capabilities[index:index + 3]
            for index in range(0, len(visible_capabilities), 3)
        ]

    for row_index, capability_row in enumerate(capability_rows):
        columns = st.columns(len(capability_row), gap="large")

        for column, capability in zip(columns, capability_row):
            with column:
                with st.expander(capability.get("name", "Capability")):
                    render_status_pill(
                        capability.get("evidence_strength", "Demonstrated")
                    )
                    st.write("")
                    st.markdown("**Evidence**")

                    evidence_names = capability.get("evidence", [])

                    for evidence_name in evidence_names:
                        related_project = next(
                            (
                                project
                                for project in projects
                                if project.get("title") == evidence_name
                            ),
                            None,
                        )

                        if related_project:
                            capability_key = capability.get(
                                "name", ""
                            ).lower().replace(" ", "_")
                            evidence_key = evidence_name.lower().replace(
                                " ", "_"
                            )

                            if st.button(
                                f"View {evidence_name} case study",
                                key=f"capability_{capability_key}_{evidence_key}",
                            ):
                                st.session_state["selected_project"] = (
                                    evidence_name
                                )
                                st.session_state["return_to_capability"] = True
                                st.rerun()
                        else:
                            st.markdown(evidence_name)

                    st.markdown("**Relevant roles**")
                    render_project_tags(
                        capability.get("relevant_roles", [])
                    )


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

water_levels = {
    "Signal": "44%",
    "Operating Model": "38%",
    "Proof of Work": "31%",
    "Application Ledger": "25%",
    "Capability Map": "19%",
    "Decision Records": "14%",
    "Live Lab": "9%",
    "Contact": "4%",
}

st.markdown(
    f'<div class="water-stage" style="--water-height: {water_levels[selected_page]};">',
    unsafe_allow_html=True,
)

# LinkedOut Shore Journey v3
# Fixed coastal canvas; horizon lowers as the selected page progresses.

shore_horizons = {
    "Signal": 34,
    "Operating Model": 41,
    "Proof of Work": 48,
    "Application Ledger": 55,
    "Capability Map": 62,
    "Decision Records": 69,
    "Live Lab": 76,
    "Contact": 83,
}

shore_css = """
<style>
/* Replace earlier background and water experiments. */
.stApp {
    --shore-horizon: HORIZON_VALUE%;
    min-height: 100dvh;
    color: #01232d !important;
    background:
        radial-gradient(
            ellipse at 86% 0%,
            rgba(255,255,255,0.94) 0%,
            rgba(255,255,255,0.35) 12%,
            transparent 34%
        ),
        linear-gradient(
            to bottom,
            #139fdd 0%,
            #64d3f4 calc(var(--shore-horizon) - 10%),
            #b8edfa var(--shore-horizon),
            #168dc8 calc(var(--shore-horizon) + 0.3%),
            #0876b7 calc(var(--shore-horizon) + 7%),
            #24a9df 85%,
            #75d4ec 91%,
            #f8e8c9 94%,
            #ead1a5 100%
        ) !important;
    background-attachment: fixed !important;
    background-size: 100% 100dvh !important;
}

/* Clear old negative-layer backgrounds and empty-wrapper waves. */
.stApp::before,
.stApp::after,
.water-stage::before,
.water-stage::after {
    content: none !important;
    display: none !important;
}

.water-stage {
    padding: 0 !important;
}

/* Shoreline remains at the bottom, regardless of page length. */
[data-testid="stAppViewContainer"] {
    background: transparent !important;
    isolation: isolate;
}

[data-testid="stAppViewContainer"]::before {
    content: "";
    position: fixed;
    left: -5%;
    width: 110%;
    bottom: 6vh;
    height: 3.5vh;
    min-height: 18px;
    z-index: 0;
    pointer-events: none;
    background:
        radial-gradient(
            ellipse at 50% 100%,
            rgba(255,255,255,0.95) 0 45%,
            transparent 48%
        ) 0 0 / 100px 24px repeat-x,
        linear-gradient(
            to bottom,
            transparent,
            rgba(255,255,255,0.85) 65%,
            rgba(255,255,255,0.4)
        );
    animation: shore-foam 14s ease-in-out infinite alternate;
}

[data-testid="stAppViewContainer"]::after {
    content: "";
    position: fixed;
    left: 0;
    right: 0;
    bottom: 0;
    height: 6.5vh;
    z-index: 0;
    pointer-events: none;
    background:
        repeating-linear-gradient(
            173deg,
            transparent 0 16px,
            rgba(255,250,235,0.28) 18px,
            transparent 24px 46px
        ),
        linear-gradient(180deg, #fae9cb, #e8cda1);
}

/* Keep actual application content above the decorative shore. */
section[data-testid="stMain"] {
    position: relative;
    z-index: 1;
}

section[data-testid="stMain"] {
    background: transparent !important;
}

section[data-testid="stSidebar"],
section[data-testid="stSidebar"] > div,
section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {
    background: transparent !important;
    border-right: 0 !important;
}

[data-testid="stToolbar"] {
    display: none !important;
}

/* Light, readable surfaces rather than dark ocean dashboard panels. */
.hero,
.metric-card,
.section-card,
.project-card,
.workflow-box,
.empty-state,
[data-testid="stExpander"] {
    background: rgba(248,253,255,0.94) !important;
    border: 1px solid rgba(255,255,255,0.8) !important;
    box-shadow: 0 8px 28px rgba(1,35,45,0.12) !important;
    color: #01232d !important;
}

.hero:hover,
.metric-card:hover,
.section-card:hover,
.project-card:hover {
    background: #f8fdff !important;
    border-color: #b5e3f2 !important;
}

.hero::after,
.workflow-box::before {
    display: none !important;
}

h1, h2, h3,
.page-heading,
.metric-value,
.linkedout-brand {
    color: #01232d !important;
}

.hero p,
.page-intro,
.metric-label,
.section-card p,
.project-card p,
.linkedout-subtitle,
.empty-state {
    color: #234957 !important;
}

.linkedout-brand span,
.eyebrow,
.workflow-arrow {
    color: #006a94 !important;
}

[data-testid="stMarkdownContainer"] {
    color: #01232d !important;
}

.linkedout-brand {
    border-bottom-color: rgba(1,35,45,0.18) !important;
}

.project-tag,
.status-pill {
    background: #e0f3fa !important;
    color: #01232d !important;
    border-color: #9bcbdc !important;
}

.stButton > button,
.stDownloadButton > button,
.stLinkButton > a {
    background: #01232d !important;
    color: #ffffff !important;
    border-color: #01232d !important;
}

.stButton > button p,
.stDownloadButton > button p,
.stLinkButton > a p {
    color: #ffffff !important;
}

.stButton > button:hover,
.stDownloadButton > button:hover,
.stLinkButton > a:hover {
    background: #07536b !important;
    color: #ffffff !important;
    border-color: #07536b !important;
}

.stButton > button:hover p,
.stDownloadButton > button:hover p,
.stLinkButton > a:hover p {
    color: #ffffff !important;
}

[data-testid="stSelectbox"] label,
[data-testid="stMultiSelect"] label,
[data-testid="stTextInput"] label,
[data-testid="stTextArea"] label {
    color: #01232d !important;
}

div[data-baseweb="select"] > div,
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea {
    background: #f8fdff !important;
    color: #01232d !important;
    border-color: #7daebe !important;
}

input::placeholder,
textarea::placeholder {
    color: #526f79 !important;
}

[data-testid="stExpander"] summary,
[data-testid="stExpander"]:hover summary {
    color: #01232d !important;
}

/* Uniform full-width navigation, not label-width rectangles. */
section[data-testid="stSidebar"] [data-testid="stRadio"],
section[data-testid="stSidebar"] div[role="radiogroup"] {
    width: 100% !important;
}

section[data-testid="stSidebar"] div[role="radiogroup"] {
    display: flex !important;
    flex-direction: column !important;
    align-items: stretch !important;
    gap: 5px !important;
}

section[data-testid="stSidebar"] div[role="radiogroup"] > div {
    width: 100% !important;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label {
    display: flex !important;
    align-items: center !important;
    align-self: stretch !important;
    box-sizing: border-box !important;
    width: 100% !important;
    max-width: none !important;
    min-height: 44px;
    margin: 0 !important;
    padding: 12px 14px !important;
    border: none !important;
    border-radius: 0 !important;
    background: transparent !important;
    color: #01232d !important;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label p {
    color: #01232d !important;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background: rgba(255,255,255,0.32) !important;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked),
section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {
    background: #01232d !important;
    color: #ffffff !important;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p,
section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] p {
    color: #ffffff !important;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label::before,
section[data-testid="stSidebar"] div[role="radiogroup"] label::after {
    display: none !important;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label:focus-within {
    outline: 2px solid #01232d;
    outline-offset: 2px;
}

@keyframes shore-foam {
    from { transform: translate3d(-12px, 0, 0); opacity: 0.8; }
    to { transform: translate3d(12px, -4px, 0); opacity: 1; }
}

@media (prefers-reduced-motion: reduce) {
    [data-testid="stAppViewContainer"]::before {
        animation: none !important;
    }
}
</style>
"""

shore_css = shore_css.replace(
    "HORIZON_VALUE", str(shore_horizons.get(selected_page, 34))
)
st.markdown(shore_css, unsafe_allow_html=True)


# LinkedOut Coastal Content Refinement v4

coastal_content_css = """
<style>
/* Hero: the primary white editorial surface. */
.hero {
    position: relative !important;
    overflow: hidden !important;
    padding: clamp(2rem, 4vw, 3.4rem) !important;
    border-radius: 24px !important;
    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.97) 0%,
            rgba(244,252,255,0.93) 62%,
            rgba(226,246,252,0.90) 100%
        ) !important;
    border: 1px solid rgba(255,255,255,0.92) !important;
    box-shadow:
        0 20px 50px rgba(1,35,45,0.15),
        inset 0 1px 0 rgba(255,255,255,0.92) !important;
}

.hero::before {
    content: "";
    position: absolute;
    right: -8%;
    bottom: -44%;
    width: min(34rem, 55vw);
    height: min(34rem, 55vw);
    border-radius: 50%;
    pointer-events: none;
    background:
        radial-gradient(
            circle,
            rgba(32,180,226,0.20) 0%,
            rgba(32,180,226,0.08) 36%,
            transparent 68%
        );
}

.hero > * {
    position: relative;
    z-index: 1;
}

.hero h1 {
    max-width: 11ch;
    font-size: clamp(2.55rem, 5.3vw, 4.65rem) !important;
    line-height: 0.98 !important;
    font-weight: 830 !important;
    color: #01232d !important;
    letter-spacing: -0.06em !important;
}

.hero p {
    max-width: 47rem !important;
    margin-top: 1.25rem !important;
    color: #234957 !important;
    font-size: clamp(1rem, 1.25vw, 1.14rem) !important;
    line-height: 1.72 !important;
}

.hero .eyebrow {
    color: #006a94 !important;
    font-weight: 800 !important;
    letter-spacing: 0.16em !important;
}

/* Stronger editorial hierarchy. */
.page-heading {
    max-width: 58rem !important;
    color: #01232d !important;
    font-size: clamp(2.2rem, 4vw, 3.75rem) !important;
    font-weight: 830 !important;
    line-height: 1.02 !important;
    letter-spacing: -0.055em !important;
}

.page-intro {
    max-width: 45rem !important;
    color: #234957 !important;
    font-size: clamp(1rem, 1.25vw, 1.12rem) !important;
    line-height: 1.72 !important;
    margin-bottom: 2.35rem !important;
}

h2 {
    color: #01232d !important;
    font-size: clamp(1.6rem, 2.4vw, 2.15rem) !important;
    font-weight: 790 !important;
    letter-spacing: -0.04em !important;
    margin-top: 3rem !important;
    margin-bottom: 1rem !important;
}

h3 {
    color: #01232d !important;
    font-weight: 760 !important;
    letter-spacing: -0.025em !important;
}

/* Cards: bright and consistent, with restrained depth. */
.metric-card,
.section-card,
.project-card {
    position: relative !important;
    overflow: hidden !important;
    border-radius: 18px !important;
    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.96),
            rgba(241,251,255,0.91)
        ) !important;
    border: 1px solid rgba(255,255,255,0.93) !important;
    box-shadow:
        0 10px 26px rgba(1,35,45,0.12),
        inset 0 1px 0 rgba(255,255,255,0.92) !important;
    transition:
        transform 180ms ease,
        box-shadow 180ms ease,
        border-color 180ms ease !important;
}

.metric-card::before,
.section-card::before,
.project-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 1.3rem;
    right: 1.3rem;
    height: 3px;
    border-radius: 0 0 999px 999px;
    background: linear-gradient(
        90deg,
        #0a88c5,
        #54c9ea,
        #0a88c5
    );
    opacity: 0.78;
}

.metric-card:hover,
.section-card:hover,
.project-card:hover {
    transform: translateY(-4px) !important;
    border-color: rgba(70,178,215,0.65) !important;
    box-shadow:
        0 18px 36px rgba(1,35,45,0.16),
        inset 0 1px 0 rgba(255,255,255,0.96) !important;
}

.metric-card {
    min-height: 9.25rem !important;
    padding: 1.55rem !important;
}

.metric-value {
    color: #01232d !important;
    font-size: clamp(2rem, 3vw, 2.8rem) !important;
    font-weight: 820 !important;
    letter-spacing: -0.05em !important;
}

.metric-label {
    color: #3d6675 !important;
    font-size: 0.85rem !important;
    font-weight: 650 !important;
    line-height: 1.45 !important;
}

.section-card {
    min-height: 9.5rem !important;
    padding: 1.6rem !important;
}

.section-card h3,
.project-card h3 {
    color: #01232d !important;
}

.section-card p,
.project-card p {
    color: #365d6c !important;
}

.project-card {
    min-height: 16rem !important;
    padding: 1.65rem !important;
}

.project-card .eyebrow {
    color: #006a94 !important;
}

/* Pills, tags, and workflow surfaces. */
.status-pill {
    background: #dff5fb !important;
    border-color: #a4d9e8 !important;
    color: #01232d !important;
    font-weight: 750 !important;
}

.project-tag {
    background: #edf9fc !important;
    border-color: #b4dfe9 !important;
    color: #164a5b !important;
    font-weight: 650 !important;
}

.workflow-box {
    border-radius: 14px !important;
    background: rgba(248,253,255,0.93) !important;
    border: 1px solid rgba(255,255,255,0.9) !important;
    color: #234957 !important;
    box-shadow: 0 8px 18px rgba(1,35,45,0.09) !important;
}

.workflow-box::before {
    display: block !important;
    background: linear-gradient(#1ca5d7, #07536b) !important;
}

.workflow-arrow {
    color: #07536b !important;
    font-weight: 800 !important;
}

/* Streamlit expander surfaces. */
[data-testid="stExpander"] {
    background: rgba(249,254,255,0.94) !important;
    border: 1px solid rgba(255,255,255,0.92) !important;
    border-radius: 16px !important;
    box-shadow: 0 8px 20px rgba(1,35,45,0.09) !important;
    overflow: hidden !important;
}

[data-testid="stExpander"]:hover {
    border-color: rgba(70,178,215,0.65) !important;
}

[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary p,
[data-testid="stExpander"] [data-testid="stMarkdownContainer"] {
    color: #01232d !important;
    font-weight: 720 !important;
}

[data-testid="stExpanderDetails"] {
    border-top: 1px solid rgba(7,83,107,0.12) !important;
}

/* Controls and forms. */
.stButton > button,
.stDownloadButton > button,
.stLinkButton > a {
    min-height: 2.85rem !important;
    border-radius: 10px !important;
    background: #01232d !important;
    border: 1px solid #01232d !important;
    color: #ffffff !important;
    font-weight: 720 !important;
    letter-spacing: -0.01em !important;
    box-shadow: 0 5px 12px rgba(1,35,45,0.14) !important;
    transition:
        transform 160ms ease,
        background 160ms ease,
        box-shadow 160ms ease !important;
}

.stButton > button:hover,
.stDownloadButton > button:hover,
.stLinkButton > a:hover {
    transform: translateY(-2px) !important;
    background: #07536b !important;
    border-color: #07536b !important;
    box-shadow: 0 9px 18px rgba(1,35,45,0.18) !important;
}

.stButton > button p,
.stDownloadButton > button p,
.stLinkButton > a p,
.stButton > button:hover p,
.stDownloadButton > button:hover p,
.stLinkButton > a:hover p {
    color: #ffffff !important;
}

[data-testid="stSelectbox"] label,
[data-testid="stMultiSelect"] label,
[data-testid="stTextInput"] label,
[data-testid="stTextArea"] label {
    color: #01232d !important;
    font-weight: 720 !important;
}

div[data-baseweb="select"] > div,
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea {
    border-radius: 10px !important;
    background: rgba(249,254,255,0.94) !important;
    border-color: #99cada !important;
    color: #01232d !important;
    box-shadow: 0 3px 10px rgba(1,35,45,0.06) !important;
}

[data-testid="stSelectbox"] [data-baseweb="select"] > div:hover,
[data-testid="stTextInput"] input:hover,
[data-testid="stTextArea"] textarea:hover {
    border-color: #3aa6cb !important;
}

[data-testid="stSelectbox"] [data-baseweb="select"] > div:focus-within,
[data-testid="stTextInput"] input:focus,
[data-testid="stTextArea"] textarea:focus {
    border-color: #006a94 !important;
    box-shadow: 0 0 0 3px rgba(84,201,234,0.25) !important;
}

/* More breathable desktop and mobile rhythm. */
.block-container {
    padding-bottom: max(8rem, 14vh) !important;
}

@media (max-width: 767px) {
    .hero {
        padding: 1.65rem !important;
        border-radius: 18px !important;
    }

    .hero h1 {
        font-size: clamp(2.35rem, 12vw, 3.15rem) !important;
    }

    .hero::before {
        width: 17rem;
        height: 17rem;
        right: -42%;
        bottom: -58%;
    }

    .page-heading {
        font-size: clamp(2rem, 10vw, 2.85rem) !important;
    }

    .metric-card,
    .section-card,
    .project-card {
        min-height: auto !important;
        padding: 1.3rem !important;
    }

    .metric-card::before,
    .section-card::before,
    .project-card::before {
        left: 1rem;
        right: 1rem;
    }

    h2 {
        margin-top: 2.3rem !important;
    }
}

@media (prefers-reduced-motion: reduce) {
    .metric-card,
    .section-card,
    .project-card,
    .stButton > button,
    .stDownloadButton > button,
    .stLinkButton > a {
        transition: none !important;
    }

    .metric-card:hover,
    .section-card:hover,
    .project-card:hover,
    .stButton > button:hover,
    .stDownloadButton > button:hover,
    .stLinkButton > a:hover {
        transform: none !important;
    }
}
</style>
"""

st.markdown(coastal_content_css, unsafe_allow_html=True)


# LinkedOut Coastal Responsive Polish v5

coastal_responsive_css = """
<style>
/* Keep content comfortably contained across viewports. */
.block-container {
    width: min(100%, 1280px) !important;
    margin-inline: auto !important;
}

/* Clear focus states for keyboard navigation. */
*:focus-visible {
    outline: 3px solid #07536b !important;
    outline-offset: 3px !important;
}

.stButton > button:focus-visible,
.stDownloadButton > button:focus-visible,
.stLinkButton > a:focus-visible,
section[data-testid="stSidebar"] div[role="radiogroup"] label:focus-within {
    outline: 3px solid #ffffff !important;
    outline-offset: 3px !important;
}

/* Touch targets remain comfortably tappable. */
.stButton > button,
.stDownloadButton > button,
.stLinkButton > a,
section[data-testid="stSidebar"] div[role="radiogroup"] label {
    min-height: 44px !important;
}

/* Prevent long content from spilling outside cards or controls. */
.hero,
.metric-card,
.section-card,
.project-card,
.workflow-box,
[data-testid="stExpander"],
.empty-state,
.page-intro,
.metric-label,
.project-card p,
.section-card p {
    overflow-wrap: anywhere !important;
    word-break: normal !important;
}

/* Prevent filters and inputs from exceeding narrow containers. */
[data-testid="stSelectbox"],
[data-testid="stMultiSelect"],
[data-testid="stTextInput"],
[data-testid="stTextArea"],
div[data-baseweb="select"],
div[data-baseweb="select"] > div {
    min-width: 0 !important;
}

/* Keep scrollbars subtle and consistent with the coastal palette. */
* {
    scrollbar-width: thin;
    scrollbar-color: rgba(1,35,45,0.42) rgba(255,255,255,0.18);
}

::-webkit-scrollbar {
    width: 9px;
    height: 9px;
}

::-webkit-scrollbar-track {
    background: rgba(255,255,255,0.14);
}

::-webkit-scrollbar-thumb {
    background: rgba(1,35,45,0.42);
    border: 2px solid rgba(255,255,255,0.14);
    border-radius: 999px;
}

/* Tablet. */
@media (max-width: 1024px) {
    .block-container {
        padding-left: clamp(1.25rem, 3vw, 2rem) !important;
        padding-right: clamp(1.25rem, 3vw, 2rem) !important;
    }

    .page-intro {
        max-width: 42rem !important;
    }

    .metric-card {
        min-height: 8.25rem !important;
    }

    .project-card {
        min-height: 14rem !important;
    }

    section[data-testid="stSidebar"] div[role="radiogroup"] label {
        padding-left: 0.85rem !important;
        padding-right: 0.85rem !important;
    }
}

/* Mobile. */
@media (max-width: 767px) {
    .block-container {
        padding:
            1.2rem
            max(1rem, env(safe-area-inset-right))
            max(7rem, calc(6rem + env(safe-area-inset-bottom)))
            max(1rem, env(safe-area-inset-left)) !important;
    }

    .page-heading {
        margin-top: 0.2rem !important;
    }

    .page-intro {
        margin-bottom: 1.55rem !important;
    }

    .eyebrow {
        letter-spacing: 0.13em !important;
        font-size: 0.68rem !important;
    }

    .metric-card,
    .section-card,
    .project-card,
    .workflow-box,
    [data-testid="stExpander"] {
        border-radius: 14px !important;
    }

    .metric-card,
    .section-card,
    .project-card {
        width: 100% !important;
    }

    .metric-label {
        font-size: 0.82rem !important;
    }

    .project-tags {
        gap: 0.35rem !important;
    }

    .project-tag {
        max-width: 100%;
        overflow-wrap: anywhere !important;
    }

    .stButton > button,
    .stDownloadButton > button,
    .stLinkButton > a {
        min-height: 46px !important;
        font-size: 0.94rem !important;
    }

    section[data-testid="stSidebar"] div[role="radiogroup"] label {
        min-height: 46px !important;
        padding: 0.78rem 0.9rem !important;
    }

    [data-testid="stExpander"] summary {
        min-height: 44px !important;
        display: flex !important;
        align-items: center !important;
    }

    /* Foam and sand remain visible without claiming too much phone space. */
    [data-testid="stAppViewContainer"]::before {
        bottom: 4.7vh !important;
        height: 2.6vh !important;
        min-height: 14px !important;
        opacity: 0.88 !important;
    }

    [data-testid="stAppViewContainer"]::after {
        height: 5vh !important;
    }
}

/* Small phones, including 375 px width. */
@media (max-width: 400px) {
    .block-container {
        padding-left: 0.82rem !important;
        padding-right: 0.82rem !important;
    }

    .hero,
    .metric-card,
    .section-card,
    .project-card {
        padding-left: 1.05rem !important;
        padding-right: 1.05rem !important;
    }

    .hero h1 {
        letter-spacing: -0.065em !important;
    }

    .page-heading {
        letter-spacing: -0.06em !important;
    }

    .project-tag {
        font-size: 0.68rem !important;
        padding: 0.2rem 0.48rem !important;
    }
}

/* Large screens remain readable rather than excessively wide. */
@media (min-width: 1440px) {
    .block-container {
        max-width: 1320px !important;
    }

    .hero p {
        max-width: 49rem !important;
    }
}

/* Respect reduced-motion preferences. */
@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        scroll-behavior: auto !important;
        transition-duration: 0.01ms !important;
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
    }
}
</style>
"""

st.markdown(coastal_responsive_css, unsafe_allow_html=True)


# LinkedOut Coastal Motion & Spacing v6

coastal_motion_spacing_css = """
<style>
/* Give card layouts more air without changing their visual language. */
[data-testid="stHorizontalBlock"] {
    gap: clamp(1.1rem, 2vw, 1.7rem) !important;
}

.metric-card,
.section-card,
.project-card,
.workflow-box {
    margin-bottom: clamp(1.1rem, 2vw, 1.7rem) !important;
}

.metric-card,
.section-card,
.project-card {
    transition:
        transform 220ms cubic-bezier(0.22, 0.61, 0.36, 1),
        box-shadow 220ms ease,
        border-color 220ms ease !important;
}

/* Animate the shoreline foam as a slow, repeating tide. */
[data-testid="stAppViewContainer"]::before {
    animation: coastal-tide 18s ease-in-out infinite !important;
    will-change: transform, opacity;
}

@keyframes coastal-tide {
    0% {
        transform: translate3d(-18px, 0, 0) scaleX(1);
        opacity: 0.72;
    }

    25% {
        transform: translate3d(6px, -3px, 0) scaleX(1.03);
        opacity: 0.9;
    }

    50% {
        transform: translate3d(20px, -1px, 0) scaleX(1);
        opacity: 1;
    }

    75% {
        transform: translate3d(-4px, 2px, 0) scaleX(0.98);
        opacity: 0.82;
    }

    100% {
        transform: translate3d(-18px, 0, 0) scaleX(1);
        opacity: 0.72;
    }
}

/* Add a second, softer foam layer for depth. */
[data-testid="stAppViewContainer"]::after {
    animation: coastal-tide-secondary 26s ease-in-out infinite !important;
    will-change: transform;
}

@keyframes coastal-tide-secondary {
    0% {
        transform: translate3d(14px, 0, 0);
    }

    50% {
        transform: translate3d(-16px, -2px, 0);
    }

    100% {
        transform: translate3d(14px, 0, 0);
    }
}

/* Keep the motion subtle and accessible. */
@media (prefers-reduced-motion: reduce) {
    [data-testid="stAppViewContainer"]::before,
    [data-testid="stAppViewContainer"]::after {
        animation: none !important;
        transform: none !important;
    }
}
</style>
"""

st.markdown(coastal_motion_spacing_css, unsafe_allow_html=True)


# LinkedOut Primary Skills Layout v7

primary_skills_css = """
<style>
/* Compact, equal-width cards reserved for the Signal page skill inventory. */
.primary-skill-card {
    min-height: 0 !important;
    margin: 0 !important;
    padding: 1.05rem 1.2rem !important;
    border-radius: 15px !important;
    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.96),
            rgba(241,251,255,0.91)
        ) !important;
    border: 1px solid rgba(255,255,255,0.93) !important;
    box-shadow:
        0 8px 20px rgba(1,35,45,0.10),
        inset 0 1px 0 rgba(255,255,255,0.92) !important;
    transition:
        transform 180ms ease,
        box-shadow 180ms ease,
        border-color 180ms ease !important;
}

.primary-skill-card::before {
    content: "";
    display: block;
    height: 3px;
    margin: -1.05rem 0 0.9rem !important;
    border-radius: 0 0 999px 999px;
    background: linear-gradient(90deg, #0a88c5, #54c9ea, #0a88c5);
    opacity: 0.78;
}

.primary-skill-card h3 {
    margin: 0 !important;
    color: #01232d !important;
    font-size: clamp(1rem, 1.15vw, 1.12rem) !important;
    font-weight: 760 !important;
    line-height: 1.25 !important;
    letter-spacing: -0.025em !important;
}

.primary-skill-card:hover {
    transform: translateY(-3px) !important;
    border-color: rgba(70,178,215,0.65) !important;
    box-shadow:
        0 14px 28px rgba(1,35,45,0.14),
        inset 0 1px 0 rgba(255,255,255,0.96) !important;
}

@media (max-width: 767px) {
    .primary-skill-card {
        padding: 0.95rem 1rem !important;
    }

    .primary-skill-card::before {
        margin-top: -0.95rem !important;
        margin-bottom: 0.78rem !important;
    }
}

@media (prefers-reduced-motion: reduce) {
    .primary-skill-card,
    .primary-skill-card:hover {
        transform: none !important;
        transition: none !important;
    }
}
</style>
"""

st.markdown(primary_skills_css, unsafe_allow_html=True)


# LinkedOut Final Sharing Polish v8

final_sharing_css = """
<style>
/* Add breathing room without changing the established skill alignment. */
.primary-skill-card {
    padding: 1.2rem 1.3rem !important;
    margin: 0 0 1rem !important;
}

.primary-skill-card::before {
    margin: -1.2rem 0 1rem !important;
}

/* A dedicated grid avoids changing Streamlit columns on other pages. */
.signal-metrics-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: clamp(1rem, 1.8vw, 1.5rem);
    margin: 0.5rem 0 1.25rem;
}

.signal-metric-card {
    box-sizing: border-box;
    min-width: 0;
    padding: 1.4rem 1.2rem;
    border-radius: 18px;
    background: linear-gradient(
        145deg,
        rgba(255,255,255,0.96),
        rgba(241,251,255,0.91)
    );
    border: 1px solid rgba(255,255,255,0.93);
    box-shadow:
        0 10px 26px rgba(1,35,45,0.12),
        inset 0 1px 0 rgba(255,255,255,0.92);
    color: #01232d;
}

.signal-metric-value {
    color: #01232d;
    font-size: clamp(2rem, 3vw, 2.8rem);
    font-weight: 820;
    line-height: 1.15;
    letter-spacing: -0.05em;
}

.signal-metric-label {
    margin-top: 0.55rem;
    color: #3d6675;
    font-size: 0.85rem;
    font-weight: 650;
    line-height: 1.45;
    overflow-wrap: anywhere;
}

@media (max-width: 767px) {
    .signal-metrics-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 1rem;
    }

    .signal-metric-card {
        padding: 1.15rem 1rem;
    }

    .primary-skill-card {
        padding: 1.1rem 1rem !important;
        margin-bottom: 1rem !important;
    }

    .primary-skill-card::before {
        margin: -1.1rem 0 0.9rem !important;
    }
}
</style>
"""

st.markdown(final_sharing_css, unsafe_allow_html=True)


# LinkedOut Final Brand and Actions v9

final_brand_actions_css = """
<style>
/* Match the sidebar logo accent in the Signal hero title. */
.hero-brand-out {
    color: #006a94 !important;
}

/* Make the three Signal actions a true equal-width row. */
.primary-actions-row {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: clamp(0.85rem, 1.5vw, 1.25rem);
    width: 100%;
}

.primary-actions-row .stButton,
.primary-actions-row .stButton > button {
    width: 100% !important;
}

@media (max-width: 767px) {
    .primary-actions-row {
        grid-template-columns: 1fr;
        gap: 0.75rem;
    }
}
</style>
"""

st.markdown(final_brand_actions_css, unsafe_allow_html=True)

PAGES[selected_page]()
st.markdown("</div>", unsafe_allow_html=True)


# LinkedOut Native Navigation Visibility v11
st.markdown(
    """
    <style>
    /* Keep the native header and toolbar available for navigation. */
    .stApp > header,
    header[data-testid="stHeader"] {
        display: flex !important;
        visibility: visible !important;
        opacity: 1 !important;
        background: transparent !important;
        background-color: transparent !important;
        box-shadow: none !important;
        color: #01232d !important;
    }

    [data-testid="stToolbar"] {
        display: flex !important;
        visibility: visible !important;
        opacity: 1 !important;
        color: #01232d !important;
    }

    /* Make the collapsed-sidebar control visible and tappable. */
    [data-testid="stSidebarCollapsedControl"],
    [data-testid="collapsedControl"] {
        display: flex !important;
        visibility: visible !important;
        opacity: 1 !important;
        pointer-events: auto !important;
        color: #01232d !important;
        background: rgba(248,253,255,0.96) !important;
        border-radius: 10px !important;
    }

    [data-testid="stSidebarCollapsedControl"] button,
    [data-testid="collapsedControl"] button,
    [data-testid="stSidebarCollapseButton"] button,
    header[data-testid="stHeader"] button {
        min-width: 44px !important;
        min-height: 44px !important;
        color: #01232d !important;
        background: rgba(248,253,255,0.96) !important;
        border-radius: 10px !important;
        opacity: 1 !important;
        visibility: visible !important;
        pointer-events: auto !important;
    }

    header[data-testid="stHeader"] svg,
    [data-testid="stSidebarCollapsedControl"] svg,
    [data-testid="collapsedControl"] svg {
        color: #01232d !important;
        fill: currentColor !important;
    }

    @media (max-width: 767px) {
        .block-container {
            padding-top: 3.8rem !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# LinkedOut Sidebar Control Colors v12
st.markdown(
    """
    <style>
    /* Change only the sidebar expand/collapse controls. */
    .stApp [data-testid="stSidebarCollapsedControl"],
    .stApp [data-testid="collapsedControl"],
    .stApp [data-testid="stSidebarCollapsedControl"] button,
    .stApp [data-testid="collapsedControl"] button,
    .stApp [data-testid="stSidebarCollapseButton"] button,
    .stApp button[aria-label="Expand sidebar"],
    .stApp button[aria-label="Collapse sidebar"] {
        background: #000000 !important;
        color: #54c9ea !important;
        border: 1px solid #54c9ea !important;
        border-radius: 10px !important;
        box-shadow: none !important;
    }

    .stApp [data-testid="stSidebarCollapsedControl"] svg,
    .stApp [data-testid="collapsedControl"] svg,
    .stApp [data-testid="stSidebarCollapseButton"] button svg,
    .stApp button[aria-label="Expand sidebar"] svg,
    .stApp button[aria-label="Collapse sidebar"] svg {
        color: #54c9ea !important;
        fill: currentColor !important;
    }

    /* Cover Streamlit versions that render icons as text spans. */
    .stApp [data-testid="stSidebarCollapsedControl"] button span,
    .stApp [data-testid="collapsedControl"] button span,
    .stApp [data-testid="stSidebarCollapseButton"] button span,
    .stApp button[aria-label="Expand sidebar"] span,
    .stApp button[aria-label="Collapse sidebar"] span {
        color: #54c9ea !important;
    }

    .stApp [data-testid="stSidebarCollapsedControl"] button:hover,
    .stApp [data-testid="collapsedControl"] button:hover,
    .stApp [data-testid="stSidebarCollapseButton"] button:hover,
    .stApp button[aria-label="Expand sidebar"]:hover,
    .stApp button[aria-label="Collapse sidebar"]:hover {
        background: #01232d !important;
        color: #54c9ea !important;
    }

    .stApp [data-testid="stSidebarCollapsedControl"] button:focus-visible,
    .stApp [data-testid="collapsedControl"] button:focus-visible,
    .stApp [data-testid="stSidebarCollapseButton"] button:focus-visible,
    .stApp button[aria-label="Expand sidebar"]:focus-visible,
    .stApp button[aria-label="Collapse sidebar"]:focus-visible {
        outline: 2px solid #54c9ea !important;
        outline-offset: 3px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# LinkedOut Unified Sidebar Labels v13
st.markdown(
    """
    <style>
    /* Prevent the collapsed-control wrapper from showing a white block. */
    .stApp [data-testid="stSidebarCollapsedControl"],
    .stApp [data-testid="collapsedControl"] {
        background: #000000 !important;
        color: #54c9ea !important;
        border-radius: 10px !important;
    }

    /* Include both wrapper-based and directly-rendered native buttons. */
    .stApp :is(
        button[data-testid="stExpandSidebarButton"],
        button[data-testid="stSidebarCollapsedControl"],
        [data-testid="stSidebarCollapsedControl"] button,
        [data-testid="collapsedControl"] button,
        [data-testid="stSidebarCollapseButton"] button,
        button[data-testid="stSidebarCollapseButton"],
        [data-testid="stSidebarHeader"] button,
        button[aria-label="Expand sidebar"],
        button[aria-label="Collapse sidebar"]
    ) {
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: auto !important;
        min-width: 100px !important;
        min-height: 44px !important;
        padding: 0.55rem 0.85rem !important;
        background: #000000 !important;
        color: #54c9ea !important;
        border: 1px solid #54c9ea !important;
        border-radius: 10px !important;
        box-shadow: none !important;
        opacity: 1 !important;
        visibility: visible !important;
        pointer-events: auto !important;
        font-size: 0.95rem !important;
        font-weight: 750 !important;
        line-height: 1.2 !important;
        white-space: nowrap !important;
    }

    /* Replace the visual icon, not the native button or its click handler. */
    .stApp :is(
        button[data-testid="stExpandSidebarButton"],
        button[data-testid="stSidebarCollapsedControl"],
        [data-testid="stSidebarCollapsedControl"] button,
        [data-testid="collapsedControl"] button,
        [data-testid="stSidebarCollapseButton"] button,
        button[data-testid="stSidebarCollapseButton"],
        [data-testid="stSidebarHeader"] button,
        button[aria-label="Expand sidebar"],
        button[aria-label="Collapse sidebar"]
    ) > * {
        display: none !important;
    }

    .stApp :is(
        button[data-testid="stExpandSidebarButton"],
        button[data-testid="stSidebarCollapsedControl"],
        [data-testid="stSidebarCollapsedControl"] button,
        [data-testid="collapsedControl"] button,
        button[aria-label="Expand sidebar"]
    )::before {
        content: "Tabs >>" !important;
        display: inline-block !important;
        color: #54c9ea !important;
        pointer-events: none;
    }

    .stApp :is(
        [data-testid="stSidebarCollapseButton"] button,
        button[data-testid="stSidebarCollapseButton"],
        [data-testid="stSidebarHeader"] button,
        button[aria-label="Collapse sidebar"]
    )::before {
        content: "Hide <<" !important;
        display: inline-block !important;
        color: #54c9ea !important;
        pointer-events: none;
    }

    .stApp :is(
        button[data-testid="stExpandSidebarButton"],
        button[data-testid="stSidebarCollapsedControl"],
        [data-testid="stSidebarCollapsedControl"] button,
        [data-testid="collapsedControl"] button,
        [data-testid="stSidebarCollapseButton"] button,
        button[data-testid="stSidebarCollapseButton"],
        [data-testid="stSidebarHeader"] button,
        button[aria-label="Expand sidebar"],
        button[aria-label="Collapse sidebar"]
    ):hover {
        background: #01232d !important;
        color: #54c9ea !important;
    }

    .stApp :is(
        button[data-testid="stExpandSidebarButton"],
        button[data-testid="stSidebarCollapsedControl"],
        [data-testid="stSidebarCollapsedControl"] button,
        [data-testid="collapsedControl"] button,
        [data-testid="stSidebarCollapseButton"] button,
        button[data-testid="stSidebarCollapseButton"],
        [data-testid="stSidebarHeader"] button,
        button[aria-label="Expand sidebar"],
        button[aria-label="Collapse sidebar"]
    ):focus-visible {
        outline: 2px solid #54c9ea !important;
        outline-offset: 3px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# LinkedOut Expanded Header Contrast v14
st.markdown(
    """
    <style>
    /* Open expanders only: black title bar, white title and arrow.
       Leave collapsed headers and expanded content unchanged. */
    .stApp [data-testid="stExpander"] details[open] > summary,
    .stApp details[data-testid="stExpander"][open] > summary,
    .stApp [data-testid="stExpander"] summary[aria-expanded="true"] {
        background: #000000 !important;
        color: #ffffff !important;
    }

    /* Override existing dark text rules within the open title bar. */
    .stApp [data-testid="stExpander"] details[open] > summary *,
    .stApp details[data-testid="stExpander"][open] > summary *,
    .stApp [data-testid="stExpander"] summary[aria-expanded="true"] * {
        color: #ffffff !important;
    }

    /* Keep SVG arrows readable alongside the white title. */
    .stApp [data-testid="stExpander"] details[open] > summary svg,
    .stApp details[data-testid="stExpander"][open] > summary svg,
    .stApp [data-testid="stExpander"] summary[aria-expanded="true"] svg {
        color: #ffffff !important;
        fill: currentColor !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
