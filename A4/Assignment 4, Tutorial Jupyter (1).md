# How To Extract The Correct Psets - Tutorial (Group 41) #

## Purpose of The Tool ##
The tool is designed to enable cost estimation for facade elements, by using information from IFC-file for precise calculations. It serves as a bridge between advanced Building Information Modeling (BIM) workflows and real-time cost analysis.

### Learning Objectives ###


## Tool Overview: How It Works ##
The tool designed is a code that can be run on python. The code runs through an IFC-file to check and extract the relevant data. The tool requires that the applicable IFC-file should be available on the computer running the tool, knowing the file path.

### Code Explanation and Analysis ###
This tool is designed to estimate the cost of facade elements (specifically IfcCurtainWall elements) in an IFC file. It looks for certain facade walls based on a name search phrase ("Basic Wall - Ext. Wall"), retrieves their surface area from the model, and calculates the total cost based on a given unit cost.

**1. Imports:** Python libraries for IFC files


```python
import ifcopenshell
import ifcopenshell.util.element
```

It is necessary to pip install ifcopenshell in python

**2. Function Definition:** The function accepts two parameters; model (IFC model) and unit_cost (Cost per unit area)


```python
def cost_estimation_of_facade_elements(model, unit_cost=4196):
```

**3. Variable Initialization:** element_count (Number of IfcCurtainWall), total_surface_area (Accumulate the surface area of all matching walls), search_phrase (String used to identify walls with the name containing phrase)


```python
element_count = 0
total_surface_area = 0.0
search_phrase = "Basic Wall:ARC - Ext. Wall"
```

**4. Iterating Over The Walls:** This loop goes through all the elements of type IfcCurtainWall in the IFC model. IfcCurtainWall represents a type of wall, typically used for building facades.


```python
for wall in model.by_type("IfcCurtainWall"):
```

**5. Checking For The Search Phrase:** Checks if the wall has a Name attribute and whether it contains the search phrase "Basic Wall:ARC - Ext. Wall". If it matches, it proceeds to process that wall.


```python
if wall.Name and search_phrase in wall.Name:
```

**6. Getting Property Sets:** Retrieves all property sets (psets) associated with the IfcCurtainWall. Property sets are used in IFC to store attributes and measurements about elements (like dimensions, material properties, and quantities).


```python
psets = ifcopenshell.util.element.get_psets(wall)
```

**7. Extracting Surface Area:** Loops through the property sets and checks for an attribute called Area (which represents the surface area of the wall). If found, the surface area is added to total_surface_area.


```python
for key, value in psets.items():
    if isinstance(value, dict) and 'Area' in value:
        surface_area = value['Area']
        if surface_area is not None:
            total_surface_area += surface_area
        break
```

**8. Calculating Total Cost:** After accumulating the total surface area of all matching walls, the total cost is calculated by multiplying the total_surface_area by the provided unit_cost.


```python
total_cost = unit_cost * total_surface_area
```

**9. Returning Results:** The function returns three values; element_count (number of walls matching the search phrase), total_surface_area (Sum of the surface areas of walls), total_cost (Total cost based on the surface area and unit cost.


```python
return element_count, total_surface_area, total_cost
```

## Test run of tool ##


```python
import ifcopenshell
import ifcopenshell.util.element

def cost_estimation_of_facade_elements(model, unit_cost=4196):
    # Counter for elements with "Basic Wall:Facade 400 mm" in the name
    element_count = 0
    total_surface_area = 0.0
    search_phrase = "Basic Wall:ARC - Ext. Wall"
    
    # Iterate over all instances of IfcCurtailWall in the model
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
file = ifcopenshell.open(r'C:\Users\louiz\Desktop\CES_BLD_24_06_ARC (1).ifc')

# Call the function to get element count, total area, and cost
facade_wall_count, total_area, total_cost = cost_estimation_of_facade_elements(file)

# Print the results
print(f'Number of elements with "Basic Wall:ARC - Ext. Wall" in the name: {facade_wall_count}')
print(f'Total surface area of elements with "Basic Wall:ARC - Ext. Wall": {total_area:.2f} square meters')
print(f'Total cost of elements with "Basic Wall:ARC - Ext. Wall": {total_cost:.2f} DDK')
```

    Number of elements with "Basic Wall:ARC - Ext. Wall" in the name: 2660
    Total surface area of elements with "Basic Wall:ARC - Ext. Wall": 5661.34 square meters
    Total cost of elements with "Basic Wall:ARC - Ext. Wall": 23754980.83 DDK
    

## Tool Development ##
The development process of the tool is systematic and efficient. It begins by identifying the necessary inputs required to generate the desired output as defined by the code. The primary input is the IFC file, which contains detailed information about the building elements and their associated properties. The tool is designed to extract the relevant data from this file, specifically focusing on the applicable element types and property sets. Once the necessary information is retrieved, the tool utilizes this data to perform a cost estimation, calculating the total cost based on the model's specifications. The final result is then provided as an output.

### BPMN ###
Business Process Model and Notation (BPMN) diagram, outlines the design process for developing a tool. The following BPMN diagram illustrates the process of developing the tool for estimating the cost of façade elements in a building:

![diagram Tool](https://github.com/user-attachments/assets/9a06e1b4-e8e7-413f-aba6-b626682c62e5)


### Description of The Design Process ###
**1. Model Preparation:** Import an IFC-file and filter it to focus on specific elements like facades or curtain walls.

**2. Property Extraction:** Load the filtered elements and extract key properties, including their surface area.

**3. Surface Area Calculation:** Measure the total surface area of the selected elements.

**4. Cost Estimation:** Define a unit cost per square meter and calculate the total cost based on the surface area.

**5. Output:** Collect the data and generate a project report to complete the process.


## Prequisites for The Tool To Function
The IDS (Information Delivery Specification) of the tool is used to define specific requirements or conditions that must be met when processing an IFC file. The following IDS includes a set of conditions or criteria that the IFC file must fulfill, for it to be considered compliant with the requirements of the tool:

![image](https://github.com/user-attachments/assets/f7a4ab44-5f47-4413-bc85-aa80a1650753)

To test whether the IFC file complies with the tool following Python Script is developed to ensure that it complies with the IDS:


```python
import ifcopenshell
import ifcopenshell.util.element

# Define the search phrase in the global scope
search_phrase = "Basic Wall:ARC - Ext. Wall"

def check_ifc_elements_and_properties(model, search_phrase):
    # Check if elements of type IfcCurtainWall are present
    elements_present = False
    properties_present = False

    # Iterate over all instances of IfcCurtainWall in the model
    for wall in model.by_type("IfcCurtainWall"):
        # Check if the wall's name contains the search phrase
        if wall.Name and search_phrase in wall.Name:
            elements_present = True
            
            # Check if there are any property sets available for this element
            psets = ifcopenshell.util.element.get_psets(wall)
            
            # If any property set is found, mark properties_present as True
            if psets:
                properties_present = True
                break  # No need to check further if we found at least one match
    
    return elements_present, properties_present

```

The code determines if the IFC file complies with the IDS

Examples of IFC files tested for IDS:

**..Model 6**


```python
import ifcopenshell
import ifcopenshell.util.element

# Define the search phrase in the global scope
search_phrase = "Basic Wall:ARC - Ext. Wall"

def check_ifc_elements_and_properties(model, search_phrase):
    # Check if elements of type IfcCurtainWall are present
    elements_present = False
    properties_present = False

    # Iterate over all instances of IfcCurtainWall in the model
    for wall in model.by_type("IfcCurtainWall"):
        # Check if the wall's name contains the search phrase
        if wall.Name and search_phrase in wall.Name:
            elements_present = True
            
            # Check if there are any property sets available for this element
            psets = ifcopenshell.util.element.get_psets(wall)
            
            # If any property set is found, mark properties_present as True
            if psets:
                properties_present = True
                break  # No need to check further if we found at least one match
    
    return elements_present, properties_present

# Load the IFC file (replace with your actual IFC file path)
file_path = r'C:\Users\louiz\Desktop\CES_BLD_24_06_ARC (1).ifc'
file = ifcopenshell.open(file_path)

# Call the function to check element presence and properties
elements_present, properties_present = check_ifc_elements_and_properties(file, search_phrase)

# Print the results
print(f'Are elements with "{search_phrase}" present in the model? {elements_present}')
print(f'Do these elements have property sets? {properties_present}')
```

**..Model 11**


```python
import ifcopenshell
import ifcopenshell.util.element

# Define the search phrase in the global scope
search_phrase = "Basic Wall:ARC - Ext. Wall"

def check_ifc_elements_and_properties(model, search_phrase):
    # Check if elements of type IfcCurtainWall are present
    elements_present = False
    properties_present = False

    # Iterate over all instances of IfcCurtainWall in the model
    for wall in model.by_type("IfcCurtainWall"):
        # Check if the wall's name contains the search phrase
        if wall.Name and search_phrase in wall.Name:
            elements_present = True
            
            # Check if there are any property sets available for this element
            psets = ifcopenshell.util.element.get_psets(wall)
            
            # If any property set is found, mark properties_present as True
            if psets:
                properties_present = True
                break  # No need to check further if we found at least one match
    
    return elements_present, properties_present

# Load the IFC file (replace with your actual IFC file path)

file_path = r'C:\Users\louiz\Desktop\CES_BLD_24_11_ARC.ifc'
file = ifcopenshell.open(file_path)

# Call the function to check element presence and properties
elements_present, properties_present = check_ifc_elements_and_properties(file, search_phrase)

# Print the results
print(f'Are elements with "{search_phrase}" present in the model? {elements_present}')
print(f'Do these elements have property sets? {properties_present}')
```

For the tool to work, it is necessary that the elements are assigned with property sets as described in the IDS. It is also necessary to know exactly which Ifc element the façade is defined as, and moreover know the specific search phrase for the element that the cost estimation is intended to. Lastly, the unit cost of the element should be known and defined as a variable in the function.

## Future Development Opportunities and Limitations ##

### Limitations ###

•	The quality of cost estimations relies heavily on the accuracy and completeness of the IFC model. If the model lacks detailed information about materials, quantities, or classifications, or if the inputs do not follow the same units of measurement, the tool's outputs may be less reliable.  
•	As a standalone tool, it may not fully support real-time collaboration between team members. Advanced integration with collaborative BIM platforms like BIM 360 or Trimble Connect would be necessary for enhanced team workflows.

### Future Development Potential ###
•	It is possible to extend the functionality of the tool to estimate the cost of any other element in an Ifc model, if it complies with the requirements. For instance, the cost can be estimated for columns, as long as the ifc element is changed, the cost unit is known and the property set extracted is volume, if that is the requirements to determine the cost.  
•	Incorporating rules to validate IFC data will improve the accuracy of cost estimates. For example, the tool could automatically identify missing material properties (like the code used in our pre-requisites) or even enrich models using external databases.  
•	Future iterations could integrate life-cycle costing and environmental impact assessments, providing users with not only cost estimations but also sustainability insights.  
•	Incorporating interactive visualizations, such as color-coded cost heatmaps on the 3D model, would improve usability and help stakeholders quickly identify high-cost areas for optimization.  
•	Integration with dynamic cost databases, such as regional pricing libraries, would allow real-time updates to material and labor costs, ensuring estimates reflect current market conditions. Future versions of the tool could incorporate machine learning algorithms or AI to predict costs based on historical project data and market trends.
