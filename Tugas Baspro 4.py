# Perkalian Matriks 5x5 Menggunakan Nested List

M1 = [
    [1,3,2,4,2],
    [2,6,5,1,4],
    [2,4,3,7,6],
    [5,4,1,3,2],
    [3,6,9,8,1],
]

M2 = [
    [2,1,3,9,2],
    [1,4,7,6,5],
    [1,2,3,6,7],
    [6,5,7,3,1],
    [4,3,1,2,5],
]

M3 = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]

# Mengalikan Matriks 5x5

for m in range(len(M1)) :
    for n in range(len(M2)) :
        M3 [m][n] = M1 [m][n] * M2 [m][n]


# Print Matriks

print("Matriks M1 : ")
for row in M1 :
    print(row)

print("\nMatriks M2 : ")
for row in M2 :
    print(row)

print("\nPerkalian dari Matriks M1 dan Matriks M2 adalah : ")
for row in M3 :
    print(row)