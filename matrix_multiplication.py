rows_a=int(input("Enter the Numbers of rows:"))
column_a=int(input("Enter the Numbers of columns:"))
print("Enter the elements of first Matrix:")
matrix_a=[[int(input()) for i in range(column_a)]
           for i in range(rows_a)]
print("First Matrix is:")
for n in matrix_a:
    print(n)
column_b=int(input("Enter the Numbers of columns for the second matrix:"))
print("Enter the elements of Second Matrix:")
matrix_b=[[int(input())for i in range(column_b)]
    for i in range(column_a)]
print("Second Matrix is:")
for n  in matrix_b:
    print(n)
result=[[0 for i in range(column_b)]
for i in range(rows_a)]
for i in range(len(matrix_a)):
    for j in range(len(matrix_b[0])):
        for k in range(len(matrix_b)):
               result[i][j]+=matrix_a[i][k]*matrix_b[k][j]
print("Matrix_a X Matrix_b is:")
for r in result:
    print(r)
