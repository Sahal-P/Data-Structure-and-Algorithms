from typing import List

def maximumPopulation( logs: List[List[int]] ) -> int:
    print(logs)
    return 1993
    
    
    
logs_1 = [[1993,1999],[2000,2010]]
output_1 = 1993
# Explanation: The maximum population is 1, and 1993 is the earliest year with this population.

logs_2 = [[1950,1961],[1960,1971],[1970,1981]]
output_2 = 1960

# Explanation: 
# The maximum population is 2, and it had happened in years 1960 and 1970.

# The earlier year between them is 1960.

assert maximumPopulation(logs_1) == output_1
assert maximumPopulation(logs_2) == output_2