import pandas

NPA_csv = pandas.read_csv("nato_phonetic_alphabet.csv")

NPA_dict = {row.letter: row.code for (index, row) in NPA_csv.iterrows()}

in_word = input("Enter a word: ").upper()
out_codes = [NPA_dict[letter] for letter in in_word]
print(out_codes)
