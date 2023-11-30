#classfiy students based on major
name=["alice","bob","charlie","dina","ethan"]
major=["computer science","mathematics","physics","economics","computer science"]
cse=[]
eco=[]
maths=[]
phys=[]
for a,b in zip(name,major):
    if b=='computer science':
        cse.append(a)
    elif b=='economics':
        eco.append(a)
    elif b=='mathematics':
        maths.append(a)
    elif b=='physics':
        phys.append(a)
print("computer science students are:",','.join(cse))
print("mathematics students are:",','.join(maths))
print("physics science students are:",','.join(phys))
print("economics science students are:",','.join(eco))