from cdmn.API import DMN


FireExpansion = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-5-1-1_FireExpansionAlongFacadeRegulation.dmn',auto_propagate=True)

print("inputs:", FireExpansion.get_inputs())
print("outputs:", FireExpansion.get_outputs())
print("other:", FireExpansion.get_intermediary())


"""
#This is not required as the fire extinguishing module copies the booleans, thus list can be immediately checked


#Fire extinguishing system module
#verify for each compartment along face
FireExtinguishing = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-5-1-1_FireExpansionAlongFacade_ExtinguishingSystemModule.dmn',auto_propagate=True)
print("inputs:", FireExtinguishing.get_inputs())
print("outputs:", FireExtinguishing.get_outputs())
print("other:", FireExtinguishing.get_intermediary())


#Define result list
Extinguishing_result=[]


for ext in Extinguishing_list:
    FireExtinguishing.set_value('PresenceFireExtinguishuingSystem', ext)
    print(FireExtinguishing.value_of('CompartmentFireExtinguishingSystemSuccess'))
    Extinguishing_result.append(FireExtinguishing.value_of('CompartmentFireExtinguishingSystemSuccess'))
"""

#Define boolean list for all compartments along facade
Extinguishing_list =[True,True,False,True]


if all(Extinguishing_list):
    CompartmentAlongFacadeFireExtinguishingSystemSuccess = True
else: 
    CompartmentAlongFacadeFireExtinguishingSystemSuccess = False

print(CompartmentAlongFacadeFireExtinguishingSystemSuccess)



FireExpansion.set_value('CompartmentAlongFacadeFireExtinguishingSystemSuccess', CompartmentAlongFacadeFireExtinguishingSystemSuccess)


#Define list of the fire resistances of each building layer in the facade
FRbuildinglayerFacade1=["E_30","E_30","E_30","E_30"]
FRbuildinglayerFacade2=["E_60","E_30","E_60","E_30"]
FRbuildinglayerFacade3=["E_30","E_45","E_30","E_60"]

FRbuildinglayerFacade4=["E_60","E_90","E_60","E_30"]
FRbuildinglayerFacade5=["E_30","E_30","E_30","E_60"]


#Define function to check same strings and alternative strings
def check_same_strings(lst):
    # Check if the list is empty
    if not lst:
        return False  # Return False if the list is empty

    # Compare the first element with all other elements
    first_element = "E_30"
    for element in lst[0:]:
        if element != first_element:
            return False  # Return False if any element is different

    return True  # Return True if all elements are the same

print(check_same_strings(FRbuildinglayerFacade1))
print(check_same_strings(FRbuildinglayerFacade2))
print(check_same_strings(FRbuildinglayerFacade3))


def check_alternating_same_strings(lst):
    is_E60 = lst[0] == "E_60"

    for i in range(1, len(lst)):
        if i % 2 == 0:
            if lst[i] != "E_60" and is_E60:
                return False
            elif lst[i] == "E_60" and not is_E60:
                return False
        else:
            if lst[i] == "E_60" and is_E60:
                return False
            elif lst[i] != "E_60" and not is_E60:
                return False

    return True
    


print("Alternating outcomes:")

print(check_alternating_same_strings(FRbuildinglayerFacade2))
print(check_alternating_same_strings(FRbuildinglayerFacade4))
print(check_alternating_same_strings(FRbuildinglayerFacade5))

FRbuildinglayerFacade1_FunctionOutcomeList=[]
FRbuildinglayerFacade1_FunctionOutcomeList.append(check_same_strings(FRbuildinglayerFacade2))
FRbuildinglayerFacade1_FunctionOutcomeList.append(check_alternating_same_strings(FRbuildinglayerFacade2))
print(FRbuildinglayerFacade1_FunctionOutcomeList)

if FRbuildinglayerFacade1_FunctionOutcomeList[0] == False and FRbuildinglayerFacade1_FunctionOutcomeList[1] == True:
    AllBuildingLayersE30 = False
    EveryTwoBuildLayersE60 = True
elif FRbuildinglayerFacade1_FunctionOutcomeList[0] == True and FRbuildinglayerFacade1_FunctionOutcomeList[1] == False:
    AllBuildingLayersE30 = True
    EveryTwoBuildLayersE60 = False
else:
    AllBuildingLayersE30 = False
    EveryTwoBuildLayersE60 = False
    
print(AllBuildingLayersE30)
print(EveryTwoBuildLayersE60)

FireExpansion.set_value('EveryTwoBuildLayersE60', AllBuildingLayersE30)
FireExpansion.set_value('AllBuildingLayersE30', EveryTwoBuildLayersE60)







#Module horizontal element
HorizontalElement = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-5-1-1_FireExpansionAlongFacade_HorizontalProtectionModule.dmn',auto_propagate=True)
FRE60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/FireResistanceE60.dmn',auto_propagate=True)


#loops over list of horizontal elements
#list is a list of lists with the following elements: FR_floorextension, FR_parapet, FR_lintel, floorthickness, continousfacade, heightparapet, height lintel,WidthFloorExtension, PresenceHorizontalFloorExtensionPastFacade
HorizontalElement_list=[["E_60","E_60","E_60",0.2,False,0.5,0.1,0.2,True],["E_60","E_30","E_60",0.2,False,0.5,0.1,0.2,True]]
HorizontalElement_result=[]

for element in HorizontalElement_list:
    #Fire resistance of floor extension through module

    FRE60.set_value('FireResistance', element[0])
    print(FRE60.value_of('FireResistanceSuccess'))
    HorizontalElement.set_value('FireResistanceFloorExtensionSuccess', FRE60.value_of('FireResistanceSuccess'))
    FRE60.clear()

    #Fire resistance of parapet through module
    FRE60.set_value('FireResistance', element[1])
    print(FRE60.value_of('FireResistanceSuccess'))
    HorizontalElement.set_value('FireResistanceParapetSuccess', FRE60.value_of('FireResistanceSuccess'))
    FRE60.clear()
    
    #Fire resistance of lintel through module
    FRE60.set_value('FireResistance', element[2])
    print(FRE60.value_of('FireResistanceSuccess'))
    HorizontalElement.set_value('FireResistanceLintelSuccess', FRE60.value_of('FireResistanceSuccess'))
    FRE60.clear()

    #Set other values

    HorizontalElement.set_value('FloorThickness', element[3])
    HorizontalElement.set_value('ContinousFacade', element[4])
    
    HorizontalElement.set_value('HeightParapet', element[5])
    HorizontalElement.set_value('HeightLintel', element[6])
    HorizontalElement.set_value('WidthFloorExtension', element[7])


    HorizontalElement.set_value('PresenceHorizontalFloorExtensionPastFacade', element[8])

    HorizontalElementResult = HorizontalElement.model_expand()
    HorizontalElement_result.append(HorizontalElement.value_of('HorizontalFireProtectionElementSuccess'))


print(HorizontalElement_result)


if all(HorizontalElement_result):
    HorizontalFireProtectionElementSuccess = True
else: 
    HorizontalFireProtectionElementSuccess = False

print(HorizontalFireProtectionElementSuccess)




FireExpansion.set_value('HorizontalFireProtectionElementSuccess', HorizontalFireProtectionElementSuccess)



#Module vertical element

VerticalElement = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-5-1-1_FireExpansionAlongFacade_VerticalProtectionModule.dmn',auto_propagate=True)

#loops over list of vertical elements
#list is a list of lists with all the variable values
VerticalElement_list=[[0.2,0.5,0.5,0.25,0.25,"E_60",True,False,"Outer_wall","Building"],[0.2,0.15,0.1,0.25,0.25,"E_60",True,False,"Outer_wall","Building"]]
VerticalElement_result=[]

for element in VerticalElement_list:
    VerticalElement.set_value('WidthWall', element[0])
    VerticalElement.set_value('WidthOfWallExtensionLeftFromCenterOfWall', element[1])
    VerticalElement.set_value('WidthOfWallExtensionRightFromCenterOfWall', element[2])

    VerticalElement.set_value('DistanceFacadePlaneToWindowPlaneLeft', element[3])
    VerticalElement.set_value('DistanceFacadePlaneToWindowPlaneRight', element[4])
    
    VerticalElement.set_value('FireResistanceExtensionElement', element[5])

    VerticalElement.set_value('PresenceWallExtensionInPlaneOfFacade', element[6])
    VerticalElement.set_value('PresenceWallExtensionPastFacade', element[7])

    VerticalElement.set_value('WallClass', element[8])
    VerticalElement.set_value('SpaceType', element[9])

    VerticalElementResult = VerticalElement.model_expand()

    VerticalElement_result.append(VerticalElement.value_of('VerticalFireProtectionElementSuccess'))


print(VerticalElement_result)


if all(VerticalElement_result):
    VerticalFireProtectionElementSuccess = True
else: 
    VerticalFireProtectionElementSuccess = False

print(VerticalFireProtectionElementSuccess)


FireExpansion.set_value('VerticalFireProtectionElementSuccess', VerticalFireProtectionElementSuccess)

FireExpansionResult = FireExpansion.model_expand()
print(FireExpansionResult)
