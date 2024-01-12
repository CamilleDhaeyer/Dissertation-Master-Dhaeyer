from cdmn.API import DMN

#get all types of variables from each DMN
EffWidth = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/EffectiveWidthOfElements_IntegerMultipleTest.dmn',auto_propagate=True)

print("inputs:", EffWidth.get_inputs())
print("outputs:", EffWidth.get_outputs())
print("other:", EffWidth.get_intermediary())


#This script only works when the " " parameter is an integer multiple of 0.6 as the ceiling(RealNumber) function does not work in cDMN
#The " " script works for all values as the ceiling() function is there implemented through python
EffWidth.set_value('MaximalValueInUserTotal', 36)
EffWidth.set_value('TypeOfEscapeWay', "Door")

EffWidth.set_value('TotalActualEffectiveWidth', 3.6)

EffWidthResult = EffWidth.model_expand()
print(EffWidthResult)