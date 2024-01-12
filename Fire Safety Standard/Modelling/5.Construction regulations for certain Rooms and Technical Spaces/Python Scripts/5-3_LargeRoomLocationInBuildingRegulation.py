from cdmn.API import DMN

#LargeRoom=zaal
LargeRoomLoc = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/5-3_LargeRoomLocationInBuildingRegulation.dmn',auto_propagate=True)

print("inputs:", LargeRoomLoc.get_inputs())
print("outputs:", LargeRoomLoc.get_outputs())
print("other:", LargeRoomLoc.get_intermediary())

LargeRoomLoc.set_value('OccupancyPerson', 50)
LargeRoomLoc.set_value('RoomLocationInBuilding', "Underground")
LargeRoomLoc.set_value('DistanceRoomFloorLevelAndNearestEvacuationFloorLevel', 3)
LargeRoomLoc.set_value('DistanceRoomFloorLevelAndAverageEvacuationFloorLevel', 4.5)

LargeRoomLocResult = LargeRoomLoc.model_expand()
print(LargeRoomLocResult)



