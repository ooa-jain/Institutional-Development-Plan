from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

import idp_data

app = Flask(__name__, template_folder="templates")
CORS(app)

# Configurations
app.config["UPLOAD_FOLDER"] = "uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# -------------------------------
# ROUTES
# -------------------------------

PRINCIPAL_COMMITTEE = [
    ("Dr. Chenraj Roychand", "Chancellor", "Chairperson"),
    ("Dr. N. Sundararajan", "Pro Chancellor", "Vice Chairperson"),
    ("Dr. Jitendra Kumar Mishra", "Vice Chancellor (In Charge) and Registrar", "Member"),
    ("Dr. Shradha Kanwar", "Chief Academic Officer", "Member"),
]


def _enabler_summaries():
    """Per-Enabler focus-area / goal counts, in canonical A–I order."""
    summaries = []
    total_goals = 0
    total_focus = 0
    for key in idp_data.ENABLER_ORDER:
        goals = idp_data.GOALS[key]
        n_focus = len(goals)
        n_goals = sum(len(v) for v in goals.values())
        total_focus += n_focus
        total_goals += n_goals
        summaries.append({
            "meta": idp_data.META[key],
            "endpoint": idp_data.ENDPOINTS[key],
            "n_focus": n_focus,
            "n_goals": n_goals,
            "sample_focus": list(goals.keys())[:3],
        })
    return summaries, total_focus, total_goals


def _dashboard_context():
    summaries, total_focus, total_goals = _enabler_summaries()
    return dict(
        sections=[],
        active_nav="home",
        summaries=summaries,
        total_focus=total_focus,
        total_goals=total_goals,
        total_enablers=len(idp_data.ENABLER_ORDER),
        principal_committee=PRINCIPAL_COMMITTEE,
    )


@app.route("/")
def dashboard():
    return render_template("dashboard.html", **_dashboard_context())

@app.route("/section/<section_id>")
def view_section(section_id):
    return render_template("dashboard.html", **_dashboard_context())

def _render_enabler(key):
    ctx = idp_data.get_enabler_context(key)
    ctx["active_nav"] = "enablers"
    return render_template("enabler_page.html", **ctx)

@app.route("/enablers")
def enablers():
    return render_template(
        "enablers.html",
        leadership=idp_data.LEADERSHIP,
        all_meta=idp_data.META,
        enabler_order=idp_data.ENABLER_ORDER,
        endpoints=idp_data.ENDPOINTS,
        principal_committee=PRINCIPAL_COMMITTEE,
        active_nav="committees",
    )

@app.route("/enablersA")
def enablersA(): return _render_enabler("a")

@app.route("/enablersb")
def enablersb(): return _render_enabler("b")

@app.route("/enablersc")
def enablersc(): return _render_enabler("c")

@app.route("/enablersd")
def enablersd(): return _render_enabler("d")

@app.route("/enablerse")
def enablerse(): return _render_enabler("e")

@app.route("/enablersf")
def enablersf(): return _render_enabler("f")

@app.route("/enablersg")
def enablersg(): return _render_enabler("g")

@app.route("/enablersh")
def enablersh(): return _render_enabler("h")

@app.route("/enablersi")
def enablersi(): return _render_enabler("i")

@app.route("/overview")
def overview():
    summaries, total_focus, total_goals = _enabler_summaries()
    return render_template(
        "overview.html",
        summaries=summaries,
        total_goals=total_goals,
        total_focus=total_focus,
        total_enablers=len(idp_data.ENABLER_ORDER),
        active_nav="overview",
    )

@app.route("/index")
def index(): return render_template("index.html")

@app.route("/Roadmap")
def Roadmap(): return render_template("Roadmap.html", active_nav="roadmap")

# -------------------------------
# Dummy API (Optional)
# -------------------------------

@app.route("/api/sections", methods=["GET"])
def get_sections():
    return jsonify([])

@app.route("/uploads/<filename>")
def serve_pdf(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

# -------------------------------
# For Local Development
# -------------------------------

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
