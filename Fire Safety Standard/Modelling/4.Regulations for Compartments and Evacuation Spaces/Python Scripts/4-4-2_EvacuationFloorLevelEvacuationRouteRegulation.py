from cdmn.API import DMN


EvacFloorLevelEvacRouteReg = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-4-2_EvacuationFloorLevelEvacuationRouteRegulation.dmn',auto_propagate=True)
EvacFloorLevelEvacRouteReg.clear()
print("inputs:", EvacFloorLevelEvacRouteReg.get_inputs())
print("outputs:", EvacFloorLevelEvacRouteReg.get_outputs())
print("other:", EvacFloorLevelEvacRouteReg.get_intermediary())








EvacIntStaircase = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-2-2-3_EvacuationRouteConnectionToInteriorStaircaseRegulation.dmn',auto_propagate=True)

#Door to Staircase
FRdoor_list=["EI_30","Selfclosing_door","Interior_staircase",1,False,"Turns_with_escape_direction"]

#call all door DMNs
DoorTypeAndFR = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/SelfClosingFRDoorModule.dmn',auto_propagate=True)
FRdoorEI30 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceDoorModuleEI30.dmn',auto_propagate=True)
DoorType = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/DoorTypeModule.dmn',auto_propagate=True)


FRdoorEI30.set_value('FireResistanceDoor', FRdoor_list[0])
DoorType.set_value('DoorType', FRdoor_list[1])
DoorType.set_value('RoomType', FRdoor_list[2])

DoorTypeAndFR.set_value('FireResistanceDoorSuccess', FRdoorEI30.value_of('FireResistanceDoorSuccess'))
DoorTypeAndFR.set_value('DoorTypeSuccess', DoorType.value_of('DoorTypeSuccess'))


EvacIntStaircase.set_value('DoorSuccess', DoorTypeAndFR.value_of('DoorSuccess'))
EvacIntStaircase.set_value('DoorEffectiveWidth', FRdoor_list[3])
EvacIntStaircase.set_value('DoorIsEquippedWithLockingSystem', FRdoor_list[4])
EvacIntStaircase.set_value('DoorTurningDirection', FRdoor_list[5])


ConnectionEvacuationRouteAndInteriorStaircaseSuccess = EvacIntStaircase.value_of('ConnectionEvacuationRouteAndInteriorStaircaseSuccess')
print(ConnectionEvacuationRouteAndInteriorStaircaseSuccess)









#Define list of fire resistances from the evacuation route walls
FRwall_list=["EI_60","EI_60","EI_30","EI_30"]


#Define empty result list
WallResults=[]



FRwallEI60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceWallModuleEI60.dmn',auto_propagate=True)
for FR in FRwall_list:
    FRwallEI60.set_value('FireResistanceWall', FR)
    WallResults.append(FRwallEI60.value_of('FireResistanceWallSuccess'))
    FRwallEI60.clear()




#Map to FireResistanceAllWallSuccess

if all(WallResults):
    FireResistanceAllWallSuccess = True
else: 
    FireResistanceAllWallSuccess = False

print(FireResistanceAllWallSuccess)










#Define list of fire resistances from the evacuation route doors except the door to the staircase
FRdoor_list=[["EI_30","Selfclosing_door","Evacuation_route_on_evacuation_floor_level"],["EI_30","Selfclosing_door","Evacuation_route_on_evacuation_floor_level"]]


#Define empty result list
DoorResults=[]


#call all door DMNs

FRdoorEI30 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceDoorModuleEI30.dmn',auto_propagate=True)
DoorType = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/DoorTypeModule.dmn',auto_propagate=True)


for Door in FRdoor_list:
    FRdoorEI30.set_value('FireResistanceDoor', Door[0])
    DoorType.set_value('DoorType', Door[1])
    DoorType.set_value('RoomType', Door[2])
    #print(FRdoorEI30.value_of('FireResistanceDoorSuccess'))
    #print(DoorType.value_of('DoorTypeSuccess'))
    DoorResults.append([FRdoorEI30.value_of('FireResistanceDoorSuccess'),DoorType.value_of('DoorTypeSuccess')])



if all(DoorResults):
    AllDoorSuccess = True
else: 
    AllDoorSuccess = False





EvacFloorLevelEvacRouteReg.set_value('FireResistanceAllWallSuccess', FireResistanceAllWallSuccess)
EvacFloorLevelEvacRouteReg.set_value('AllDoorSuccess', AllDoorSuccess)

EvacFloorLevelEvacRouteReg.set_value('ConnectionEvacuationRouteAndInteriorStaircaseSuccess', ConnectionEvacuationRouteAndInteriorStaircaseSuccess)




EvacFloorLevelEvacRouteRegResult = EvacFloorLevelEvacRouteReg.model_expand()
print(EvacFloorLevelEvacRouteRegResult)
