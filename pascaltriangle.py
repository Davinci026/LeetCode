def fatorial (number):
    if number == 1 or number == 0:
        return 1
    else:
        return number*fatorial(number-1)
def pascal_triangle(rows):
    triangle=[]
    for i in range(rows):
        triangle.append([0 for j in range(i+1)])
    for k in range(rows):
        for l in range(k+1):
            triangle[k][l]= (fatorial(k)//(fatorial(l)*fatorial(k-l)))
    for row in triangle:
        print(row)  

pascal_triangle(10)