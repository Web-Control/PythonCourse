"""
If statements in Python
"""
def CompareIt(Factor1,Factor2,Factor3):
    Output = False
    Factor1 = int(Factor1)
    Factor2 = int(Factor2)
    Factor3 = int(Factor3)

    if Factor1 == Factor2:
        Output = True
    elif Factor1 == Factor3:
        Output = True
    elif Factor2 == Factor3:
        Output = True
    
    return Output

Test = CompareIt(6,5,"5")
print(Test)