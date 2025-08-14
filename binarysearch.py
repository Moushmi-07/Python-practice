def binary_search(l,s):
    first=0
    last=len(l)-1
    found=False
    while (first<=last and not found):
        mid=(first+last)//2
        if l[mid]==s:
            found=True
        else:
            if s<l[mid]:
                last=mid-1
            else:
                first=mid+1
    return found
print(binary_search([1,2,3,4,5,6,7,8,9,10],7))
print(binary_search([1,2,3,4,5,6,7,8,9,10],3))
print(binary_search([1,2,3,4,5,6,7,8,9,10],11))
print(binary_search([1,4,8,2,5,7,6],8))
