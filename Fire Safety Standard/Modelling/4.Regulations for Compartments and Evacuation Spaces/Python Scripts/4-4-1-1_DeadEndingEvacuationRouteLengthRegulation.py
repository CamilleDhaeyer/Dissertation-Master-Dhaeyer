from cdmn.API import DMN


EvacDeadEnd = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-4-1-1_DeadEndingEvacuationRouteLengthRegulation.dmn',auto_propagate=True)
EvacDeadEnd.clear()


print("inputs:", EvacDeadEnd.get_inputs())
print("outputs:", EvacDeadEnd.get_outputs())
print("other:", EvacDeadEnd.get_intermediary())

EvacDeadEnd.set_value('DeadEndingEvacuationRouteLengthSuccess', True)

EvacDeadEndResult = EvacDeadEnd.model_expand()
print(EvacDeadEndResult)

