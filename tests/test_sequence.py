from biopackage.sequence import BaseSeq, DNASeq, RNASeq, ProteinSeq

def test_dna_sequence():
    dna_seq = DNASeq("ACGTAGCTAG")
    assert isinstance(dna_seq, BaseSeq)
    assert repr(dna_seq) == "DNASeq('ACGTAGCTAG')"

def test_rna_sequence():
    rna_seq = RNASeq("ACGUAGCUAG")
    assert isinstance(rna_seq, BaseSeq)
    assert repr(rna_seq) == "RNASeq('ACGUAGCUAG')"

def test_protein_sequence():
    protein_seq = ProteinSeq("ACDEFGHIKLMNPQRSTVWY")
    assert isinstance(protein_seq, BaseSeq)
    assert repr(protein_seq) == "ProteinSeq('ACDEFGHIKLMNPQRSTVWY')"

def run_tests():
        
        print("Running Sequence tests...")

        tests = [
            test_dna_sequence,
            test_rna_sequence,
            test_protein_sequence
        ]
        for test in tests:
            test()
        
        print("Done!")

if __name__ == "__main__":
    run_tests()