# Project's scope

- Permite a criação de um objeto `seq` genérico (DNA, RNA, PTN) via pacote podendo este ser integrado ao código do usuário.

# Schedule

- [x] Semana I : verificar qual padrão de projeto criacional se adequa à solução proposta
- [x] Semana II: implementar a solução proposta
- [x] Semana III: implementar testes e inserir tratamentos de erros
- [x] Semana IV: revisar implementação e documentação

# Modelagem 

```python

import Seq
import SeqFile

seq_dna = Seq("ATCG")
seq_dna.wich_alphabet == "dna" # True

seq_rna = Seq("AUCG")
seq_rna.wich_alphabet == "rna" # True

seq_ptn = Seq("PDTHCJC")
seq_ptn.wich_alphabet == "ptn" # True

# DNA properties and methods
print(seq_dna.seq())
print(seq_dna.lenght())
print(seq_dna.gc_content())
print(seq_dna.translate())

# RNA properties and methods
print(seq_rna.seq())
print(seq_rna.lenght())
print(seq_rna.gc_content())
print(seq_rna.transcribe())

# PTN properties and methods
print(seq_ptn.seq())
print(seq_ptn.lenght())
print(seq_ptn.molecular_weight())

# Read Fasta File
sequences = SeqFile.read('/data/sequences.fasta')

# Write Fasta File
SeqFile.write(sequences, '/data/project/2025/sequences.fasta')

```