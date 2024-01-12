from cdmn.API import DMN


ElevatorElementApply = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-1-2-3_ElevatorElementRegulationApplianceRule.dmn',auto_propagate=True)

print("inputs:", ElevatorElementApply.get_inputs())
print("outputs:", ElevatorElementApply.get_outputs())
print("other:", ElevatorElementApply.get_intermediary())

ElevatorElementApply.set_value('ElevatorElementRegulationNotRequiredSuccess', True)


ElevatorElementApplyResult = ElevatorElementApply.model_expand()
print(ElevatorElementApplyResult)