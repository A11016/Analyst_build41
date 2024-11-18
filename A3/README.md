# A3 - 03

## About the tool

**State the problem / claim that your tool is solving:**  
The tool has the purpose of checking the cost estimation of façade elements.

**State where you found that problem:**  
The claim is found in the report *‘CES_BLD_24_06_PM_Appendix’*.  
The claim is found in appendix C, in page 6 in the table named *‘Construction Costs’*, 4th row with Molio name *‘Facadeelement af beton beton/320mm isolering/puds’*. See image below.
![image](https://github.com/user-attachments/assets/853f70c4-6757-486a-ad80-979c173fcab5)

**Description of the tool**  
The tool achieves its purpose by firstly looping through the model, identifying each IfcCurtainWall, and searching specifically for the wall elements that are façade elements. Then the tool extracts the relevant IfcPsets, which in this case is the surface area of each element and sums it up. Lastly, the total surface area of the facades is multiplied by the cost price of one unit (m^2) of façade element.

**Instructions to run the tool**  
* Firstly, the Ifc file must be downloaded and have a known file path  
* The tool must be run on python with ifcopenshell installed by using the code in the console: pip install ifcopenshell  
* Insert the file path of the ifc file in the variable ‘file_path’ at the top of the code  
* Run code

## Advanced Building Design

**What Advanced Building Design Stage (A,B,C or D) would your tool be useful?**  
1. The tool would be useful in the stage where the BIM file is made, which probably would be the B-stage ‘project proposal’ to calculate the cost.  
2. The tool would also be useful in the stage where the subcontractor is in the process of execution, where the cost can be checked with the initial estimation. That would be the C-stage ‘project execution’.

**Which subjects might use it?**  
Cost estimation is primarily the concern of the build subject, which would use the tool to estimate the costs and/or check that the cost is correct according to the model.

**What information is required in the model for your tool to work?**  
* The model must be the correct model including façade elements, and for example not being a structural model.
* The model must contain property sets for all elements, as the tool extracts those information.





