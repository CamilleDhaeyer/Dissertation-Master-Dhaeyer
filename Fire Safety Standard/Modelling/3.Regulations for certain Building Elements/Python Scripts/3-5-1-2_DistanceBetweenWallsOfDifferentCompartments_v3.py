import numpy as np
from cdmn.API import DMN

DistanceFacadeCompartments = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-5-1-2_DistanceBetweenWallsOfDifferentCompartments_v3.dmn')

print("inputs:", DistanceFacadeCompartments.get_inputs())
print("outputs:", DistanceFacadeCompartments.get_outputs())
print("other:", DistanceFacadeCompartments.get_intermediary())

#set value for enclosed corner
EnclosedCornerBetweenTheFacades = 5



#verify same compartment; IDP can not process comparing strings
#list should always have 2 elements only from the combination of every facade wall with another
List=["Compartment1","Compartment2"]

if List[0] == List[1]:
    SameCompartment = True
else:
    SameCompartment = False
    

#Element1 is from facadewall1; Element2 is from facadewall2; multiple combinations could also be possible here ==> for loop
Element1_list=["Compartment1","E_45",90,None,5]
Element2_list=["Compartment2","E_30",90,None,7]

#verify is elements are unsufficient
FRE60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/FireResistanceE60.dmn',auto_propagate=True)
FR_elements_result=[]


FRE60.set_value('FireResistance', Element1_list[1])
FR_elements_result.append(FRE60.value_of('FireResistanceSuccess'))
FRE60.clear()
FRE60.set_value('FireResistance', Element2_list[1])
FR_elements_result.append(FRE60.value_of('FireResistanceSuccess'))

print(FR_elements_result)

if all(not elem for elem in FR_elements_result):
    UnsufficientSuccess = True
else:
    UnsufficientSuccess = False
    
print(UnsufficientSuccess)


#define function to calculate distance
def calculate_unknown_side(side_a, side_b, angle_C):
    
    # Convert angle from degrees to radians
    angle_C_rad = np.radians(angle_C)
    
    # Use Law of Cosines to find the unknown side
    side_c_squared = side_a**2 + side_b**2 - 2 * side_a * side_b * np.cos(angle_C_rad)
    side_c = np.sqrt(side_c_squared)
    
    return side_c

#define when function needs to be used:
if Element1_list[3] == None and Element2_list[3] == None:
    DistanceBetweenUnsufficientFireResistanceElements = calculate_unknown_side(Element1_list[4], Element2_list[4], Element1_list[2])
elif Element1_list[4] == None and Element2_list[4] == None:
    DistanceBetweenUnsufficientFireResistanceElements = Element1_list[3]
    
    
print(DistanceBetweenUnsufficientFireResistanceElements)

DistanceFacadeCompartments.set_value('UnsufficientSuccess', UnsufficientSuccess)
DistanceFacadeCompartments.set_value('SameCompartment', SameCompartment)
DistanceFacadeCompartments.set_value('EnclosedCornerBetweenTheFacades', EnclosedCornerBetweenTheFacades)
DistanceFacadeCompartments.set_value('DistanceBetweenUnsufficientFireResistanceElements', DistanceBetweenUnsufficientFireResistanceElements)

DistanceFacadeCompartmentsResult = DistanceFacadeCompartments.model_expand()
print(DistanceFacadeCompartmentsResult)