from cdmn.API import DMN


MachineRoom = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-1-2-4_ElevatorAndGoodsElevator_MachineRoomRegulation.dmn',auto_propagate=True)

print("inputs:", MachineRoom.get_inputs())
print("outputs:", MachineRoom.get_outputs())
print("other:", MachineRoom.get_intermediary())


ElevatorDrivingSystem="Non oleo hydraulic elevator"


if ElevatorDrivingSystem == "Oleo hydraulic elevator":
    #define list of all machine room walls
    FRRoomwall_list=["EI_120","EI_180","EI_120","EI_120"]

    FRwallEI120 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/FireResistanceWallModuleEI120.dmn',auto_propagate=True)


    #Define empty result list
    WallRoomResults=[]


    #Call general wall EI 60 DMN
    FRwallEI120 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/FireResistanceWallModuleEI120.dmn',auto_propagate=True)
    for FR in FRRoomwall_list:
        FRwallEI120.set_value('FireResistanceWall', FR)
        WallRoomResults.append(FRwallEI120.value_of('FireResistanceWallSuccess'))
        FRwallEI120.clear()


    #Map to FireResistanceAllWallSuccess

    if all(WallRoomResults):
        FireResistanceAllWallSuccess = True
    else: 
        FireResistanceAllWallSuccess = False


    MachineRoom.set_value('FireResistanceAllWallSuccess', FireResistanceAllWallSuccess)
    
    
    #Define access method
    AirlockPresent=False

    if AirlockPresent == True:
        #airlock regulation DMN
        Airlock = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/AirlockRegulation.dmn',auto_propagate=True)


        #Define list of fire resistances from the airlock walls
        FRwall_list=["EI_60","EI_60","EI_90","EI_90"]


        #Define empty result list
        WallResults=[]


        #Call general wall EI 60 DMN
        for FR in FRwall_list:
            FRwallEI120.set_value('FireResistanceWall', FR)
            WallResults.append(FRwallEI120.value_of('FireResistanceWallSuccess'))
            FRwallEI120.clear()


        #Map to AirlockAllWallSuccess

        if all(WallResults):
            AirlockAllWallSuccess = True
        else: 
            AirlockAllWallSuccess = False



        #Define list of fire resistances from the airlock doors
        FRdoor_list=[["EI_30","Selfclosing_door","Airlock"],["EI_30","Selfclosing_door","Airlock"]]


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
            AirlockAllDoorSuccess = True
        else: 
            AirlockAllDoorSuccess = False


        #set values for the airlock DMN
        Airlock.set_value('AreaOfAirlock', 2)
        Airlock.set_value('AirlockAllWallSuccess', AirlockAllWallSuccess)
        Airlock.set_value('AirlockAllDoorSuccess', AirlockAllDoorSuccess)

        MachineRoom.set_value('FireResistanceAccessSuccess', Airlock.value_of('AirlockRegulationSuccess'))
        
        

        MachineRoomResult =MachineRoom.model_expand()
        print(MachineRoomResult)

    elif AirlockPresent == False:
        
        FREI60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/FireResistanceModuleEI60.dmn',auto_propagate=True)
        DoorTypeAndFR = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/SelfClosingFRDoorModule.dmn',auto_propagate=True)
        DoorType = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/DoorTypeModule.dmn',auto_propagate=True)

        MachineRoomDoor=["EI_60","Selfclosing_door","Machine_room"]
        
        FREI60.set_value('FireResistance', MachineRoomDoor[0])
        DoorType.set_value('DoorType', MachineRoomDoor[1])
        DoorType.set_value('RoomType', MachineRoomDoor[2])
        
        DoorTypeAndFR.set_value('DoorTypeSuccess', DoorType.value_of('DoorTypeSuccess'))
        DoorTypeAndFR.set_value('FireResistanceDoorSuccess', FREI60.value_of('FireResistanceSuccess'))

        MachineRoom.set_value('FireResistanceAccessSuccess', DoorTypeAndFR.value_of('DoorSuccess'))
        

        MachineRoomResult =MachineRoom.model_expand()
        print(MachineRoomResult)
    

if ElevatorDrivingSystem == "Non oleo hydraulic elevator":
    #define list of all machine room walls without the wall facing the elevator shaft
    FRRoomwall_list=["EI_120","EI_180","EI_120","EI_120"]


    #Define empty result list
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


    MachineRoom.set_value('FireResistanceAllWallSuccess', FireResistanceAllWallSuccess)
    
    
    #Define list of fire resistances from the airlock doors
    FRdoor_list=["EI_30","EI_30"]


    #Define empty result list
    DoorResults=[]
    
    
    FRdoorEI30 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceDoorModuleEI30.dmn',auto_propagate=True)
    for Door in FRdoor_list:
        FRdoorEI30.set_value('FireResistanceDoor', Door)
        DoorResults.append(FRdoorEI30.value_of('FireResistanceDoorSuccess'))


    if all(DoorResults):
        FireResistanceAccessSuccess = True
    else: 
        FireResistanceAccessSuccess = False

    
    
    MachineRoom.set_value('FireResistanceAccessSuccess', FireResistanceAccessSuccess)
    

    MachineRoomResult =MachineRoom.model_expand()
    print(MachineRoomResult)