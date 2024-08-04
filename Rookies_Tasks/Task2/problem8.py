n, m, a, b = map(int, input().split())

cost_single_tickets = n * a

full_m_tickets = n // m
remaining_rides = n % m

cost_full_multi_tickets = full_m_tickets * b + remaining_rides * a

cost_full_multi_plus_one = (full_m_tickets + 1) * b

min_cost = min(cost_single_tickets, cost_full_multi_tickets, cost_full_multi_plus_one)

print(min_cost)
