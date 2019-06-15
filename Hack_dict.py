x=into(input())
temp={}
for i in range(x):
    d1=input().split(" ")
    temp[d1[0]]=d1[1]
white(true):
    srch=input()
    if(srch in temp.keys()):
        print(srch+"="+d1[srch])
    else:
        print("Not found")
