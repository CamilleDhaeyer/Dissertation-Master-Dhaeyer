from cdmn.API import DMN


GlazedFacade = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/1-2_GlazedFacadeAboveBuildingSegmentRegulation_v2.dmn',auto_propagate=True)
GlazedFacade.clear()

print("inputs:", GlazedFacade.get_inputs())
print("outputs:", GlazedFacade.get_outputs())
print("other:", GlazedFacade.get_intermediary())

RoofModule = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/1-2_GlazedFacade_RoofOfBuildingSegmentFireResistanceModule.dmn',auto_propagate=True)
RoofModule.clear()


print("inputs:", RoofModule.get_inputs())
print("outputs:", RoofModule.get_outputs())
print("other:", RoofModule.get_intermediary())


FacadeModule = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/1-2_GlazedFacade_FacadeOfBuildingFireResistanceModule.dmn',auto_propagate=True)
FacadeModule.clear()


print("inputs:",FacadeModule.get_inputs())
print("outputs:", FacadeModule.get_outputs())
print("other:", FacadeModule.get_intermediary())



RoofModule.set_value('HorizontalDistanceFromFacade', 2)
RoofModule.set_value('FireResistanceRoof', "EI_60")

RoofModuleResult = RoofModule.model_expand()
print(RoofModuleResult)


print(RoofModule.value_of('ProvidedFireResistanceRoof'))



FacadeModule.set_value('HeightFromRoof', 2)
FacadeModule.set_value('FireResistanceFacade', "EI_60")

FacadeModuleResult = FacadeModule.model_expand()
print(FacadeModuleResult)

print(FacadeModule.value_of('ProvidedFireResistanceFacade'))




GlazedFacade.set_value('HeightFromRoof', 2)
GlazedFacade.set_value('ProvidedFireResistanceFacade', FacadeModule.value_of('ProvidedFireResistanceFacade'))
GlazedFacade.set_value('HorizontalDistanceFromFacade', 2)
GlazedFacade.set_value('ProvidedFireResistanceRoof', RoofModule.value_of('ProvidedFireResistanceRoof'))


GlazedFacadeResult = GlazedFacade.model_expand()
print(GlazedFacadeResult)

