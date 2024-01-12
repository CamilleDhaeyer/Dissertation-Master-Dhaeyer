from cdmn.API import DMN


FRstructuralElement = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-2_StructuralElementFireResistance.dmn',auto_propagate=True)

print("inputs:", FRstructuralElement.get_inputs())
print("outputs:", FRstructuralElement.get_outputs())
print("other:", FRstructuralElement.get_intermediary())


#Possible values of inputs
print(FRstructuralElement.possible_values_of('LowestFloorEvacuationLevel'))
print(FRstructuralElement.possible_values_of('FloorLevelOfStructuralElement'))
print(FRstructuralElement.possible_values_of('FireResistanceOfStructuralElement'))

#Possible values of intermediate
print(FRstructuralElement.possible_values_of('AboveEvacuationLevel'))

#Possible values of output
print(FRstructuralElement.possible_values_of('StructuralElementFireResistanceSuccess'))


#set values

FRstructuralElement.set_value('LowestFloorEvacuationLevel', 1)
FRstructuralElement.set_value('FloorLevelOfStructuralElement', 2)
FRstructuralElement.set_value('FireResistanceOfStructuralElement',"R_90")

FRstructuralElementResult = FRstructuralElement.model_expand()
print(FRstructuralElementResult)
