"""Script to generate CML data for various maps and coupling strengths."""

from eps_scan_constants import (
    EPS_DATA_DIR,
    EPSILONS,
    N_ITER,
    N_MAPS,
    N_TRANSIENT,
    SEED,
    maps,
)

from te_toolbox.systems.lattice import CMLConfig, CoupledMapLatticeGenerator
from te_toolbox.systems.maps import Map


def create_cml(map_function: Map) -> None:
    """Generate CML data for a given map across different coupling strengths.

    Args:
    ----
        map_function: Map to use for the CML

    """
    # Generate data for each coupling strength
    for eps in EPSILONS:
        print(f"Generating {map_function.__class__.__name__} with eps={eps:.2f}")

        # Create configuration
        config = CMLConfig(
            map_function=map_function,
            n_maps=N_MAPS,
            coupling_strength=eps,
            n_steps=N_ITER,
            warmup_steps=N_TRANSIENT,
            seed=SEED,
            output_dir=str(EPS_DATA_DIR),
        )

        # Generate and save data
        generator = CoupledMapLatticeGenerator(config)
        cml = generator.generate()
        cml.save()


def main():
    """Generate data for all maps."""
    for map_function in maps.values():
        create_cml(map_function)


if __name__ == "__main__":
    main()
