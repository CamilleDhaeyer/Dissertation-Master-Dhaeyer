from cdmn.API import DMN

RoofModule = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/1-2_GlazedFacade_RoofOfBuildingSegmentFireResistanceModule.dmn')

print("inputs:", RoofModule.get_inputs())
print("outputs:", RoofModule.get_outputs())
print("other:", RoofModule.get_intermediary())

RoofModule.clear()

RoofModule.set_value('HorizontalDistanceFromFacade', 2)
RoofModule.set_value('FireResistanceRoof', "EI_60")

RoofModuleResult = RoofModule.model_expand()
print(RoofModuleResult)

