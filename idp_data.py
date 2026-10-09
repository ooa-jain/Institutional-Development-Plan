"""
Central content model for the Institutional Development Plan (IDP) site.

Holds the leadership (committee) rosters and descriptive metadata for every
Enabler (A-I), plus a loader for the short-term strategic goals extracted
from the IDP Goals workbook. Only SHORT-TERM goals are tracked site-wide —
mid-term and long-term horizons have been retired from the plan.
"""
import json
import os

_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
_GOALS_PATH = os.path.join(_BASE_DIR, "data", "idp_goals.json")

with open(_GOALS_PATH, encoding="utf-8") as _f:
    GOALS = json.load(_f)

ENABLER_ORDER = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

ENDPOINTS = {
    "a": "enablersA",
    "b": "enablersb",
    "c": "enablersc",
    "d": "enablersd",
    "e": "enablerse",
    "f": "enablersf",
    "g": "enablersg",
    "h": "enablersh",
    "i": "enablersi",
}

LEADERSHIP = {
    "a": [
        ("Dr. Easwaran Iyer, Advisor, Chancellor's Advisory Board", "Chairperson"),
        ("Dr. Asha Rajiv, Director, IQAC", "Convenor"),
        ("Mr. Ravindra Bhandary, Vice President, JGI", "Advisor"),
        ("Dr. J. Letha, Pro Vice-Chancellor", "Member"),
        ("Ms. Aparna Prasad, Director, Office of Communications and Human Resources", "Member"),
        ("Mr. M.S. Parswanath, Director, Projects and Facilities, JGI", "Member"),
    ],
    "b": [
        ("Mr. Ravindra Bhandary, Vice President, JGI", "Chairperson"),
        ("Mr. M.S. Santhosh, Joint Registrar", "Convenor"),
        ("Dr. N V H Krishnan, Advisor, Chancellor's Advisory Board", "Member"),
        ("Ms. Aparna Prasad, Director, Office of Communications and Human Resources", "Member"),
        ("Mr. M.S. Parswanath, Director, Projects and Facilities, JGI", "Member"),
    ],
    "c": [
        ("Dr. Shradha Kanwar, Chief Academic Officer", "Chairperson"),
        ("Dr. S Kiran, Deputy Dean, Academics", "Convenor"),
        ("Dr. Sridhara Murthi K R, Advisor, Chancellor's Advisory Board", "Member"),
        ("Dr. Srividya Shivakumar, Director, School of Allied Healthcare and Sciences", "Member"),
        ("Dr. Sagar Gulati, Director, School of CS and IT", "Member"),
        ("Dr. Simmy Kurian, Deputy Director, CMS B-School, Off-Campus, Kochi", "Member"),
        ("Dr. Neelima M, Deputy Director (In-Charge), School of Commerce", "Member"),
        ("Dr. Beemkumar N, Professor, Mechanical Engineering, FET", "Member"),
    ],
    "d": [
        ("Dr. Varalakshmi K N, Director Research (Sciences), CRPAS, JAIN (Deemed-to-be University)", "Chairperson"),
        ("Dr. Jitendra K Mishra, Vice Chancellor (In Charge) and Registrar", "Convenor"),
        ("Dr. Manav Saxena, Head, CREI", "Member"),
        ("Dr. Geetha Balakrishna, Director, Centre for Nano and Materials Science (CNMS)", "Member"),
        ("Dr. Chetan Nag K S, Deputy Director, Centre for Urban Ecology, Bio-Diversity, Evolution and Climate Change (CUBEC)", "Member"),
        ("Dr. Simmy Kurian, Deputy Director, CMS B-School, Off-Campus, Kochi", "Member"),
        ("Dr. Mahavir Kurkuri, Associate Director and Professor, Centre for Research in Functional Materials (CRFM)", "Member"),
        ("Dr. Beem Kumar, Professor, Mechanical Engineering, FET", "Member"),
    ],
    "e": [
        ("Ms. Aparna Prasad, Director, Office of Communications and Human Resources", "Chairperson"),
        ("Ms. Roopa, Head, Human Resources", "Convenor"),
        ("Dr. Asha Rajiv, Director of IQAC, School of Sciences", "Member"),
        ("Dr. Shradha Kanwar, Chief Academic Officer", "Member"),
    ],
    "f": [
        ("Dr. Easwaran Iyer, Advisor, Chancellor's Advisory Board", "Chairperson"),
        ("Ms. Preeti Bhandary, Chief Manager, Placements and Corporate Relations", "Convenor"),
        ("Mr. M.S. Santhosh, Joint Registrar", "Member"),
        ("Dr. Deepak Sinha, Deputy Director, FET", "Member"),
        ("Dr. Krishna Koppa, Deputy Director, CMS B-School", "Member"),
    ],
    "g": [
        ("Mr. Ravindra Bhandary, Vice President, JGI", "Chairperson"),
        ("Dr. N V H Krishnan, Advisor, Chancellor's Advisory Board", "Convenor"),
        ("Mr. M.S. Parswanath, Director, Projects and Facilities, JGI", "Member"),
        ("Mr. Vishal C, Director, Strategy and Development, JGI", "Member"),
        ("Dr. Neelima M, Deputy Director (In-Charge), School of Commerce", "Member"),
        ("Dr. J. Letha, Pro Vice-Chancellor", "Member"),
    ],
    "h": [
        ("Prof. N S Manjunath, Controller of Examinations", "Chairperson"),
        ("Dr. S Kiran, Deputy Dean, Academics", "Convenor"),
        ("Dr. Felix M. Philip, Deputy Director, School of Computer Science and IT, Off-Campus, Kochi", "Member"),
        ("Dr. Sangeeta Devanathan, Deputy Dean, Academics", "Member"),
        ("Dr. Sagar Gulati, Director, School of Computer Science and Information Technology", "Member"),
        ("Mr. TSM Kumar, Director, IT", "Member"),
    ],
    "i": [
        ("Mr. Nayaz Ahmed, CEO, JAIN Incubation", "Chairperson"),
        ("Asst. Prof. Anila Bajpai, Area Chair - Entrepreneurship", "Convenor"),
        ("Dr. Sagar Gulati, Director, School of Computer Science and Information Technology", "Member"),
        ("Dr. Bhaskar Dixit, Director, Fire and Combustion Research Center, Jain University (FCRC)", "Member"),
        ("Dr. Krishna Koppa, Deputy Director, CMS B-School", "Member"),
    ],
}

META = {
    "a": {
        "key": "a",
        "title": "Enabler A – Governance Enabler",
        "short_name": "Governance",
        "vision": "A transparent, accountable, and digitally empowered governance structure that ensures strategic leadership, regulatory compliance, and participatory decision-making across the institution.",
        "outcome": "Institutional readiness, transparency, inclusivity, and participatory governance.",
        "image": "ea.png",
        "icon": "fa-landmark",
    },
    "b": {
        "key": "b",
        "title": "Enabler B – Financial Strategy and Funding Models Enabler",
        "short_name": "Financial Sustainability",
        "vision": "A financially resilient and diversified funding ecosystem that ensures sustained institutional growth, surplus generation, and strategic reinvestment in academic and research excellence.",
        "outcome": "Diversified revenue streams, financial resilience, and sustainable reinvestment capacity.",
        "image": "eb.png",
        "icon": "fa-sack-dollar",
    },
    "c": {
        "key": "c",
        "title": "Enabler C – Academic Innovation and Excellence Enabler",
        "short_name": "Academic Innovation",
        "vision": "A future-ready academic ecosystem that ensures flexible, technology-integrated learning, enhanced skill development, strong industry alignment, and measurable student success in national and global opportunities.",
        "outcome": "Future-ready graduates, stronger industry alignment, and measurable learning outcomes.",
        "image": "ec.png",
        "icon": "fa-graduation-cap",
    },
    "d": {
        "key": "d",
        "title": "Enabler D – Research and Intellectual Property Enabler",
        "short_name": "Research & IP",
        "vision": "A robust research and innovation culture that drives high-impact publications, increased IP generation, strong industry collaboration, and multidisciplinary solutions aligned with national and global priorities.",
        "outcome": "Enhanced research capacity, international collaborations, and impactful innovation outcomes.",
        "image": "ed.png",
        "icon": "fa-flask",
    },
    "e": {
        "key": "e",
        "title": "Enabler E – Human Resources and Supportive–Facilitative Enabler",
        "short_name": "Human Resources",
        "vision": "A people-first ecosystem that empowers faculty, staff, and students through inclusive support systems, continuous skill development, digital enablement, and holistic well-being for sustained institutional excellence.",
        "outcome": "Improved student success, staff capacity, and an inclusive campus culture aligned with global opportunities.",
        "image": "ee.png",
        "icon": "fa-people-group",
    },
    "f": {
        "key": "f",
        "title": "Enabler F – Networking and Collaborations Enabler",
        "short_name": "Networking & Collaboration",
        "vision": "A globally connected collaboration ecosystem that strengthens academic excellence, drives innovation with industry and communities, and expands opportunities for students and faculty through robust alumni, national, and international partnerships.",
        "outcome": "Enhanced external engagement, stronger alumni networks, and impactful community partnerships.",
        "image": "ef.png",
        "icon": "fa-diagram-project",
    },
    "g": {
        "key": "g",
        "title": "Enabler G – Physical Enabler – Facilitative Enabler",
        "short_name": "Physical Infrastructure",
        "vision": "A sustainable, technology-enabled and future-ready campus infrastructure that enhances learning, research, safety, and student living while supporting institutional growth and global competitiveness.",
        "outcome": "Improved campus resilience, safer student living, and digitally-enabled learning environments.",
        "image": "eg.png",
        "icon": "fa-building-columns",
    },
    "h": {
        "key": "h",
        "title": "Enabler H – Digital Transformation Enabler",
        "short_name": "Digital Transformation",
        "vision": "A unified, secure and AI-enabled digital ecosystem that enhances learning experiences, streamlines governance, drives data-based decisions, and ensures seamless connectivity across academic and administrative functions.",
        "outcome": "Efficient administration, improved learning outcomes, and resilient digital operations.",
        "image": "eh.png",
        "icon": "fa-network-wired",
    },
    "i": {
        "key": "i",
        "title": "Enabler I – Entrepreneurship Enabler",
        "short_name": "Entrepreneurship",
        "vision": "A thriving entrepreneurial ecosystem that nurtures student and faculty innovation, accelerates venture creation, and embeds startup thinking across academic, research, and institutional pathways.",
        "outcome": "A self-sustaining startup pipeline, stronger industry-academia venture linkages, and an institution-wide entrepreneurial culture.",
        "image": None,
        "icon": "fa-rocket",
    },
}


def get_enabler_context(key):
    """Assemble the full render context for one Enabler page."""
    key = key.lower()
    goals = GOALS[key]
    total_goals = sum(len(v) for v in goals.values())
    total_focus = len(goals)

    idx = ENABLER_ORDER.index(key)
    prev_key = ENABLER_ORDER[idx - 1] if idx > 0 else ENABLER_ORDER[-1]
    next_key = ENABLER_ORDER[(idx + 1) % len(ENABLER_ORDER)]

    return {
        "meta": META[key],
        "goals": goals,
        "leadership": LEADERSHIP[key],
        "total_goals": total_goals,
        "total_focus": total_focus,
        "enabler_order": ENABLER_ORDER,
        "all_meta": META,
        "endpoints": ENDPOINTS,
        "prev_meta": META[prev_key],
        "next_meta": META[next_key],
        "prev_endpoint": ENDPOINTS[prev_key],
        "next_endpoint": ENDPOINTS[next_key],
    }
