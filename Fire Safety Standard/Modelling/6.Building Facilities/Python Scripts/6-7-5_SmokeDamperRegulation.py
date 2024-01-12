from cdmn.API import DMN

#for fire dampers
SmokeDamperRegulation = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-7-5_SmokeDamperRegulation.dmn',auto_propagate=True)

print("inputs:", SmokeDamperRegulation.get_inputs())
print("outputs:", SmokeDamperRegulation.get_outputs())
print("other:", SmokeDamperRegulation.get_intermediary())


SmokeDamperRegulation.set_value('SmokeDamperRegulationSuccess', True)


SmokeDamperRegulationResult =SmokeDamperRegulation.model_expand()
print(SmokeDamperRegulationResult)