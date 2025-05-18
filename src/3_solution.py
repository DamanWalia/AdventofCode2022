FILEPATH = "./input/3_input.txt"

# solution for part 1
with open(FILEPATH) as input:
    items = []
    sum_prior = 0
    for rucksack in input:
        subitem = []
        r_part1, r_part2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:] # divide compartments
        for c1 in r_part1:
            for c2 in r_part2:
                if c2 == c1 and c2 not in subitem:
                    subitem.append(c2)
                    if c2.islower():
                        sum_prior += ord(c2)-97+1 # normalizing ASCII for lowercase
                    else: 
                        sum_prior += ord(c2)-65+27 # normalizing ASCII for uppercase
        items.append(subitem)
print("Total of the priorities is %d." %sum_prior)

# solution for part 2
with open(FILEPATH) as input:
    items = []
    sum_prior = 0
    counter = 0
    for rucksack1, rucksack2, rucksack3 in zip(input, input, input):
        common_items = set(rucksack1.strip()).intersection(rucksack2.strip(), rucksack3.strip())
        for c in common_items:
            if c.islower():
                sum_prior += ord(c)-97+1 # normalizing ASCII for lowercase
            else: 
                sum_prior += ord(c)-65+27 # normalizing ASCII for uppercase
print("Total of the priorities is %d." %sum_prior)