from biopackage.alphabet import Alphabet, DNAAlphabet, RNAAlphabet, ProteinAlphabet

def test_dna_alphabet():
    dna_alphabet = DNAAlphabet()
    assert repr(dna_alphabet) == "Alphabet(name=dna, symbols=['A', 'C', 'G', 'T'])"
    assert isinstance(dna_alphabet, Alphabet)

def test_rna_alphabet():
    rna_alphabet = RNAAlphabet()
    assert repr(rna_alphabet) == "Alphabet(name=rna, symbols=['A', 'C', 'G', 'U'])"
    assert isinstance(rna_alphabet, Alphabet)   

def test_protein_alphabet():
    protein_alphabet = ProteinAlphabet()
    assert repr(protein_alphabet) == ("Alphabet(name=ptn, symbols=['A', 'R', 'N', 'D', "
                                      "'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', "
                                      "'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'])")
    assert isinstance(protein_alphabet, Alphabet)

def run_tests():
        
        print("Running Alphabet tests...")

        tests = [
            test_dna_alphabet,
            test_rna_alphabet,
            test_protein_alphabet
        ]
        for test in tests:
            test()
        
        print("Done!")


if __name__ == "__main__":
    run_tests()