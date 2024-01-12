from cdmn.API import DMN


#get all types of variables from each DMN
MultiFloorCompartments = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-2-2-4_MultipleCompartmentsForOneFloorLevelRegulationForInteriorStaircaseConnection.dmn',auto_propagate=True)

print("inputs:", MultiFloorCompartments.get_inputs())
print("outputs:", MultiFloorCompartments.get_outputs())
print("other:", MultiFloorCompartments.get_intermediary())


MultiFloorCompartments.set_value('NumberOfCompartmentsInFloorLevel', 2)

MultiFloorCompartmentsResult = MultiFloorCompartments.model_expand()
print(MultiFloorCompartmentsResult)