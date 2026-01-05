# Expected Results – Validation Checklist

## Common to All Tests
- Codon-optimized DNA generated
- Forward + reverse primers designed
- Tm between 57–63 °C
- GC between 40–60%
- SnapGene diagram visible
- .dna and .gb export successful

---

## TEST1_ecoli_enzyme
Options:
- Host: ecoli
- Signal peptide: None
- His-tag: Yes
- Enzymes: NdeI / XhoI

Expected:
- ATG start codon
- 6×His tag before stop codon
- Stop codon present (TAA)
- NdeI site at 5′ primer
- XhoI site at 3′ primer

---

## TEST2_secreted_protein
Options:
- Host: ecoli
- Signal peptide: PelB
- His-tag: No
- Enzymes: EcoRI / BamHI

Expected:
- Signal peptide sequence at 5′ end
- No His-tag
- EcoRI / BamHI cloning primers
- Clear signal peptide region in diagram

---

## TEST3_longer_domain
Options:
- Host: yeast
- Signal peptide: None
- His-tag: Yes

Expected:
- Yeast codon bias visible
- Stable primer Tm
- Longer amplicon (>150 bp)
