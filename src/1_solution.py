FILEPATH = "./input/1_input.txt"
# solution for part 1 
with open(FILEPATH) as input:
    total_cal = 0 
    max_cal = 0
    for cal in input:
        if cal != "\n":
            total_cal += int(cal)
        else:
            if max_cal < total_cal:
                max_cal = total_cal
            total_cal = 0
    if max_cal < total_cal:
        max_cal = total_cal
print(max_cal)

# solution for part 2
with open(FILEPATH) as input:
    list_cal = []
    total_cal = 0
    for cal in input:
        if cal != "\n":
            total_cal += int(cal)
        else:
            list_cal.append(total_cal)
            total_cal = 0
    list_cal.append(total_cal)
    list_cal.sort(reverse=True)
    print("Sum of calories of top three elves is %d." %(sum(list_cal[0:3])))