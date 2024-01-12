from cdmn.API import DMN


EvacIntStaircase = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-2-2-3_EvacuationRouteConnectionToInteriorStaircaseRegulation.dmn',auto_propagate=True)

print("inputs:", EvacIntStaircase.get_inputs())
print("outputs:", EvacIntStaircase.get_outputs())
print("other:", EvacIntStaircase.get_intermediary())


FRdoor_list=["EI_30","Selfclosing_door","Interior_staircase"]

#call all door DMNs

DoorTypeAndFR = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/SelfClosingFRDoorModule.dmn',auto_propagate=True)
FRdoorEI30 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceDoorModuleEI30.dmn',auto_propagate=True)
DoorType = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/DoorTypeModule.dmn',auto_propagate=True)



FRdoorEI30.set_value('FireResistanceDoor', FRdoor_list[0])
DoorType.set_value('DoorType', FRdoor_list[1])
DoorType.set_value('RoomType', FRdoor_list[2])

DoorTypeAndFR.set_value('FireResistanceDoorSuccess', FRdoorEI30.value_of('FireResistanceDoorSuccess'))
DoorTypeAndFR.set_value('DoorTypeSuccess', DoorType.value_of('DoorTypeSuccess'))



EvacIntStaircase.set_value('DoorSuccess', DoorTypeAndFR.value_of('DoorSuccess'))
EvacIntStaircase.set_value('DoorEffectiveWidth', 1)
EvacIntStaircase.set_value('DoorTurningDirection', "Turns_with_escape_direction")
EvacIntStaircase.set_value('DoorIsEquippedWithLockingSystem', False)



EvacIntStaircaseResult = EvacIntStaircase.model_expand()
print(EvacIntStaircaseResult)