"""
primer_design.py
----------------
Primer design using Primer3 thermodynamics.
"""

import primer3

def design_primers(dna_seq: str,
                   product_min: int = 150,
                   product_max: int = None) -> dict:
    """
    Design primers using Primer3.
    Returns Primer3 output dictionary.
    """

    if product_max is None:
        product_max = len(dna_seq)

    primers = primer3.bindings.designPrimers(
        {
            'SEQUENCE_TEMPLATE': dna_seq
        },
        {
            'PRIMER_OPT_SIZE': 22,
            'PRIMER_MIN_SIZE': 18,
            'PRIMER_MAX_SIZE': 25,
            'PRIMER_OPT_TM': 60.0,
            'PRIMER_MIN_TM': 57.0,
            'PRIMER_MAX_TM': 63.0,
            'PRIMER_MIN_GC': 40.0,
            'PRIMER_MAX_GC': 60.0,
            'PRIMER_PICK_INTERNAL_OLIGO': 0,
            'PRIMER_PRODUCT_SIZE_RANGE': [[product_min, product_max]]
        }
    )

    if "PRIMER_LEFT_0_SEQUENCE" not in primers:
        raise RuntimeError("Primer3 failed to design primers")

    return {
        "forward_seq": primers["PRIMER_LEFT_0_SEQUENCE"],
        "reverse_seq": primers["PRIMER_RIGHT_0_SEQUENCE"],
        "forward_tm": primers["PRIMER_LEFT_0_TM"],
        "reverse_tm": primers["PRIMER_RIGHT_0_TM"],
        "forward_gc": primers["PRIMER_LEFT_0_GC_PERCENT"],
        "reverse_gc": primers["PRIMER_RIGHT_0_GC_PERCENT"]
    }
