from cdmn.API import DMN


VentilationDamperReg = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-1-3-3_VentilationDamperControlMethodRegulation.dmn',auto_propagate=True)

print("inputs:", VentilationDamperReg.get_inputs())
print("outputs:", VentilationDamperReg.get_outputs())
print("other:", VentilationDamperReg.get_intermediary())

VentilationDamperReg.set_value('VentilationDamperControlMethodSuccess', True)


VentilationDamperRegResult = VentilationDamperReg.model_expand()
print(VentilationDamperRegResult)