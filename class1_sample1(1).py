def sample(a,b,c):
    """
This is a sample function with 2 parms
"""
    sol = a+b+c
    sol2 = a-b-c
    ls = []
    ls.append(sol)
    ls.append(sol2)
    return ls

def main():
    print(sample(80000, 16.5, 40))


main()


