"""
snapgene_export.py
------------------
Minimal SnapGene (.dna) export for inserts.
"""

import base64
from textwrap import wrap

def export_snapgene(dna_seq: str,
                    name: str = "Insert") -> bytes:
    """
    Export DNA as a SnapGene-compatible .dna file.
    Returns binary content.
    """

    header = f""";SnapGene DNA File
LOCUS       {name}        {len(dna_seq)} bp    DNA
ORIGIN
"""

    body = "\n".join(wrap(dna_seq.lower(), 60))
    footer = "\n//"

    snapgene_text = header + body + footer
    return snapgene_text.encode("utf-8")

def export_base64(dna_seq: str, name: str = "Insert") -> str:
    """
    Base64 encoded SnapGene content (for web download).
    """
    return base64.b64encode(export_snapgene(dna_seq, name)).decode()
