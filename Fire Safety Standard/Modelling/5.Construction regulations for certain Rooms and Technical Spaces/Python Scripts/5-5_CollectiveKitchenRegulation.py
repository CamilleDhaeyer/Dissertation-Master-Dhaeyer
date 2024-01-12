from cdmn.API import DMN

#LargeRoom=zaal
CollectiveKitchen = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/5-5_CollectiveKitchenRegulation.dmn',auto_propagate=True)

print("inputs:", CollectiveKitchen.get_inputs())
print("outputs:", CollectiveKitchen.get_outputs())
print("other:", CollectiveKitchen.get_intermediary())


#module to determine: FireResistanceAllWallSuccess
#Define list of fire resistances from the walls
FRwall_list=["EI_60","EI_60","EI_30","EI_30"]


#Define empty result list
WallResults=[]


#Call general wall EI 60 DMN
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


#module to determine: AllDoorTypeSuccess
#Define list of variables from the doors
FRdoor_list=[["EI_30","Selfclosing_door","Collective_kitchen","Door_rotates_in_direction_of_evacuation"],["EI_30","Selfclosing_door_during_fire","Collective_kitchen","Door_rotates_in_direction_of_evacuation"]]


#Define empty result list
DoorResults_FR=[]
DoorResults_Type=[]
DoorResults_Rot=[]


#call all door DMNs
FRdoorEI30 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceDoorModuleEI30.dmn',auto_propagate=True)
DoorType = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/DoorTypeModule.dmn',auto_propagate=True)
DoorRotation = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/DoorRotationModule.dmn',auto_propagate=True)



for Door in FRdoor_list:
    FRdoorEI30.set_value('FireResistanceDoor', Door[0])
    DoorType.set_value('DoorType', Door[1])
    DoorType.set_value('RoomType', Door[2])
    DoorRotation.set_value('DoorRotation', Door[3])
    #DoorResults.append([FRdoorEI30.value_of('FireResistanceDoorSuccess'),DoorType.value_of('DoorTypeSuccess'),DoorRotation.value_of('DoorRotationSuccess')])
    DoorResults_FR.append(FRdoorEI30.value_of('FireResistanceDoorSuccess'))
    DoorResults_Type.append(DoorType.value_of('DoorTypeSuccess'))
    DoorResults_Rot.append(DoorRotation.value_of('DoorRotationSuccess'))
    
print(DoorResults_FR)
print(DoorResults_Type)
print(DoorResults_Rot)

if all(DoorResults_FR):
    FireResistanceAllDoorSuccess = True
else: 
    FireResistanceAllDoorSuccess = False

if all(DoorResults_Type):
    AllDoorTypeSuccess = True
else: 
    AllDoorTypeSuccess = False

if all(DoorResults_Rot):
    AllDoorRotationSuccess = True
else: 
    AllDoorRotationSuccess = False




#set values from modules
CollectiveKitchen.set_value('AllDoorTypeSuccess', AllDoorTypeSuccess)
CollectiveKitchen.set_value('FireResistanceAllDoorSuccess', FireResistanceAllDoorSuccess)
CollectiveKitchen.set_value('AllDoorRotationSuccess', AllDoorRotationSuccess)

CollectiveKitchen.set_value('FireResistanceAllWallSuccess', FireResistanceAllWallSuccess)

CollectiveKitchenResult = CollectiveKitchen.model_expand()
print(CollectiveKitchenResult)
