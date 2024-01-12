from cdmn.API import DMN


EscalatorReg = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-3_EscalatorStaircaseRegulation.dmn',auto_propagate=True)

print("inputs:", EscalatorReg.get_inputs())
print("outputs:", EscalatorReg.get_outputs())
print("other:", EscalatorReg.get_intermediary())


#define list of all escalator staircase walls
FRRoomwall_list=["EI_120","EI_180","EI_120","EI_120"]


#Define empty result lists
WallRoomResults=[]

FRwallEI60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceWallModuleEI60.dmn',auto_propagate=True)
for FR in FRRoomwall_list:
    FRwallEI60.set_value('FireResistanceWall', FR)
    WallRoomResults.append(FRwallEI60.value_of('FireResistanceWallSuccess'))
    FRwallEI60.clear()


#Map to FireResistanceAllWallSuccess

if all(WallRoomResults):
    FireResistanceAllWallSuccess = True
else: 
    FireResistanceAllWallSuccess = False

EscalatorReg.set_value('FireResistanceAllWallSuccess',FireResistanceAllWallSuccess)



#Define list of fire resistances from the airlock doors
FRdoor_list=[["EI_30","Selfclosing_door","Escalator_staircase"],["EI_30","Selfclosing_door_during_fire","Escalator_staircase"]]


#Define empty result list
DoorResults=[]


#call all door DMNs

FRdoorEI30 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceDoorModuleEI30.dmn',auto_propagate=True)
DoorType = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/DoorTypeModule.dmn',auto_propagate=True)

for Door in FRdoor_list:
    FRdoorEI30.set_value('FireResistanceDoor', Door[0])
    DoorType.set_value('DoorType', Door[1])
    DoorType.set_value('RoomType', Door[2])
    DoorResults.append([FRdoorEI30.value_of('FireResistanceDoorSuccess'),DoorType.value_of('DoorTypeSuccess')])

if all(DoorResults):
    AllDoorSuccess = True
else: 
    AllDoorSuccess = False



EscalatorReg.set_value('AllDoorSuccess', AllDoorSuccess)
EscalatorReg.set_value('NumberOfCompartmentsConnectedToEscalatorStaircase', 3)

EscalatorRegResult =EscalatorReg.model_expand()
print(EscalatorRegResult)