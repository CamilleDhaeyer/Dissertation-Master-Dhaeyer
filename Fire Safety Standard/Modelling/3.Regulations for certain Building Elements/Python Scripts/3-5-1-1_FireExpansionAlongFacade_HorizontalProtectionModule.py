from cdmn.API import DMN


HorizontalElement = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-5-1-1_FireExpansionAlongFacade_HorizontalProtectionModule.dmn',auto_propagate=True)

print("inputs:", HorizontalElement.get_inputs())
print("outputs:", HorizontalElement.get_outputs())
print("other:", HorizontalElement.get_intermediary())

FRE60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/FireResistanceE60.dmn',auto_propagate=True)

print("inputs:", FRE60.get_inputs())
print("outputs:", FRE60.get_outputs())
print("other:", FRE60.get_intermediary())



#Fire resistance of floor extension through module

FRE60.set_value('FireResistance', "E_60")
print(FRE60.value_of('FireResistanceSuccess'))
HorizontalElement.set_value('FireResistanceFloorExtensionSuccess', FRE60.value_of('FireResistanceSuccess'))
FRE60.clear()

#Fire resistance of parapet through module
FRE60.set_value('FireResistance', "E_60")
print(FRE60.value_of('FireResistanceSuccess'))
HorizontalElement.set_value('FireResistanceParapetSuccess', FRE60.value_of('FireResistanceSuccess'))
FRE60.clear()

#Fire resistance of lintel through module
FRE60.set_value('FireResistance', "E_60")
print(FRE60.value_of('FireResistanceSuccess'))
HorizontalElement.set_value('FireResistanceLintelSuccess', FRE60.value_of('FireResistanceSuccess'))
FRE60.clear()

#Set other values

HorizontalElement.set_value('FloorThickness', 0.2)
HorizontalElement.set_value('ContinousFacade', False)

HorizontalElement.set_value('HeightParapet', 0.5)
HorizontalElement.set_value('HeightLintel', 0.1)
HorizontalElement.set_value('WidthFloorExtension', 0.2)


HorizontalElement.set_value('PresenceHorizontalFloorExtensionPastFacade', True)

HorizontalElementResult = HorizontalElement.model_expand()
print(HorizontalElementResult)
print(HorizontalElement.value_of('HorizontalFireProtectionElementSuccess'))