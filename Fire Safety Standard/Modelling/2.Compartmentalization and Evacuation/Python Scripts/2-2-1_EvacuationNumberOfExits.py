from cdmn.API import DMN
import numpy as np

SpaceType = "Compartment"#nog in DMN vorm zetten?

if SpaceType == "Compartment":

    #get all types of variables from each DMN
    CompartmentExits = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/2.Compartimentering en evacuatie/final/2-2-1_CompartmentEvacuation_NumberOfExits.dmn',auto_propagate=True)

    print("inputs:", CompartmentExits.get_inputs())
    print("outputs:", CompartmentExits.get_outputs())
    print("other:", CompartmentExits.get_intermediary())
    
    #Dependency on facadeaccess DMN
    FacadeAccess = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/1-4_AccessibilityOfFacadeOpenings.dmn',auto_propagate=True)
    
    print("inputs:", FacadeAccess.get_inputs())
    print("outputs:", FacadeAccess.get_outputs())
    
    #Dependency on wall module
    FRwallE60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/2.Compartimentering en evacuatie/final/FireResistanceWallModuleE60.dmn',auto_propagate=True)
    print("inputs:", FRwallE60.get_inputs())
    print("outputs:", FRwallE60.get_outputs())
    
    '''
    
    ##set input values
    
    #verification decision table (DT)
    CompartmentExits.set_value('NumberOfCompartmentExits', 1)
    
    #Minimal exits (DT)
    CompartmentExits.set_value('MaximalOccupancy', 49)
    CompartmentExits.set_value('StaircaseInExitPathToFacadeOrTerrace', False)
    CeilingMaximalOccupancy = np.ceil(CompartmentExits.value_of('MaximalOccupancy')/1000)
    CompartmentExits.set_value('CeilingMaximalOccupancy', CeilingMaximalOccupancy)#cMDN can not evaluate ceiling function

    #Exit Type accessibility DT
    CompartmentExits.set_value('ExitType', "Exit_possible_through_a_terrace")
    
    FacadeAccess.set_value('DistanceEdgeOfTheRoadToPlaneOfFacade', 6)
    CompartmentExits.set_value('AccessibilityFacadeOpeningSuccess', FacadeAccess.value_of('AccessibilityFacadeOpeningSuccess'))
    
    #validate all terrace requirements DT
    CompartmentExits.set_value('DirectExitToExterior', True)
    
    #Terrace accessibility DT
    CompartmentExits.set_value('DistanceEdgeOfTheRoadToPlaneOfTerrace', 4)
    

    #Terrace requirements DT
    FRwallE60.set_value('FireResistanceWall', "E_60")
    CompartmentExits.set_value('FireResistanceWallTerraceFacadeSuccess', FRwallE60.value_of('FireResistanceWallSuccess'))
    CompartmentExits.set_value('DistanceTerraceRailFromFacade', 0.8)
    
    #Fire resistance terrace DT
    CompartmentExits.set_value('FireResistanceTerraceFloor', "REI_60")

    CompartmentExitsResult = CompartmentExits.model_expand()
    print(CompartmentExitsResult)
    
    '''
    ##set output values + MaximalOccupancy due to the ceiling function
    CompartmentExits.set_value('CompartmentNumberOfExitsVerification', True)
    
    CompartmentExits.set_value('MaximalOccupancy', 49)
    CeilingMaximalOccupancy = np.ceil(CompartmentExits.value_of('MaximalOccupancy')/1000)
    CompartmentExits.set_value('CeilingMaximalOccupancy', CeilingMaximalOccupancy)#cMDN can not evaluate ceiling function

    CompartmentExitsResult = CompartmentExits.model_expand()
    print(CompartmentExitsResult)
    
    #extra to reduce models
    CompartmentExits.set_value('NumberOfCompartmentExits', 4)
    CompartmentExits.set_value('TerracePresent', True)
    CompartmentExits.set_value('FireResistanceTerraceFloor', "REI_60")
    CompartmentExits.set_value('FireResistanceWallTerraceFacadeSuccess', True)
    CompartmentExits.set_value('DistanceTerraceRailFromFacade', 2)
    CompartmentExits.set_value('DistanceEdgeOfTheRoadToPlaneOfTerrace', 5)
    CompartmentExits.set_value('ExitType', "Exit_possible_through_a_terrace")
    

    
    CompartmentExitsResult = CompartmentExits.model_expand()
    print(CompartmentExitsResult)
    
    print(type(CompartmentExitsResult))
    
    data_string = CompartmentExitsResult
    models = data_string.split('\n\n')
    
    '''
    Facade_Access_to_retrieve = 'AccessibilityFacadeOpening'
    
    Facade_Access_success_values = []
    
    # Iterate through each model
    for model_data in models:
        if model_data.strip():  # Ensure the model data is not empty
            lines = model_data.split('\n')
            model = {}
            for line in lines[1:]:  # Skip the model title line
                parts = line.split(':=')
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip().rstrip('.')
                    model[key] = value
            print(model)  # Process each model (in this case, just printing)
            print('-----------------------')
            if Facade_Access_to_retrieve in model:
                Facade_Access_success_value = model[Facade_Access_to_retrieve]
                if Facade_Access_success_value is not None:
                    Facade_Access_success_values.append(Facade_Access_success_value)
            else:
                Facade_Access_success_values.append(None)
    
    print(Facade_Access_success_values[:-1])
    
    i=1
    for success_value in Facade_Access_success_values[:-1]:
        if success_value is not None:
            FacadeAccess.set_value('AccessibilityFacadeOpening', success_value)
            FacadeAccessResult = FacadeAccess.model_expand()
            print(f"These possibilities correspond to main model {i}")
            print(FacadeAccessResult)
        else:
            print(f"The specific variable value has no influence on main model {i}\n")
        i += 1
    

    '''
    FR_succes_to_retrieve = 'FireResistanceWallTerraceFacadeSuccess'
    
    FR_success_values = []
    
    # Iterate through each model
    for model_data in models:
        if model_data.strip():  # Ensure the model data is not empty
            lines = model_data.split('\n')
            model = {}
            for line in lines[1:]:  # Skip the model title line
                parts = line.split(':=')
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip().rstrip('.')
                    model[key] = value
            print(model)  # Process each model (in this case, just printing)
            print('-----------------------')
            if FR_succes_to_retrieve in model:
                FR_success_value = model[FR_succes_to_retrieve]
                if FR_success_value is not None:
                    FR_success_values.append(FR_success_value)
            else:
                FR_success_values.append(None)
    
    print(FR_success_values[:-1])
    
    i=1
    for success_value in FR_success_values[:-1]:
        if success_value is not None:
            FRwallE60.set_value('FireResistanceWallSuccess', success_value)
            FRwallE60Result = FRwallE60.model_expand()
            print(f"These possibilities correspond to model {i}")
            print(FRwallE60Result)
        else:
            print(f"The specific variable value has no influence on model {i}\n")
        i += 1
    
        
    '''
    data_string = CompartmentExitsResult

    # Split the string into lines
    lines = data_string.split('\n')

    # Create a dictionary to store key-value pairs
    data = {}

    for line in lines:
        # Split each line by ':=' to extract key and value
        parts = line.split(':=')
        if len(parts) == 2:
            key = parts[0].strip()
            value = parts[1].strip()
            data[key] = value

    # Now you have a dictionary 'data' containing the key-value pairs
    # Example usage:
    print(data['AccessibilityFacadeOpening']) 
    '''

elif SpaceType == "BuildingLayer":
    #also verify number of exits for a complete building layer if buildinglayer occupancy is [50..500[

    BuildingLayerExits = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/2.Compartimentering en evacuatie/final/2-2-1_BuildingLayerEvacuation_NumberOfExits_v2.dmn',auto_propagate=True)

    print("inputs:", BuildingLayerExits.get_inputs())
    print("outputs:", BuildingLayerExits.get_outputs())
    print("other:", BuildingLayerExits.get_intermediary())
    
    BuildingLayerExits.set_value('MaximalOccupancy', 1000)
    
    #because cMDN can not evaluate the ceiling function in DMN
    CeilingMaximalOccupancy = np.ceil(BuildingLayerExits.value_of('MaximalOccupancy')/1000)
    
    BuildingLayerExits.set_value('CeilingMaximalOccupancy', CeilingMaximalOccupancy)
    BuildingLayerExits.set_value('NumberOfBuildingLayerExits', 4)
    
    BuildingLayerExitsResult = BuildingLayerExits.model_expand()
    print(BuildingLayerExitsResult)

elif SpaceType == "Room":

    #also verify number of exits for a single room if room occupancy is [50..500[

    RoomExits = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/2.Compartimentering en evacuatie/final/2-2-1_RoomEvacuation_NumberOfExits_v2.dmn',auto_propagate=True)
    
    
    print("inputs:", RoomExits.get_inputs())
    print("outputs:", RoomExits.get_outputs())
    print("other:", RoomExits.get_intermediary())

    RoomExits.set_value('MaximalOccupancy', 1000)
    
    #because cMDN can not evaluate the ceiling function in DMN
    CeilingMaximalOccupancy = np.ceil(RoomExits.value_of('MaximalOccupancy')/1000)
    
    RoomExits.set_value('CeilingMaximalOccupancy', CeilingMaximalOccupancy)
    RoomExits.set_value('NumberOfRoomExits', 4)
    
    RoomExitsResult = RoomExits.model_expand()
    print(RoomExitsResult)