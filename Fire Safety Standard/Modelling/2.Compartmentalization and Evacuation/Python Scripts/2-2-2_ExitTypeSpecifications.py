from cdmn.API import DMN


ExitTypeSpec = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/2.Compartimentering en evacuatie/final/2-2-2_ExitTypeSpecifications.dmn',auto_propagate=True)

print("inputs:", ExitTypeSpec.get_inputs())
print("outputs:", ExitTypeSpec.get_outputs())
print("other:", ExitTypeSpec.get_intermediary())

ExitTypeSpec.set_value('BuildingLayerLevel', 2)
ExitTypeSpec.set_value('SpaceType', "Compartment")

#CompartmentExits.set_value('CompartmentNumberOfExitsVerification', True)

ExitTypeSpecResult = ExitTypeSpec.model_expand()
print(ExitTypeSpecResult)
