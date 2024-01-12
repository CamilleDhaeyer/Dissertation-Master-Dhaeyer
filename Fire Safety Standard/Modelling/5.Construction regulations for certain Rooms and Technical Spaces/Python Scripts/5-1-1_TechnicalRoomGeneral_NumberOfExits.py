from cdmn.API import DMN

TechnRoomGeneralNumberExit = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/5-1-1_TechnicalRoomGeneral_NumberOfExits.dmn',auto_propagate=True)

print("inputs:", TechnRoomGeneralNumberExit.get_inputs())
print("outputs:", TechnRoomGeneralNumberExit.get_outputs())
print("other:", TechnRoomGeneralNumberExit.get_intermediary())


TechnRoomGeneralNumberExit.set_value('ExitNumberRegulationSuccess', True)
TechnRoomGeneralNumberExit.set_value('AreaOfCompartment', 1200)

TechnRoomGeneralNumberExitResult = TechnRoomGeneralNumberExit.model_expand()
print(TechnRoomGeneralNumberExitResult)