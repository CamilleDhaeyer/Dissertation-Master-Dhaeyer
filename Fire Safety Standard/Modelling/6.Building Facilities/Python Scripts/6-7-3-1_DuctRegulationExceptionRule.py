from cdmn.API import DMN

#ONLY for exhaust ducts
DuctRegException = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-7-3-1_DuctRegulationExceptionRule.dmn',auto_propagate=True)

print("inputs:", DuctRegException.get_inputs())
print("outputs:", DuctRegException.get_outputs())
print("other:", DuctRegException.get_intermediary())


DuctRegException.set_value('DuctRegulationExceptionSuccess', True)



DuctRegExceptionResult =DuctRegException.model_expand()
print(DuctRegExceptionResult)