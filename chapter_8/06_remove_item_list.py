list=['harry','larry','carry','marry','parry','barry','ha']
def rem(item):
    new=[]
    for i in list:
        if item!=i:
            new.append(i.strip(item))
    return new
item=input("Enter the item to remove: ")
print(rem(item))
