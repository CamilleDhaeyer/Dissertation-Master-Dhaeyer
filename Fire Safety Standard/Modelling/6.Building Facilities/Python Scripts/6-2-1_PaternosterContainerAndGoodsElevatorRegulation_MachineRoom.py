from cdmn.API import DMN


Paternoster_MachineRoom = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-2-1_PaternosterContainerAndGoodsElevatorRegulation_MachineRoom.dmn',auto_propagate=True)

print("inputs:", Paternoster_MachineRoom.get_inputs())
print("outputs:", Paternoster_MachineRoom.get_outputs())
print("other:", Paternoster_MachineRoom.get_intermediary())





#define list of all machine room walls
FRRoomwall_list=["EI_120","EI_180","EI_120","EI_120"]
#Define list of fire resistances from the machine room door(s)
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


Paternoster_MachineRoom.set_value('FireResistanceAllDoorSuccess', FireResistanceAllDoorSuccess)
Paternoster_MachineRoom.set_value('FireResistanceAllWallSuccess', FireResistanceAllWallSuccess)


Paternoster_MachineRoomResult =Paternoster_MachineRoom.model_expand()
print(Paternoster_MachineRoomResult)