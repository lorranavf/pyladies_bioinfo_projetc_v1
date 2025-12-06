from biopackage.sequence_record import SeqMultiObj
from biopackage.file import FastaValidator

class FileHandler():

    supported_exts = ["fasta", "fa", "faa", "fna"]
    fasta_exts = ["fasta", "fa", "faa", "fna"]

    @classmethod
    def read(cls, path: str, ext: str = "fasta") -> SeqMultiObj:

        if not ext in cls.supported_exts:
            raise ValueError(f"File extension .{ext} is not supported.")
        
        if ext in cls.fasta_exts:
            validator = FastaValidator(path, ext)
        
        if validator.validate_file():
            return validator.sequences

    @classmethod
    def write(cls, sequences: SeqMultiObj, path: str) -> bool:
        with open(path, 'w') as file:
            for seq_obj in sequences.sequences:
                file.write(f">{seq_obj.id} {seq_obj.description}\n")
                file.write(f"{seq_obj.sequence.sequence}\n")
        return True
        