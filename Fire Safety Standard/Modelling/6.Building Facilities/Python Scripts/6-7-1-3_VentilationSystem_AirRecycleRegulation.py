from cdmn.API import DMN


Ventilation_AirRecycle = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-7-1-3_VentilationSystem_AirRecycleRegulation.dmn',auto_propagate=True)

print("inputs:", Ventilation_AirRecycle.get_inputs())
print("outputs:", Ventilation_AirRecycle.get_outputs())
print("other:", Ventilation_AirRecycle.get_intermediary())


AirRecycle_SameRoom = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-7-1-3_VentilationSystem_AirRecycleRegulation_SameRoomModule.dmn',auto_propagate=True)

print("inputs:", AirRecycle_SameRoom.get_inputs())
print("outputs:", AirRecycle_SameRoom.get_outputs())
print("other:", AirRecycle_SameRoom.get_intermediary())


AirRecycle_SameRoom.set_value('AirRecycleVolume', 3000)
AirRecycle_SameRoom.set_value('SmokeDamperRegulationSuccess', True)#6-7-5
AirRecycle_SameRoom.set_value('RecyclingDuctHasSmokeDamper', True)

SameRoomAirRecirculationSuccess=AirRecycle_SameRoom.value_of('SameRoomAirRecirculationSuccess')


AirRecycle_OtherRoom = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-7-1-3_VentilationSystem_AirRecycleRegulation_OtherRoomModule.dmn',auto_propagate=True)

print("inputs:", AirRecycle_OtherRoom.get_inputs())
print("outputs:", AirRecycle_OtherRoom.get_outputs())
print("other:", AirRecycle_OtherRoom.get_intermediary())


AirRecycle_OtherRoom.set_value('AirRecycleVolume', 3000)
AirRecycle_OtherRoom.set_value('OtherRoomHasDirectExteriorExhaust', True)#6-7-5
AirRecycle_OtherRoom.set_value('ExhaustDuctHasSmokeDetectionInstallation', True)
AirRecycle_OtherRoom.set_value('ExhaustDuctHasSmokeDamper', True)

OtherRoomAirRecirculationSuccess=AirRecycle_OtherRoom.value_of('OtherRoomAirRecirculationSuccess')


Ventilation_AirRecycle.set_value('OtherRoomAirRecirculationSuccess', OtherRoomAirRecirculationSuccess)
Ventilation_AirRecycle.set_value('SameRoomAirRecirculationSuccess', SameRoomAirRecirculationSuccess)

Ventilation_AirRecycle.set_value('RoomType', "Other")


Ventilation_AirRecycleResult =Ventilation_AirRecycle.model_expand()
print(Ventilation_AirRecycleResult)