from cdmn.API import DMN


#get all types of variables from each DMN
ExceptionAllowedElement = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-2-2-7_AllowedExceptionElementsInInteriorStaircase.dmn',auto_propagate=True)

print("inputs:", ExceptionAllowedElement.get_inputs())
print("outputs:", ExceptionAllowedElement.get_outputs())
print("other:", ExceptionAllowedElement.get_intermediary())

ExceptionAllowedElement.set_value('ExceptionElementsInStaircase', "Electrical_cables")


ExceptionAllowedElementResult = ExceptionAllowedElement.model_expand()
print(ExceptionAllowedElementResult)



