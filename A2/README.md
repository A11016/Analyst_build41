## A2a
**Group Coding level total:** 2

**Focus Area:** Build

**Role:** Analysts

## A2b
**Building** #2411

**Claim:** Cost estimation of facades (Structural):

 ![Claim](https://github.com/user-attachments/assets/e06ca37e-38bf-4d04-9617-c1fc3579b36e)


The purpose of the claim is to estimate the cost of the façade of the building by estimating the area/amount of the façade surface and relate it to the m2 unit price. From this information it will be possible to estimate the collective price of the façade elements. 
It is important because money matters. A healthy project has a healthy cost, and therefore this claim ensures that the correct amount was budgeted, not less and especially not more.

## A2c
## Use Case:
### •	How would you check this claim?
By verifying the number of façade elements and area of these façade elements using meshes in blender, we can find out the cost associated with the facade construction. This can then be matched to the cost in the report appendix.

### •	When would this claim need to be checked?
This claim needs to be checked during pre-construction phase after an early design for the building has been submitted and cost determination is underway.

### •	What information does this claim rely on?
Firstly, the information relies on the façade design details, being the types of façades (e.g. glass façade, curtain walls). Also, the surface area measurements - the total area of each façade element to be installed are relevant. Lastly, the unit cost data is needed from product datasheet to determine the price per square meter for each façade type.

### •	What phase? planning, design, build or operation.
The design phase is the primary phase where the claim would be checked as it is closely related to estimating the cost of the building elements and finalizing the design. In the design phase, detailed cost estimates are essential to ensure that the project remains within the budget. It can also be used in the planning phase for early cost analysis and estimates.

### •	What BIM purpose is required? Gather, generate, analyse, communicate or realise?
This claim involves analyzing the façade surface area. Material cost and unit prices to estimate the overall cost. It could also involve communicating the cost estimate to stakeholders like project manager, contractors and clients once the analysis is complete. 

### •	Review use case examples - do any of these help?, What BIM use case is this closest to? If you cannot find one from the examples, you can make a new one.
The closest to the claim is use case 02 - Cost Estimation 

### •	Produce a BPMN drawing for your chosen use case. link to this so we can see it in your markdown file. To do this you will have to save it as an SVG, please also save the BPMN with it. You can use this online tool to create a BPMN file.

Diagram
•	Describe all stages and processes of the use case
•	Shows the exchange of information between the stakeholders in the use case * Show the inputs and outputs between your tool and other data models, experts, stakeholders etc.
•	Clearly show the exchange of information between your tool and the IFC model. Which specific IFC classes are being checked or manipulated?
Scope:
•	From the ‘whole use case’ identify where a new script / function / tool is needed. Highlight this in your BPMN diagram. Show this clearly in a new SVG diagram. You may wish to change the SVG diagram, you can use inkscape for this task.


Tool idea:
•	Describe in words your idea for your own OpenBIM ifcOpenShell Tool in Python.
The idea is for the Python tool to ensure that the cost estimates that were made early in a design process are correct, by running through the BIM model. The tool ensures that if any changes or mistakes are made, that they can be outlined, and perhaps prevent a future problem.
•	What is the business and societal value of your tool?
The value of the tool can be measured directly in monetary value, as the cost estimation can hinder an unlucky situation were calculations could be made wrongfully or faulty design.
•	Produce a BPMN diagram to summarise your idea. Save this in a folder in your repository along with an SVG of the disagram and embed the SVG in the Markdown as an image.

Information requirement:
•	Identify what information you need to extract from the model
o	Where is this in IFC?
The information needed is IfcElementType of the facades, so that the different types of façade will be included in the correct amount. 
o	Is it in the model?
Yes, it is in the model
o	Do you know how to get it in ifcOpenShell?
No
o	What will you need to learn to do this? [Enrolled students only]: add to this excel in teams
Identify Software:

