from abc import abstractmethod
from os import path

from biopackage.sequence_factory import SeqHandler
from biopackage.sequence_record import SeqObj, SeqMultiObj

class FileValidator():
    def __init__(self, path: str, ext: str = "fasta"):
        self.path = path
        self.ext = ext
        self.sequences: SeqMultiObj = None
        self.content: str = ""
        self.supported_exts = ["fasta", "fa", "faa", "fna"]

    def validate_path(self) -> bool:
        if not path.exists(self.path):
            raise FileNotFoundError(f"The file at {self.path} does not exist.")
        
    def validate_extension(self) -> bool:

        if self.ext not in self.supported_exts:
            raise ValueError(f"The extension .{self.ext} is not supported. Supported extensions are: {', '.join(self.supported_exts)}.")
        
        if not self.path.endswith(f".{self.ext}"):
            raise ValueError(f"The file at {self.path} does not have the correct .{self.ext} extension.")
            
    def read_file(self):
        with open(self.path, 'r') as file:
            content = file.read()
            self.content = content
        return True
    
    @abstractmethod
    def validate_content(self):
        pass

    @abstractmethod
    def parse_file(self):
        pass

    def validate_file(self) -> bool:
        self.validate_path()
        self.validate_extension()
        self.read_file()
        self.validate_content()
        self.parse_file()
        return True

class FastaValidator(FileValidator):

    def validate_content(self):
        lines = self.content.strip().split('\n')
        
        if not lines[0].startswith('>'):
            raise ValueError("The FASTA file is not properly formatted. The first line must start with '>'.")
        
        for i in range(1, len(lines)):
            if lines[i].startswith('>'):
                continue
            if not all(char.isalnum() or char in "-._" for char in lines[i]):
                raise ValueError(f"Invalid characters found in sequence line: {lines[i]}")
        
    def parse_file(self) -> SeqMultiObj:
        lines = self.content.strip().split('\n')
        sequences = []
        seq_id = ""
        description = ""
        seq_lines = []

        for line in lines:
            if line.startswith('>'):
                if seq_lines:
                    sequence_str = ''.join(seq_lines)
                    sequence = SeqHandler(sequence_str)
                    sequences.append(SeqObj(sequence, seq_id, description))
                    seq_lines = []
                header_parts = line[1:].split(' ', 1)
                seq_id = header_parts[0]
                description = header_parts[1] if len(header_parts) > 1 else ""
            else:
                seq_lines.append(line.strip())
        
        if seq_lines:
            sequence_str = ''.join(seq_lines)
            sequence = SeqHandler(sequence_str)
            sequences.append(SeqObj(sequence, seq_id, description))
            self.sequences = SeqMultiObj(sequences)
        
