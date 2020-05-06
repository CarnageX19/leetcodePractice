n=input().split()
max_so_far=-696969
max_right_now=0
for i in n:
    max_right_now+=int(i)
    if max_right_now>max_so_far:
        max_so_far=max_right_now
    if max_right_now<0:
        max_right_now=0
print(max_so_far)
