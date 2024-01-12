from cdmn.API import DMN


LoweredCeilingSpecific = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-4-1_SpecificRoomsLoweredCeilingRequirement.dmn',auto_propagate=True)

print("inputs:", LoweredCeilingSpecific.get_inputs())
print("outputs:", LoweredCeilingSpecific.get_outputs())
print("other:", LoweredCeilingSpecific.get_intermediary())


LoweredCeilingSpecific.set_value('RoomType', "Publicly_accessible_room")
LoweredCeilingSpecific.set_value('SpaceType', "Room")

LoweredCeilingSpecificResult = LoweredCeilingSpecific.model_expand()
print(LoweredCeilingSpecificResult)

