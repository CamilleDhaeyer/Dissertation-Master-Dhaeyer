from cdmn.API import DMN

#Camunda method
HeightVerification = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/2.Compartimentering en evacuatie/final/2-1_CompartmentGeneralHeightVerification_v2.dmn',auto_propagate=True)

print("inputs:", HeightVerification.get_inputs())
print("outputs:", HeightVerification.get_outputs())
print("other:", HeightVerification.get_intermediary())


HeightVerification.set_value('HeightOfCompartmentFloorLevel', 2)
HeightVerification.set_value('HeightOfCompartment', 3)


HeightVerificationResult = HeightVerification.model_expand()
print(HeightVerificationResult)