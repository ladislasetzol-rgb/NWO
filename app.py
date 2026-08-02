import os
import numpy as np
import matplotlib
# Force matplotlib to use the non-interactive backend (Agg) for cloud environments
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from flask import Flask, send_file
import io

app = Flask(__name__)

def simulate_plasmoids(
    grid_size: int = 128,
    steps: int = 120,
    compress_strength: float = 0.09,
    reconnection_threshold: float = 1.75,
    dissipation: float = 0.975,
    noise_level: float = 0.04,
    snapshot_interval: int = 15
):
    """
    Vectorized Viriato-Lite simulation.
    Models compressive forcing leading to magnetic reconnection and plasmoid instability.
    Designed for cloud/web rendering (lightweight + clear visual stages).
    """
    grid = np.zeros((grid_size, grid_size), dtype=np.float32)
    mid = grid_size // 2
    grid[mid-3:mid+4, :] = 0.55

    history = []
    history.append(grid.copy())

    y_indices = np.arange(grid_size)

    for t in range(steps):
        new_grid = grid.copy()

        # === 1. Compressive Forcing (vectorized) ===
        above = y_indices < mid
        below = y_indices > mid

        new_grid[1:, :][above[1:]] += compress_strength * grid[:-1, :][above[1:]]
        new_grid[:-1, :][above[:-1]] -= compress_strength * 0.6 * grid[:-1, :][above[:-1]]

        new_grid[:-1, :][below[:-1]] += compress_strength * grid[1:, :][below[:-1]]
        new_grid[1:, :][below[1:]] -= compress_strength * 0.6 * grid[1:, :][below[1:]]

        # === 2. Magnetic Reconnection + Plasmoid Instability ===
        current_sheet = new_grid[mid, :]
        hotspots = np.where(current_sheet > reconnection_threshold)[0]

        for j in hotspots:
            y_slice = slice(max(0, mid-4), min(grid_size, mid+5))
            x_slice = slice(max(0, j-3), min(grid_size, j+4))
            new_grid[y_slice, x_slice] += 1.6

            left = slice(max(0, j-7), j)
            right = slice(j+1, min(grid_size, j+8))
            new_grid[mid, left] += 0.55
            new_grid[mid, right] += 0.55

            new_grid[mid, j] = 0.4

        # === 3. Ambient MHD Turbulence + Dissipation ===
        new_grid += np.random.normal(0, noise_level, (grid_size, grid_size)).astype(np.float32)
        new_grid *= dissipation
        np.clip(new_grid, 0.0, 4.0, out=new_grid)

        grid = new_grid

        if (t + 1) % snapshot_interval == 0 or t == steps - 1:
            history.append(grid.copy())

    return history

def render_stages(history, title_prefix="Viriato-Lite"):
    """Generate a clean multi-panel visualization suitable for cloud rendering."""
    n = len(history)
    cols = min(4, n)
    rows = (n + cols - 1) // cols

    fig, axes = plt.subplots(rows, cols, figsize=(4.2*cols, 3.8*rows))
    axes = np.array(axes).reshape(-1)

    colors = ["#0a0a12", "#1a1a3a", "#3a1a5a", "#8b1a3a", "#e05a1a", "#ffcc44", "#ffffff"]
    cmap = LinearSegmentedColormap.from_list("plasmoid", colors)

    for i, frame in enumerate(history):
        ax = axes[i]
        im = ax.imshow(frame, cmap=cmap, origin="lower", vmin=0, vmax=3.5)
        ax.set_title(f"t = {i * 15}", fontsize=10)
        ax.axis("off")

    for j in range(i+1, len(axes)):
        axes[j].axis("off")

    fig.suptitle(f"{title_prefix}: Compressive Forcing → Plasmoid Instability", fontsize=13, y=0.98)
    plt.tight_layout()
    return fig

@app.route('/')
def index():
    # Run the simulation when the page is hit
    history = simulate_plasmoids(
        grid_size=128,
        steps=90,
        compress_strength=0.085,
        reconnection_threshold=1.7,
        snapshot_interval=15
    )

    # Render the figure
    fig = render_stages(history)
    
    # Save the figure to a BytesIO object (in memory) to serve to the web client
    img_io = io.BytesIO()
    fig.savefig(img_io, format='png', dpi=140, bbox_inches="tight")
    img_io.seek(0)
    plt.close(fig) # Clear memory
    
    # Send the image directly as the HTTP response
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    # Use the PORT environment variable if available, otherwise default to 10000
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
