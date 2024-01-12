from cdmn.API import DMN


ExitCombo = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/5-2_ParkingBuildingEvacuationRegulation_ExitsCombo.dmn',auto_propagate=True)

print("inputs:", ExitCombo.get_inputs())
print("outputs:", ExitCombo.get_outputs())
print("other:", ExitCombo.get_intermediary())

print(ExitCombo.possible_values_of('FloorLevelEvacuationExitsCombination'))

ExitCombo.set_value('FloorLevelEvacuationExitsCombination', "Minimal_2_staircases")

ExitComboResult = ExitCombo.model_expand()
print(ExitComboResult)