num=int(input())
bi='{0:b}'.format(num)
cnt=len(bi)-1
res=0
for i in bi:
    if i!='1':
        res+=1*pow(2,cnt)
    cnt-=1
print(res)
