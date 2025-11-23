class Alphabet():
    """Base class for different biological alphabets."""
    
    def __init__(self):
        self.name = ""
        self.symbols = []
        self.dictionary = {}
           
class DNAAlphabet(Alphabet):
    """Alphabet for DNA sequences."""

    def __init__(self):
        self.name = "dna"
        self.symbols = ['A', 'C', 'G', 'T']
        self.dictionary = {
        'A': 'Adenine',
        'C': 'Cytosine',
        'G': 'Guanine',
        'T': 'Thymine'
    }

class RNAAlphabet(Alphabet):
    """Alphabet for RNA sequences."""
    def __init__(self):
        self.name = "rna"
        self.symbols = ['A', 'C', 'G', 'U']
        self.dictionary = {
        'A': 'Adenine',
        'C': 'Cytosine',
        'G': 'Guanine',
        'U': 'Uracil'
    }

class ProteinAlphabet(Alphabet):
    """Alphabet for Protein sequences."""
    def __init__(self):
        self.name = "ptn"
        self.symbols = [
            'A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I',
            'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'
        ]
        self.dictionary = {
        'A': 'Alanine',
        'R': 'Arginine',
        'N': 'Asparagine',
        'D': 'Aspartic acid',
        'C': 'Cysteine',
        'Q': 'Glutamine',
        'E': 'Glutamic acid',
        'G': 'Glycine',
        'H': 'Histidine',
        'I': 'Isoleucine',
        'L': 'Leucine',
        'K': 'Lysine',
        'M': 'Methionine',
        'F': 'Phenylalanine',
        'P': 'Proline',
        'S': 'Serine',
        'T': 'Threonine',
        'W': 'Tryptophan',
        'Y': 'Tyrosine',
        'V': 'Valine'
    }

class CustomAlphabet(Alphabet):
    """Alphabet for custom sequences defined by the user."""

    def __init__(self, symbols: list, dictionary: dict, name: str = "custom"):
        self.name = name
        self.symbols = symbols
        self.dictionary = dictionary