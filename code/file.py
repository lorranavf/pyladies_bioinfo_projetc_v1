from sequence import BaseSeq

class SeqFile():
    def __init__(self, path: str, ext: str = "fasta"):
        self.path = path
        self.ext = ext

    def validate_sequence(self, sequence: BaseSeq):
        pass

    def get_sequences(self) -> list[BaseSeq]:
        pass

    @staticmethod
    def read() -> list[BaseSeq]:
        pass

    @staticmethod
    def write(sequences: list[BaseSeq], path: str) -> True:
        pass
    