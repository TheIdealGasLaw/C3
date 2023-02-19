cals = 0
elf_cals_total = []
with open("C3/day_1/p1_input.txt", 'r') as f:
    for line in f:
        if line != "\n":
            cals = cals + int(line)

        else:
            elf_cals_total.append(cals)
            cals = 0

print(max(elf_cals_total))

ect_sorted = sorted(elf_cals_total, reverse=True)

print(ect_sorted[0] + ect_sorted[1] + ect_sorted[2])