def hammingWeight(n):
    k=list(bin(n))
    total=0
    for i in range(2,len(k)):
        if k[i] == '1':
            total+=1
    print(total)
hammingWeight(3)
        