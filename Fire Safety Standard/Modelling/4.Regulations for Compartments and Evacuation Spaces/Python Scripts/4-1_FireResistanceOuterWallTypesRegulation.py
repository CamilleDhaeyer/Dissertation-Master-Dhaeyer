from cdmn.API import DMN


#get all types of variables from each DMN
FROuterWall = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-1_FireResistanceOuterWallTypesRegulation.dmn',auto_propagate=True)

print("inputs:", FROuterWall.get_inputs())
print("outputs:", FROuterWall.get_outputs())
print("other:", FROuterWall.get_intermediary())

print(FROuterWall.possible_values_of('FacadeMessage'))


FROuterWall.set_value('FireResistanceWall', "EI_60")

FROuterWallResult = FROuterWall.model_expand()
print(FROuterWallResult)