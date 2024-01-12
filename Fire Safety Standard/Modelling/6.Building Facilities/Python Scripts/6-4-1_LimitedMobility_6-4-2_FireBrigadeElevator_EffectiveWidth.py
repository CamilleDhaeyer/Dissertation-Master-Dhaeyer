from cdmn.API import DMN
from datetime import datetime


#For limited mobility elevators and firebrigade elevators
EffWidthShaftDoor = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-4-1_LimitedMobility_6-4-2_FireBrigadeElevator_EffectiveWidth.dmn',auto_propagate=True)

print("inputs:", EffWidthShaftDoor.get_inputs())
print("outputs:", EffWidthShaftDoor.get_outputs())
print("other:", EffWidthShaftDoor.get_intermediary())


def is_after_2017(date_string):
    # Convert the input string to a datetime object
    date_format = "%Y-%m-%d"
    input_date = datetime.strptime(date_string, date_format)

    # Check if the date is after January 1, 2000
    compare_date = datetime(2017, 4, 1)
    if input_date > compare_date:
        return True
    else:
        return False

#set date
date_to_check = "2023-10-11"
After1April2017 = is_after_2017(date_to_check)
print(After1April2017)
    
#set values
EffWidthShaftDoor.set_value('After1April2017', After1April2017)
    


EffWidthShaftDoorResult =EffWidthShaftDoor.model_expand()
print(EffWidthShaftDoorResult)