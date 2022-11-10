a = int(input())
b = int(input())
c = int(input())
dis = b ** 2 - 4 * a * c
if dis >= 0:
    if ((-b + dis ** 0.5) / (2 * a)) != ((-b - dis ** 0.5) / (2 * a)):
        print((-b + dis ** 0.5) / (2 * a), (-b - dis ** 0.5) / (2 * a))
    else:
        print((-b + dis ** 0.5) / (2 * a))