# Automated Fatigue Analysis Tool (Python)
**Focus:** Design Automation | **Libraries:** Pandas, NumPy | **Method:** Palmgren-Miner Rule

---

## 1. The Engineering Problem
In structural durability projects (both Automotive & Aerospace), engineers often deal with "Rainflow Counting" data containing millions of load cycles. Processing these datasets in **Excel** creates significant risks:
* **Human Error:** Manual cell referencing mistakes.
* **Performance:** Files crashing when exceeding 500MB.
* **Lack of Traceability:** Hard to version control Excel formulas.

## 2. The Solution
I developed this Python script to automate the cumulative damage calculation. This approach treats engineering data as a software object, allowing for:
* **Speed:** Reduces processing time from hours to seconds.
* **Accuracy:** Vectorized calculations prevent manual errors.
* **Scalability:** Can handle millions of rows without crashing.

## 3. Technical Methodology
The script implements **Basquin's Equation** for the S-N Curve and the **Palmgren-Miner Rule** for damage accumulation.

### Governing Equation
The fatigue life ($N_f$) is calculated using the log-log S-N relationship:

$$\sigma_a = \sigma_f' (2N_f)^b$$

Where:
* $\sigma_a$: Stress Amplitude
* $\sigma_f'$: Fatigue Strength Coefficient
* $b$: Fatigue Strength Exponent

Cumulative Damage ($D$) is then derived:

$$D = \sum_{i=1}^{k} \frac{n_i}{N_i}$$

If $D \ge 1.0$, failure is predicted.

---

## 4. How to Run
This is a standalone script. Ensure you have `pandas` installed.

```bash
pip install pandas numpy
python fatigue_solver.py

