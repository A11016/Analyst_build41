# BIManalyst group 41

# Focus area: Build

# The claim that is being checked: Amount of parking spaces for bikes

# Place where claim was found: 
  # In report: CES_BLD_24_06_PM_2
    # Page: 9, section 4.1 General requirements

# Description of Bikespace.py script: 
  # In the report, a claim was made that there should be a minimum of 1006 bike parking spaces, and that there is 1212.
  # The Bikespace.py script has a definition made to check the if the claim is valid.
  
  # First off, the script creates 'proxy_type_count' and 'element_count' to be integers with initial value 0. 
  
  # Then a loop-function is used, to loop over all 'IfcBuildingElementProxyType' in the Ifc file in Blender, as every bicycle stand is within 'IfcBuildingElementProxyType'. All the types are loaded into a list called 'type_name'.
  
  # Then the loop checks if 'Furniture_Shelving-Storage' is in the name of the types listed in 'type_name' because every bicycle stand is called 'Furniture_Shelving-Storage'. If yes, it increments 'proxy_type_count' so we have an amount of how many bicycle stand types there are. 
  
  # Then the loop checks for each relevant type, how many items there are, and add it to 'element_count'.

  # Then to distinguish the type that has 6 parking spaces, and the item that has 12 parking spaces - we know that the type with 6 parking spaces, has the word 'enkelt' in it's name. Therefore we loop through 'element_count', and here we multiply the amount of stands with 6, by knowing the name of the exact type is having the word 'enkelt' which the other type does not. If the word does not occur in 'element_count' the quantity is multiplied by 12. 

  # The sum of the multiplication are the total amount of parking spaces for bicycles.
