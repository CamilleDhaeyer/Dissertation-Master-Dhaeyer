from cdmn.API import DMN


#get all types of variables from each DMN
FacadeOpeningRule = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/1-2_OpeningInFacadeRegulation.dmn',auto_propagate=True)


print("inputs:",FacadeOpeningRule.get_inputs())
print("outputs:", FacadeOpeningRule.get_outputs())
print("other:", FacadeOpeningRule.get_intermediary())

FacadeOpeningModule = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/1-2_OpeningInFacade_OpeningElementFireResistanceModule.dmn',auto_propagate=True)


print("inputs:",FacadeOpeningModule.get_inputs())
print("outputs:", FacadeOpeningModule.get_outputs())
print("other:", FacadeOpeningModule.get_intermediary())


RoofElementModule = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/1-2_OpeningInFacade_ProtectiveElementFireResistanceModule.dmn',auto_propagate=True)


print("inputs:",RoofElementModule.get_inputs())
print("outputs:", RoofElementModule.get_outputs())
print("other:", RoofElementModule.get_intermediary())


#set values for the module DMNs

FacadeOpeningModule.set_value('FireResistanceOpeningElement', "EI_60")
FacadeOpeningModule.set_value('HeightOfOpeningFromRoof', 2 )

FacadeOpeningModuleResult = FacadeOpeningModule.model_expand()
#print(FacadeOpeningModuleResult)


RoofElementModule.set_value('FireResistanceProtectiveElement', "EI_60")
RoofElementModule.set_value('HorizontalDistanceFromFacade', 3 )

RoofElementModuleResult = RoofElementModule.model_expand()
#print(RoofElementModuleResult)



#verify values of output variables from the modules
#print(FacadeOpeningModule.value_of('OpeningElementProvidedFireResistance'))

#print(RoofElementModule.value_of('ProtectiveElementProvidedFireResistance'))

#set values of the main DMN model
FacadeOpeningRule.set_value('OpeningElementProvidedFireResistance', FacadeOpeningModule.value_of('OpeningElementProvidedFireResistance'))
FacadeOpeningRule.set_value('ProtectiveElementProvidedFireResistance', RoofElementModule.value_of('ProtectiveElementProvidedFireResistance'))
FacadeOpeningRule.set_value('HorizontalDistanceFromFacade', 3)
FacadeOpeningRule.set_value('HeightOfOpeningFromRoof', 2)



FacadeOpeningRuleResult = FacadeOpeningRule.model_expand()
print(FacadeOpeningRuleResult)
