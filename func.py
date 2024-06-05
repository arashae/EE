def POM1(i,n,P):
    F = P * (1 + i) ** n
    return F
def FOM1(i,n,F):
    P = F / (1 + i) ** n 
def fp_formula(value, n):
    return value / (1 + 0.05)**n
def efactor(n):
    return 2.71828183**(-n/50)

def ap_factor(i, n):
    return (1 - (1 + i)**(-n)) / i