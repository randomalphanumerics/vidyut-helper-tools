from vidyut.kosha import Kosha
from vidyut.lipi import detect, transliterate, Scheme
from vidyut.prakriya import *

kosha = Kosha("./data-0/kosha")
data = Data("./data-0/prakriya/")
code_to_sutra = {(s.source, s.code): s.text for s in data.load_sutras()}
input_word = input("enter word to lookup: ")
output = transliterate(input_word, detect(input_word), Scheme.Slp1)


array = kosha.get(output)
for entry in array:
    print(entry)
to_derive = int(input("Which word index do you wish to derive: "))

v = Vyakarana()

entry = array[to_derive - 1]

print(entry.pratipadika_entry.dhatu_entry)
print(entry.pratipadika_entry.dhatu_entry.artha_en)

prakriyas = v.derive(entry)

for prakriya in prakriyas:
    print(prakriya.text)
    print('===================')
    for step in prakriya.history:
        result = ' + '.join(step.result)
        key = (step.source, step.code)

        sutra = code_to_sutra.get(key, "(missing)")
        print("{:<10}: {:<15} {}".format(step.code, result, transliterate(sutra, Scheme.Slp1, Scheme.Iso15919)))

