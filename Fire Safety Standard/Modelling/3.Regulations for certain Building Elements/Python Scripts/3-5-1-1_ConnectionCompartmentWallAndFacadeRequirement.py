from cdmn.API import DMN


CompartmentWallFacadeConnection = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-5-1-1_ConnectionCompartmentWallAndFacadeRequirement.dmn',auto_propagate=True)
CompartmentWallFacadeConnection.clear()


print("inputs:", CompartmentWallFacadeConnection.get_inputs())
print("outputs:", CompartmentWallFacadeConnection.get_outputs())
print("other:", CompartmentWallFacadeConnection.get_intermediary())



print(CompartmentWallFacadeConnection.possible_values_of('FireResistanceCompartmentWallConnectionToFacade'))



CompartmentWallFacadeConnection.set_value('FireResistanceCompartmentWallConnectionToFacadeSuccess', True)


CompartmentWallFacadeConnectionResult = CompartmentWallFacadeConnection.model_expand()
print(CompartmentWallFacadeConnectionResult)
