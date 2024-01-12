from cdmn.API import DMN

ExtStaircaseGeneral = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-3_ExteriorStaircaseGeneralRegulation.dmn',auto_propagate=True)

print("inputs:", ExtStaircaseGeneral.get_inputs())
print("outputs:", ExtStaircaseGeneral.get_outputs())
print("other:", ExtStaircaseGeneral.get_intermediary())

ExtStaircaseGeneral.set_value('ExteriorStaircaseGeneralRegulationSuccess', True)

ExtStaircaseGeneralResult = ExtStaircaseGeneral.model_expand()
print(ExtStaircaseGeneralResult)