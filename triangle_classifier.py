def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a valid triangle"

    sides = [a, b, c]
    sides.sort()

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return "Scalene and Right"
    elif sides[0] == sides[1] == sides[2]:
        return "Equilateral"
    elif sides[0] == sides[1] or sides[1] == sides[2]:
        return "Isosceles"
    else:
        return "Scalene"
