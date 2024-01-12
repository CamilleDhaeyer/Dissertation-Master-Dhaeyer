from cdmn.API import DMN


#get all types of variables from each DMN
ConnectionMBandOB = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/1-3_ConnectionRequirementBetweenMBandOB.dmn',auto_propagate=True)

#no intermediates
print("inputs:",ConnectionMBandOB.get_inputs())
print("outputs:", ConnectionMBandOB.get_outputs())


#airlock regulation DMN
Airlock = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/AirlockRegulation.dmn',auto_propagate=True)

print("inputs:", Airlock.get_inputs())
print("outputs:", Airlock.get_outputs())
print("other:", Airlock.get_intermediary())




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
    AirlockAllWallSuccess = True
else: 
    AirlockAllWallSuccess = False

print(AirlockAllWallSuccess)


#Define list of fire resistances from the airlock doors
Door_list=[["EI_30","Selfclosing_door","Airlock"],["EI_30","Selfclosing_door","Airlock"]]
TypeOfBuilding = "Any_other_building"

#Define empty result list
DoorResults=[]


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



for Door in Door_list:
    FRdoorEI30.set_value('FireResistanceDoor', Door[0])
    DoorType.set_value('DoorType', Door[1])
    DoorType.set_value('RoomType', Door[2])
    DoorType.set_value('TypeOfBuilding',TypeOfBuilding)
    print(FRdoorEI30.value_of('FireResistanceDoorSuccess'))
    print(DoorType.value_of('DoorTypeSuccess'))
    DoorTypeAndFR.set_value('FireResistanceDoorSuccess', FRdoorEI30.value_of('FireResistanceDoorSuccess'))
    DoorTypeAndFR.set_value('DoorTypeSuccess', DoorType.value_of('DoorTypeSuccess'))
    DoorResults.append(DoorTypeAndFR.value_of('DoorSuccess'))
    
print(DoorResults)

if all(DoorResults):
    AirlockAllDoorSuccess = True
else: 
    AirlockAllDoorSuccess = False

print(AirlockAllDoorSuccess)



#set values for the airlock DMN
Airlock.set_value('AreaOfAirlock', 2)
Airlock.set_value('AirlockAllWallSuccess', AirlockAllWallSuccess)
Airlock.set_value('AirlockAllDoorSuccess', AirlockAllDoorSuccess)


AirlockResult = Airlock.model_expand()
print(AirlockResult)



#set values for the ConnectionMBandOB DMN
ConnectionMBandOB.set_value('AirlockRegulationSuccess', Airlock.value_of('AirlockRegulationSuccess'))
ConnectionMBandOB.set_value('AirlockConnectsToStaircase', False)
ConnectionMBandOB.set_value('ConnectionWithAirlock', True)

ConnectionMBandOBResult = ConnectionMBandOB.model_expand()
print(ConnectionMBandOBResult)


