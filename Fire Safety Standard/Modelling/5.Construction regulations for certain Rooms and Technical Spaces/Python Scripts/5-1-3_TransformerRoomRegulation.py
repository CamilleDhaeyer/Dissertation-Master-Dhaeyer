from cdmn.API import DMN
#For the elements connected to a technical room: Evacuation route; intermediate stair landing; stair landing; airlock
TransformerRoom = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/5-1-3_TransformerRoomRegulation.dmn',auto_propagate=True)

print("inputs:", TransformerRoom.get_inputs())
print("outputs:", TransformerRoom.get_outputs())
print("other:", TransformerRoom.get_intermediary())



FRdoorEI60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/FireResistanceDoorModuleEI60.dmn',auto_propagate=True)

#define door FR
FRdoorList =["EI_60","EI_60"]
FRdoorResult=[]
for FR in FRdoorList:
    FRdoorEI60.set_value('FireResistanceDoor', FR)
    FRdoorResult.append(FRdoorEI60.value_of('FireResistanceDoorSuccess'))

if all(FRdoorResult):
    FireResistanceAllDoorSuccess = True
else:
    FireResistanceAllDoorSuccess = False


#define wall FR
#If the transformer room is not temporary made on site or a prefab; no exterior walls are included in the wall list


FRwallEI120 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/FireResistanceWallModuleEI120.dmn',auto_propagate=True)

#define door FR
FRwallList =["EI_120","EI_120","EI_90"]
FRwallResult=[]

for FR in FRwallList:
    FRwallEI120.set_value('FireResistanceWall', FR)
    FRwallResult.append(FRwallEI120.value_of('FireResistanceWallSuccess'))

if all(FRwallResult):
    FireResistanceAllWallSuccess = True
else:
    FireResistanceAllWallSuccess = False



TransformerRoom.set_value('FireResistanceAllDoorSuccess', FireResistanceAllDoorSuccess)
TransformerRoom.set_value('FireResistanceAllWallSuccess', FireResistanceAllWallSuccess)


TransformerRoomResult = TransformerRoom.model_expand()
print(TransformerRoomResult)
