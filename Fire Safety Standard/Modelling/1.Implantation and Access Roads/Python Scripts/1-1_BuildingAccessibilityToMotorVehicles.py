from cdmn.API import DMN

BuildingAccess = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/1-1_BuildingAccessibilityToMotorVehicles.dmn', auto_propagate=True)

print("inputs:", BuildingAccess.get_inputs())
print("outputs:", BuildingAccess.get_outputs())
print("other:", BuildingAccess.get_intermediary())





#check possible values of the input variables
#boolean, integer and double (real) types give 'None'

print(BuildingAccess.possible_values_of('DoesAccessRoadDeadEnd'))


print(BuildingAccess.possible_values_of('TonnageCapacity'))
print(BuildingAccess.possible_values_of('HeightClearance'))
print(BuildingAccess.possible_values_of('TurnCircleInside'))
print(BuildingAccess.possible_values_of('Slope'))
print(BuildingAccess.possible_values_of('TurnCircleOutside'))
print(BuildingAccess.possible_values_of('WidthClearance'))


print(BuildingAccess.possible_values_of('RoadType'))
print(BuildingAccess.possible_values_of('RoadAllowsMotorVehicleAccess'))
print(BuildingAccess.possible_values_of('RoadAllowsParkingFacilitiesToMotorVehicles'))


print(BuildingAccess.possible_values_of('DistanceEdgeOfTheRoadToPlaneOfFacade'))
print(BuildingAccess.possible_values_of('BuildingCanSupport3MotorVehiclesOf15t'))




#check possible values of the intermediate variables

print("DeadEnds:", BuildingAccess.possible_values_of('DeadEnds'))

print(BuildingAccess.possible_values_of('AccessRoadRegulationSuccess'))

print(BuildingAccess.possible_values_of('BuildingOnAccessRoadRegulationSuccess'))



#check possible values of the output variables


print("BuildingAccessible:", BuildingAccess.possible_values_of('BuildingAccessible'))



"""
#Set values of a partial set of input variables

BuildingAccess.clear()

BuildingAccess.set_value('TonnageCapacity', 6)
BuildingAccess.set_value('HeightClearance', 6)
BuildingAccess.set_value('TurnCircleInside', 6)
BuildingAccess.set_value('Slope', 6)
BuildingAccess.set_value('TurnCircleOutside', 6)
BuildingAccess.set_value('WidthClearance', 6)
"""

BuildingAccess.clear()
#Specify which road type because the public road option does not require the acces road conditions to be true as it does not apply
BuildingAccess.set_value('RoadType', "Acces_road_from_the_drivable_roadway_of_the_public_road")
#Set value of output variable
BuildingAccess.set_value('BuildingAccessible', "Building_is_continuously_accessible_to_motor_vehicles")


AccessResult = BuildingAccess.model_expand()
print(AccessResult)