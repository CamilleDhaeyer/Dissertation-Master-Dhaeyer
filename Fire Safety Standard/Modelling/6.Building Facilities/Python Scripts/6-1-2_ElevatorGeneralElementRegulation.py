from cdmn.API import DMN


ElevatorElementReg = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-1-2_ElevatorGeneralElementRegulation.dmn',auto_propagate=True)

print("inputs:", ElevatorElementReg.get_inputs())
print("outputs:", ElevatorElementReg.get_outputs())
print("other:", ElevatorElementReg.get_intermediary())

AreaCompare = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-1-2_ElevatorGeneralElement_AirlockSmallerRegulationModule.dmn',auto_propagate=True)

AirlockSmallerDoorReg = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-1-2_ElevatorGeneralElement_AirlockSmallerDoorModule.dmn',auto_propagate=True)

print("inputs:", AirlockSmallerDoorReg.get_inputs())
print("outputs:", AirlockSmallerDoorReg.get_outputs())
print("other:", AirlockSmallerDoorReg.get_intermediary())

AreaCompare.set_value('AreaOfAirlock', 10)
AreaCompare.set_value('AreaOfElevatorCage', 8)

#possibly define a list of door variable values

if AreaCompare.value_of('IsAirlockSmallerThanElevator') == True:
    AirlockSmallerDoorReg.set_value('SmokeDetectionSystemLocation', "Other")
    AirlockSmallerDoorReg.set_value('FireResistanceDoor', "EI_30")
    AirlockSmallerDoorReg.set_value('DoorType', "Selfclosing_door_during_fire")
    AirlockSmallerDoorReg.set_value('HasFireDetectionInstallation', True)

    ElevatorElementReg.set_value('AllDoorSuccess', AirlockSmallerDoorReg.value_of('DoorSuccess'))#module EI30

elif AreaCompare.value_of('IsAirlockSmallerThanElevator') == False:
    #Define list of fire resistances from the elevator to airlock doors
    FRdoor_list=[["EI_30","Selfclosing_door","Elevator_airlock_room"],["EI_30","Selfclosing_door_during_fire","Elevator_airlock_room"]]


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

    ElevatorElementReg.set_value('AllDoorSuccess', AllDoorSuccess)

ElevatorElementReg.set_value('FireResistanceAllWallSuccess', False)#module EI60
ElevatorElementReg.set_value('FireResistanceElevatorShaftDoorSuccess', True)#module EI30

ElevatorElementRegResult = ElevatorElementReg.model_expand()
print(ElevatorElementRegResult)