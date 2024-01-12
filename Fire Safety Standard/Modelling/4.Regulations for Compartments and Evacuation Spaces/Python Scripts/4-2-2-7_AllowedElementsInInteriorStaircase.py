from cdmn.API import DMN


#get all types of variables from each DMN
AllowedElement = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-2-2-7_AllowedElementsInInteriorStaircase.dmn',auto_propagate=True)

print("inputs:", AllowedElement.get_inputs())
print("outputs:", AllowedElement.get_outputs())
print("other:", AllowedElement.get_intermediary())

AllowedElement.set_value('ElementInStaircase', "Smoke_extraction_system")


AllowedElementResult = AllowedElement.model_expand()
print(AllowedElementResult)

