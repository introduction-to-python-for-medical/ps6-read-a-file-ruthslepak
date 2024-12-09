file_path = "/content/data/codons.txt"
def create_codon_dict(file_path):
  codons_acids = {}
  with open(file_path, 'r') as file:
    for row in file:
      row = row.strip().split('\t')
      codon = row[0]
      amino_acid = row[2]
      codons_acids[codon] = amino_acid
  return codons_acids
 

