from cdmn.API import DMN

ExtStaircaseCompCon = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-3_ExteriorStaircaseConnectionToCompartmentRegulation.dmn',auto_propagate=True)

print("inputs:", ExtStaircaseCompCon.get_inputs())
print("outputs:", ExtStaircaseCompCon.get_outputs())
print("other:", ExtStaircaseCompCon.get_intermediary())

ExtStaircaseCompCon.set_value('ExteriorStaircaseConnectionToCompartmentSuccess', True)

ExtStaircaseCompConResult = ExtStaircaseCompCon.model_expand()
print(ExtStaircaseCompConResult)