# BIManalyst group 41

# Focus area: Build

# Claim under review: Number of bicycle parking spaces

# Place where claim was found: 
  # In report: CES_BLD_24_06_PM_2 Page: 9, section 4.1 General requirements

# Description of Bikespace.py script: 
  # In the report, a requirement specified a minimum of 1006 bike parking spaces, and a claim that the actual number of bike parking spaces is 1212.
  # The Bikespace.py script has a definition made to check if the claim is valid.
  
  # Firstly, the script creates 'proxy_type_count' and 'element_count' to be integers with initial value 0 to keep count of the relevant elements and their associated types. 
  
  # Then a loop-function is used, to loop over all 'IfcBuildingElementProxyType' instances in the Ifc file in Blender, as every bicycle stand is within 'IfcBuildingElementProxyType'. All the type names are loaded into a list called 'type_name'.
  
  # Then the loop checks if 'Furniture_Shelving-Storage' is in the name of the different types listed in 'type_name' because every bicycle stand is labelled with 'Furniture_Shelving-Storage'. If yes, it increments 'proxy_type_count' so we have a number of how many bicycle stand types there are. 
  
  # Then the loop checks for the number of elements for each relevant type, and add it to 'element_count'.

  # Then to distinguish the type that has 6 parking spaces, and the type that has 12 parking spaces - the type with 6 parking spaces, has the word 'enkelt' in its name. Therefore a loop is made through 'element_count', and if the element has the word 'enkelt' in it, the multiplier is set to 6, and if not then it is set to 12. 

# After the loop, a total amount of elements for the two types of bicycle parking stands are counted, and respectively multiplied by 6 or 12, and summed up to know the exact amount of bicycle parking spaces.
