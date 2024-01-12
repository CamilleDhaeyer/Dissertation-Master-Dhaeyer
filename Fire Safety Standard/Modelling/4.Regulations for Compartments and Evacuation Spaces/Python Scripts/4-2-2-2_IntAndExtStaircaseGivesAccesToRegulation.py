from cdmn.API import DMN


#get all types of variables from each DMN
StaircaseAccessTo = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-2-2-2_IntAndExtStaircaseGivesAccesToRegulation.dmn',auto_propagate=True)

print("inputs:", StaircaseAccessTo.get_inputs())
print("outputs:", StaircaseAccessTo.get_outputs())
print("other:", StaircaseAccessTo.get_intermediary())

StaircaseAccessTo.set_value('StaircaseAccesToSuccess', True)


StaircaseAccessToResult = StaircaseAccessTo.model_expand()
print(StaircaseAccessToResult)

