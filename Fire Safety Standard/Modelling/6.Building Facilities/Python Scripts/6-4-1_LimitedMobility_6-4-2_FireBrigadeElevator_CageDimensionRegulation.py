from cdmn.API import DMN

#For limited mobility elevators and firebrigade elevators
CageDim = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-4-1_LimitedMobility_6-4-2_FireBrigadeElevator_CageDimensionRegulation.dmn',auto_propagate=True)

print("inputs:", CageDim.get_inputs())
print("outputs:", CageDim.get_outputs())
print("other:", CageDim.get_intermediary())


CageDim.set_value('ElevatorCageDimensionSuccess', True)

CageDimResult =CageDim.model_expand()
print(CageDimResult)

