def area(radius,pi=3.14):
    result = pi*radius**2
    return result

def cost(circle_area,cost_per_sqa):
    total_cost = circle_area*cost_per_sqa
    return total_cost


print(cost(area(10),2))