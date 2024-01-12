from cdmn.API import DMN

#for fire dampers
NumberOfDevices = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-8-3-1_RequiredNumberOfFireDetectionSignalingDevices.dmn',auto_propagate=True)
AreaModule = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-8-3-1_RequiredFireDetectionSignalingDevices_BuildingLayerModule.dmn',auto_propagate=True)

print("inputs:", NumberOfDevices.get_inputs())
print("outputs:", NumberOfDevices.get_outputs())
print("other:", NumberOfDevices.get_intermediary())

#define list of areas of all building layers
Area_list=[500,500,400,400]
Area_result=[]
for area in Area_list:
    AreaModule.set_value('AreaOfBuildingLayer', area)
    Area_result.append(AreaModule.value_of('AreaOfBuildingLayerSuccess'))
    
if all(Area_result):
    AllAreaOfBuildingLayerSuccess = True
else:
    AllAreaOfBuildingLayerSuccess = False
    
NumberOfDevices.set_value('AllAreaOfBuildingLayerSuccess', AllAreaOfBuildingLayerSuccess)


NumberOfDevicesResult =NumberOfDevices.model_expand()
print(NumberOfDevicesResult)