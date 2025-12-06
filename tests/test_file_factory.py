from biopackage.file_factory import FileHandler
from tests.input_file_fasta import FastaFileTest

def test_file_handler_read_fasta():
    fasta_test = FastaFileTest()
    fasta_test.write()
    sequences = FileHandler.read(fasta_test.path, ext="fasta")
    fasta_test.remove()
    assert len(sequences) == 3
    assert FileHandler.write(sequences, "tests/test.fasta") == True
    fasta_test.remove()

def run_tests():
    print("Running File Factory tests...")
    test_file_handler_read_fasta()
    print("Done!")

if __name__ == "__main__":
    run_tests()