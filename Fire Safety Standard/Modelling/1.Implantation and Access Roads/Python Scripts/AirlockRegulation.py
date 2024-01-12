from cdmn.API import DMN

#airlock regulation DMN
Airlock = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/AirlockRegulation.dmn',auto_propagate=True)

#Define list of fire resistances from the airlock walls
FRwall_list=["EI_60","EI_60","EI_30","EI_30","EI_30","EI_30"]

#Define empty result list
WallResults=[]

#Call general wall EI 60 DMN
FRwallEI60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceWallModuleEI60.dmn',auto_propagate=True)

for FR in FRwall_list:
    FRwallEI60.set_value('FireResistanceWall', FR)
    WallResults.append(FRwallEI60.value_of('FireResistanceWallSuccess'))
    FRwallEI60.clear()

#Map to AirlockAllWallSuccess

if all(WallResults):
    AirlockAllWallSuccess = True
else: 
    AirlockAllWallSuccess = False


#Define list of airlock door characteristics and type of building
Door_list=[["EI_30","Selfclosing_door","Airlock"],["EI_30","Selfclosing_door","Airlock"]]
TypeOfBuilding = "Any_other_building"

#Define empty result list
DoorResults=[]
#call all door DMNs

DoorTypeAndFR = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/SelfClosingFRDoorModule.dmn',auto_propagate=True)
FRdoorEI30 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceDoorModuleEI30.dmn',auto_propagate=True)
DoorType = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/DoorTypeModule.dmn',auto_propagate=True)


for Door in Door_list:
    FRdoorEI30.set_value('FireResistanceDoor', Door[0])
    DoorType.set_value('DoorType', Door[1])
    DoorType.set_value('RoomType', Door[2])
    DoorType.set_value('TypeOfBuilding',TypeOfBuilding)
    DoorTypeAndFR.set_value('FireResistanceDoorSuccess', FRdoorEI30.value_of('FireResistanceDoorSuccess'))
    DoorTypeAndFR.set_value('DoorTypeSuccess', DoorType.value_of('DoorTypeSuccess'))
    DoorResults.append(DoorTypeAndFR.value_of('DoorSuccess'))


if all(DoorResults):
    AirlockAllDoorSuccess = True
else: 
    AirlockAllDoorSuccess = False



#set values for the airlock DMN
Airlock.set_value('AreaOfAirlock', 2)
Airlock.set_value('AirlockAllWallSuccess', AirlockAllWallSuccess)
Airlock.set_value('AirlockAllDoorSuccess', AirlockAllDoorSuccess)


AirlockResult = Airlock.model_expand()
print(AirlockResult)