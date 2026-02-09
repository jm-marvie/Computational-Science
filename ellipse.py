from decimal import Decimal, getcontext

# Set precision for arbitrary-precision arithmetic
getcontext().prec = 120

# True value of pi (100 decimal places)
pi = Decimal(
    "3.14159265358979323846264338327950288419716939937510"
    "58209749445923078164062862089986280348253421170679"
)

# Ellipse parameters
a = Decimal("5")
b = Decimal("3")

# Reference (true) area
real_area = pi * a * b

# Truncate a Decimal value to a given number of decimals
def truncate(value, decimals):
    factor = Decimal(10) ** decimals
    return (value * factor // 1) / factor

# Decimal places of pi to test
decimals = [20, 40, 60, 80, 100]

error_trunc = []
error_round = []

print("===== ELLIPSE AREA COMPUTATION =====\n")
print("True Area:", real_area)
print()

# Compute area using truncated and rounded pi
for d in decimals:
    pi_t = truncate(pi, d)
    pi_r = pi.quantize(Decimal(f"1e-{d}"))

    area_t = pi_t * a * b
    area_r = pi_r * a * b

    error_trunc.append(abs(real_area - area_t))
    error_round.append(abs(real_area - area_r))

    print(f"Precision: {d} decimal places")
    print(f"Truncated pi = {pi_t}")
    print(f"Area (Truncation) = {area_t}")
    print(f"Rounded pi = {pi_r}")
    print(f"Area (Rounding) = {area_r}")
    print(f"Difference = {abs(area_r - area_t)}")
    print()
