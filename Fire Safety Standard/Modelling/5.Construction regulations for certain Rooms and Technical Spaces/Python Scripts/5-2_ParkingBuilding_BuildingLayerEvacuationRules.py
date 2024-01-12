from cdmn.API import DMN


BuildingLayerAccessGen = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/5-2_ParkingBuilding_BuildingLayerEvacuationRules_General.dmn',auto_propagate=True)

print("inputs:", BuildingLayerAccessGen.get_inputs())
print("outputs:", BuildingLayerAccessGen.get_outputs())
print("other:", BuildingLayerAccessGen.get_intermediary())

Combination = "Combo 5"

if Combination == "Combo 8" or Combination == "Combo 9" or Combination == "Combo 10" or Combination == "Combo 11":
    ComboAllowedModule = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/5-2_ParkingBuilding_BuildingLayerEvacuationRules_ComboAllowedModule.dmn',auto_propagate=True)
    
    ComboAllowedModule.set_value('NumberOfBuildingLayersAboveGround', 2)
    ComboAllowedModule.set_value('CurrentBuildingLayerToVehicleExitLevelDistanceInLevels', 1)
    ComboAllowedModule.set_value('MaximumDistanceToAccessPointOfEvacuationRoute', 30)
    ComboAllowedModule.set_value('MaximumDistanceToAccessPointOfExit', 30)
    
    IsAllowed = ComboAllowedModule.value_of('IsCombo8or9or10or11Allowed')
    if IsAllowed == False:
        Combination = "Not allowed"

if Combination == "Combo 1" or Combination == "Combo 2" or  Combination == "Combo 3" or Combination == "Combo 4" or Combination == "Combo 5" or Combination == "Combo 6" or Combination == "Combo 7" or Combination == "Combo 8" or Combination == "Combo 9" or Combination == "Combo 10" or Combination == "Combo 11":
    LargestDistance = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/5-2_ParkingBuilding_BuildingLayerEvacuationRules_LargestDistanceModule.dmn',auto_propagate=True)
    EffWidth = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/5-2_ParkingBuilding_BuildingLayerEvacuationRules_EffectiveWidthModule.dmn',auto_propagate=True)

    #Assumed that only the largest distance on the building layer is extracted from Revit 
    LargestDistance.set_value('LargestDistanceToNearestExit', 30)
    AllStairsMaximumDistanceSuccess = LargestDistance.value_of('StairMaximumDistanceSuccess')
    #define list of all effective widths of all stair elements of all stairs connected to the building layer
    StairElementEffWidthList=[1.2,0.8,0.8,1.2]
    StairElementEffWidthResult=[]
    for e in StairElementEffWidthList:
        EffWidth.set_value('StairElementWidth', e)
        StairElementEffWidthResult.append(EffWidth.value_of('StairEffectiveWidthSuccess'))

    if all(StairElementEffWidthResult):
        AllStairsEffectiveWidthSuccess = True
    else:
            AllStairsEffectiveWidthSuccess = False


    BuildingLayerAccessGen.set_value('NumberOfEvacuationOptionsConnectedToBuildingLayer', 3)
    BuildingLayerAccessGen.set_value('AllStairsAccessibleEverywhereOnBuildingLayer', True)
    BuildingLayerAccessGen.set_value('AllStairsEffectiveWidthSuccess', AllStairsEffectiveWidthSuccess)
    BuildingLayerAccessGen.set_value('AllStairsMaximumDistanceSuccess', AllStairsMaximumDistanceSuccess)

if Combination == "Combo 4" or Combination == "Combo 5" or Combination == "Combo 10":
    #Additional check on the direct exit door
    DirectExit = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/5-2_ParkingBuilding_BuildingLayerEvacuationRules_DirectExitModule.dmn',auto_propagate=True)
    
    ExitReg = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-2-2-3_EvacuationRouteConnectionToInteriorStaircaseRegulation.dmn',auto_propagate=True)
    
    
    #Define a list of the required variables of the direct exit door
    DirectExit_list=["EI_30","Selfclosing_door","Building_layer",1.2,"Turns_with_escape_direction",False]

    #call all door DMNs

    DoorTypeAndFR = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/SelfClosingFRDoorModule.dmn',auto_propagate=True)
    FRdoorEI30 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceDoorModuleEI30.dmn',auto_propagate=True)
    DoorType = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/DoorTypeModule.dmn',auto_propagate=True)



    FRdoorEI30.set_value('FireResistanceDoor', DirectExit_list[0])
    DoorType.set_value('DoorType', DirectExit_list[1])
    DoorType.set_value('RoomType', DirectExit_list[2])

    DoorTypeAndFR.set_value('FireResistanceDoorSuccess', FRdoorEI30.value_of('FireResistanceDoorSuccess'))
    DoorTypeAndFR.set_value('DoorTypeSuccess', DoorType.value_of('DoorTypeSuccess'))



    ExitReg.set_value('DoorSuccess', DoorTypeAndFR.value_of('DoorSuccess'))
    ExitReg.set_value('DoorEffectiveWidth', DirectExit_list[3])
    ExitReg.set_value('DoorTurningDirection', DirectExit_list[4])
    ExitReg.set_value('DoorIsEquippedWithLockingSystem', DirectExit_list[5])
    
    ConnectionEvacuationRouteAndInteriorStaircaseSuccess = ExitReg.value_of('ConnectionEvacuationRouteAndInteriorStaircaseSuccess')
    
    DirectExit.set_value('ConnectionEvacuationRouteAndInteriorStaircaseSuccess', ConnectionEvacuationRouteAndInteriorStaircaseSuccess)
    DirectExit.set_value('BuildingLayerLocation', "Underground")
    
    DirectExitResult = DirectExit.model_expand()
    print(DirectExitResult)
    
if Combination == "Combo 6" or Combination == "Combo 7" or Combination == "Combo 11":
    #additional check on the sloped road
    SlopedRoad = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/5-2_ParkingBuilding_BuildingLayerEvacuationRules_SlopedRoadModule.dmn',auto_propagate=True)
    FREI120 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/FireResistanceWallModuleEI120.dmn',auto_propagate=True)
    
    #define list of the fire resistances of the walls along the sloped road
    Wall_list= ["EI_120","EI_120"]
    Wall_result=[]
    for FR in Wall_list:
        FREI120.set_value('FireResistanceWall', FR)
        Wall_result.append(FREI120.value_of('FireResistanceWallSuccess'))
        
    if all(Wall_result):
        FireResistanceAllWallSuccess = True
    else:
        FireResistanceAllWallSuccess = False
    SlopedRoad.set_value('FireResistanceAllWallSuccess', FireResistanceAllWallSuccess)
    
    SlopedRoad.set_value('SlopeOfAccessRoad', 5)
    SlopedRoad.set_value('AreaOfCompartment', 450)
    SlopedRoad.set_value('CanEvacuateBySlopingAccessRoad', True)
    
    SlopedRoadResult = SlopedRoad.model_expand()
    print(SlopedRoadResult)
    
if Combination == "Not allowed":
    print("Combination of exits is not allowed for this building layer")

    
    

BuildingLayerAccessGenResult = BuildingLayerAccessGen.model_expand()
print(BuildingLayerAccessGenResult)