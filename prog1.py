str = "ARR"
chr_A = [[" " for i in range (3)] for j in range (6)]
chr_R = [[" " for i in range (3)] for j in range (6)]
chr_R1 = [[" " for i in range (3)] for j in range (6)]

#for letter A
for r in range (6):
    for c in range (3):
        if (c == 0 and r > 0) or (c == 1 and r == 0) or (c == 1 and r == 3) or (c == 2 and r > 0):
            chr_A [r][c] = "*"

#for letter R
for r in range (6):
    for c in range (3):
        if (c == 0) or (c == 1 and (r == 0 or r == 3) ) or (c == 2 and r != 0) and (c == 2 and r != 3):
            chr_R [r][c] = "*"

#for second letter R
for r in range (6):
    for c in range (3):
        if (c == 0) or (c == 1 and (r == 0 or r == 3) ) or (c == 2 and r != 0) and (c == 2 and r != 3):
            chr_R1 [r][c] = "*"

for j in range (6):
    for i in range (3):
        print(chr_A[j][i], end = " ")
    print (end = "  ")
    for i in range (3):
        print (chr_R[j][i], end = " ")
    print (end = "  ")
    for i in range (3):
        print (chr_R1[j][i], end = " ")
    print ()
