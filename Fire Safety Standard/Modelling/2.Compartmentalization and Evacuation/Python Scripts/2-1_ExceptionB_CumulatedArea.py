from cdmn.API import DMN


#get all types of variables from each DMN
CumulatedArea = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/2.Compartimentering en evacuatie/final/2-1_ExceptionB_CumulatedArea.dmn',auto_propagate=True)

print("inputs:", CumulatedArea.get_inputs())
print("outputs:", CumulatedArea.get_outputs())
print("other:", CumulatedArea.get_intermediary())

CumulatedAreaResult = CumulatedArea.model_expand()
print(CumulatedAreaResult)

