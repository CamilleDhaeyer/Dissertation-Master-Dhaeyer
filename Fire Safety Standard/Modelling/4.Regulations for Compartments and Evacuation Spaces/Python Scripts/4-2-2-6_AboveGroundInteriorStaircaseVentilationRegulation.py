from cdmn.API import DMN


#get all types of variables from each DMN
VentilationHatch = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-2-2-6_AboveGroundInteriorStaircaseVentilationRegulation.dmn',auto_propagate=True)

print("inputs:", VentilationHatch.get_inputs())
print("outputs:", VentilationHatch.get_outputs())
print("other:", VentilationHatch.get_intermediary())

VentilationHatch.set_value('AreaOfVentilationOpening', 2)


VentilationHatchResult = VentilationHatch.model_expand()
print(VentilationHatchResult)

