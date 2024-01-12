from cdmn.API import DMN


#get all types of variables from each DMN
DuplexIntStaircase = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-2-2-3_DuplexConnectionToInteriorStaircaseRegulation.dmn',auto_propagate=True)

print("inputs:", DuplexIntStaircase.get_inputs())
print("outputs:", DuplexIntStaircase.get_outputs())
print("other:", DuplexIntStaircase.get_intermediary())


DuplexIntStaircase.set_value('DuplexAreaFirstFloor', 40)
DuplexIntStaircase.set_value('DuplexAreaSecondFloor', 50)

DuplexIntStaircaseResult = DuplexIntStaircase.model_expand()
print(DuplexIntStaircaseResult)
