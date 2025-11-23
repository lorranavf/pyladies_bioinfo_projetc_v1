from .alphabet import Alphabet, DNAAlphabet, RNAAlphabet, ProteinAlphabet, CustomAlphabet

class BaseSeq():
    """Class representing a biological sequence."""
    def __init__(self, sequence: str, alphabet: Alphabet):
        self.sequence = sequence
        self.alphabet = alphabet

    def which_alphabet(self):
        return self.alphabet.name
    
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

    def gc_content(self):
        pass

    def reverse_complement(self):
        pass

    def transcribe(self):
        pass

class RNASeq(BaseSeq):
    """Class representing an RNA sequence."""
    def __init__(self, sequence: str):
        super().__init__(sequence, RNAAlphabet())

    def gc_content(self):
        pass

    def reverse_transcribe(self):
        pass

    def translate(self):
        pass

class ProteinSeq(BaseSeq):
    """Class representing a Protein sequence."""
    def __init__(self, sequence: str):
        super().__init__(sequence, ProteinAlphabet())

class CustomSeq(BaseSeq):
    """Class representing a custom sequence defined by the user."""
    def __init__(self, sequence: str, alphabet: CustomAlphabet):
        super().__init__(sequence, alphabet)

class SeqHandler():
    """Class that receives a str and attributes it with the corresponding type Seq."""
    def __new__(cls, sequence: str, alphabet: CustomAlphabet = None):
        
        if cls is SeqHandler:
            
            if all(base in DNAAlphabet().symbols for base in sequence):
                return DNASeq(sequence)
            
            if all(base in RNAAlphabet().symbols for base in sequence):
                return RNASeq(sequence)
            
            if all(residue in ProteinAlphabet().symbols for residue in sequence):
                return ProteinSeq(sequence)

            if alphabet is not None:
                if all(sym in alphabet.symbols for sym in sequence):
                    return CustomSeq(sequence, alphabet)
                raise ValueError("Sequence contains invalid characters for the provided custom alphabet.")
            
            raise ValueError("Sequence contains invalid characters for DNA, RNA, or Protein alphabets.")
        return super().__new__(cls)

class SeqObj():
    """Class representing a sequence record with metadata."""
    def __init__(self, sequence: BaseSeq, id: str = "", description: str = ""):
        self.sequence = sequence
        self.id = id
        self.description = description

    def __repr__(self):
        return f"SeqObj(id='{self.id}', description='{self.description}', seq={repr(self.sequence)})"
    
class SeqMultiObj():
    """Class representing multiple sequence records."""
    def __init__(self, sequences: list[SeqObj]):
        self.sequences = sequences

    def __len__(self):
        return len(self.sequences)
    
    def __getitem__(self, index):
        return self.sequences[index]
    
    def __repr__(self):
        return f"SeqMultiObj(sequences={repr(self.sequences)})"