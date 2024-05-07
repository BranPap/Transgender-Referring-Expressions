breitbartNgrams = [687, 639, 511, 319, 375, 306, 332, 328, 1811, 232]

PinkNewsNgrams = [1834, 1549, 423, 509, 193, 385, 162, 216, 229, 499]

BreitbartOut = []
PinkNewsOut = []

for item in breitbartNgrams:
    wpm = item/8831627*1000000
    BreitbartOut.append(wpm)

for item in PinkNewsNgrams:
    wpm = item/5829504*1000000
    PinkNewsOut.append(wpm)

print(BreitbartOut)
print(PinkNewsOut)
