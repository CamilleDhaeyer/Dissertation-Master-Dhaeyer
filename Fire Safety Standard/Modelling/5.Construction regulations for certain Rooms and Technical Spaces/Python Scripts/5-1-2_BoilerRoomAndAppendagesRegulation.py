from cdmn.API import DMN
#For the elements connected to a technical room: Evacuation route; intermediate stair landing; stair landing; airlock
BoilerRoom = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/5-1-2_BoilerRoomAndAppendagesRegulation.dmn',auto_propagate=True)

print("inputs:", BoilerRoom.get_inputs())
print("outputs:", BoilerRoom.get_outputs())
print("other:", BoilerRoom.get_intermediary())


BoilerRoom.set_value('GeneratorHeatCapacity', 70)

BoilerRoomResult = BoilerRoom.model_expand()
print(BoilerRoomResult)

