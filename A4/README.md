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

**6. Getting Property Sets:** Retrieves all property sets (psets) associated with the IfcCurtainWall. Property sets are used in IFC to store attributes and measurements about elements (like dimensions, material properties, and quantities).
![image](https://github.com/user-attachments/assets/51fcacb0-acbb-455c-b91d-e275750eb14b)

**7. Extracting Surface Area:** Loops through the property sets and checks for an attribute called Area (which represents the surface area of the wall). If found, the surface area is added to total_surface_area.
![image](https://github.com/user-attachments/assets/34339d39-96e4-469f-8989-83238c1567a2)

**8. Calculating Total Cost:** After accumulating the total surface area of all matching walls, the total cost is calculated by multiplying the total_surface_area by the provided unit_cost.
![image](https://github.com/user-attachments/assets/42282706-7bb3-4cf2-81b0-0d5d9ae76654)

**9. Returning Results:** The function returns three values; element_count (number of walls matching the search phrase), total_surface_area (Sum of the surface areas of walls), total_cost (Total cost based on the surface area and unit cost.
![image](https://github.com/user-attachments/assets/8addc4c7-6668-4faa-8224-b243b223d4b7)

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