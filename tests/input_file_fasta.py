
import os

fasta_content = """>seq1 Description of sequence 1
ATCGTAGCTAGCTAGC
>seq2 Description of sequence 2
AUCGAUGCUAGCUAGC
>seq3 Description of sequence 3
ACDEFGHIKLMNPQRSTVWY
"""

class File():
    def __init__(self):
        self.path = ""
        self.content: str = ""
    
    def write(self) -> bool:
        with open(self.path, 'w') as file:
            file.write(self.content)
        return True
    
    def remove(self) -> bool:
        if os.path.exists(self.path):
            os.remove(self.path)
            return True
        return False

class FastaFileTest(File):
    def __init__(self):
        super().__init__()
        self.path = "tests/test.fasta"
        self.content = fasta_content
