import ifcopenshell
import ifcopenshell.util.element

# Insert the file path
file_path = (r'[insert file path here]')

from .A3 import cost_estimation_of_facade_elements

# Load the IFC file

file = ifcopenshell.open(file_path)

# Call the function to get element count, total area, and cost
facade_wall_count, total_area, total_cost = cost_estimation_of_facade_elements(file)

# Print the results
print(f'Number of elements with "Basic Wall:ARC - Ext. Wall" in the name: {facade_wall_count}')
print(f'Total surface area of elements with "Basic Wall:ARC - Ext. Wall": {total_area:.2f} square meters')
print(f'Total cost of elements with "Basic Wall:ARC - Ext. Wall": {total_cost:.2f} DDK')
