
satu = ['ayam', 'angsa', 'sapi', 'domba']
a = len(satu)
print(a)
print(satu)
dua=[0]*4
count=0
for i in range(0,a):
    if count==0:
        dua[0]=satu[a-1]
    elif count==(a-1):
        dua[a-1]=satu[0]
    else:
        dua[count]=satu[count]
    count+=1
print(dua)
print (count)






