from cdmn.API import DMN

#verify if parking building is one large compartment
ParkingCompartment = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/5-2_ParkingBuildingCompartmentRegulation.dmn',auto_propagate=True)

print("inputs:", ParkingCompartment.get_inputs())
print("outputs:", ParkingCompartment.get_outputs())


ParkingCompartment.set_value('ParkingBuildingIsOneCompartment', True)

ParkingCompartmentResult = ParkingCompartment.model_expand()
print(ParkingCompartmentResult)


#To verify the outer walls of the parking building ==> use DMNs of 3-5


#DMN to check walls and access of non-residential premises in parking building (if present)
#non-residential premises such as transformer rooms, storage areas, archives, technical rooms
ParkingNonResRoom = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/5-2_ParkingBuildingNonResidentialRoomRegulation.dmn',auto_propagate=True)


AirlockPresent=False

if AirlockPresent == True:
    #airlock regulation DMN
    Airlock = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/AirlockRegulation.dmn',auto_propagate=True)


    #Define list of fire resistances from the airlock walls
    FRwall_list=["EI_60","EI_60","EI_90","EI_90"]


    #Define empty result list
    WallResults=[]


    #Call general wall EI 60 DMN
    FRwallEI60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceWallModuleEI60.dmn',auto_propagate=True)
    for FR in FRwall_list:
        FRwallEI60.set_value('FireResistanceWall', FR)
        FRwallEI60.propagate()#niet per se nodig want staat al op autopropagate
        print(FRwallEI60.value_of('FireResistanceWallSuccess'))
        WallResults.append(FRwallEI60.value_of('FireResistanceWallSuccess'))
        FRwallEI60.clear()


    #Map to AirlockAllWallSuccess

    if all(WallResults):
        AirlockAllWallSuccess = True
    else: 
        AirlockAllWallSuccess = False



    #Define list of fire resistances from the airlock doors
    FRdoor_list=[["EI_30","Selfclosing_door","Non_residential_premises"],["EI_30","Selfclosing_door","Non_residential_premises"]]


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

    
    
    ParkingNonResRoom.set_value('AirlockRegulationSuccess', Airlock.value_of('AirlockRegulationSuccess'))#module
    ParkingNonResRoom.set_value('AccessType', "Airlock")
    

    FRwall_list_NonResRoom=["EI_60","EI_60","EI_60","EI_60"]
    FRwall_list_NonResRoom_result=[]
    for FR in FRwall_list_NonResRoom:
        FRwallEI60.set_value('FireResistanceWall', FR)
        FRwall_list_NonResRoom_result.append(FRwallEI60.value_of('FireResistanceWallSuccess'))
        FRwallEI60.clear()



    #Map to FireResistanceAllWallSuccess

    if all(WallResults):
        FireResistanceAllWallSuccess = True
    else: 
        FireResistanceAllWallSuccess = False

    print(FireResistanceAllWallSuccess)
    
    
    
    ParkingNonResRoom.set_value('FireResistanceAllWallSuccess', FireResistanceAllWallSuccess)#module


    ParkingNonResRoomResult = ParkingNonResRoom.model_expand()
    print(ParkingNonResRoomResult)

elif AirlockPresent == False:
    FRwallEI60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceWallModuleEI60.dmn',auto_propagate=True)
        
    FRwall_list_NonResRoom=["EI_60","EI_60","EI_60","EI_60"]
    FRwall_list_NonResRoom_result=[]
    for FR in FRwall_list_NonResRoom:
        FRwallEI60.set_value('FireResistanceWall', FR)
        FRwall_list_NonResRoom_result.append(FRwallEI60.value_of('FireResistanceWallSuccess'))
        FRwallEI60.clear()



    #Map to FireResistanceAllWallSuccess

    if all(FRwall_list_NonResRoom_result):
        FireResistanceAllWallSuccess = True
    else: 
        FireResistanceAllWallSuccess = False

    print(FireResistanceAllWallSuccess)
    
    
    
    ParkingNonResRoom.set_value('FireResistanceAllWallSuccess', FireResistanceAllWallSuccess)#module

    
    FREI60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/FireResistanceModuleEI60.dmn',auto_propagate=True)
    DoorTypeAndFR = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/SelfClosingFRDoorModule.dmn',auto_propagate=True)
    DoorType = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/DoorTypeModule.dmn',auto_propagate=True)

    WasteDisposalDoor=["EI_60","Selfclosing_door","Non_residential_premises"]
    
    FREI60.set_value('FireResistance', WasteDisposalDoor[0])
    DoorType.set_value('DoorType', WasteDisposalDoor[1])
    DoorType.set_value('RoomType', WasteDisposalDoor[2])
    
    DoorTypeAndFR.set_value('DoorTypeSuccess', DoorType.value_of('DoorTypeSuccess'))
    DoorTypeAndFR.set_value('FireResistanceDoorSuccess', FREI60.value_of('FireResistanceSuccess'))

    

    ParkingNonResRoom.set_value('DoorSuccess', DoorTypeAndFR.value_of('DoorSuccess'))#module
    ParkingNonResRoom.set_value('AccessType', "Door")

    
    ParkingNonResRoomResult = ParkingNonResRoom.model_expand()
    print(ParkingNonResRoomResult)


