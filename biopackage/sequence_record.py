from biopackage.sequence import BaseSeq

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