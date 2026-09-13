import math

print("Calculate Circle Area and Circumference")
r = float(input("Moi ban nhap ban kinh r: "))
cv = 2 * math.pi * r
dt = math.pi * (r ** 2)

print(f"Ban kinh r = {r}")
print(f"Chu vi hinh tron: cv = 2 * pi * r = {cv:.4f}")
print(f"Dien tich hinh tron: dt = pi * r^2 = {dt:.4f}")
