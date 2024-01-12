from cdmn.API import DMN


EvacDoorReg = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-4-1-2_EvacuationDoorRegulation.dmn',auto_propagate=True)
EvacDoorReg.clear()


print("inputs:", EvacDoorReg.get_inputs())
print("outputs:", EvacDoorReg.get_outputs())
print("other:", EvacDoorReg.get_intermediary())

EvacDoorReg.set_value('EvacuationDoorRegulationSuccess', True)

EvacDoorRegResult = EvacDoorReg.model_expand()
print(EvacDoorRegResult)

