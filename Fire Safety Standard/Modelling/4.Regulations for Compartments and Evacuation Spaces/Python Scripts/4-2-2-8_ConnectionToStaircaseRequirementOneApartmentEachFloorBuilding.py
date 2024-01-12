from cdmn.API import DMN


#get all types of variables from each DMN
OneApartment = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-2-2-8_ConnectionToStaircaseRequirementOneApartmentEachFloorBuilding.dmn',auto_propagate=True)

print("inputs:", OneApartment.get_inputs())
print("outputs:", OneApartment.get_outputs())
print("other:", OneApartment.get_intermediary())


#verify door to above ground staircase
ApartmentIntStaircase = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-2-2-8_BuildingOnlyApartmentConnectionToInteriorStaircaseRegulation_Door.dmn',auto_propagate=True)
DoorTypeAndFR = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/SelfClosingFRDoorModule.dmn',auto_propagate=True)
FRdoorEI30 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceDoorModuleEI30.dmn',auto_propagate=True)
DoorType = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/DoorTypeModule.dmn',auto_propagate=True)

#door above ground staircase
AboveIntStaircaseDoorList=["EI_30","Selfclosing_door","Apartment","BuildingWithOnly1ApartmentPerFloorLevel",1,"Turns_with_escape_direction",False]


FRdoorEI30.set_value('FireResistanceDoor', AboveIntStaircaseDoorList[0])
DoorType.set_value('DoorType', AboveIntStaircaseDoorList[1])
DoorType.set_value('RoomType', AboveIntStaircaseDoorList[2])
DoorType.set_value('TypeOfBuilding', AboveIntStaircaseDoorList[3])

DoorTypeAndFR.set_value('FireResistanceDoorSuccess', FRdoorEI30.value_of('FireResistanceDoorSuccess'))
DoorTypeAndFR.set_value('DoorTypeSuccess', DoorType.value_of('DoorTypeSuccess'))


ApartmentIntStaircase.set_value('DoorSuccess', DoorTypeAndFR.value_of('DoorSuccess'))
ApartmentIntStaircase.set_value('DoorEffectiveWidth', AboveIntStaircaseDoorList[4])
ApartmentIntStaircase.set_value('DoorIsEquippedWithLockingSystem', AboveIntStaircaseDoorList[6])


ConnectionApartmentAndInteriorStaircaseSuccess = ApartmentIntStaircase.value_of('ConnectionApartmentAndInteriorStaircaseSuccess')



OneApartment.set_value('ConnectionApartmentAndInteriorStaircaseSuccess', ConnectionApartmentAndInteriorStaircaseSuccess)#DMN 4.2.2.3
OneApartment.set_value('AutomaticFireDetectionSystemPresentInBuilding', True)



OneApartmentResult = OneApartment.model_expand()
print(OneApartmentResult)