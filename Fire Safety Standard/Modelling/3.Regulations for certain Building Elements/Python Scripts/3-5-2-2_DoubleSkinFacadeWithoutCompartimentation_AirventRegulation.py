from cdmn.API import DMN

#DSF stands for Double Skin Facade
Airvent = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-5-2-2_DoubleSkinFacadeWithoutCompartimentation_AirventRegulation.dmn',auto_propagate=True)


print("inputs:", Airvent.get_inputs())
print("outputs:", Airvent.get_outputs())
print("other:", Airvent.get_intermediary())



CloseOpenSystem = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-5-2-3_AutomaticClosingAndOpeningSystemRegulation.dmn',auto_propagate=True)


#List of corresponding input variable values for the smoke detection system
#If multiple smokedetection systems are present it could be a list of lists
FireDetection_list=[True,True,False,True,"Fire_Detection_Installation",True,True]
FireDetection_result=[]

CloseOpenSystem.set_value('AutomaticClosingAndOpeningByFireDetectionInstallation', FireDetection_list[0])
CloseOpenSystem.set_value('FireDetectionInstallationHasManualOpeningAndClosingOperatingSystem', FireDetection_list[1])

CloseOpenSystem.set_value('NormalPowerSourceAvailability', FireDetection_list[2])
CloseOpenSystem.set_value('AutomaticNotificationWithPowerOutage', FireDetection_list[3])
CloseOpenSystem.set_value('OpeningClosingSystemInSecurePositionBy', FireDetection_list[4])

CloseOpenSystem.set_value('OpeningClosingSystemHasPositiveSecurity', FireDetection_list[5])
CloseOpenSystem.set_value('OpeningClosingSystemCableRequirements', FireDetection_list[6])

CloseOpenSystemResult =CloseOpenSystem.model_expand()
FireDetection_result.append(CloseOpenSystem.value_of('AutomaticClosingAndOpeningByFireDetectionInstallation'))

if all(FireDetection_result):
    AutomaticOpeningClosingSystemSuccess = True
else:
    AutomaticOpeningClosingSystemSuccess = False



Airvent.set_value('AutomaticOpeningClosingSystemSuccess', AutomaticOpeningClosingSystemSuccess)#module

#set other variables
Airvent.set_value('SecurePositionActivatedByFireDetectionInstallation', True)
Airvent.set_value('FireDetectionInstallationLocation', "in_each_compartment_along_the_facade")


Airvent.set_value('AirventType', "Rigid_airventilation")
Airvent.set_value('AirventAngleWithHorizontal', 30)
Airvent.set_value('AirventOrientation', "Upwards_angled_to_exterior")
Airvent.set_value('AirventExteriorWallAreaPercentage', 60)


AirventResult =Airvent.model_expand()
print(AirventResult)



