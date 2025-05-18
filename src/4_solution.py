FILEPATH = "./input/4_input.txt"

# solution for part 1
with open(FILEPATH) as input:
    counter = 0
    for lst_sections in input:
        elf_1, elf_2 = lst_sections.strip().split(",")
        start1, end1 = elf_1.split("-")
        start2, end2 = elf_2.split("-")
        list1 = list(range(int(start1), int(end1)+1))
        list2 = list(range(int(start2), int(end2)+1))
        if set(list1).issubset(list2) or set(list2).issubset(list1):
            counter += 1
print("Total number of pairs that one fully contains the other are %d." %counter)

# solution for part 2
with open(FILEPATH) as input:
    counter = 0
    for lst_sections in input:
        elf_1, elf_2 = lst_sections.strip().split(",")
        start1, end1 = elf_1.split("-")
        start2, end2 = elf_2.split("-")
        list1 = list(range(int(start1), int(end1)+1))
        list2 = list(range(int(start2), int(end2)+1))
        if set(list1).intersection(list2):
            counter += 1
print("Total number of pairs that have some intersection are %d." %counter)