from cdmn.API import DMN

#DSF stands for Double Skin Facade
DSFnoCompartimentation = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-5-2-2_DoubleSkinFacadeWithoutCompartimentationRegulation.dmn',auto_propagate=True)


print("inputs:", DSFnoCompartimentation.get_inputs())
print("outputs:", DSFnoCompartimentation.get_outputs())
print("other:", DSFnoCompartimentation.get_intermediary())


#Define list of the fire resistances of each building layer of the interior wall
Innerwall1=["E_30","E_30","EI_30","E_30"]
Innerwall2=["EI_30","E_30","EI_30","E_60"]

#Define function to check same strings and alternative strings
def check_same_strings(lst):
    # Check if the list is empty
    if not lst:
        return False  # Return False if the list is empty

    # Compare the first element with all other elements
    first_element = "E_30"
    for element in lst[0:]:
        if element != first_element:
            return False  # Return False if any element is different

    return True  # Return True if all elements are the same

print(check_same_strings(Innerwall1))
print(check_same_strings(Innerwall2))


def check_alternating_same_strings(lst):
    is_E60 = lst[0] == "EI_30"

    for i in range(1, len(lst)):
        if i % 2 == 0:
            if lst[i] != "EI_30" and is_E60:
                return False
            elif lst[i] == "EI_30" and not is_E60:
                return False
        else:
            if lst[i] == "EI_30" and is_E60:
                return False
            elif lst[i] != "EI_30" and not is_E60:
                return False

    return True
    


print("Alternating outcomes:")

print(check_alternating_same_strings(Innerwall1))
print(check_alternating_same_strings(Innerwall2))




Innerwall1_FunctionOutcomeList=[]
Innerwall1_FunctionOutcomeList.append(check_same_strings(Innerwall1))
Innerwall1_FunctionOutcomeList.append(check_alternating_same_strings(Innerwall1))
print(Innerwall1_FunctionOutcomeList)


if all(not item for item in Innerwall1_FunctionOutcomeList):
    InteriorWallRequirementSuccess = False
else:
    InteriorWallRequirementSuccess = True






#for the AllAirventRequirementSuccess variable
Airvent = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-5-2-2_DoubleSkinFacadeWithoutCompartimentation_AirventRegulation.dmn',auto_propagate=True)
CloseOpenSystem = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-5-2-3_AutomaticClosingAndOpeningSystemRegulation.dmn',auto_propagate=True)


#List of corresponding input variable values for the smoke detection system
#If multiple airvents are present it could be a list of lists
Airvent_list=[[True,True,False,True,"Fire_Detection_Installation",True,True,True,"in_each_compartment_along_the_facade","Rigid_airventilation",30,"Upwards_angled_to_exterior",60]]
Airvent_result=[]

Total_airvent_result=[]

for element in Airvent_list:
    CloseOpenSystem.set_value('AutomaticClosingAndOpeningByFireDetectionInstallation', element[0])
    CloseOpenSystem.set_value('FireDetectionInstallationHasManualOpeningAndClosingOperatingSystem', element[1])

    CloseOpenSystem.set_value('NormalPowerSourceAvailability',element[2])
    CloseOpenSystem.set_value('AutomaticNotificationWithPowerOutage', element[3])
    CloseOpenSystem.set_value('OpeningClosingSystemInSecurePositionBy', element[4])

    CloseOpenSystem.set_value('OpeningClosingSystemHasPositiveSecurity', element[5])
    CloseOpenSystem.set_value('OpeningClosingSystemCableRequirements',element[6])

    CloseOpenSystemResult =CloseOpenSystem.model_expand()
    Airvent_result.append(CloseOpenSystem.value_of('AutomaticClosingAndOpeningByFireDetectionInstallation'))

    if all(Airvent_result):
        AutomaticOpeningClosingSystemSuccess = True
    else:
        AutomaticOpeningClosingSystemSuccess = False


    Airvent.set_value('AutomaticOpeningClosingSystemSuccess', AutomaticOpeningClosingSystemSuccess)#module
    
    #set other variables
    Airvent.set_value('SecurePositionActivatedByFireDetectionInstallation', element[7])
    Airvent.set_value('FireDetectionInstallationLocation', element[8])


    Airvent.set_value('AirventType', element[9])
    Airvent.set_value('AirventAngleWithHorizontal', element[10])
    Airvent.set_value('AirventOrientation', element[11])
    Airvent.set_value('AirventExteriorWallAreaPercentage', element[12])


    AirventResult =Airvent.model_expand()
    Total_airvent_result.append(Airvent.value_of('AirventRequirementSuccess'))
    


if all(Total_airvent_result):
    AllAirventRequirementSuccess = True
else:
    AllAirventRequirementSuccess = False





DSFnoCompartimentation.set_value('ExteriorWallPercentageBetweenLevelsOfUnspecifiedFRelements', 20)
DSFnoCompartimentation.set_value('InteriorWallRequirementSuccess', InteriorWallRequirementSuccess)#module
DSFnoCompartimentation.set_value('ExteriorWallHasAutomaticAirVents', True)
DSFnoCompartimentation.set_value('AllAirventRequirementSuccess', AllAirventRequirementSuccess)#module


DSFnoCompartimentationResult =DSFnoCompartimentation.model_expand()
print(DSFnoCompartimentationResult)












