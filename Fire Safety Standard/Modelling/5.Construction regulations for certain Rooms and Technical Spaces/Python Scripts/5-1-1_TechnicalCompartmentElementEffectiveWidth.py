from cdmn.API import DMN
#For the elements connected to a technical room: Evacuation route; intermediate stair landing; stair landing; airlock
TechnRoomElementEffWidth = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/5-1-1_TechnicalCompartmentElementEffectiveWidth.dmn',auto_propagate=True)

print("inputs:", TechnRoomElementEffWidth.get_inputs())
print("outputs:", TechnRoomElementEffWidth.get_outputs())
print("other:", TechnRoomElementEffWidth.get_intermediary())


TechnRoomElementEffWidth.set_value('ElementEffectiveWidth', 1.2)

TechnRoomElementEffWidthResult = TechnRoomElementEffWidth.model_expand()
print(TechnRoomElementEffWidthResult)