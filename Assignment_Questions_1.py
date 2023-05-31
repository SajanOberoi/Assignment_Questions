# Question-1
def indices(li,tar):
    for i in range(len(li)):
        for j in range(i,(len(li))):
            if li[i]+li[j]==tar or li[i]*li[j]==tar or abs(li[i]-li[j])==tar or li[i]/li[j]==tar or li[j]/li[i]==tar:
                return [i,j]


# Question-2
def occurrences(li,k):
    count=0
    for i in range(len(li)):
        if li[i]==k:
            del(li[i])
            li.append('_')
            count+=1
    print(len(li)-count,', nums = ',li)



# Question-3
def distinct(li,k):
    count=0
    for i in range(len(li)):
        if li[i]==k:
            return i
        elif li[i]>k:
            return i



# Question-4
def for_9(li):
    last=len(li)-1
    while li[last]==9:
        li[last]=0
        last=last-1
    if last<=0:
        li=[1]+li
        return li
    else:
        li[last]=li[last]+1
        return li



# Question-5
def concat_list(li1,li2,m,n):
    li1=li1[:m]
    li1=li1+li2
    li1=sorted(li1)
    return li1



# Question-6
def dup(li):
    if len(li)==len(set(li)):
        return True
    else:
        return False



# Question-7
def relative(li):
    for i in range(len(li)):
        if li[i]==0:
            del(li[i])
            li.append(0)
    return li



# Question-8
def occurs(li):
    for i in range(len(li)):
        if li[i+1]!=li[i]+1:
            return [li[i],li[i]+1]