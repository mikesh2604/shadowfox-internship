import random
rolls = 20

count_for_6 = 0
count_for_1 = 0
two_6s_in_row = 0

last_roll = 0

for i in range(rolls):
    roll = random.randint(1,6)
    print("Roll",i+1, ":", roll)

    if roll == 6:
       count_for_6 += 1
    if roll == 1:
       count_for_1 += 1
    if last_roll == 6 and roll == 6:
       two_6s_in_row += 1

    last_roll = roll
print("Number of times 6 was rolled:", count_for_6)
print("Number of times 1 was rolled:", count_for_1)
print("Number of times two 6s came in a row:", two_6s_in_row)