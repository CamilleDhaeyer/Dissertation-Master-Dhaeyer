from cdmn.API import DMN


ElevatorGeneralReg = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-1-1_ElevatorAndGoodsElevatorGeneralRegulation.dmn',auto_propagate=True)

print("inputs:", ElevatorGeneralReg.get_inputs())
print("outputs:", ElevatorGeneralReg.get_outputs())
print("other:", ElevatorGeneralReg.get_intermediary())


ElevatorGeneralReg.set_value('ElevatorShaftHasFireFightingEquipmentWithWater', False)
ElevatorGeneralReg.set_value('ElevatorOilReservoirLocation', "Oil_reservoir_in_machine_room")
ElevatorGeneralReg.set_value('ElevatorDriverSystemLocation', "Machine_room")
ElevatorGeneralReg.set_value('ElevatorDrivingSystem', "Oleo_hydraulic_elevator")
ElevatorGeneralReg.set_value('ElevatorType', "Elevator")

ElevatorGeneralRegResult = ElevatorGeneralReg.model_expand()
print(ElevatorGeneralRegResult)