from cdmn.API import DMN


#get all types of variables from each DMN
IntStaircaseAboveUnder = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-2-2-5_RespectiveLocationUnderGroundAndAboveGroundInteriorStaircaseRequirements.dmn',auto_propagate=True)

print("inputs:", IntStaircaseAboveUnder.get_inputs())
print("outputs:", IntStaircaseAboveUnder.get_outputs())
print("other:", IntStaircaseAboveUnder.get_intermediary())


#Define list of fire resistances from the above and under ground interior staircase walls
AboveIntStaircaseWallList=["EI_60","EI_60","EI_60","EI_60"]
UnderIntStaircaseWallList=["EI_90","EI_90","EI_90","EI_90"]


#Define empty result list
AboveWallResults=[]
UnderWallResults=[]


#Call general wall EI 60 DMN
FRwallEI60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceWallModuleEI60.dmn',auto_propagate=True)

for FR in AboveIntStaircaseWallList:
    FRwallEI60.set_value('FireResistanceWall', FR)
    AboveWallResults.append(FRwallEI60.value_of('FireResistanceWallSuccess'))
    FRwallEI60.clear()
    
for FR in UnderIntStaircaseWallList:
    FRwallEI60.set_value('FireResistanceWall', FR)
    UnderWallResults.append(FRwallEI60.value_of('FireResistanceWallSuccess'))
    FRwallEI60.clear()



#Map to FireresistanceAllWallOfAboveGroundStaircaseSuccess and FireresistanceAllWallOfUnderGroundStaircaseSuccess

if all(AboveWallResults):
    FireresistanceAllWallOfAboveGroundStaircaseSuccess = True
else: 
    FireresistanceAllWallOfAboveGroundStaircaseSuccess = False


if all(UnderWallResults):
    FireresistanceAllWallOfUnderGroundStaircaseSuccess = True
else: 
    FireresistanceAllWallOfUnderGroundStaircaseSuccess = False


#verify door to above ground staircase
EvacIntStaircase = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-2-2-3_EvacuationRouteConnectionToInteriorStaircaseRegulation.dmn',auto_propagate=True)
DoorTypeAndFR = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/SelfClosingFRDoorModule.dmn',auto_propagate=True)
FRdoorEI30 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceDoorModuleEI30.dmn',auto_propagate=True)
DoorType = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/DoorTypeModule.dmn',auto_propagate=True)

#door above ground staircase
AboveIntStaircaseDoorList=["EI_30","Selfclosing_door","Interior_staircase",1,"Turns_with_escape_direction",False]




FRdoorEI30.set_value('FireResistanceDoor', AboveIntStaircaseDoorList[0])
DoorType.set_value('DoorType', AboveIntStaircaseDoorList[1])
DoorType.set_value('RoomType', AboveIntStaircaseDoorList[2])

DoorTypeAndFR.set_value('FireResistanceDoorSuccess', FRdoorEI30.value_of('FireResistanceDoorSuccess'))
DoorTypeAndFR.set_value('DoorTypeSuccess', DoorType.value_of('DoorTypeSuccess'))


EvacIntStaircase.set_value('DoorSuccess', DoorTypeAndFR.value_of('DoorSuccess'))
EvacIntStaircase.set_value('DoorEffectiveWidth', AboveIntStaircaseDoorList[3])
EvacIntStaircase.set_value('DoorTurningDirection', AboveIntStaircaseDoorList[4])
EvacIntStaircase.set_value('DoorIsEquippedWithLockingSystem', AboveIntStaircaseDoorList[5])


ConnectionEvacuationRouteAndAboveGroundInteriorStaircaseSuccess=EvacIntStaircase.value_of('ConnectionEvacuationRouteAndInteriorStaircaseSuccess')

#door under ground staircase
UnderIntStaircaseDoorList=["EI_30","Selfclosing_door","Interior_staircase",1,"Turns_with_escape_direction",False]

FRdoorEI30.clear()
DoorType.clear()
DoorTypeAndFR.clear()
EvacIntStaircase.clear()

FRdoorEI30.set_value('FireResistanceDoor', UnderIntStaircaseDoorList[0])
DoorType.set_value('DoorType', UnderIntStaircaseDoorList[1])
DoorType.set_value('RoomType', UnderIntStaircaseDoorList[2])

DoorTypeAndFR.set_value('FireResistanceDoorSuccess', FRdoorEI30.value_of('FireResistanceDoorSuccess'))
DoorTypeAndFR.set_value('DoorTypeSuccess', DoorType.value_of('DoorTypeSuccess'))


EvacIntStaircase.set_value('DoorSuccess', DoorTypeAndFR.value_of('DoorSuccess'))
EvacIntStaircase.set_value('DoorEffectiveWidth', UnderIntStaircaseDoorList[3])
EvacIntStaircase.set_value('DoorTurningDirection', UnderIntStaircaseDoorList[4])
EvacIntStaircase.set_value('DoorIsEquippedWithLockingSystem', UnderIntStaircaseDoorList[5])


ConnectionEvacuationRouteAndUnderGroundInteriorStaircaseSuccess = EvacIntStaircase.value_of('ConnectionEvacuationRouteAndInteriorStaircaseSuccess')





IntStaircaseAboveUnder.set_value('ConnectionEvacuationRouteAndAboveGroundInteriorStaircaseSuccess', ConnectionEvacuationRouteAndAboveGroundInteriorStaircaseSuccess)#DMN 4.2.2.3
IntStaircaseAboveUnder.set_value('ConnectionEvacuationRouteAndUnderGroundInteriorStaircaseSuccess', ConnectionEvacuationRouteAndUnderGroundInteriorStaircaseSuccess)#DMN 4.2.2.3


IntStaircaseAboveUnder.set_value('FireresistanceAllWallOfAboveGroundStaircaseSuccess', FireresistanceAllWallOfAboveGroundStaircaseSuccess)#module EI60
IntStaircaseAboveUnder.set_value('FireresistanceAllWallOfUnderGroundStaircaseSuccess', FireresistanceAllWallOfUnderGroundStaircaseSuccess)#module EI60

IntStaircaseAboveUnderResult = IntStaircaseAboveUnder.model_expand()
print(IntStaircaseAboveUnderResult)