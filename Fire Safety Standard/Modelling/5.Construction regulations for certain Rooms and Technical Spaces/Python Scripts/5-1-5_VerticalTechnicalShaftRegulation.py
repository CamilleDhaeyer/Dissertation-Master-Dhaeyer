from cdmn.API import DMN


VerticalShaft = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/5-1-5_VerticalTechnicalShaftRegulation.dmn',auto_propagate=True)

print("inputs:", VerticalShaft.get_inputs())
print("outputs:", VerticalShaft.get_outputs())
print("other:", VerticalShaft.get_intermediary())

FREI60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/FireResistanceModuleEI60.dmn',auto_propagate=True)
FREI30 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/FireResistanceModuleEI30.dmn',auto_propagate=True)


#define fire resistances of elements
HorizontalScreen="EI_30"

FREI30.set_value('FireResistance', HorizontalScreen)
FireResistanceHorizontalScreenSuccess = FREI30.value_of('FireResistanceSuccess')
VerticalShaft.set_value('FireResistanceHorizontalScreenSuccess', FREI30.value_of('FireResistanceSuccess'))
FREI30.clear()

VerticalShaftDoorList=["EI_30","EI_60","EI_30","EI_90"]
VerticalShaftWallList=["EI_60","EI_60","EI_60","EI_60"]

VerticalShaftDoorResult=[]
VerticalShaftWallResult=[]


if HorizontalScreen != "None":
    for FR in VerticalShaftDoorList:
        FREI60.set_value('FireResistance', FR)
        VerticalShaftDoorResult.append(FREI60.value_of('FireResistanceSuccess'))
        FREI60.clear()
    for FR in VerticalShaftWallList:
        FREI60.set_value('FireResistance', FR)
        VerticalShaftWallResult.append(FREI60.value_of('FireResistanceSuccess'))
        FREI60.clear()

    if all(VerticalShaftDoorResult):
        FireResistanceAllDoorSuccess60 = True
    else:
        FireResistanceAllDoorSuccess60 = False
    
    if all(VerticalShaftWallResult):
        FireResistanceAllWallSuccess60 = True
    else:
        FireResistanceAllWallSuccess60 = False
        
    VerticalShaft.set_value('FireResistanceAllDoorSuccess60', FireResistanceAllDoorSuccess60)
    VerticalShaft.set_value('FireResistanceAllWallSuccess60', FireResistanceAllWallSuccess60)

elif HorizontalScreen == "None":
    for FR in VerticalShaftDoorList:
        FREI30.set_value('FireResistance', FR)
        VerticalShaftDoorResult.append(FREI30.value_of('FireResistanceSuccess'))
        FREI30.clear()
    for FR in VerticalShaftWallList:
        FREI30.set_value('FireResistance', FR)
        VerticalShaftWallResult.append(FREI30.value_of('FireResistanceSuccess'))
        FREI30.clear()

    if all(VerticalShaftDoorResult):
        FireResistanceAllDoorSuccess30 = True
    else:
        FireResistanceAllDoorSuccess30 = False
    
    if all(VerticalShaftWallResult):
        FireResistanceAllWallSuccess30 = True
    else:
        FireResistanceAllWallSuccess30 = False

    VerticalShaft.set_value('FireResistanceAllDoorSuccess30', FireResistanceAllDoorSuccess30)
    VerticalShaft.set_value('FireResistanceAllWallSuccess30', FireResistanceAllWallSuccess30)



PenetratedWall="EI_60"
BuildingElement="EI_60"



VerticalShaft.set_value('HorizontalScreenMaterialClass', "Class_A1")
VerticalShaft.set_value('TechnicalShaftHasHorizontalScreenAtCompartmentIntersection', True)
VerticalShaft.set_value('HorizontalScreenCoversFullTechnicalShaftCrossSection', True)

VerticalShaft.set_value('DoesShaftPenetrateWall', True)

VerticalShaft.set_value('FireResistancePenetratedWall', "Reference_wall_is_E_60")
VerticalShaft.set_value('FireResistanceBuildingElementAtWallPenetration', "EI_30")




#To propagate in the reverse direction
#VerticalShaft.set_value('VerticalTechnicalShaftRegulationSuccess', True)

VerticalShaftResult = VerticalShaft.model_expand()
print(VerticalShaftResult)
