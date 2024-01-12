from cdmn.API import DMN


ElectricalDuct = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-5-2_InstallationsElectricalDuctRegulation.dmn',auto_propagate=True)

print("inputs:", ElectricalDuct.get_inputs())
print("outputs:", ElectricalDuct.get_outputs())
print("other:", ElectricalDuct.get_intermediary())


ElectricalDuct.set_value('InstallationElectricalDuctRegulationSuccess', True)


ElectricalDuctResult =ElectricalDuct.model_expand()
print(ElectricalDuctResult)