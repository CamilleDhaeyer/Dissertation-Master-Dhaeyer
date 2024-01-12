from cdmn.API import DMN


ElevatorVentilationReg = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-1-3-1_VentilationPossibilityRegulation.dmn',auto_propagate=True)

print("inputs:", ElevatorVentilationReg.get_inputs())
print("outputs:", ElevatorVentilationReg.get_outputs())
print("other:", ElevatorVentilationReg.get_intermediary())

ElevatorVentilationReg.set_value('VentilationOptionSuccess', True)


ElevatorVentilationRegResult = ElevatorVentilationReg.model_expand()
print(ElevatorVentilationRegResult)