import ifcopenshell

from .rules import BikeSpace

model = ifcopenshell.open("path/to/ifcfile.ifc")

BikeSpace = BikeSpace.count_furniture_shelving_storage(model)

print (f"/nFinal calculated sum of counts: {final_count}")
