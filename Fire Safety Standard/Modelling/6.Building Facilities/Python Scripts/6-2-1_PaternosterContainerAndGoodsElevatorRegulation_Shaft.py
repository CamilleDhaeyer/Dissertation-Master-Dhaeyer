from cdmn.API import DMN


Paternoster_shaft = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-2-1_PaternosterContainerAndGoodsElevatorRegulation_Shaft.dmn',auto_propagate=True)

print("inputs:", Paternoster_shaft.get_inputs())
print("outputs:", Paternoster_shaft.get_outputs())
print("other:", Paternoster_shaft.get_intermediary())





Airlock = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/AirlockRegulation.dmn',auto_propagate=True)
#for each airlock on each floor level that the elevator connects to
#Define list of fire resistances from the airlock walls
FRwall=[["EI_60","EI_60","EI_30","EI_30"],["EI_60","EI_60","EI_60","EI_60"]]


#Define empty result list
WallResults=[]


#Call general wall EI 60 DMN
FRwallEI60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceWallModuleEI60.dmn',auto_propagate=True)
for FRwall_list in FRwall:
    for FR in FRwall_list:
        FRwallEI60.set_value('FireResistanceWall', FR)
        WallResults.append(FRwallEI60.value_of('FireResistanceWallSuccess'))
        FRwallEI60.clear()

#Map to AirlockAllWallSuccess

if all(WallResults):
    AirlockAllWallSuccess = True
else: 
    AirlockAllWallSuccess = False

#Define list of fire resistances from the airlock doors
FRdoor=[[["EI_30","Selfclosing_door","Airlock"],["EI_30","Selfclosing_door","Airlock"]],[["EI_30","Selfclosing_door","Airlock"],["EI_30","Selfclosing_door","Airlock"]]]


#Define empty result list
DoorResult=[]

FRdoorEI30 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceDoorModuleEI30.dmn',auto_propagate=True)
DoorType = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/DoorTypeModule.dmn',auto_propagate=True)

for FRdoor_list in FRdoor:
    for Door in FRdoor_list:
        FRdoorEI30.set_value('FireResistanceDoor', Door[0])
        DoorType.set_value('DoorType', Door[1])
        DoorType.set_value('RoomType', Door[2])
        DoorResult.append([FRdoorEI30.value_of('FireResistanceDoorSuccess'),DoorType.value_of('DoorTypeSuccess')])


if all(DoorResult):
    AirlockAllDoorSuccess = True
else: 
    AirlockAllDoorSuccess = False


#set values for the airlock DMN
Airlock.set_value('AreaOfAirlock', 2)
Airlock.set_value('AirlockAllWallSuccess', AirlockAllWallSuccess)
Airlock.set_value('AirlockAllDoorSuccess', AirlockAllDoorSuccess)




Paternoster_shaft.set_value('ElevatorAllAirlockRegulationSuccess', Airlock.value_of('AirlockRegulationSuccess'))



#define list of all elevator shaft walls
FRRoomwall_list=["EI_120","EI_180","EI_120","EI_120"]
#Define list of fire resistances from the elevator shaft door(s)
FRdoor_list=["EI_60"]

#Define empty result lists
WallRoomResults=[]
DoorResults=[]


FRwallEI60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceWallModuleEI60.dmn',auto_propagate=True)
FREI60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/FireResistanceModuleEI60.dmn',auto_propagate=True)
 
for FR in FRRoomwall_list:
    FRwallEI60.set_value('FireResistanceWall', FR)
    WallRoomResults.append(FRwallEI60.value_of('FireResistanceWallSuccess'))
    FRwallEI60.clear()


#Map to FireResistanceAllWallSuccess

if all(WallRoomResults):
    FireResistanceAllWallSuccess = True
else: 
    FireResistanceAllWallSuccess = False


for Door in FRdoor_list:
    FREI60.set_value('FireResistance', Door)
    DoorResults.append(FREI60.value_of('FireResistanceSuccess'))


if all(DoorResults):
    FireResistanceAllDoorSuccess = True
else: 
    FireResistanceAllDoorSuccess = False



Paternoster_shaft.set_value('FireResistanceAllDoorSuccess', FireResistanceAllDoorSuccess)
Paternoster_shaft.set_value('FireResistanceAllWallSuccess', FireResistanceAllWallSuccess)


Paternoster_shaftResult =Paternoster_shaft.model_expand()
print(Paternoster_shaftResult)