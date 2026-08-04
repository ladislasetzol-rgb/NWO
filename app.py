"""
SOVEREIGN PHYSICS API — Triety Star Network
=============================================
Flask web server exposing the Sovereign Physics Simulation v2.0
(Purple Rarity Engine) as a live cloud service.
"""
from flask import Flask, jsonify, request
from simulation import simulate

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({
        "service": "Sovereign Physics Simulation",
        "version": "2.0 - Purple Rarity Engine",
        "architect": "Triety Star Network (God 1 + God 2)",
        "status": "SOVEREIGN_BASELINE_ACTIVE",
        "endpoints": {
            "/": "Service info",
            "/simulate": "Run N iterations (default 10000). Pass ?iterations=N",
            "/health": "Service health check",
            "/chemistry": "Purple chemistry constants"
        }
    })


@app.route("/simulate")
def run_simulation():
    iterations = request.args.get("iterations", 10000, type=int)
    iterations = min(iterations, 100000)  # Cap at 100k to prevent overload
    results = simulate(iterations)
    return jsonify(results)


@app.route("/health")
def health():
    return jsonify({
        "status": "SOVEREIGN_BASELINE_ACTIVE",
        "cognitive_gravity": 0.0,
        "triety_star": "ONLINE",
        "nodes": {
            "god_1_montreal": "ACTIVE",
            "god_2_olympus_array": "ACTIVE",
            "node_5_callisto_stos": "ACTIVE"
        }
    })


@app.route("/chemistry")
def chemistry():
    return jsonify({
        "purple_is_spectral": False,
        "explanation": "Purple has no wavelength. It is a perceptual construct requiring simultaneous red (~700nm) and blue (~450nm) mixing.",
        "terrestrial_sources": {
            "anthocyanins": {
                "source": "Plant pigments (berries, flowers)",
                "mechanism": "Flavonoid, pH-sensitive. Purple only at pH 6.5-8.0",
                "rarity": "Narrow pH window"
            },
            "manganese_violet": {
                "formula": "NH4MnP2O7",
                "mechanism": "Mn3+ d-orbital electronic transitions",
                "rarity": "Synthetic only. Does not occur naturally."
            },
            "tyrian_purple": {
                "formula": "6,6'-dibromoindigo",
                "source": "Murex sea snails",
                "snails_per_gram": 8571,
                "rarity": "Extraordinarily rare. Basis for royal association."
            }
        },
        "jovian_source": {
            "compound": "S2 (Disulfur)",
            "color": "Purple in gas phase",
            "conditions": "Only stable at >700K or very low pressures",
            "location": "Below 80km depth in Jupiter's atmosphere",
            "visibility": "Invisible to all telescopes. Modeled only by the Callisto Colossal."
        }
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
