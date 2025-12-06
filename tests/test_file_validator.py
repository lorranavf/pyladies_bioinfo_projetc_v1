from biopackage.file import FileValidator, FastaValidator

from tests.input_file_fasta import FastaFileTest

def test_fasta_validator():
    fasta_test = FastaFileTest()
    fasta_test.write()
    validator = FastaValidator(path=fasta_test.path, ext="fasta")
    assert validator.validate_file() == True
    assert len(validator.sequences) == 3
    fasta_test.remove()

def run_tests():
    print("Running File Validator tests...")
    test_fasta_validator()
    print("Done!")

if __name__ == "__main__":
    run_tests()