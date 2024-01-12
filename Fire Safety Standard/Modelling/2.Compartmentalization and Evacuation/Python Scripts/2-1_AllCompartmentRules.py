from datetime import datetime


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




from cdmn.API import DMN


#get all types of variables from each DMN
CompartmentException = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/2.Compartimentering en evacuatie/final/2-1_DefinitionCompartmentExceptionType.dmn',auto_propagate=True)

print("inputs:", CompartmentException.get_inputs())
print("outputs:", CompartmentException.get_outputs())
print("other:", CompartmentException.get_intermediary())


#check possible values

print(CompartmentException.possible_values_of('RoomType'))
print(CompartmentException.possible_values_of('TypeOfBuilding'))

print(CompartmentException.possible_values_of('StructureIsParkingBuilding'))

print(CompartmentException.possible_values_of('ParkingBuildingMessage'))
print(CompartmentException.possible_values_of('ExceptionType'))

#set values

CompartmentException.set_value('RoomType', "Standard_Room")


CompartmentExceptionResult = CompartmentException.model_expand()
print(CompartmentExceptionResult)

if CompartmentException.value_of('ExceptionType') == "Standard_Rules":
    General = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/2.Compartimentering en evacuatie/final/2-1_CompartmentGeneralRules.dmn',auto_propagate=True)
    General.clear()
    print("inputs:", General.get_inputs())
    print("outputs:", General.get_outputs())
    print("other:", General.get_intermediary())
    
    """
    #Heightverification in python code because IDP can not handle the DMN about it
    #If found a method that works so this is not needed anymore in python
    HeightOfCompartmentFloorLevel = 3   
    HeightOfCompartment = 3
    if HeightOfCompartment == HeightOfCompartmentFloorLevel:
        HeightVerification = True
    else:
        HeightVerification = False
    print(HeightVerification)
    """
    
    General.set_value('HeightOfCompartment', 3)
    General.set_value('HeightOfFloorLevel', 4)
    General.set_value('ExceptionType', CompartmentException.value_of('ExceptionType'))
    General.set_value('AreaOfCompartment', 100)
    
    GeneralResult = General.model_expand()
    print(GeneralResult)


elif CompartmentException.value_of('ExceptionType') == "Exception_b":
    ExceptionB = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/2.Compartimentering en evacuatie/final/2-1_CompartmentExceptionB.dmn',auto_propagate=True)
    ExceptionB.clear()
    print("inputs:", ExceptionB.get_inputs())
    print("outputs:", ExceptionB.get_outputs())
    print("other:", ExceptionB.get_intermediary())
    
    
    
    #"Date" type is an unknown variable type for the DMN APi
    #see definition of date function above

    #set date
    date_to_check = "2023-10-11"
    After1April2017 = is_after_2017(date_to_check)
    print(After1April2017)
    
    #set values
    ExceptionB.set_value('After1April2017', After1April2017)
    
    
    ExceptionB.set_value('DuplexAreaFirstFloor', 700)
    ExceptionB.set_value('DuplexAreaSecondFloor', 1000)
    
    ExceptionB.set_value('HeightFirstFloorLevelOfDuplex', 3)
    ExceptionB.set_value('HeightSecondFloorLevelOfDuplex', 4)
    ExceptionB.set_value('HeightOfCompartment', 7)
    
    
    #expand
    ExceptionBResult = ExceptionB.model_expand()
    print(ExceptionBResult)
    
elif CompartmentException.value_of('ExceptionType') == "Exception_b_1":
    ExceptionB1 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/2.Compartimentering en evacuatie/final/2-1_CompartmentExceptionB1.dmn',auto_propagate=True)
    ExceptionB1.clear()
    print("inputs:", ExceptionB1.get_inputs())
    print("outputs:", ExceptionB1.get_outputs())
    print("other:", ExceptionB1.get_intermediary())
    
    
    #set values
    ExceptionB1.set_value('ExceptionType', "Exception_b_1")
    
    
    ExceptionB1.set_value('TriplexAreaFirstFloor', 700)
    ExceptionB1.set_value('TriplexAreaSecondFloor', 1000)
    ExceptionB1.set_value('TriplexAreaThirdFloor', 1000)
    
    ExceptionB1.set_value('HeightFirstFloorLevelOfTriplex', 3)
    ExceptionB1.set_value('HeightSecondFloorLevelOfTriplex', 3)
    ExceptionB1.set_value('HeightThirdFloorLevelOfTriplex', 4)
    ExceptionB1.set_value('HeightOfCompartment', 10)
    
    
    #expand
    ExceptionB1Result = ExceptionB1.model_expand()
    print(ExceptionB1Result)
    
elif CompartmentException.value_of('ExceptionType') == "Exception_c":
    ExceptionC = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/2.Compartimentering en evacuatie/final/2-1_CompartmentExceptionC.dmn',auto_propagate=True)
    ExceptionC.clear()
    print("inputs:", ExceptionC.get_inputs())
    print("outputs:", ExceptionC.get_outputs())
    print("other:", ExceptionC.get_intermediary())
    
    #"Date" type is an unknown variable type for the DMN APi
    #see definition of date function above

    #set date
    date_to_check = "2023-10-12"
    After1April2017 = is_after_2017(date_to_check)
    print(After1April2017)
    
    #set values
    ExceptionC.set_value('After1April2017', After1April2017)
    
    ExceptionC.set_value('ExceptionType', "Exception_c")
    ExceptionC.set_value('VolumeOfCompartment', 100)
    
    ExceptionCResult = ExceptionC.model_expand()
    print(ExceptionCResult)
    
    
elif CompartmentException.value_of('ExceptionType') == "Exception_e":
    ExceptionE = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/2.Compartimentering en evacuatie/final/2-1_CompartmentExceptionE.dmn',auto_propagate=True)
    ExceptionE.clear()
    print("inputs:", ExceptionE.get_inputs())
    print("outputs:", ExceptionE.get_outputs())
    print("other:", ExceptionE.get_intermediary())
    
    ExceptionE.set_value('CumulatedHeightOfAllBuildingLayersInCompartment', 10)
    ExceptionE.set_value('HeightOfCompartment', 10)
    ExceptionE.set_value('NumberOfBuildingLayersInCompartment', 3)
    
    ExceptionEResult = ExceptionE.model_expand()
    print(ExceptionEResult)
    
    #FireEvacuationRequirementsSucces comes from the evacuation DMNs
elif CompartmentException.value_of('ExceptionType') == "See_Rules_5_1_1":
    print("Verify DMN of section 5_1_1")
    
    
    
    
elif CompartmentException.value_of('ExceptionType') == "See_Rules_5_2":
    print("Verify DMN of section 5_2")