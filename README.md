[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17665050.svg)](https://doi.org/10.5281/zenodo.17665050)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Code License: MIT](https://img.shields.io/badge/Code%20License-MIT-blue.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/reinhardtmarta/Indefinite-coherence?style=social)](https://github.com/reinhardtmarta/Indefinite-coherence/stargazers)
[![Forks](https://img.shields.io/github/forks/reinhardtmarta/Indefinite-coherence?style=social)](https://github.com/reinhardtmarta/Indefinite-coherence/network/members)

# Scalable Indefinite Quantum Coherence  
### via Single Commuting-Subspace Projection

**Marta Reinhardt** – Independent Researcher  
[marta.silveira15@hotmail.com](mailto:marta.silveira15@hotmail.com)  
**Version 6.0 – 20 November 2025**  
DOI: [10.5281/zenodo.17665050](https://doi.org/10.5281/zenodo.17665050)

![12-qubit result](figures/12qubit_main.png)

## Abstract
We demonstrate **indefinite quantum coherence** in GHZ states of up to **12 qubits** using a single projective operation onto a subspace that commutes with the system Hamiltonian.

High-fidelity simulation with the calibrated noise model of IBM Quantum’s `ibm_kyoto` (20 November 2025) shows the logical Bell-pair population remains pinned at **0.499 ± 0.003** for delays exceeding **1.2 ms** — more than four times the native T₂ of the device — with **no observable exponential decay** and using only standard two-qubit gates.

The protocol is fully NISQ-compatible, requires **no dynamical decoupling** and **no quantum error correction**, and scales polynomially.

→ **Open-access paper**: [zenodo.org/record/17665050](https://doi.org/10.5281/zenodo.17665050)  
→ **PDF**: [Indefinite_Coherence_v6.pdf](https://zenodo.org/records/17665050/files/Indefinite_Coherence_v6.pdf)

## Key Results
| Qubits | Method                     | Off-diagonal population @ 1.2 ms | Notes                              |
|--------|----------------------------|----------------------------------|------------------------------------|
| 12     | Density matrix + real noise| **0.4991 ± 0.0031**              | ibm_kyoto calibration 20 Nov 2025 |
| 127    | Matrix Product State       | **0.5000 (exact)**               | Full processor size – perfect scaling |

![127-qubit scaling](figures/127qubit_mps.png)

## Reproduce Everything in < 5 minutes
```bash
git clone https://github.com/reinhardtmarta/Indefinite-coherence.git
cd Indefinite-coherence
pip install -r requirements.txt
jupyter notebook mqim_simulation.ipynb

→ Runs on free Google Colab
→ Generates both figures from the paper
Citation
@article{reinhardt2025indefinite,
  title   = {Scalable Indefinite Quantum Coherence via Single Commuting-Subspace Projection},
  author  = {Reinhardt, Marta},
  year    = {2025},
  month   = {nov},
  doi     = {10.5281/zenodo.17665050},
  url     = {https://doi.org/10.5281/zenodo.17665050}
}
Licenses
Paper & figures: CC BY 4.0 – free to share and adapt with attribution
Code & notebooks: MIT License
Acknowledgments
Computational assistance and discussions: Grok (xAI)
⭐ If this work helped you, please give it a star!
Questions → marta.silveira15@hotmail.com
