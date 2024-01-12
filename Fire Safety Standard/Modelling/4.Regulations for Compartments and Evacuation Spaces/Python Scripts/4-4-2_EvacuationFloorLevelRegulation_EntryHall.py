from cdmn.API import DMN


EvacRouteEntryHall = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-4-2_EvacuationFloorLevelRegulation_EntryHall.dmn',auto_propagate=True)

print("inputs:", EvacRouteEntryHall.get_inputs())
print("outputs:", EvacRouteEntryHall.get_outputs())
print("other:", EvacRouteEntryHall.get_intermediary())



EvacRouteEntryHall.set_value('EntryHallRequirementSuccess', True)



EvacRouteEntryHallResult = EvacRouteEntryHall.model_expand()
print(EvacRouteEntryHallResult)
