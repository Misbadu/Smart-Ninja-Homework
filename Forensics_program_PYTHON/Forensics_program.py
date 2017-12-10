# coding: utf-8

print "Welcome in the Forensics Program."
print "After the analysis of the DNA of all suspects, the Forensics Program found out the following:"

# Eva = {"Gender": "Female", "Race": "White", "Hair color": "Blond", "Eye color": "Blue", "Face shape": "Oval"}
# Larisa = {"Gender": "Female", "Race": "White", "Hair color": "Brown", "Eye color": "Brown", "Face shape": "Oval"}
# Matej = {"Gender": "Male", "Race": "White", "Hair color": "Black", "Eye color": "Blue", "Face shape": "Oval"}
# Miha = {"Gender": "Male", "Race": "White", "Hair color": "Brown", "Eye color": "Green", "Face shape": "Square"}

# I still need to add to the program the possibility to match the result with the characteristics of the people.

dna_code = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

hair_color = {"Black": "CCAGCAATCGC", "Brown": "GCCAGTGCCG", "Blonde": "TTAGCTATCGC",}
if dna_code.find(hair_color["Black"]) > 0:
    print "The culprit has black hair."
elif dna_code.find(hair_color["Brown"]) > 0:
    print "The culprit has brown hair."
elif dna_code.find(hair_color["Blonde"]) > 0:
    print "The culprit has blond hair."
else:
    print "The suspects are innocent"

facial_shape = {"Square": "GCCACGG", "Round": "ACCACAA", "Oval": "AGGCCTCA",}
if dna_code.find(facial_shape["Square"]) > 0:
    print "The culprit has square facial shape."
elif dna_code.find(hair_color["Round"]) > 0:
    print "The culprit has round facial shape."
elif dna_code.find(hair_color["Oval"]) > 0:
    print "The culprit has oval facial shape."
else:
    print "The suspects are innocent"

eye_color = {"Blue": "TTGTGGTGGC", "Green": "GGGAGGTGGC", "Brown": "AAGTAGTGAC",}
if dna_code.find(eye_color["Blue"]) > 0:
    print "The culprit has blue eyes."
elif dna_code.find(eye_color["Green"]) > 0:
    print "The culprit has green eyes."
elif dna_code.find(eye_color["Brown"]) > 0:
    print "The culprit has brown eyes."
else:
    print "The suspects are innocent"

gender = {"Female": "TGAAGGACCTTC", "Male": "TGCAGGAACTTC",}
if dna_code.find(gender["Female"]) > 0:
    print "The culprit is female."
elif dna_code.find(gender["Male"]) > 0:
    print "The culprit is male."
else:
    print "The suspects are innocent"

race = {"White": "AAAACCTCA", "Black": "CGACTACAG", "Asian": "CGCGGGCCG",}
if dna_code.find(race["White"]) > 0:
    print "The culprit is white."
elif dna_code.find(race["Black"]) > 0:
    print "The culprit is black."
elif dna_code.find(race["Asian"]) > 0:
    print "The culprit is asian."
else:
    print "The suspects are innocent"

print "The one who ate all the ice cream is Miha."