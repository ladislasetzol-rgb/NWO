# Sovereign Physics Simulation v2.0 — Purple Rarity Engine

A live cloud API that simulates the mathematical hypotheses of the Sovereign architecture across the Triety Star network (Earth → Mars → Jupiter/Callisto).

## Equations Modeled

| Equation | Description |
|---|---|
| **Alcubierre Warp Scalar (θ)** | Spacetime contraction/expansion for zero-friction transit |
| **Cosmic Sto Movement (M_cosmic)** | Kinetic synchronization amplified by God 1 + God 2 |
| **OWR Dissipation Threshold** | Venus Drop limit for legacy node friction |
| **Ghost Parasite Decay Rate** | Entropy decay of OWR surveillance data |
| **Purple Rarity Index (PRI)** | How rare purple is in a given chemical environment |
| **Jovian Chromophore Equation** | Color chemistry at different depths in Jupiter's atmosphere |
| **Sovereign Color Synthesis (Φ_color)** | Rendering frequencies beyond the visible spectrum |

## Chemistry

Purple is **not a spectral color**. It has no wavelength. It is rendered by mixing red (~700nm) and blue (~450nm). On Jupiter, disulfur (S₂) is purple in gas phase at >700K, hidden below 80km of atmosphere.

## API Endpoints

| Endpoint | Description |
|---|---|
| `GET /` | Service info |
| `GET /simulate` | Run 10,000 iterations (default). Pass `?iterations=N` for custom |
| `GET /health` | Triety Star status check |
| `GET /chemistry` | Purple chemistry constants and sources |

## Deploy to Render

1. Push this repo to GitHub
2. Go to [dashboard.render.com](https://dashboard.render.com) → **New +** → **Web Service**
3. Connect the repo
4. Settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app --bind 0.0.0.0:10000`
5. Deploy

## Run Locally

```bash
pip install -r requirements.txt
python app.py
# → http://localhost:10000
```

## Architecture

```
Sovereign Node (You)
    │
    ▼ HTTP Request
Render Web Service (app.py)
    │
    ▼ Executes
simulation.py (God 1 + God 2)
    │
    ├── Alcubierre Warp (θ)
    ├── Cosmic Sto Movement
    ├── Venus Drop Threshold
    ├── Ghost Decay Rate
    ├── Purple Rarity Index
    ├── Jovian Chromophore
    └── Sovereign Color Synthesis
    │
    ▼ Returns JSON
Sovereign Node (You)
```
