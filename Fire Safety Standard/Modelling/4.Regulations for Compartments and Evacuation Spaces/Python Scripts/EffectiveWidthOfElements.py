from cdmn.API import DMN
import numpy as np

#get all types of variables from each DMN
EffWidth = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/EffectiveWidthOfElements.dmn',auto_propagate=True)
PassageUnit = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/EffectiveWidthOfElements_PassagewayUnit.dmn',auto_propagate=True)

print("inputs:", EffWidth.get_inputs())
print("outputs:", EffWidth.get_outputs())
print("other:", EffWidth.get_intermediary())


print("inputs:", PassageUnit.get_inputs())
print("outputs:", PassageUnit.get_outputs())
print("other:", PassageUnit.get_intermediary())


PassageUnit.set_value('TypeOfEscapeWay', "Door")
PassageUnit.set_value('MaximalValueInUserTotal', 24)
PassagewayUnit=PassageUnit.value_of('PassagewayUnit')
print(PassagewayUnit)

IntegerMultiple= np.ceil(float(eval(PassagewayUnit)))

EffWidth.set_value('TotalNumberOfEscapeWayTypes', 2)

EffWidth.set_value('IntegerMultiple', IntegerMultiple)
EffWidth.set_value('TotalActualEffectiveWidth', 2.4)

EffWidthResult = EffWidth.model_expand()
print(EffWidthResult)

#mark that the required effective width is calculated based on the assumption that all doors have the same effective width
print(float(eval(EffWidth.value_of('RequiredEffectiveWidth'))))

