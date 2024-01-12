from cdmn.API import DMN


#get all types of variables from each DMN
DuplexHeight = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/2.Compartimentering en evacuatie/final/2-1_ExceptionB_DuplexHeightVerification.dmn',auto_propagate=True)

print("inputs:", DuplexHeight.get_inputs())
print("outputs:", DuplexHeight.get_outputs())
print("other:", DuplexHeight.get_intermediary())

DuplexHeight.set_value('HeightFirstFloorLevelOfDuplex', 2)
DuplexHeight.set_value('HeightSecondFloorLevelOfDuplex', 3)
DuplexHeight.set_value('HeightOfCompartment', 4)


DuplexHeightResult = DuplexHeight.model_expand()
print(DuplexHeightResult)


