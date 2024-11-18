# How To Extract The Correct Psets - Tutorial (Group 41) #

## Purpose of The Tool ##
The tool is designed to enable cost estimation for facade elements, by using information from IFC-file for precise calculations. It serves as a bridge between advanced Building Information Modeling (BIM) workflows and real-time cost analysis.

### Learning Objectives ###


## Tool Overview: How It Works ##
The tool designed is a code that can be run on python. The code runs through an IFC-file to check extract the relevant data, so the applicable IFC-file should also be available on the computer running the tool.

### Code Explanation and Analysis ###
This tool is designed to estimate the cost of facade elements (specifically IfcCurtainWall elements) in an IFC file. It looks for certain facade walls based on a name search phrase ("Basic Wall - Ext. Wall"), retrieves their surface area from the model, and calculates the total cost based on a given unit cost.

**1. Imports:** Python libraries for IFC files
![image](https://github.com/user-attachments/assets/711db219-f4e1-4541-ad52-1cfe384fe476)

It is necessary to pip install ifcopenshell in python

**2. Function Definition:** The function accepts two parameters; model (IFC model) and unit_cost (Cost per unit area)
![image](https://github.com/user-attachments/assets/068cb7de-69c2-4b02-8b90-8334b159d2c1)

**3. Variable Initialization:** element_count (Amount of IfcCurtainWall), total_surface_area (Accumulate the surface area of all matching walls), search_phrase (String used to identify walls with the name containing phrase)
![image](https://github.com/user-attachments/assets/14515a24-1177-4f6c-9701-1049624c489c)

**4. Iterating Over The Walls:** This loop goes through all the elements of type IfcCurtainWall in the IFC model. IfcCurtainWall represents a type of wall, typically used for building facades.
![image](https://github.com/user-attachments/assets/c606ba35-d4f5-48b4-810f-bd21addc9625)

**5. Checking For The Search Phrase:** Checks if the wall has a Name attribute and whether it contains the search phrase "Basic Wall:ARC - Ext. Wall". If it matches, it proceeds to process that wall.
![image](https://github.com/user-attachments/assets/cd9c1bc0-05ae-4870-b034-91591d54a794)


### Walkthrough ###

### Prerequisites for the functionality of the code ###
