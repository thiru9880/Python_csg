def area(radius,pi=3.14):
    result = pi*radius**2
    return result

def cost(circle_area,cost_per_sqa):
    total_cost = circle_area*cost_per_sqa
    return total_cost


calculated_area = area(10)
tc = cost(calculated_area,2)

print(tc)