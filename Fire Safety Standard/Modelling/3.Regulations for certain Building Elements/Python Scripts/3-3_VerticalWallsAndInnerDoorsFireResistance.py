from cdmn.API import DMN


FRstructuralElement = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-3_VerticalWallsAndInnerDoorsFireResistance.dmn',auto_propagate=True)

print("inputs:", FRstructuralElement.get_inputs())
print("outputs:", FRstructuralElement.get_outputs())
print("other:", FRstructuralElement.get_intermediary())


#Define list of fire resistances from the airlock walls
FRwall_list=["EI_60","EI_60","EI_30","EI_30"]


#Define empty result list
WallResults=[]


#Call general wall EI 60 DMN
FRwallEI60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceWallModuleEI60.dmn',auto_propagate=True)
print("inputs:",FRwallEI60.get_inputs())
print("outputs:", FRwallEI60.get_outputs())
print("other:", FRwallEI60.get_intermediary())

for FR in FRwall_list:
    FRwallEI60.set_value('FireResistanceWall', FR)
    FRwallEI60.propagate()#niet per se nodig want staat al op autopropagate
    print(FRwallEI60.value_of('FireResistanceWallSuccess'))
    WallResults.append(FRwallEI60.value_of('FireResistanceWallSuccess'))
    FRwallEI60.clear()


print(WallResults)

#Map to AirlockAllWallSuccess

if all(WallResults):
    AllWallSuccess = True
else: 
    AllWallSuccess = False

print(AllWallSuccess)


#Define list of fire resistances from the airlock doors
FRdoor_list=[["EI_30","Selfclosing_door_during_fire","Archive_room"],["EI_30","Selfclosing_door","Archive_room"]]


#Define empty result list
DoorResults=[]

DoorFRresults=[]

#call all door DMNs

DoorTypeAndFR = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/SelfClosingFRDoorModule.dmn',auto_propagate=True)
print("inputs:",DoorTypeAndFR.get_inputs())
print("outputs:", DoorTypeAndFR.get_outputs())
print("other:", DoorTypeAndFR.get_intermediary())


FRdoorEI30 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceDoorModuleEI30.dmn',auto_propagate=True)
print("inputs:",FRdoorEI30.get_inputs())
print("outputs:", FRdoorEI30.get_outputs())
print("other:", FRdoorEI30.get_intermediary())


DoorType = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/DoorTypeModule.dmn',auto_propagate=True)
print("inputs:",DoorType.get_inputs())
print("outputs:", DoorType.get_outputs())
print("other:", DoorType.get_intermediary())



for Door in FRdoor_list:
    FRdoorEI30.set_value('FireResistanceDoor', Door[0])
    DoorFRresults.append(FRdoorEI30.value_of('FireResistanceDoorSuccess'))
    DoorType.set_value('DoorType', Door[1])
    DoorType.set_value('RoomType', Door[2])
    print(FRdoorEI30.value_of('FireResistanceDoorSuccess'))
    print(DoorType.value_of('DoorTypeSuccess'))
    DoorResults.append([FRdoorEI30.value_of('FireResistanceDoorSuccess'),DoorType.value_of('DoorTypeSuccess')])

print(DoorFRresults)
print(DoorResults)


if all(DoorFRresults):
    FireResistanceAllDoorSuccess = True
else: 
    FireResistanceAllDoorSuccess = False
    
    
print(FireResistanceAllDoorSuccess)
    
if all(DoorResults):
    AllDoorSuccess = True
else: 
    AllDoorSuccess = False

print(AllDoorSuccess)


FRstructuralElement.set_value('RoomType', "Archive_room")
FRstructuralElement.set_value('AllWallSuccess', AllWallSuccess)
FRstructuralElement.set_value('AllDoorSuccess', AllDoorSuccess)


FRstructuralElementResult = FRstructuralElement.model_expand()
print(FRstructuralElementResult)
