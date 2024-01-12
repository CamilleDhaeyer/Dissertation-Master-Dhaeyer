from cdmn.API import DMN

#for fire dampers
FireDamperRegulation = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-7-4_FireDamperRegulation.dmn',auto_propagate=True)

print("inputs:", FireDamperRegulation.get_inputs())
print("outputs:", FireDamperRegulation.get_outputs())
print("other:", FireDamperRegulation.get_intermediary())


FireDamperRegulation.set_value('FireDamperRegulationSuccess', True)


FireDamperRegulationResult =FireDamperRegulation.model_expand()
print(FireDamperRegulationResult)
