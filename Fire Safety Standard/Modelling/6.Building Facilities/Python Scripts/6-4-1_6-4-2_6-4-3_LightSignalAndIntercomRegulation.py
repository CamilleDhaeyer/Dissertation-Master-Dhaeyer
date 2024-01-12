from cdmn.API import DMN
from datetime import datetime


#For limited mobility elevators and firebrigade elevators
LightSignal_Intercom = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-4-1_6-4-2_6-4-3_LightSignalAndIntercomRegulation.dmn',auto_propagate=True)

print("inputs:", LightSignal_Intercom.get_inputs())
print("outputs:", LightSignal_Intercom.get_outputs())
print("other:", LightSignal_Intercom.get_intermediary())


def is_after_may_2017(date_string):
    # Convert the input string to a datetime object
    date_format = "%Y-%m-%d"
    input_date = datetime.strptime(date_string, date_format)

    # Check if the date is after January 1, 2000
    compare_date = datetime(2017, 5, 31)
    if input_date > compare_date:
        return True
    else:
        return False

#set date
date_to_check = "2023-10-11"
After31may2017 = is_after_may_2017(date_to_check)
print(After31may2017)
 
#set values
LightSignal_Intercom.set_value('After31may2017', After31may2017)
 


LightSignal_Intercom.set_value('ElevatorLightSignalAndIntercomRegulationSuccess', True)

LightSignal_IntercomResult =LightSignal_Intercom.model_expand()
print(LightSignal_IntercomResult)
