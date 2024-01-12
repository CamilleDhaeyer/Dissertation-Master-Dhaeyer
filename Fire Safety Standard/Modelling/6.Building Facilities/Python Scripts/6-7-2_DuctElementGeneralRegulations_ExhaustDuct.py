from cdmn.API import DMN

#ONLY for exhaust ducts
ExhaustDuctReg = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-7-2_DuctElementGeneralRegulations_ExhaustDuct.dmn',auto_propagate=True)

print("inputs:", ExhaustDuctReg.get_inputs())
print("outputs:", ExhaustDuctReg.get_outputs())
print("other:", ExhaustDuctReg.get_intermediary())

DuctLocation = "Duct_coming_from_collective_kitchen"

if DuctLocation == "Duct_in_evacuation_route" or DuctLocation == "Duct_inside_of_collective_kitchen":
    FREI30 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/FireResistanceModuleEI30.dmn',auto_propagate=True)
    FR_DuctWalls_List=["EI_30","EI_30","EI_30","EI_30"]
    FR_Suspensiont_List=["EI_45"]
    
    FR_DuctWalls_Result=[]
    FR_Suspension_Result=[]
    
    for FR in FR_DuctWalls_List:
        FREI30.set_value('FireResistance', FR)
        FR_DuctWalls_Result.append(FREI30.value_of('FireResistanceSuccess'))
        FREI30.clear()
        
    for FR in FR_Suspensiont_List:
        FREI30.set_value('FireResistance', FR)
        FR_Suspension_Result.append(FREI30.value_of('FireResistanceSuccess'))
        FREI30.clear()

    
    if all(FR_DuctWalls_Result):
        FireResistanceDuctAllWallSuccess = True
    else:
        FireResistanceDuctAllWallSuccess = False
        
    if all(FR_Suspension_Result):
        FireResistanceDuctSuspensionSuccess = True
    else:
        FireResistanceDuctSuspensionSuccess = False
    
    
    ExhaustDuctReg.set_value('FireResistanceDuctAllWallSuccess', FireResistanceDuctAllWallSuccess)
    ExhaustDuctReg.set_value('FireResistanceDuctSuspensionSuccess', FireResistanceDuctSuspensionSuccess)
    
    

elif DuctLocation =="Duct_coming_from_collective_kitchen":
    FRwallEI60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceWallModuleEI60.dmn',auto_propagate=True)

    FR_DuctWalls_List=["EI_30","EI_30","EI_30","EI_30"]
    FR_DuctShaftWalls_List=["EI_60","EI_60","EI_60","EI_60"]
    
    FR_DuctWalls_Result=[]
    FR_DuctShaftWalls_Result=[]

    
    for FR in FR_DuctWalls_List:
        FRwallEI60.set_value('FireResistanceWall', FR)
        FR_DuctWalls_Result.append(FRwallEI60.value_of('FireResistanceWallSuccess'))
        FRwallEI60.clear()
        
    for FR in FR_DuctShaftWalls_List:
        FRwallEI60.set_value('FireResistanceWall', FR)
        FR_DuctShaftWalls_Result.append(FRwallEI60.value_of('FireResistanceWallSuccess'))
        FRwallEI60.clear()
    
    
    if all(FR_DuctWalls_Result):
        FireResistanceDuctAllWallSuccess = True
    else: 
        FireResistanceDuctAllWallSuccess = False
        
    if all(FR_DuctShaftWalls_Result):
        FireResistanceDuctShaftAllWallSuccess = True
    else: 
        FireResistanceDuctShaftAllWallSuccess = False
        
    
    ExhaustDuctReg.set_value('FireResistanceDuctAllWallSuccess', FireResistanceDuctAllWallSuccess)
    ExhaustDuctReg.set_value('FireResistanceDuctShaftAllWallSuccess', FireResistanceDuctShaftAllWallSuccess)
    

ExhaustDuctReg.set_value('DuctLocation', DuctLocation)
ExhaustDuctReg.set_value('ExhaustDuctLocationSuccess', True)



ExhaustDuctRegResult =ExhaustDuctReg.model_expand()
print(ExhaustDuctRegResult)