from cdmn.API import DMN

FacadeModule = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/1-2_GlazedFacade_FacadeOfBuildingFireResistanceModule.dmn')

print("inputs:",FacadeModule.get_inputs())
print("outputs:", FacadeModule.get_outputs())
print("other:", FacadeModule.get_intermediary())

FacadeModule.clear()

FacadeModule.set_value('HeightFromRoof', 2)
FacadeModule.set_value('FireResistanceFacade', "EI_60")

FacadeModuleResult = FacadeModule.model_expand()
print(FacadeModuleResult)
