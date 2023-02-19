cals = 0
elf_cals_total = []
with open("C3/day_1/p1_input.txt", 'r') as f:
    for line in f:
        if line != "\n":
            cals = cals + int(line)

        else:
            elf_cals_total.append(cals)

print(max(elf_cals_total))