from cdmn.API import DMN

TechnRoomGeneralExitReg = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/5-1-1_TechnicalRoomGeneral_ExitRegulation.dmn',auto_propagate=True)

print("inputs:", TechnRoomGeneralExitReg.get_inputs())
print("outputs:", TechnRoomGeneralExitReg.get_outputs())
print("other:", TechnRoomGeneralExitReg.get_intermediary())


ExitConnectionTo = "Exit_connects_to_exterior_reaching_an_evacuation_level"


#this can possibly be set in a foor loop to go over all doors that either connect to a compartment or staircase
if ExitConnectionTo == "Exit_connects_to_other_comparment":
    TechnRoomGeneralExitReg.clear()
    FRdoorEI60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/FireResistanceDoorModuleEI60.dmn',auto_propagate=True)

    #define exit to compartment door
    FRdoor ="EI_60"
    FRdoorEI60.set_value('FireResistanceDoor', FRdoor)
    FireResistanceDoorSuccess=FRdoorEI60.value_of('FireResistanceDoorSuccess')


    TechnRoomGeneralExitReg.set_value('FireResistanceDoorSuccess', FireResistanceDoorSuccess)
    TechnRoomGeneralExitReg.set_value('ExitConnectionTo', "Exit_connects_to_other_comparment")
    
    
    TechnRoomGeneralExitRegResult = TechnRoomGeneralExitReg.model_expand()
    print(TechnRoomGeneralExitRegResult)




elif ExitConnectionTo == "Exit_connects_to_staircase":
    TechnRoomGeneralExitReg.clear()
    Airlock = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/AirlockRegulation.dmn',auto_propagate=True)

    #Define list of fire resistances from the airlock walls
    FRwall_list=["EI_60","EI_60","EI_30","EI_30"]

    WallResults=[]

    FRwallEI60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceWallModuleEI60.dmn',auto_propagate=True)


    for FR in FRwall_list:
        FRwallEI60.set_value('FireResistanceWall', FR)
        FRwallEI60.propagate()#niet per se nodig want staat al op autopropagate
        print(FRwallEI60.value_of('FireResistanceWallSuccess'))
        WallResults.append(FRwallEI60.value_of('FireResistanceWallSuccess'))
        FRwallEI60.clear()

    if all(WallResults):
        AirlockAllWallSuccess = True
    else: 
        AirlockAllWallSuccess = False

    print(AirlockAllWallSuccess)


    #Define list of fire resistances from the airlock doors
    FRdoor_list=[["EI_30","Selfclosing_door","Airlock"],["EI_30","Selfclosing_door","Airlock"]]

    DoorResults=[]

    DoorTypeAndFR = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/SelfClosingFRDoorModule.dmn',auto_propagate=True)
    FRdoorEI30 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceDoorModuleEI30.dmn',auto_propagate=True)
    DoorType = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/DoorTypeModule.dmn',auto_propagate=True)

    for Door in FRdoor_list:
        FRdoorEI30.set_value('FireResistanceDoor', Door[0])
        DoorType.set_value('DoorType', Door[1])
        DoorType.set_value('RoomType', Door[2])
        DoorResults.append([FRdoorEI30.value_of('FireResistanceDoorSuccess'),DoorType.value_of('DoorTypeSuccess')])


    if all(DoorResults):
        AirlockAllDoorSuccess = True
    else: 
        AirlockAllDoorSuccess = False

    #set values for the airlock DMN
    Airlock.set_value('AreaOfAirlock', 2)
    Airlock.set_value('AirlockAllWallSuccess', AirlockAllWallSuccess)
    Airlock.set_value('AirlockAllDoorSuccess', AirlockAllDoorSuccess)


    AirlockRegulationSuccess=Airlock.value_of('AirlockRegulationSuccess')


    TechnRoomGeneralExitReg.set_value('ExitConnectionTo', "Exit_connects_to_staircase")
    TechnRoomGeneralExitReg.set_value('AirlockRegulationSuccess', AirlockRegulationSuccess)


    TechnRoomGeneralExitRegResult = TechnRoomGeneralExitReg.model_expand()
    print(TechnRoomGeneralExitRegResult)

elif ExitConnectionTo == "Exit_connects_to_exterior_reaching_an_evacuation_level":
    TechnRoomGeneralExitReg.clear()
    TechnRoomGeneralExitReg.set_value('ExitConnectionTo', "Exit_connects_to_exterior_reaching_an_evacuation_level")
    TechnRoomGeneralExitRegResult = TechnRoomGeneralExitReg.model_expand()
    print(TechnRoomGeneralExitRegResult)