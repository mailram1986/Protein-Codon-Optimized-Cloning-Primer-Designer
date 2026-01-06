# ================================
# Streamlit configuration
# MUST be first Streamlit command
# ================================
import streamlit as st
st.set_page_config(layout="wide")

# ================================
# Standard imports
# ================================
from io import StringIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

# ================================
# Core module imports
# ================================
from core.codon import back_translate
from core.primer_design import design_primers
from core.visualization import plot_gene_with_primers
from core.snapgene_export import export_snapgene

# ================================
# CONSTANTS
# ================================
RESTRICTION_SITES = {
    "NdeI": "CATATG",
    "XhoI": "CTCGAG",
    "EcoRI": "GAATTC",
    "BamHI": "GGATCC"
}

HIS_TAG_DNA = "CATCACCATCACCATCAC"  # 6×His (DNA)
STOP_CODON = "TAA"

SIGNAL_PEPTIDES = {
    "None": "",
    "PelB (E. coli)": "ATGAAATACCTGCTGCCGACGCTGCTGCTGCTGCTG"
}

# ================================
# TEST DATASET
# ================================
TEST_SEQS = {
    "TEST1 – E. coli enzyme":
        "MKKLSTAVLALAPALAADKSELVQKAKLAEELGADVVAVSTSKGG",
    "TEST2 – Secreted protein":
        "MKAILVVLLYTFATANADQAADKQLAEELKNTLAG",
    "TEST3 – Longer domain":
        "MSTAVLEQLKELGADVIVSTSKGGVKELGATVVAVGQDTLAGRLAD"
}

# ================================
# SIDEBAR – TEST DATASET
# ================================
st.sidebar.header("Test Dataset")

selected_test = st.sidebar.selectbox(
    "Load example protein sequence",
    ["None"] + list(TEST_SEQS.keys())
)

# ================================
# MAIN UI
# ================================
st.title("Protein → Codon-Optimized Cloning & Primer Designer")

protein_seq = st.text_area(
    "Paste Protein Sequence (single-letter amino acid code)",
    height=150
)

if selected_test != "None":
    protein_seq = TEST_SEQS[selected_test]

host = st.selectbox(
    "Expression Host (Codon Usage)",
    ["ecoli", "yeast"]
)

signal_choice = st.selectbox(
    "Signal Peptide",
    list(SIGNAL_PEPTIDES.keys())
)

add_histag = st.checkbox("Add C-terminal 6×His-tag")

st.subheader("Restriction Cloning Options")
enzyme_5 = st.selectbox("5′ Restriction Enzyme", list(RESTRICTION_SITES.keys()))
enzyme_3 = st.selectbox("3′ Restriction Enzyme", list(RESTRICTION_SITES.keys()))

# ================================
# RUN PIPELINE
# ================================
if st.button("Generate Cloning-Ready Primers"):

    # ----------------------------
    # Input sanitation
    # ----------------------------
    protein_seq = protein_seq.replace("\n", "").replace(" ", "").upper()

    if len(protein_seq) < 20:
        st.error("Protein sequence is too short for reliable primer design.")
        st.stop()

    # ----------------------------
    # Back-translation
    # ----------------------------
    dna_core = back_translate(protein_seq, host)

    # ----------------------------
    # Add signal peptide
    # ----------------------------
    dna = SIGNAL_PEPTIDES[signal_choice] + dna_core

    # ----------------------------
    # Add His-tag + stop codon
    # ----------------------------
    if add_histag:
        dna += HIS_TAG_DNA + STOP_CODON
    else:
        dna += STOP_CODON

    # ----------------------------
    # Primer3 design
    # ----------------------------
    primers = design_primers(dna)

    fwd = primers["forward_seq"]
    rev = primers["reverse_seq"]

    # ----------------------------
    # Add restriction sites
    # ----------------------------
    fwd_cloning = RESTRICTION_SITES[enzyme_5] + fwd
    rev_cloning = RESTRICTION_SITES[enzyme_3] + rev

    # ============================
    # OUTPUTS
    # ============================
    st.subheader("Final Insert DNA (5′ → 3′)")
    st.code(dna)

    st.subheader("Cloning Primers (5′ → 3′)")
    st.code(
        f"Forward ({enzyme_5}): {fwd_cloning}\n"
        f"Reverse ({enzyme_3}): {rev_cloning}"
    )

    col1, col2 = st.columns(2)
    col1.metric("Forward Tm (°C)", round(primers["forward_tm"], 2))
    col2.metric("Reverse Tm (°C)", round(primers["reverse_tm"], 2))

    # ----------------------------
    # Visualization
    # ----------------------------
    fig = plot_gene_with_primers(
        dna_length=len(dna),
        forward_len=len(fwd),
        reverse_len=len(rev),
        title="Primer Binding Diagram"
    )
    st.pyplot(fig)

    # ----------------------------
    # SnapGene export
    # ----------------------------
    snapgene_bytes = export_snapgene(dna, name="Cloning_Insert")

    st.download_button(
        "Download SnapGene (.dna)",
        data=snapgene_bytes,
        file_name="insert.dna"
    )

    # ----------------------------
    # GenBank export (FIXED)
    # ----------------------------
    record = SeqRecord(
        Seq(dna),
        id="Insert",
        name="Cloning_Insert",
        description="Codon-optimized synthetic insert"
    )

    # REQUIRED annotations for GenBank
    record.annotations["molecule_type"] = "DNA"
    record.annotations["topology"] = "linear"
    record.annotations["organism"] = "synthetic construct"
    record.annotations["source"] = "in silico designed sequence"

    gb_buffer = StringIO()
    SeqIO.write(record, gb_buffer, "genbank")

    st.download_button(
        "Download GenBank (.gb)",
        data=gb_buffer.getvalue(),
        file_name="insert.gb"
    )
