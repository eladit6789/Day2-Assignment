
# DNA Molecular Biology Calculator

## Description

This Python program performs a well-known calculation in molecular biology. It calculates the total DNA mass, molar concentration, and approximate number of DNA molecules in a sample of double-stranded DNA.

The program asks the user to enter three values:

1. DNA concentration in ng/uL.
2. DNA fragment length in base pairs (bp).
3. Sample volume in uL.

It then calculates and displays the results.

## Scientific Background

The calculation uses the average molecular mass of double-stranded DNA, approximately 660 g/mol per base pair, and Avogadro's constant (6.022 x 10^23 molecules/mol).

The total DNA mass is calculated as:

DNA mass (ng) = DNA concentration (ng/uL) x sample volume (uL)

The molar concentration is calculated from the DNA mass concentration and the molecular mass of the DNA fragment.

The number of DNA molecules is calculated by converting the total DNA mass to grams, calculating the number of moles, and multiplying by Avogadro's constant.

## How to Run

Make sure Python is installed. Open a terminal in the `day02` directory and run:

```bash
python dna_calculator.py
```

On some Windows systems, use:

```bash
py dna_calculator.py
```

## Sample Input

```text
DNA concentration (ng/uL): 50
DNA fragment length (bp): 1000
Sample volume (uL): 2
```

## Expected Output

```text
Results:
Total DNA mass: 100.00 ng
Molar concentration: 75.76 nM
Number of DNA molecules: 9.123e+10
```

## Limitations

The calculation assumes double-stranded DNA and an average molecular mass of 660 g/mol per base pair. The number of molecules is an estimate based on the entered concentration, fragment length, and volume.

## AI Assistance

AI tool used: ChatGPT by OpenAI.

Purpose: Assistance with selecting a scientific calculation, writing and explaining the Python program, and preparing this README file.

Prompts used:

- "Can you help me create a Python script that performs a well-known calculation in molecular biology?"
- "How can I run the code in Visual Studio Code?"
- "Please help me update my assignment according to the assignment requirements, including a README file and AI disclosure."

The code and documentation should be reviewed and understood by the student before submission.
