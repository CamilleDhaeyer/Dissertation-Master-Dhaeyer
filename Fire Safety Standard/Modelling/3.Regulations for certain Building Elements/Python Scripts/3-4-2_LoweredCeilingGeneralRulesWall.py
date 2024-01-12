from cdmn.API import DMN


LoweredCeilingGeneral = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-4-2_LoweredCeilingGeneralRulesWall.dmn',auto_propagate=True)
LoweredCeilingGeneral.clear()


print("inputs:", LoweredCeilingGeneral.get_inputs())
print("outputs:", LoweredCeilingGeneral.get_outputs())
print("other:", LoweredCeilingGeneral.get_intermediary())



FRwallEI30 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/FireResistanceWallModuleEI30.dmn',auto_propagate=True)

FRwallEI30.set_value('FireResistanceWall', "EI_30")



LoweredCeilingGeneral.set_value('FireResistanceWallSuccess', FRwallEI30.value_of('FireResistanceWallSuccess'))
LoweredCeilingGeneral.set_value('RoomHeightTillCeiling', 4)
LoweredCeilingGeneral.set_value('RoomHeightTillLoweredCeiling', 3.7)
LoweredCeilingGeneral.set_value('WallHeight', 4)

LoweredCeilingGeneral.set_value('PresenceLoweredCeilingInRoom', True)
LoweredCeilingGeneral.set_value('PresenceAutomaticExtinguishingSystem', False)
LoweredCeilingGeneral.set_value('ProjectedCeilingAreaInscribableIn25mSquare', False)


LoweredCeilingGeneralResult = LoweredCeilingGeneral.model_expand()
print(LoweredCeilingGeneralResult)

