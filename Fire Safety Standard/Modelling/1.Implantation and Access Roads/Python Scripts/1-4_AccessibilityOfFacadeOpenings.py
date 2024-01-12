from cdmn.API import DMN


#get all types of variables from each DMN
FacadeAccess = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/1-4_AccessibilityOfFacadeOpenings.dmn',auto_propagate=True)
print("inputs:", FacadeAccess.get_inputs())
print("outputs:", FacadeAccess.get_outputs())
print("other:", FacadeAccess.get_intermediary())

#check possible values of the input variables
#boolean, integer and double (real) types give 'None'

print(FacadeAccess.possible_values_of('DistanceEdgeOfTheRoadToPlaneOfFacade'))


FacadeAccess.set_value('DistanceEdgeOfTheRoadToPlaneOfFacade', 6)

FacadeAccessResult = FacadeAccess.model_expand()
print(FacadeAccessResult)