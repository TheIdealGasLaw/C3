from itertools import groupby

with open("C3/day_1/p1_input.txt", 'r') as elf_cals:
    elf_cals_list = [i.split('\n', 1)[0] for i in elf_cals.readlines()]  #reads the file and removes the newline characters





###   Solutions I've Tried that didn't work as desired   ###

#elf_cals_index = elf_cals_list.index('')
#elf_cals_split = [elf_cals_list.split(i, 1)[0] for i in elf_cals_index]

##I honestly dont know how this works, I found this solution for spliting the list to a list of lists here:
##https://www.geeksforgeeks.org/python-splitting-list-on-empty-string/
#elf_cals_split = [list(sub) for ele, sub in groupby(elf_cals_list, key = bool) if ele]



print (elf_cals_list)