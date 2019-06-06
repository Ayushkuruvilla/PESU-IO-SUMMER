num=list()
lim=input("Enter the number of elements you want")
print("Enter the numbers")
for i in range(int(lim)):
 ele=input("Number:")
 num.append(int(ele))
n=int(input("Enter the number to be searched for"))
l=0
h=len(num)
flag=False
while l<=h:
    mid=(l+h)//2
    if num[mid]==n:
     print("Number found")
     flag=True
     break;
    elif num[mid]<n:
     l=mid+1
    else :
     h=mid-1
if flag==False:
    print("Number not found")
    
