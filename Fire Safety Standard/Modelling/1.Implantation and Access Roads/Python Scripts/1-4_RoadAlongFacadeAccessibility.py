from cdmn.API import DMN


#get all types of variables from each DMN
RoadAccess = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/1-4_RoadAlongFacadeAccessibility.dmn',auto_propagate=True)
print("inputs:", RoadAccess.get_inputs())
print("outputs:", RoadAccess.get_outputs())
print("other:", RoadAccess.get_intermediary())

#check possible values of the input variables
#boolean, integer and double (real) types give 'None'


print(RoadAccess.possible_values_of('BuildingAccessible'))#Comes from 1-1_BuildingAccessibility DMN

print(RoadAccess.possible_values_of('NumberOfOtherFacadesAlongRoad'))
print(RoadAccess.possible_values_of('NumberOfPrincipleFacadesAlongRoad'))

print(RoadAccess.possible_values_of('OtherFacadeHasMainEntrance'))
print(RoadAccess.possible_values_of('PrincipleFacadeHasMainEntrance'))

#Set values

RoadAccess.set_value('NumberOfOtherFacadesAlongRoad', 2)
RoadAccess.set_value('NumberOfPrincipleFacadesAlongRoad', 1)

RoadAccessResult = RoadAccess.model_expand()
print(RoadAccessResult)

