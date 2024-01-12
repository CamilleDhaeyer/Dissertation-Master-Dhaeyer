from cdmn.API import DMN

TechnRoomGeneralExitConf = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/5-1-1_TechnicalRoomGeneral_ExitConfigurationRegulation.dmn',auto_propagate=True)

print("inputs:", TechnRoomGeneralExitConf.get_inputs())
print("outputs:", TechnRoomGeneralExitConf.get_outputs())
print("other:", TechnRoomGeneralExitConf.get_intermediary())


TechnRoomGeneralExitConf.set_value('AreaOfCompartment', 100)

TechnRoomGeneralExitConfResult = TechnRoomGeneralExitConf.model_expand()
print(TechnRoomGeneralExitConfResult)