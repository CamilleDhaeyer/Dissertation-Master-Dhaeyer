from cdmn.API import DMN


NoEvacFloorLevelEvacRouteReg = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-4-3_NoEvacuationFloorLevelEvacuationRouteRegulation.dmn',auto_propagate=True)

print("inputs:", NoEvacFloorLevelEvacRouteReg.get_inputs())
print("outputs:", NoEvacFloorLevelEvacRouteReg.get_outputs())
print("other:", NoEvacFloorLevelEvacRouteReg.get_intermediary())



ExceptionToFR = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-4-3_NoEvacuationFloorLevelEvacuationRouteRegulation_ExceptionRules.dmn',auto_propagate=True)

print("inputs:", ExceptionToFR.get_inputs())
print("outputs:", ExceptionToFR.get_outputs())
print("other:", ExceptionToFR.get_intermediary())




ExceptionToFR.set_value('OccupancyTime', "Day_occupancy_only")
ExceptionToFR.set_value('DayOccupancyCompartmentRuleSuccess', True)
ExceptionToFR.set_value('AreaOfCompartment', 1000)

ExceptionToFireResistanceRequirementsSuccess = ExceptionToFR.value_of('ExceptionToFireResistanceRequirementsSuccess')




#Define list of fire resistances from the evacuation route walls
FRwall_list=["EI_60","EI_60","EI_30","EI_30"]


#Define empty result list
WallResults=[]



FRwallEI30 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/FireResistanceWallModuleEI30.dmn',auto_propagate=True)
for FR in FRwall_list:
    FRwallEI30.set_value('FireResistanceWall', FR)
    WallResults.append(FRwallEI30.value_of('FireResistanceWallSuccess'))
    FRwallEI30.clear()



#Map to FireResistanceAllWallSuccess

if all(WallResults):
    FireResistanceAllWallSuccess = True
else: 
    FireResistanceAllWallSuccess = False




#Define list of fire resistances from the evacuation route doors except the door to the staircase
FRdoor_list=["EI_60","EI_60","EI_30","EI_30"]

#Define empty result list
DoorResults=[]


#call all door DMNs

FRdoorEI30 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceDoorModuleEI30.dmn',auto_propagate=True)


for FR in FRdoor_list:
    FRdoorEI30.set_value('FireResistanceDoor', FR)
    #print(FRdoorEI30.value_of('FireResistanceDoorSuccess'))
    DoorResults.append(FRdoorEI30.value_of('FireResistanceDoorSuccess'))


if all(DoorResults):
    FireResistanceAllDoorSuccess = True
else: 
    FireResistanceAllDoorSuccess = False





NoEvacFloorLevelEvacRouteReg.set_value('FireResistanceAllDoorSuccess', FireResistanceAllDoorSuccess)
NoEvacFloorLevelEvacRouteReg.set_value('FireResistanceAllWallSuccess', FireResistanceAllWallSuccess)
NoEvacFloorLevelEvacRouteReg.set_value('ExceptionToFireResistanceRequirementsSuccess', ExceptionToFireResistanceRequirementsSuccess)


NoEvacFloorLevelEvacRouteRegResult = NoEvacFloorLevelEvacRouteReg.model_expand()
print(NoEvacFloorLevelEvacRouteRegResult)