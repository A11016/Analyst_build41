import ifcopenshell

# List of IFC types and their corresponding full names
ifc_elements = [
    ('IfcColumn', 'Columns'),
    ('IfcBeam', 'Beams'),
    ('IfcWall', 'Walls'),
    ('IfcRailing', 'Railings'),
    ('IfcRamp', 'Ramps'),
    ('IfcSlab', 'Slabs'),
    ('IfcStair', 'Stairs'),
    ('IfcCovering', 'Coverings'),
    ('IfcStairFlight', 'Stair Flights')
]

# Loop through the list, get the elements by type, and print their quantities
for ifc_type, full_name in ifc_elements:
    elements = file.by_type(ifc_type)
    print(f'Number of {full_name}: {len(elements)}')
    
    
