PYTHON = python3
export PYTHONPATH = .

test-alphabet:
	$(PYTHON) tests/test_alphabet.py

test-sequence:
	$(PYTHON) tests/test_sequence.py

test-sequence-record:
	$(PYTHON) tests/test_sequence_record.py

test-sequence-factory:
	$(PYTHON) tests/test_sequence_factory.py

test-file-validator:
	$(PYTHON) tests/test_file_validator.py

test-file-factory:
	$(PYTHON) tests/test_file_factory.py

test:
	@echo "----------------------------------"
	@echo "Rodando testes."
	@echo "----------------------------------"
	$(PYTHON) tests/test_alphabet.py
	$(PYTHON) tests/test_sequence.py
	$(PYTHON) tests/test_sequence_record.py
	$(PYTHON) tests/test_sequence_factory.py
	$(PYTHON) tests/test_file_validator.py
	$(PYTHON) tests/test_file_factory.py
	@echo "----------------------------------"
	@echo "Todos os testes foram concluídos."
	@echo "----------------------------------"