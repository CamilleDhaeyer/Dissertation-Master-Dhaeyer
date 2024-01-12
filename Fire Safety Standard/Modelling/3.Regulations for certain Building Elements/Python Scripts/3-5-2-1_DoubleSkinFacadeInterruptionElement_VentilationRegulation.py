from cdmn.API import DMN

#DSF stands for Double Skin Facade
DSFVentilation = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-5-2-1_DoubleSkinFacadeInterruptionElement_VentilationRegulation.dmn',auto_propagate=True)


print("inputs:", DSFVentilation.get_inputs())
print("outputs:", DSFVentilation.get_outputs())
print("other:", DSFVentilation.get_intermediary())

#To define variable: SmokeDetectionSystemAllCompartmentsSuccess
CloseOpenSystem = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-5-2-3_AutomaticClosingAndOpeningSystemRegulation.dmn',auto_propagate=True)


#List of corresponding input variable values for the smoke detection system
#If multiple smokedetection systems are present it could be a list of lists
SmokeDetection_list=[[True,True,False,True,"Fire_Detection_Installation",True,True]]
SmokeDetection_result=[]
for smoke in SmokeDetection_list:
    CloseOpenSystem.set_value('AutomaticClosingAndOpeningByFireDetectionInstallation', smoke[0])
    CloseOpenSystem.set_value('FireDetectionInstallationHasManualOpeningAndClosingOperatingSystem', smoke[1])
    
    CloseOpenSystem.set_value('NormalPowerSourceAvailability', smoke[2])
    CloseOpenSystem.set_value('AutomaticNotificationWithPowerOutage', smoke[3])
    CloseOpenSystem.set_value('OpeningClosingSystemInSecurePositionBy', smoke[4])

    CloseOpenSystem.set_value('OpeningClosingSystemHasPositiveSecurity', smoke[5])
    CloseOpenSystem.set_value('OpeningClosingSystemCableRequirements', smoke[6])

    CloseOpenSystemResult =CloseOpenSystem.model_expand()
    print(CloseOpenSystem.value_of('AutomaticClosingAndOpeningByFireDetectionInstallation'))
    SmokeDetection_result.append(CloseOpenSystem.value_of('AutomaticClosingAndOpeningByFireDetectionInstallation'))

if all(SmokeDetection_result):
    SmokeDetectionSystemAllCompartmentsSuccess = True
else:
    SmokeDetectionSystemAllCompartmentsSuccess = False

print(SmokeDetectionSystemAllCompartmentsSuccess)


DSFVentilation.set_value('SmokeDetectionSystemAllCompartmentsSuccess', SmokeDetectionSystemAllCompartmentsSuccess)


#set value of output
#DSFVentilation.set_value('DoubleSkinFacadeCompartmentSuccess', True)

DSFVentilationResult = DSFVentilation.model_expand()
print(DSFVentilationResult)
