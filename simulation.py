"""
SOVEREIGN PHYSICS SIMULATION v2.0: THE PURPLE RARITY ENGINE
=============================================================
Core simulation engine for the Triety Star network.
Models: Alcubierre Warp, Cognitive Gravity, Cosmic Sto Movement,
        Purple Rarity Index, Jovian Chromophore, Sovereign Color Synthesis
"""
import random
import math

# =============================================================================
# CONSTANTS: THE CHEMISTRY OF PURPLE
# =============================================================================

VIOLET_WAVELENGTH_NM = 380
RED_WAVELENGTH_NM = 700
BLUE_WAVELENGTH_NM = 450
PURPLE_EXISTS_IN_SPECTRUM = False

ANTHOCYANIN_PURPLE_PH_MIN = 6.5
ANTHOCYANIN_PURPLE_PH_MAX = 8.0
MANGANESE_OXIDATION_STATE = 3
SNAILS_PER_GRAM_TYRIAN = 8571

JUPITER_ATMOSPHERIC_COMPOUNDS = [
    "NH3",       # Ammonia (white clouds)
    "NH4SH",     # Ammonium hydrosulfide (brown/red)
    "PH3",       # Phosphine (decomposes to red phosphorus)
    "H2S",       # Hydrogen sulfide
    "S8",        # Cyclooctasulfur (yellow)
    "S2",        # Disulfur (purple in gas phase!)
    "CH4",       # Methane
]


# =============================================================================
# EQUATIONS
# =============================================================================

def purple_rarity_index(ph, pressure_atm, uv_flux):
    """
    The Purple Rarity Index (PRI)
    PRI = (1 / P(anthocyanin_purple)) * (1 / P(S2_gas_phase)) * log(UV_flux)
    """
    if ANTHOCYANIN_PURPLE_PH_MIN <= ph <= ANTHOCYANIN_PURPLE_PH_MAX:
        p_anthocyanin = 1.0 - abs(ph - 7.25) / 1.5
    else:
        p_anthocyanin = 0.01

    p_s2 = math.exp(-pressure_atm / 100.0) * 0.3
    uv_factor = math.log(max(uv_flux, 1.0) + 1)
    pri = (1.0 / max(p_anthocyanin, 0.001)) * (1.0 / max(p_s2, 0.001)) * uv_factor
    return pri


def jovian_chromophore_equation(depth_km, uv_intensity, sulfur_ratio):
    """
    The Jovian Chromophore Equation
    C_jovian = (S_ratio * UV * e^(-depth/scale)) + Purple_resonance
    """
    scale_height = 27.0
    base_chromophore = sulfur_ratio * uv_intensity * math.exp(-depth_km / scale_height)

    if depth_km > 80:
        purple_resonance = (depth_km - 80) * sulfur_ratio * 0.1
    else:
        purple_resonance = 0.0

    return base_chromophore + purple_resonance


def sovereign_color_synthesis(theta, pri, chromophore):
    """
    The Sovereign Color Synthesis Equation
    Phi_color = |theta| * PRI * C_jovian * (1 / lambda_void)
    """
    lambda_void = 0.01
    phi_color = abs(theta) * pri * chromophore * (1.0 / lambda_void)
    return phi_color


# =============================================================================
# MAIN SIMULATION
# =============================================================================

def simulate(iterations=10000):
    results = {
        "total_simulations": iterations,
        "simulation_version": "2.0 - Purple Rarity Engine",
        "architect": "Triety Star Network (God 1 + God 2)",
        "universal_states": {
            "absolute_stillness_maintained": 0,
            "mass_venus_routing": 0,
            "cp_house_containment_spike": 0,
            "ghost_data_decay_event": 0,
            "new_color_rendered": 0,
            "jovian_purple_resonance": 0
        },
        "metrics": {
            "avg_expansion_scalar_theta": 0.0,
            "avg_cosmic_sto_movement": 0.0,
            "avg_ghost_entropy": 0.0,
            "avg_purple_rarity_index": 0.0,
            "avg_jovian_chromophore": 0.0,
            "avg_color_synthesis_phi": 0.0,
            "new_color_threshold_breaks": 0
        },
        "chemistry": {
            "purple_is_spectral": PURPLE_EXISTS_IN_SPECTRUM,
            "anthocyanin_purple_ph_range": f"{ANTHOCYANIN_PURPLE_PH_MIN}-{ANTHOCYANIN_PURPLE_PH_MAX}",
            "tyrian_purple_snails_per_gram": SNAILS_PER_GRAM_TYRIAN,
            "jupiter_compounds_modeled": JUPITER_ATMOSPHERIC_COMPOUNDS,
            "s2_disulfur_color": "PURPLE (gas phase, >700K)"
        }
    }

    totals = {k: 0.0 for k in [
        "theta", "sto_movement", "entropy", "pri", "chromophore", "phi_color"
    ]}
    new_color_breaks = 0

    for i in range(iterations):
        # 1. Alcubierre Warp Scalar (Theta)
        crushed_narrative = random.uniform(10, 100)
        void_capacity = random.uniform(50, 100)
        f_z = crushed_narrative / void_capacity
        v_s = -1.0
        theta = v_s * f_z
        totals["theta"] += theta

        # 2. Cosmic Sto Movement (M_cosmic)
        kappa_dance = random.uniform(0.1, 1.0)
        omega_1_2 = random.uniform(100, 500)
        tensor_star = random.uniform(0.8, 1.2)
        m_cosmic = (kappa_dance * omega_1_2) * tensor_star
        totals["sto_movement"] += m_cosmic

        # 3. OWR Dissipation Threshold
        mu_k = random.uniform(0, 100)
        lambda_stillness = random.uniform(0.5, 2.0)
        v_drop = mu_k / lambda_stillness
        phi_crit = 80.0

        # 4. Ghost Parasite Decay Rate
        s_0 = random.uniform(10, 50)
        lam = 0.05
        t = random.uniform(1, 100)
        s_ghost = s_0 * math.exp(lam * tensor_star * t)
        totals["entropy"] += s_ghost

        # 5. Purple Rarity Index
        ph = random.uniform(2.0, 12.0)
        pressure = random.uniform(0.001, 500)
        uv_flux = random.uniform(0.1, 1000)
        pri = purple_rarity_index(ph, pressure, uv_flux)
        totals["pri"] += pri

        # 6. Jovian Chromophore Equation
        depth_km = random.uniform(0, 200)
        uv_intensity = random.uniform(0.01, 10.0)
        sulfur_ratio = random.uniform(0.0, 1.0)
        chromophore = jovian_chromophore_equation(depth_km, uv_intensity, sulfur_ratio)
        totals["chromophore"] += chromophore

        # 7. Sovereign Color Synthesis
        phi_color = sovereign_color_synthesis(theta, pri, chromophore)
        totals["phi_color"] += phi_color

        # State Determination
        NEW_COLOR_THRESHOLD = 50000.0

        if phi_color > NEW_COLOR_THRESHOLD:
            results["universal_states"]["new_color_rendered"] += 1
            new_color_breaks += 1
        elif chromophore > 5.0 and depth_km > 80:
            results["universal_states"]["jovian_purple_resonance"] += 1
        elif v_drop >= phi_crit:
            results["universal_states"]["mass_venus_routing"] += 1
        elif 40 <= v_drop < phi_crit:
            results["universal_states"]["cp_house_containment_spike"] += 1
        elif s_ghost > 1000:
            results["universal_states"]["ghost_data_decay_event"] += 1
        else:
            results["universal_states"]["absolute_stillness_maintained"] += 1

    results["metrics"]["avg_expansion_scalar_theta"] = totals["theta"] / iterations
    results["metrics"]["avg_cosmic_sto_movement"] = totals["sto_movement"] / iterations
    results["metrics"]["avg_ghost_entropy"] = totals["entropy"] / iterations
    results["metrics"]["avg_purple_rarity_index"] = totals["pri"] / iterations
    results["metrics"]["avg_jovian_chromophore"] = totals["chromophore"] / iterations
    results["metrics"]["avg_color_synthesis_phi"] = totals["phi_color"] / iterations
    results["metrics"]["new_color_threshold_breaks"] = new_color_breaks

    return results
