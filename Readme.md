Protein → Codon-Optimized Cloning & Primer Designer

A local, open-source bioinformatics tool for converting protein sequences into codon-optimized DNA, designing cloning-ready primers using Primer3 thermodynamics, and exporting SnapGene and GenBank files with visualization.

This tool is intended for research labs, teaching practicals, and student projects, and avoids reliance on commercial software.

Features

Protein → DNA back-translation

Host-specific codon optimization

Escherichia coli

Saccharomyces cerevisiae

Primer design using Primer3 (nearest-neighbor thermodynamics)

Restriction cloning primers (NdeI, XhoI, EcoRI, BamHI)

Optional:

Signal peptide (PelB)

C-terminal 6×His tag

SnapGene-style visualization

Export formats:

SnapGene (.dna)

GenBank (.gb)

Built-in test dataset for validation and teaching

Runs fully offline after installation

Project Structure
protein_primer_app/
├── app.py                 # Main Streamlit application
├── run_app.py             # Desktop launcher (optional)
├── core/
│   ├── __init__.py
│   ├── codon.py           # Codon back-translation
│   ├── primer_design.py   # Primer3 integration
│   ├── visualization.py   # SnapGene-like diagrams
│   └── snapgene_export.py # SnapGene export
└── README.md

Requirements

Python ≥ 3.8

Works on Linux / Windows / macOS

System dependencies (Linux)
sudo apt install primer3

Installation
1. Clone the repository
git clone https://github.com/<your-username>/protein_primer_app.git
cd protein_primer_app

2. Create and activate a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate


Windows:

venv\Scripts\activate

3. Install Python dependencies
pip install --upgrade pip
pip install streamlit biopython primer3-py dna-features-viewer matplotlib

Running the Application
Run as a local web app
streamlit run app.py


The app will open at:

http://localhost:8501

Usage Workflow

Paste a protein sequence (single-letter amino acid code)

Or load a test dataset from the sidebar

Select:

Expression host

Signal peptide (optional)

His-tag (optional)

Restriction enzymes

Click Generate Cloning-Ready Primers

Review:

Codon-optimized DNA

Primer sequences and melting temperatures

SnapGene-style diagram

Download:

.dna (SnapGene)

.gb (GenBank)

Built-in Test Dataset

The app includes example protein sequences to validate:

Codon optimization

Primer design

Export functionality

Use the sidebar to load test sequences.

Desktop Executable (Optional)

A desktop launcher can be created using PyInstaller.

Build executable
pip install pyinstaller
pyinstaller --onefile --noconsole --add-data "core:core" run_app.py


The executable will be available in:

dist/run_app


Double-click to launch the app in your browser.

Scientific Notes & Limitations

Protein back-translation is non-unique; codon usage bias is applied.

Primer designs are computational predictions and must be experimentally validated.

Signal peptide cleavage is not automatically predicted.

Restriction sites are added without frame enforcement (user responsibility).

Intended Use

Molecular cloning design

Wet-lab primer planning

Teaching bioinformatics / biotechnology

Internal lab tooling

Student projects

License

This project is released under the MIT License.
Free for academic, educational, and commercial use.

Citation (Suggested)

If you use this tool in teaching or research, please cite as:

Protein → Codon-Optimized Cloning & Primer Designer, GitHub repository, YYYY.