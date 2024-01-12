from cdmn.API import DMN


#get all types of variables from each DMN
TriplexIntStaircase = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-2-2-3_TriplexConnectionToInteriorStaircaseRegulation_v2.dmn',auto_propagate=True)

print("inputs:", TriplexIntStaircase.get_inputs())
print("outputs:", TriplexIntStaircase.get_outputs())
print("other:", TriplexIntStaircase.get_intermediary())

TriplexIntStaircase.set_value('TriplexAreaFirstFloor', 40)
TriplexIntStaircase.set_value('TriplexAreaSecondFloor', 50)
TriplexIntStaircase.set_value('TriplexAreaThirdFloor', 30)


TriplexIntStaircaseResult = TriplexIntStaircase.model_expand()
print(TriplexIntStaircaseResult)
