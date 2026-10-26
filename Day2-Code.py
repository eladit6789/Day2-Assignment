
# DNA Calculator
# Calculate DNA mass, molar concentration, and molecule copy number.

AVOGADRO = 6.022e23
AVERAGE_MASS_PER_BP = 660  # g/mol per base pair for double-stranded DNA


def calculate_dna(concentration, length_bp, volume):
    """Calculate DNA mass, molarity, and number of molecules."""

    # Calculate total DNA mass in nanograms
    mass_ng = concentration * volume

    # Calculate molar concentration in nanomolar (nM)
    molarity_nM = concentration * 1e6 / (
        length_bp * AVERAGE_MASS_PER_BP
    )

    # Calculate the number of DNA molecules in the sample
    mass_g = mass_ng * 1e-9
    moles = mass_g / (length_bp * AVERAGE_MASS_PER_BP)
    copies = moles * AVOGADRO

    return mass_ng, molarity_nM, copies


def main():
    print("=== DNA Molecular Biology Calculator ===")

    try:
        concentration = float(
            input("DNA concentration (ng/uL): ")
        )
        length_bp = float(
            input("DNA fragment length (bp): ")
        )
        volume = float(
            input("Sample volume (uL): ")
        )

        if concentration <= 0 or length_bp <= 0 or volume <= 0:
            print("Error: All values must be positive.")
            return

        mass, molarity, copies = calculate_dna(
            concentration, length_bp, volume
        )

        print("\n--- Results ---")
        print(f"Total DNA mass: {mass:.2f} ng")
        print(f"Molar concentration: {molarity:.2f} nM")
        print(f"Number of DNA molecules: {copies:.3e}")

    except ValueError:
        print("Error: Please enter valid numerical values.")


if __name__ == "__main__":
    main()
