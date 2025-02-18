"""Constants for the Surface Plots."""

from pathlib import Path

import numpy as np

from te_toolbox.systems import TentMap

SURFACE_DATA_DIR = Path("analysis/data/entropy_surface/")
SURFACE_DATA_DIR.mkdir(exist_ok=True, parents=True)

SURFACE_PLOT_DIR = Path("analysis/plots/entropy_surface/")
SURFACE_PLOT_DIR.mkdir(exist_ok=True, parents=True)

SEED = 42
EPS = 0.5

N_TRANSIENT = 10**5
N_MAPS = 20
N_ITER = 10 * 10**3
LAG = 1

MIN_BINS = 2
MAX_BINS = 350
BIN_STEP = 10

N_BINS = 100  # int((MAX_BINS - MIN_BINS) / BIN_STEP)

MIN_LEN = 50
N_LENS = 100

# bin_range = np.arange(MIN_BINS, MAX_BINS, BIN_STEP)
bin_range = np.floor(np.geomspace(MIN_BINS, MAX_BINS, num=N_BINS)).astype(int)
length_range = np.geomspace(MIN_LEN, N_ITER, num=N_LENS)

maps = {
    "TentMap(r=2)": TentMap(r=2),
}
