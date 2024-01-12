from cdmn.API import DMN

#for fire dampers
MountedReel = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-8-5-3-1_WallMountedReelRegulation.dmn',auto_propagate=True)

print("inputs:", MountedReel.get_inputs())
print("outputs:", MountedReel.get_outputs())
print("other:", MountedReel.get_intermediary())


MountedReel.set_value('AreaOfCompartment', 1000)
MountedReel.set_value('ProvidedNumberOfWallMountedReels', 2)
MountedReel.set_value('CanWaterJetReachEachPointInCompartment', False)



MountedReelResult =MountedReel.model_expand()
print(MountedReelResult)

