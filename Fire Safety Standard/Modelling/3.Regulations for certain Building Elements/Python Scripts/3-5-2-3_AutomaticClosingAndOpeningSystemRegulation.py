from cdmn.API import DMN

#DSF stands for Double Skin Facade
CloseOpenSystem = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-5-2-3_AutomaticClosingAndOpeningSystemRegulation.dmn',auto_propagate=True)


print("inputs:", CloseOpenSystem.get_inputs())
print("outputs:", CloseOpenSystem.get_outputs())
print("other:", CloseOpenSystem.get_intermediary())

"""
print(DSFVentilation.possible_values_of('DoubleSkinFacadeCompartmentSuccess'))
#set (partial) input variable values
DSFVentilation.set_value('WidthInterruptionElement', 0.3)
DSFVentilation.set_value('WidthCavity', 0.3)
DSFVentilation.set_value('LengthInterruptionElement', 0.6)
"""
List=[True,True,False,True,"Fire_Detection_Installation",True,True]


CloseOpenSystem.set_value('AutomaticClosingAndOpeningByFireDetectionInstallation', List[0])
CloseOpenSystem.set_value('FireDetectionInstallationHasManualOpeningAndClosingOperatingSystem', List[1])

CloseOpenSystem.set_value('NormalPowerSourceAvailability', List[2])
CloseOpenSystem.set_value('AutomaticNotificationWithPowerOutage', List[3])
CloseOpenSystem.set_value('OpeningClosingSystemInSecurePositionBy', List[4])

CloseOpenSystem.set_value('OpeningClosingSystemHasPositiveSecurity', List[5])
CloseOpenSystem.set_value('OpeningClosingSystemCableRequirements', List[6])

CloseOpenSystemResult =CloseOpenSystem.model_expand()
print(CloseOpenSystem.value_of('AutomaticClosingAndOpeningByFireDetectionInstallation'))


#set value of output
#CloseOpenSystem.set_value('AutomaticOpeningClosingSystemSuccess', True)

print(CloseOpenSystemResult)