def bin_search(n,l):
    beg=0
    end=len(l)-1
    mid=len(l)//2
    while beg<=end:
        if n>l[mid]:
            beg=mid+1
            mid=(beg+end)//2
        elif n<l[mid]:
            end=mid-1
            mid=(beg+end)//2
        else:
            return mid
    return -1

l=list(map(int,input("Enter integers to form a list : ").split()))
n=int(input("Enter number to be searched : "))
if bin_search(n,l)==-1:
    print("number not found")
else:
    print("The number {0} is at index {1}!!".format(n,bin_search(n,l)))

input("press Enter to quit")
