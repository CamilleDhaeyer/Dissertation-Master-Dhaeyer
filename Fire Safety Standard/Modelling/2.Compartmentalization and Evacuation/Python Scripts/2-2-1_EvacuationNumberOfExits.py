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
    CompartmentExits.set_value('AccessibilityFacadeOpening', FacadeAccess.value_of('AccessibilityFacadeOpening'))
    
    
    #Terrace accessibility DT
    CompartmentExits.set_value('ConnectionToTerracePossible', True)
    CompartmentExits.set_value('DistanceEdgeOfTheRoadToPlaneOfTerrace', 4)
    

    #Terrace requirements DT
    FRwallE60.set_value('FireResistanceWall', "E_60")
    CompartmentExits.set_value('FireResistanceWallTerraceFacadeSuccess', FRwallE60.value_of('FireResistanceWallSuccess'))
    CompartmentExits.set_value('DistanceTerraceRailFromFacade', 0.8)
    
    #Fire resistance terrace DT
    CompartmentExits.set_value('FireResistanceTerraceFloor', "REI_60")

    '''
    ##set output values + MaximalOccupancy due to the ceiling function
    CompartmentExits.set_value('CompartmentNumberOfExitsVerification', True)
    
    CompartmentExits.set_value('MaximalOccupancy', 1000)
    CeilingMaximalOccupancy = np.ceil(CompartmentExits.value_of('MaximalOccupancy')/1000)
    CompartmentExits.set_value('CeilingMaximalOccupancy', CeilingMaximalOccupancy)#cMDN can not evaluate ceiling function
    

    #CompartmentExits.set_value('AccessibilityFacadeOpening', FacadeAccess.value_of('AccessibilityFacadeOpening'))
    #CompartmentExits.set_value('FireResistanceWallTerraceFacadeSuccess', FRwallE60.value_of('FireResistanceWallSuccess'))
    '''
    
    CompartmentExitsResult = CompartmentExits.model_expand()
    print(CompartmentExitsResult)
    
    print(type(CompartmentExitsResult))

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