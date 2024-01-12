from cdmn.API import DMN


#get all types of variables from each DMN
HorizontalDistance2 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/1-3_HorizontalDistanceRequirementBetweenMBandOB_v2.dmn',auto_propagate=True)

print("inputs:",HorizontalDistance2.get_inputs())
print("outputs:", HorizontalDistance2.get_outputs())
print("other:", HorizontalDistance2.get_intermediary())

wallModule = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/1-3_WallFireResistanceModule.dmn',auto_propagate=True)

print("inputs:",wallModule.get_inputs())
print("outputs:", wallModule.get_outputs())
print("other:", wallModule.get_intermediary())


WallMB = [["EI_60",True],["REI_120",True]]
WallOB = [["EI_120",False]]

resultsMB=[]
resultsOB=[]

#check fire resistance of wall MB
for MB in WallMB:
    wallModule.set_value('FireResistanceWall', MB[0])
    wallModule.set_value('IsWallLoadbearing', MB[1])
    wallModule.propagate()
    print(wallModule.value_of('FRWallSuccess'))
    resultsMB.append(wallModule.value_of('FRWallSuccess'))
    wallModule.clear()
    
#check fire resistance of wall OB

for OB in WallOB:
    wallModule.set_value('FireResistanceWall', OB[0])
    wallModule.set_value('IsWallLoadbearing', OB[1])
    wallModule.propagate()
    print(wallModule.value_of('FRWallSuccess'))
    resultsOB.append(wallModule.value_of('FRWallSuccess'))
    wallModule.clear()
    

    
print(resultsMB)
print(resultsOB)


#Map to FRWallMBSuccess and FRWallOBSuccess

if all(resultsMB):
    FRWallMBSuccess = True
else: 
    FRWallMBSuccess = False
    
    
    
if all(resultsOB):
    FRWallOBSuccess = True
else: 
    FRWallOBSuccess = False
    


#set values of the main DMN model
HorizontalDistance2.set_value('FRWallMBSuccess', FRWallMBSuccess)
HorizontalDistance2.set_value('FRWallOBSuccess', FRWallOBSuccess)





HorizontalDistance2Result = HorizontalDistance2.model_expand()
print(HorizontalDistance2Result)
