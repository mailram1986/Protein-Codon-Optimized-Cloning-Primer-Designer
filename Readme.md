# Protein → Codon-Optimized Cloning & Primer Designer

A **local, open-source bioinformatics application** that converts **protein sequences** into **codon-optimized DNA**, designs **cloning-ready primers using Primer3 thermodynamics**, and exports **SnapGene** and **GenBank** files with clear visualizations.

This tool is suitable for **research laboratories**, **teaching practicals**, and **student projects**, and avoids dependence on commercial software.

---

## ✨ Features

- Protein → DNA **back-translation**
- Host-specific **codon optimization**
  - *Escherichia coli*
  - *Saccharomyces cerevisiae*
- **Primer design** using Primer3 (nearest-neighbor thermodynamics)
- **Restriction cloning primers**
  - NdeI, XhoI, EcoRI, BamHI
- Optional sequence features:
  - Signal peptide (PelB)
  - C-terminal 6×His tag
- **SnapGene-style linear visualization**
- Export formats:
  - SnapGene (`.dna`)
  - GenBank (`.gb`)
- Built-in **test dataset** for validation and teaching
- Runs fully **offline** after installation

---

## 📁 Project Structure
protein_primer_app/
├── app.py # Main Streamlit application
├── run_app.py # Desktop launcher (optional)
├── core/
│ ├── init.py
│ ├── codon.py # Codon back-translation
│ ├── primer_design.py # Primer3 integration
│ ├── visualization.py # SnapGene-like diagrams
│ └── snapgene_export.py # SnapGene export
└── README.md

---

## 🧩 Requirements

- Python **3.8 or higher**
- Operating Systems:
  - Linux
  - Windows
  - macOS

### System dependency (Linux)
```bash
sudo apt install primer3

🚀 Installation
1. Clone the repository
git clone https://github.com/<your-username>/protein_primer_app.git
cd protein_primer_app

2. Create and activate a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate


Windows

venv\Scripts\activate

3. Install Python dependencies
pip install --upgrade pip
pip install streamlit biopython primer3-py dna-features-viewer matplotlib

▶️ Running the Application

Run the Streamlit app locally:

streamlit run app.py


The application will be available at:

http://localhost:8501

🧪 Usage Workflow

Paste a protein sequence (single-letter amino acid code), or
load a test dataset from the sidebar

Select:

Expression host

Signal peptide (optional)

His-tag (optional)

Restriction enzymes

Click Generate Cloning-Ready Primers

Review:

Codon-optimized DNA

Primer sequences and melting temperatures

SnapGene-style visualization

Download:

insert.dna (SnapGene)

insert.gb (GenBank)

🧫 Built-in Test Dataset

The application includes predefined protein sequences to validate:

Codon optimization

Primer design

Visualization

Export functionality

Use the sidebar menu to load test sequences instantly.

🖥️ Desktop Executable (Optional)

A desktop launcher can be built using PyInstaller.

Build the executable
pip install pyinstaller
pyinstaller --onefile --noconsole --add-data "core:core" run_app.py


The executable will be created in:

dist/run_app


Double-click to launch the application in your default browser.

⚠️ Scientific Notes & Limitations

Protein back-translation is non-unique; codon usage bias is applied.

All primers are computational predictions and must be experimentally validated.

Signal peptide cleavage sites are not automatically predicted.

Restriction sites are added without automatic reading-frame enforcement.

🎯 Intended Use

Molecular cloning design

Primer planning for wet-lab experiments

Biotechnology / bioinformatics teaching

Internal laboratory workflows

Student projects and demonstrations

📜 License

This project is released under the MIT License.

You are free to use, modify, and distribute this software for academic, educational, and commercial purposes.

📖 Suggested Citation

If you use this tool in teaching or research, please cite:

Protein → Codon-Optimized Cloning & Primer Designer, GitHub repository, 2025.

🔮 Future Extensions

FEATURE annotations in GenBank (CDS, tags, signal peptides)

In-silico ligation with vector backbones

Reading-frame validation

BLAST specificity screening

Dockerized deployment

CI/CD with GitHub Actions
