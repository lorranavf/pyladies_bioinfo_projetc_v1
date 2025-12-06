from biopackage.sequence_factory import SeqHandler

def test_sequence_factory():
    dna_seq = SeqHandler("ATCGTAGCTAGCTAGC")
    assert dna_seq.__class__.__name__ == "DNASeq"

    rna_seq = SeqHandler("AUCGAUGCUAGCUAGC")
    assert rna_seq.__class__.__name__ == "RNASeq"
    protein_seq = SeqHandler("ACDEFGHIKLMNPQRSTVWY")
    assert protein_seq.__class__.__name__ == "ProteinSeq"

    try:
        invalid_seq = SeqHandler("ATCGX")
    except ValueError as e:
        assert str(e) == "Sequence contains invalid characters for DNA, RNA, or Protein alphabets."


def run_tests():
    print("Running Sequence Factory tests...")
    test_sequence_factory()
    print("Done!")

if __name__ == "__main__":
    run_tests()