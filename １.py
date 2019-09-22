# 3位数，１，２，３，４进行组合，不重复的共有几个
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=j) and (i!= k) and (j!=k):
                print(i,j,k)
