from cdmn.API import DMN
import numpy as np

EffWidthReg = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-2-3-2_EffectiveWidthOfInteriorEscapewayElementsRegulation.dmn',auto_propagate=True)

print("inputs:", EffWidthReg.get_inputs())
print("outputs:", EffWidthReg.get_outputs())
print("other:", EffWidthReg.get_intermediary())


EffWidth = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/EffectiveWidthOfElements.dmn',auto_propagate=True)
PassageUnit = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/EffectiveWidthOfElements_PassagewayUnit.dmn',auto_propagate=True)


PassageUnit.set_value('TypeOfEscapeWay', "Door")
PassageUnit.set_value('MaximalValueInUserTotal', 24)
PassagewayUnit=PassageUnit.value_of('PassagewayUnit')
print(PassagewayUnit)

IntegerMultiple= np.ceil(float(eval(PassagewayUnit)))

EffWidth.set_value('TotalNumberOfEscapeWayTypes', 2)

EffWidth.set_value('IntegerMultiple', IntegerMultiple)
EffWidth.set_value('TotalActualEffectiveWidth', 2.4)

#mark that the required effective width is calculated based on the assumption that all doors have the same effective width
print(float(eval(EffWidth.value_of('RequiredEffectiveWidth'))))

RequiredEffectiveWidth= EffWidth.value_of('RequiredEffectiveWidth')

EffWidthReg.set_value('RequiredEffectiveWidth', float(eval(EffWidth.value_of('RequiredEffectiveWidth'))))
EffWidthReg.set_value('ElementEffectiveWidth', 1.8)


EffWidthRegResult = EffWidthReg.model_expand()
print(EffWidthRegResult)