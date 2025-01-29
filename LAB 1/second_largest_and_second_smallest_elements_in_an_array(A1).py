def second_largest(num):
    m1, m2 = None, None
    for x in num:
        if m1 is None or x > m1:
            m1, m2 = x, m1
        elif m2 is None or x > m2:
            m2 = x
    return m2

def second_smallest(num):
    m1, m2 = None, None
    for x in num:
        if m1 is None or x < m1:
            m1, m2 = x, m1
        elif m2 is None or x < m2:
            m2 = x
    return m2

num = [10, 89, 9, 56, 4, 80, 8]
secondlargest = second_largest(num)
secondsmallest = second_smallest(num)
print("Second largest element:", secondlargest)
print("second largest element:", type(secondlargest))
print("Second smallest element:", secondsmallest)
print("second smallest element:", type(secondsmallest))
