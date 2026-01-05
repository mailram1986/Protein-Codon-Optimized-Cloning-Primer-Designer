import streamlit as st
from Bio.Data import CodonTable
from Bio.Seq import Seq
import primer3
from dna_features_viewer import GraphicFeature, GraphicRecord
import matplotlib.pyplot as plt
import random
import base64
from snapgene_reader import snapgene_file

# -----------------------------
# Codon Usage Tables (Simplified)
# -----------------------------
CODON_USAGE = {
    "ecoli": {
        "A": ["GCG","GCC","GCA"],
        "C": ["TGC","TGT"],
        "D": ["GAT","GAC"],
        "E": ["GAA","GAG"],
        "F": ["TTT","TTC"],
        "G": ["GGT","GGC","GGA"],
        "H": ["CAT","CAC"],
        "I": ["ATT","ATC"],
        "K": ["AAA","AAG"],
        "L": ["CTG","TTA","TTG"],
        "M": ["ATG"],
        "N": ["AAT","AAC"],
        "P": ["CCG","CCA"],
        "Q": ["CAA","CAG"],
        "R": ["CGT","CGC"],
        "S": ["TCG","TCC"],
        "T": ["ACC","ACA"],
        "V": ["GTG","GTT"],
        "W": ["TGG"],
        "Y": ["TAT","TAC"],
        "*": ["TAA"]
    },
    "yeast": {
        "A": ["GCT","GCC"],
        "C": ["TGT","TGC"],
        "D": ["GAT"],
        "E": ["GAA"],
        "F": ["TTT"],
        "G": ["GGT"],
        "H": ["CAT"],
        "I": ["ATT"],
        "K": ["AAA"],
        "L": ["TTA"],
        "M": ["ATG"],
        "N": ["AAT"],
        "P": ["CCA"],
        "Q": ["CAA"],
        "R": ["AGA"],
        "S": ["TCT"],
        "T": ["ACT"],
        "V": ["GTT"],
        "W": ["TGG"],
        "Y": ["TAT"],
        "*": ["TAA"]
    }
}

def back_translate(protein, host):
    dna = ""
    for aa in protein:
        dna += random.choice(CODON_USAGE[host][aa])
    return dna

# -----------------------------
# Primer3 Design
# -----------------------------
def design_primers_primer3(dna):
    primers = primer3.bindings.designPrimers(
        {
            'SEQUENCE_TEMPLATE': dna
        },
        {
            'PRIMER_OPT_SIZE': 22,
            'PRIMER_PICK_INTERNAL_OLIGO': 0,
            'PRIMER_MIN_SIZE': 18,
            'PRIMER_MAX_SIZE': 25,
            'PRIMER_OPT_TM': 60.0,
            'PRIMER_MIN_TM': 57.0,
            'PRIMER_MAX_TM': 63.0,
            'PRIMER_MIN_GC': 40.0,
            'PRIMER_MAX_GC': 60.0,
            'PRIMER_PRODUCT_SIZE_RANGE': [[200, len(dna)]]
        }
    )
    return primers

# -----------------------------
# SnapGene Export (Minimal)
# -----------------------------
def export_snapgene(dna_seq):
    content = f""";SnapGene DNA File
LOCUS       Insert        {len(dna_seq)} bp    DNA
ORIGIN
"""
    for i in range(0, len(dna_seq), 60):
        content += dna_seq[i:i+60] + "\n"
    content += "//"

    b64 = base64.b64encode(content.encode()).decode()
    return b64

# -----------------------------
# Visualization
# -----------------------------
def plot_diagram(dna_len, f_len, r_start):
    features = [
        GraphicFeature(0, dna_len, strand=+1, label="Gene", color="#ffd966"),
        GraphicFeature(0, f_len, strand=+1, label="Forward Primer", color="#6fa8dc"),
        GraphicFeature(r_start, dna_len, strand=-1, label="Reverse Primer", color="#e06666")
    ]
    record = GraphicRecord(sequence_length=dna_len, features=features)
    ax, _ = record.plot(figure_width=10)
    st.pyplot(ax.figure)

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(layout="wide")
st.title("Protein → Codon-Optimized Primer Designer")

protein = st.text_area("Paste Protein Sequence (single-letter code)")
host = st.selectbox("Expression Host", ["ecoli", "yeast"])

if st.button("Generate DNA & Primers"):
    protein = protein.replace("\n","").replace(" ","").upper()
    dna = back_translate(protein, host)

    primers = design_primers_primer3(dna)

    fwd = primers["PRIMER_LEFT_0_SEQUENCE"]
    rev = primers["PRIMER_RIGHT_0_SEQUENCE"]

    st.subheader("Codon-Optimized DNA")
    st.code(dna)

    col1, col2 = st.columns(2)
    col1.metric("Forward Primer Tm", round(primers["PRIMER_LEFT_0_TM"],2))
    col2.metric("Reverse Primer Tm", round(primers["PRIMER_RIGHT_0_TM"],2))

    st.subheader("Primer Sequences")
    st.code(f"Forward: {fwd}\nReverse: {rev}")

    plot_diagram(len(dna), len(fwd), len(dna)-len(rev))

    snap = export_snapgene(dna)
    st.download_button(
        "Download SnapGene (.dna)",
        data=base64.b64decode(snap),
        file_name="insert.dna"
    )
