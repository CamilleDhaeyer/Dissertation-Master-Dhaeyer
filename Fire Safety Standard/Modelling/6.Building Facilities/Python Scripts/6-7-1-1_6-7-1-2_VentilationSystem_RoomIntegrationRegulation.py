from cdmn.API import DMN


Ventilation_RoomIntegr = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-7-1-1_6-7-1-2_VentilationSystem_RoomIntegrationRegulation.dmn',auto_propagate=True)

print("inputs:", Ventilation_RoomIntegr.get_inputs())
print("outputs:", Ventilation_RoomIntegr.get_outputs())
print("other:", Ventilation_RoomIntegr.get_intermediary())


Ventilation_RoomIntegr.set_value('RoomCompliesWithDuctRegulation', True)#from running DMN 6-7-2


Ventilation_RoomIntegr.set_value('SpaceCanBeIntegratedInAirNetwork', True)


Ventilation_RoomIntegrResult =Ventilation_RoomIntegr.model_expand()
print(Ventilation_RoomIntegrResult)