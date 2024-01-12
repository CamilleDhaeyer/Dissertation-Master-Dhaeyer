from cdmn.API import DMN

GlazedFacade = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/1-2_GlazedFacadeAboveBuildingSegmentRegulation_v2.dmn')

print("inputs:", GlazedFacade.get_inputs())
print("outputs:", GlazedFacade.get_outputs())
print("other:", GlazedFacade.get_intermediary())

#check possible values of the input variables
#boolean, integer and double (real) types give 'None'
print(GlazedFacade.possible_values_of('HeightFromRoof'))
print(GlazedFacade.possible_values_of('ProvidedFireResistanceFacade'))
print(GlazedFacade.possible_values_of('HorizontalDistanceFromFacade'))
print(GlazedFacade.possible_values_of('ProvidedFireResistanceRoof'))


#check possible values of the intermediate variables
print(GlazedFacade.possible_values_of('FireResistanceBuildingFacadeSuccess'))


#check possible values of the output variables
print(GlazedFacade.possible_values_of('GlazedFacadeAboveBuildingSuccess'))


#Set values of a (partial) set of input variables

GlazedFacade.clear()

GlazedFacade.set_value('HeightFromRoof', 2)
GlazedFacade.set_value('ProvidedFireResistanceFacade', "Facade_is_E_60_or_higher")
GlazedFacade.set_value('HorizontalDistanceFromFacade', 2)
GlazedFacade.set_value('ProvidedFireResistanceRoof', "Roof_is_E_60_or_higher")


GlazedFacadeResult = GlazedFacade.model_expand()
print(GlazedFacadeResult)


"""
GlazedFacade.propagate()
print(GlazedFacade.value_of('GlazedFacadeAboveBuildingSuccess'))
"""
