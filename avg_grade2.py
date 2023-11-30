names=['alice','bob','charlie','dina','ethan']
grades=[[85,92,78],[68,75,80],[95,88,92],[72,70,65],[90,85,88]]
for name,grade in zip(names,grades):
    print(name,':',sum(grade)//len(grade))
