import ifcopenshell
from collections import defaultdict

def count_furniture_shelving_storage(model):
    proxy_type_count = defaultdict(int)
    element_count = defaultdict(int)
    
    # Iterate over all instances of IfcBuildingElementProxyType in the model
    for element_type in model.by_type("IfcBuildingElementProxyType"):
        type_name = element_type.Name if element_type.Name else "Unnamed"
        if "Furniture_Shelving-Storage" in type_name:
            proxy_type_count[type_name] += 1
            # Count elements associated with this type
            for element in model.by_type("IfcBuildingElementProxy"):
                if element.IsTypedBy and element.IsTypedBy[0].RelatingType == element_type:
                    element_count[type_name] += 1
    
    # Calculate the final sum
    final_sum = 0
    for type_name, count in element_count.items():
        multiplier = 6 if "enkelt" in type_name.lower() else 12
        final_sum += count * multiplier
    
    result = print(f"\nFinal calculated sum of counts: {final_sum}")

    return result

# Get the IFC file using IfcStore
model = IfcStore.get_file()

# Call the function and get the final count
count_furniture_shelving_storage(model)


