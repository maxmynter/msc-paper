"""Constants and configuration for binning analysis."""

from pathlib import Path

import numpy as np

from te_toolbox.binning import (
    aic_bins,
    bic_bins,
    doanes_bins,
    freedman_diaconis_bins,
    knuth_bins,
    rice_rule_bins,
    scotts_rule_bins,
    shimazaki_bins,
    small_sample_akaike_bins,
    sqrt_n_bins,
    sturges_bins,
)
from te_toolbox.systems import TentMap

# Directory Structure
BASE_DIR = Path("analysis")
DATA_DIR = BASE_DIR / "data" / "binning_method_consistency"
PLOT_DIR = BASE_DIR / "plots" / "binning_method_consistency"

# Create directories if they don't exist
DATA_DIR.mkdir(exist_ok=True, parents=True)
PLOT_DIR.mkdir(exist_ok=True, parents=True)

# Analysis Parameters
SEED = 42
EPS = 0.5
N_TRANSIENT = 10**5
N_MAPS = 25
LAG = 1
MIN_SAMPLE = 50
MAX_SAMPLE = 1.5 * 10**4
N_SAMPLE = 25
SAMPLE_SIZES = [int(i) for i in np.geomspace(MIN_SAMPLE, MAX_SAMPLE, N_SAMPLE)]

# Binning Methods
BINNING_METHODS = {
    "AIC": aic_bins,
    "BIC": bic_bins,
    "Doane": doanes_bins,
    "Freedman-Diaconis": freedman_diaconis_bins,
    "Knuth": knuth_bins,
    "Rice": rice_rule_bins,
    "Scott": scotts_rule_bins,
    "Shimazaki": shimazaki_bins,
    "Small-Sample AIC": small_sample_akaike_bins,
    "Sqrt-n": sqrt_n_bins,
    "Sturges": sturges_bins,
}

# Map Configuration
DEFAULT_MAP = TentMap(r=2)

# Plot Configuration
PLOT_STYLES = {
    "figure.figsize": (15, 8),
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans"],
    "mathtext.fontset": "stix",
    "text.usetex": True,
}

# File naming patterns
RESULTS_FILE_PATTERN = "binning_results_size_{}.pkl"
VIOLIN_PLOT_PATTERN = "binning_comparison_{}_size_{}.png"
STD_PLOT_PATTERN = "std_comparison_{}.png"
CRITERION_BINS_PATTERN = "bin_criterion_size_comparison_{}.png"
