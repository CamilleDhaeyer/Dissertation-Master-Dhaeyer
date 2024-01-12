from cdmn.API import DMN

#LargeRoom=zaal
CommercialComplex = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/5-4_RetailAndCommercialComplexRegulation.dmn',auto_propagate=True)

print("inputs:", CommercialComplex.get_inputs())
print("outputs:", CommercialComplex.get_outputs())
print("other:", CommercialComplex.get_intermediary())


#module to determine: FireResistanceAllOuterWallSuccess
#Define list of fire resistances from the walls connecting to other building parts
FRExtwall_list=["EI_60","EI_60","EI_60","EI_60"]


#Define empty result list
WallExtResults=[]


FRwallEI60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceWallModuleEI60.dmn',auto_propagate=True)

for FR in FRExtwall_list:
    FRwallEI60.set_value('FireResistanceWall', FR)
    WallExtResults.append(FRwallEI60.value_of('FireResistanceWallSuccess'))
    FRwallEI60.clear()

#Map to FireResistanceAllWallSuccess

if all(WallExtResults):
    FireResistanceAllOuterWallSuccess = True
else: 
    FireResistanceAllOuterWallSuccess = False
    

#module to determine: FireResistanceAllInnerWallSuccess
#Define list of fire resistances from the interior walls 
FRIntwall_list=["EI_30","EI_30","EI_45","EI_45"]


#Define empty result list
WallIntResults=[]

FRwallEI30 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/FireResistanceWallModuleEI30.dmn',auto_propagate=True)


for FR in FRIntwall_list:
    FRwallEI30.set_value('FireResistanceWall', FR)
    WallIntResults.append(FRwallEI30.value_of('FireResistanceWallSuccess'))
    FRwallEI30.clear()

#Map to FireResistanceAllInnerWallSuccess

if all(WallIntResults):
    FireResistanceAllInnerWallSuccess = True
else: 
    FireResistanceAllInnerWallSuccess = False
    




CommercialComplex.set_value('FireResistanceAllOuterWallSuccess', FireResistanceAllOuterWallSuccess)
CommercialComplex.set_value('FireResistanceAllInnerWallSuccess', FireResistanceAllInnerWallSuccess)
CommercialComplex.set_value('AllWallThroughLoweredCeilingSuccess', True)#DMN 3-4-2_LoweredCeilingGeneralRulesWall.py

CommercialComplex.set_value('RetailOrCommercialComplexHasSeparateExits', True)

CommercialComplexResult = CommercialComplex.model_expand()
print(CommercialComplexResult)