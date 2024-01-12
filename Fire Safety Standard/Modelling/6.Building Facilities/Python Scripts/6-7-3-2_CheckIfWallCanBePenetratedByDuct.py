from cdmn.API import DMN


DuctInWallPossible = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-7-3-2_CheckIfWallCanBePenetratedByDuct.dmn',auto_propagate=True)
DuctInWallPossible.clear()

print("inputs:", DuctInWallPossible.get_inputs())
print("outputs:", DuctInWallPossible.get_outputs())
print("other:", DuctInWallPossible.get_intermediary())


FRwallEI60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceWallModuleEI60.dmn',auto_propagate=True)
FREI30 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/FireResistanceModuleEI30.dmn',auto_propagate=True)


PenetratedWallType = "Wall"
DuctInWallPossible.set_value('PenetratedWallType', PenetratedWallType)



#two different names due to the duplicate error
FR_Penetratedwall = "EI_60"
FRPenetratedWall = "Reference_wall_is_EI_60"


#check fire resistance of penetrated wall depending on type
if PenetratedWallType == "Wall" or PenetratedWallType == "Shared wall of two compartments":
    
    
    FRwallEI60.set_value('FireResistanceWall', FR_Penetratedwall)
    FireResistancePenetratedWallSuccess = FRwallEI60.value_of('FireResistanceWallSuccess')

    DuctInWallPossible.set_value('FireResistancePenetratedWallSuccess', FireResistancePenetratedWallSuccess)

elif PenetratedWallType == "Wall of service duct shaft":
    FREI30.set_value('FireResistance', FR_Penetratedwall)
    FireResistancePenetratedWallSuccess = FREI30.value_of('FireResistanceSuccess')
    
    DuctInWallPossible.set_value('FireResistancePenetratedWallSuccess', FireResistancePenetratedWallSuccess)



DamperPresent = False
FREI = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/FREI_Module.dmn',auto_propagate=True)

#verify exception options; still to put in if-statements
if DamperPresent == True:
    #check fire resistance of damper element
    FR_damper="E_60"
    FREI.set_value('FRPenetratedWall', FRPenetratedWall)
    FREI.set_value('FireResistance', FR_damper)
    FireResistanceDamperSuccess = FREI.value_of('EqOrLargerFireResistanceSuccess')
    

    DuctInWallPossible.set_value('ProvidedElementAtWallPassage', "Fire_resistant_damper")
    DuctInWallPossible.set_value('FireResistanceDamperSuccess', FireResistanceDamperSuccess)
    DuctInWallPossible.set_value('DamperRegulationSuccess', True)#module DMN 6-7-4


elif DamperPresent == False:

    #verify duct walls or duct shaft walls
    FR_DuctWalls_List=["EI_30","EI_30","EI_30","EI_30"]
    FR_DuctShaftWalls_List=["EI_60","EI_60","EI_60","EI_60"]

    FR_DuctWalls_Result=[]
    FR_DuctShaftWalls_Result=[]

    
    for FR in FR_DuctWalls_List:
        FREI.set_value('FRPenetratedWall', FRPenetratedWall)
        FREI.set_value('FireResistance', FR)
        FR_DuctWalls_Result.append(FREI.value_of('EqOrLargerFireResistanceSuccess'))
        FREI.clear()
    
    for FR in FR_DuctShaftWalls_List:
        FREI.set_value('FRPenetratedWall', FRPenetratedWall)
        FREI.set_value('FireResistance', FR)
        FR_DuctShaftWalls_Result.append(FREI.value_of('EqOrLargerFireResistanceSuccess'))
        FREI.clear()


    if all(FR_DuctWalls_Result):
        FireResistanceDuctAllWallSuccess = True
    else: 
        FireResistanceDuctAllWallSuccess = False
    
    if all(FR_DuctShaftWalls_Result):
        FireResistanceDuctShaftAllWallSuccess = True
    else: 
        FireResistanceDuctShaftAllWallSuccess = False

    DuctInWallPossible.set_value('FireResistanceDuctShaftAllWallSuccess', FireResistanceDuctShaftAllWallSuccess)
    DuctInWallPossible.set_value('FireResistanceDuctAllWallSuccess', FireResistanceDuctAllWallSuccess)




DuctInWallPossible.set_value('AreaOfPassageOpeningInWall', 20)
DuctInWallPossible.set_value('DuctHasFireClosingDevice', True)

DuctInWallPossibleResult =DuctInWallPossible.model_expand()
print(DuctInWallPossibleResult)