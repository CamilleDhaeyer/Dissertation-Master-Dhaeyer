from cdmn.API import DMN
import numpy as np

CompEvacFurthestPoint = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-4-1-1_CompartmentFurthestPointToExitRequirement.dmn',auto_propagate=True)

print("inputs:", CompEvacFurthestPoint.get_inputs())
print("outputs:", CompEvacFurthestPoint.get_outputs())
print("other:", CompEvacFurthestPoint.get_intermediary())


CompEvacFurthestPoint.set_value('FurthestPointInCompartmentSuccess', True)

CompEvacFurthestPointResult = CompEvacFurthestPoint.model_expand()
print(CompEvacFurthestPointResult)
