
from biopackage.sequence import DNASeq, RNASeq, ProteinSeq
from biopackage.sequence_record import SeqObj, SeqMultiObj

def test_seq_obj():
    seq_obj_dna = SeqObj(sequence=DNASeq("ACGT"), id="seq1", description="Test DNA sequence")
    assert isinstance(seq_obj_dna, SeqObj)
    assert repr(seq_obj_dna) == "SeqObj(id='seq1', description='Test DNA sequence', seq=DNASeq('ACGT'))"

    seq_obj_rna = SeqObj(sequence=RNASeq("ACGU"), id="seq2", description="Test RNA sequence")
    assert isinstance(seq_obj_rna, SeqObj)
    assert repr(seq_obj_rna) == "SeqObj(id='seq2', description='Test RNA sequence', seq=RNASeq('ACGU'))"

    seq_obj_protein = SeqObj(sequence=ProteinSeq("ACDEFGHIK"), id="seq3", description="Test Protein sequence")
    assert isinstance(seq_obj_protein, SeqObj)
    assert repr(seq_obj_protein) == "SeqObj(id='seq3', description='Test Protein sequence', seq=ProteinSeq('ACDEFGHIK'))"

def test_seq_multi_obj():
    seq1 = SeqObj(sequence=DNASeq("ACGT"), id="seq1", description="Test DNA sequence 1")
    seq2 = SeqObj(sequence=RNASeq("ACGU"), id="seq2", description="Test RNA sequence 2")
    seq3 = SeqObj(sequence=ProteinSeq("ACDEFGHIK"), id="seq3", description="Test Protein sequence 3")
    multi_obj = SeqMultiObj(sequences=[seq1, seq2, seq3])  # Exclude last to test length 2
    
    assert len(multi_obj) == 3
    assert multi_obj[0] == seq1
    assert multi_obj[1] == seq2
    assert multi_obj[2] == seq3
    assert repr(multi_obj) == f"SeqMultiObj(sequences={repr([seq1, seq2, seq3])})"

def run_tests():
        
        print("Running Sequence Record tests...")

        tests = [
            test_seq_obj,
            test_seq_multi_obj
        ]
        for test in tests:
            test()
        
        print("Done!")

if __name__ == "__main__":
    run_tests()