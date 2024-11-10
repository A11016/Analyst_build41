import ifcopenshell
from bonsai.bim.ifc import IfcStore

def cost_estimation_of_facade_elements(model, unit_cost=4196):
    # Counter for elements with "Basic Wall:Facade 400 mm" in the name
    element_count = 0
    total_surface_area = 0.0
    search_phrase = "Basic Wall:ARC - Ext. Wall"
    
    # Iterate over all instances of IfcWall in the model
    for wall in model.by_type("IfcCurtainWall"):
        # Check if "Basic Wall:Facade 400 mm" is part of the wall's name
        if wall.Name and search_phrase in wall.Name:
            element_count += 1
            
            # Get all properties and quantities of the wall element
            psets = ifcopenshell.util.element.get_psets(wall)
            
            # Look for 'Surface Area' in the psets
            for key, value in psets.items():
                if isinstance(value, dict) and 'Area' in value:
                    surface_area = value['Area']
                    if surface_area is not None:
                        total_surface_area += surface_area  # Add the surface area to the total
                    break  # Stop searching after finding the surface area

    # Calculate the cost based on unit cost and total surface area
    total_cost = unit_cost * total_surface_area

    return element_count, total_surface_area, total_cost

# Load the IFC file
file = IfcStore.get_file()

# Call the function to get element count, total area, and cost
facade_wall_count, total_area, total_cost = cost_estimation_of_facade_elements(file)

# Print the results
print(f'Number of elements with "Basic Wall:ARC - Ext. Wall" in the name: {facade_wall_count}')
print(f'Total surface area of elements with "Basic Wall:ARC - Ext. Wall": {total_area:.2f} square meters')
print(f'Total cost of elements with "Basic Wall:ARC - Ext. Wall": {total_cost:.2f} DDK')
