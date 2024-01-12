from cdmn.API import DMN
#Python script without modules
RoofOpeningRule = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/1-2_OpeningInRoofRegulation.dmn')

print("inputs:",RoofOpeningRule.get_inputs())
print("outputs:", RoofOpeningRule.get_outputs())
print("other:", RoofOpeningRule.get_intermediary())

RoofOpeningRule.set_value('HorizontalDistanceOfOpeningFromFacade', 2)
RoofOpeningRule.set_value('OpeningElementProvidedFireResistance', "Element_in_opening_is_E_60_or_higher")

RoofOpeningRule.set_value('HorizontalDistanceFromFacade', 3)
RoofOpeningRule.set_value('ProtectiveElementProvidedFireResistance', "EI_60")

RoofOpeningRule.set_value('OpeningInRoofPresent', True)
RoofOpeningRule.set_value('OpeningsTotalArea', 0.005)

RoofOpeningRuleResult = RoofOpeningRule.model_expand()
print(RoofOpeningRuleResult)

