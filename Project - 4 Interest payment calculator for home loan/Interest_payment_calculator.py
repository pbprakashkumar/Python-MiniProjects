"""
Formula for EMI Calculation is -
P x R x (1+R)^N / [(1+R)^N-1] where-
P = Principal loan amount
N = Loan tenure in months
R = Monthly interest rate
The rate of interest (R) on your loan is calculated per month.
R = Annual Rate of interest/12/100
If rate of interest is 7.2% p.a. then r = 7.2/12/100 = 0.006
"""
def calculate():
    print("\t MONTHLY PAYMENT LOAN CALCULATOR")
    print("")


    P=float(input("Enter the loan amount:"))
    r=float(input("Enter yearly interest:"))
    N=int(input("Enter number of years:"))

    months=N*12
    R=r/(12*100)

    eqn=(1+R)**months
    monthly_payment = (P*R*eqn)/(eqn-1)

    print("The monthly payment for this : ", monthly_payment)

calculate()



