from biopackage.alphabet import DNAAlphabet, RNAAlphabet, ProteinAlphabet, CustomAlphabet
from biopackage.sequence import DNASeq, RNASeq, ProteinSeq, CustomSeq

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