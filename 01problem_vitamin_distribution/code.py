def count_distributions(divisor, limit):    
    """Count the number of multiples of `divisor` up to `limit`."""
    # The `-1` ensures we don't exceed the year when counting days
    return limit // divisor

def calculate_events(limit):
    # Count the individual distributions
    vitamin_c_days = count_distributions(3, limit)
    vitamin_d_days = count_distributions(5, limit)
    
    # Count the days when both vitamins are given to avoid double counting
    both_vitamins_days = count_distributions(15, limit)
    
    # Total distribution events is the sum of individual distributions minus the overlap
    total_events = vitamin_c_days + vitamin_d_days - both_vitamins_days
    return total_events

total_distribution_events = calculate_events(365)
print(f"Total vitamin distribution events in a year: {total_distribution_events}")
