from cdmn.API import DMN

#for fire dampers
Hydrant = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-8-5-4-1_HydrantRegulation.dmn',auto_propagate=True)

print("inputs:", Hydrant.get_inputs())
print("outputs:", Hydrant.get_outputs())
print("other:", Hydrant.get_intermediary())

#set output values
Hydrant.set_value('PublicWaterSupplyNetworkIsSupplier', True)
Hydrant.set_value('IsHydrantRequired', True)


HydrantResult =Hydrant.model_expand()
print(HydrantResult)