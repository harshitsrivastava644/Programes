A = [[1,4,5,],
    [5,8,9],
    [6,7,11]]
print("A=",A)
print("A[1] =",A[1])
print("A[1][2]",A[1][2])
result=[[0,0,0],
       [0,0,0],
       [0,0,0]]
for i in range(len(A)):
  for j in range(len(A[0])):
    result[j][i] = A[i][j]

for r in result:
  print(r)