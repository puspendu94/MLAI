def computepay(h,r):
    if h <= 40.0:
        return h * r
    else:
        return r * (1.5 * h - 20)

h = input("Enter Hours: ")
hour = float(h)
r = input("Enter rate: ")
rate = float(r)
p = computepay(hour, rate)
print(p)
input("Enter any to EXIT...................Thank you")
