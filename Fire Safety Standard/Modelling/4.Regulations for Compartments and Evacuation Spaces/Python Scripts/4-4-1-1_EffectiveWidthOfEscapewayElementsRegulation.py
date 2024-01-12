from cdmn.API import DMN
import numpy as np

EscapewayEffWidth = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-4-1-1_EffectiveWidthOfEscapewayElementsRegulation.dmn',auto_propagate=True)

print("inputs:", EscapewayEffWidth.get_inputs())
print("outputs:", EscapewayEffWidth.get_outputs())
print("other:", EscapewayEffWidth.get_intermediary())

#DMNs required to define the RequiredEffectiveWidth
EffWidth = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/EffectiveWidthOfElements.dmn',auto_propagate=True)
PassageUnit = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/EffectiveWidthOfElements_PassagewayUnit.dmn',auto_propagate=True)
PassageUnit.set_value('TypeOfEscapeWay', "Door")
PassageUnit.set_value('MaximalValueInUserTotal', 24)
PassagewayUnit=PassageUnit.value_of('PassagewayUnit')
IntegerMultiple= np.ceil(float(eval(PassagewayUnit)))
EffWidth.set_value('TotalNumberOfEscapeWayTypes', 2)
EffWidth.set_value('IntegerMultiple', IntegerMultiple)
EffWidth.set_value('TotalActualEffectiveWidth', 2.4)

#mark that the required effective width is calculated based on the assumption that all doors have the same effective width
print(float(eval(EffWidth.value_of('RequiredEffectiveWidth'))))

RequiredEffectiveWidth= EffWidth.value_of('RequiredEffectiveWidth')

EscapewayEffWidth.set_value('RequiredEffectiveWidth', float(eval(EffWidth.value_of('RequiredEffectiveWidth'))))
EscapewayEffWidth.set_value('ElementEffectiveWidth', 0.8)

EscapewayEffWidthResult = EscapewayEffWidth.model_expand()
print(EscapewayEffWidthResult)