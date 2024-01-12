from cdmn.API import DMN

#Not for exhaust ducts
DuctElementReg = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-7-2_DuctElementGeneralRegulations_ExceptExhaustDuct.dmn',auto_propagate=True)

print("inputs:", DuctElementReg.get_inputs())
print("outputs:", DuctElementReg.get_outputs())
print("other:", DuctElementReg.get_intermediary())


DuctElementReg.set_value('DuctElementRegulationSuccess', True)


DuctElementRegResult =DuctElementReg.model_expand()
print(DuctElementRegResult)