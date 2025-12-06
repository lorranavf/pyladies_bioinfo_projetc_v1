from biopackage.alphabet import Alphabet, DNAAlphabet, RNAAlphabet, ProteinAlphabet, CustomAlphabet

class BaseSeq():
    """Class representing a biological sequence."""
    def __init__(self, sequence: str, alphabet: Alphabet):
        self.sequence = sequence
        self.ALPHABET = alphabet

    def alphabet(self):
        return self.ALPHABET.__class__.__name__
    
    def length(self):
        return len(self.sequence)
    
    def __str__(self):
        return f"{self.__class__.__name__}('{self.sequence}')"
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.sequence}')"

class DNASeq(BaseSeq):
    """Class representing a DNA sequence."""
    def __init__(self, sequence: str):
        super().__init__(sequence, DNAAlphabet())

class RNASeq(BaseSeq):
    """Class representing an RNA sequence."""
    def __init__(self, sequence: str):
        super().__init__(sequence, RNAAlphabet())

class ProteinSeq(BaseSeq):
    """Class representing a Protein sequence."""
    def __init__(self, sequence: str):
        super().__init__(sequence, ProteinAlphabet())

class CustomSeq(BaseSeq):
    """Class representing a custom sequence defined by the user."""
    def __init__(self, sequence: str, alphabet: CustomAlphabet):
        super().__init__(sequence, alphabet)

# print("sequence.py loaded successfully.")