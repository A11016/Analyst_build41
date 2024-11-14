def cost_estimation_of_facade_elements(model, unit_cost=4196):
    # Counter for elements with "Basic Wall:Facade 400 mm" in the name
    element_count = 0
    total_surface_area = 0.0
    search_phrase = "Basic Wall:ARC - Ext. Wall"
    
    # Iterate over all instances of IfcCurtainWall in the model
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
