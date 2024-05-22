lst=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
sum_list=[]
for i in lst:
    sum=0
    for j in i:
        sum=sum+j
    sum_list.append(sum)
print(lst[sum_list.index(max(sum_list))])
