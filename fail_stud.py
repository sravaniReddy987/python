#
name=["alice","bob","charlie","dina","ethan"]
grades=[[85,92,78],[68,75,89],[95,88,92],[72,70,65],[90,85,88]]
fail_students=[]
for i in range(len(name)):
    if any(grade <70 for grade in grades[i]):
        fail_students.append(name[i])
print("failing students:",fail_students)