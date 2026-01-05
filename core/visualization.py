"""
visualization.py
----------------
Gene and primer visualization using dna_features_viewer.
"""

from dna_features_viewer import GraphicFeature, GraphicRecord
import matplotlib.pyplot as plt

def plot_gene_with_primers(dna_length: int,
                           forward_len: int,
                           reverse_len: int,
                           title: str = "Primer Binding Diagram"):
    """
    Plot gene and primers similar to SnapGene.
    """

    features = [
        GraphicFeature(
            start=0,
            end=dna_length,
            strand=+1,
            color="#ffd966",
            label="Gene"
        ),
        GraphicFeature(
            start=0,
            end=forward_len,
            strand=+1,
            color="#6fa8dc",
            label="Forward Primer"
        ),
        GraphicFeature(
            start=dna_length - reverse_len,
            end=dna_length,
            strand=-1,
            color="#e06666",
            label="Reverse Primer"
        )
    ]

    record = GraphicRecord(sequence_length=dna_length, features=features)
    ax, _ = record.plot(figure_width=10)
    ax.set_title(title)

    return ax.figure
