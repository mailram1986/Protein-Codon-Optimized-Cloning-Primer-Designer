"""
codon.py
--------
Back-translation with host-specific codon usage.
"""

import random

CODON_USAGE = {
    "ecoli": {
        "A": ["GCG", "GCC", "GCA"],
        "C": ["TGC", "TGT"],
        "D": ["GAT", "GAC"],
        "E": ["GAA", "GAG"],
        "F": ["TTT", "TTC"],
        "G": ["GGT", "GGC", "GGA"],
        "H": ["CAT", "CAC"],
        "I": ["ATT", "ATC"],
        "K": ["AAA", "AAG"],
        "L": ["CTG", "TTA", "TTG"],
        "M": ["ATG"],
        "N": ["AAT", "AAC"],
        "P": ["CCG", "CCA"],
        "Q": ["CAA", "CAG"],
        "R": ["CGT", "CGC"],
        "S": ["TCG", "TCC"],
        "T": ["ACC", "ACA"],
        "V": ["GTG", "GTT"],
        "W": ["TGG"],
        "Y": ["TAT", "TAC"],
        "*": ["TAA"]
    },
    "yeast": {
        "A": ["GCT", "GCC"],
        "C": ["TGT", "TGC"],
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

def back_translate(protein_seq: str, host: str = "ecoli") -> str:
    """
    Back-translate protein sequence into codon-optimized DNA.
    """
    protein_seq = protein_seq.upper()
    dna = ""

    for aa in protein_seq:
        if aa not in CODON_USAGE[host]:
            raise ValueError(f"Unsupported amino acid: {aa}")
        dna += random.choice(CODON_USAGE[host][aa])

    return dna
