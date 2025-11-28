import sys

if len(sys.argv) == 4:
    script_name = sys.argv[0]
    principal = float(sys.argv[1])
    rate = float(sys.argv[2])
    time = float(sys.argv[3])
else:
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest: "))
    time = float(input("Enter the time period: "))

simple_interest = (principal * rate * time) / 100

print("Principal Amount is:", principal)
print("Rate of Interest is:", rate)
print("Time Period is:", time)
print("Simple Interest is:", simple_interest)
