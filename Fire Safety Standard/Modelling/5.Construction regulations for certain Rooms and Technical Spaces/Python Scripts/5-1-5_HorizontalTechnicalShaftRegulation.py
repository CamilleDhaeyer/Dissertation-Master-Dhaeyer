from cdmn.API import DMN


HorizontalShaft = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/5-1-5_HorizontalTechnicalShaftRegulation.dmn',auto_propagate=True)

print("inputs:", HorizontalShaft.get_inputs())
print("outputs:", HorizontalShaft.get_outputs())
print("other:", HorizontalShaft.get_intermediary())

FREI = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/FREI_Module.dmn',auto_propagate=True)
FREI30 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/FireResistanceModuleEI30.dmn',auto_propagate=True)


#define fire resistances of elements
VerticalScreen="None"

FREI30.set_value('FireResistance', VerticalScreen)
FireResistanceVerticalScreenSuccess = FREI30.value_of('FireResistanceSuccess')
HorizontalShaft.set_value('FireResistanceVerticalScreenSuccess', FREI30.value_of('FireResistanceSuccess'))


HorizontalShaftDoorList=["EI_30","EI_60","EI_30","EI_90"]
HorizontalShaftWallList=["EI_60","EI_60","EI_60","EI_60"]

HorizontalShaftDoorAndWallResult=[]
HorizontalShaftDoorResult=[]
HorizontalShaftWallResult=[]

PenetratedWall="Reference_wall_is_E_60"

if VerticalScreen != "None":
    for FR in HorizontalShaftDoorList:
        FREI.set_value('FRPenetratedWall', PenetratedWall)
        FREI.set_value('FireResistance', FR)
        HorizontalShaftDoorAndWallResult.append(FREI.value_of('EqOrLargerFireResistanceSuccess'))
        FREI.clear()
    for FR in HorizontalShaftWallList:
        FREI.set_value('FRPenetratedWall', PenetratedWall)
        FREI.set_value('FireResistance', FR)
        HorizontalShaftDoorAndWallResult.append(FREI.value_of('EqOrLargerFireResistanceSuccess'))
        FREI.clear()

    if all(HorizontalShaftDoorAndWallResult):
        Measure1Success = True
    else:
        Measure1Success = False

        
    HorizontalShaft.set_value('Measure1Success', Measure1Success)

elif VerticalScreen == "None":
    for FR in HorizontalShaftDoorList:
        FREI30.set_value('FireResistance', FR)
        HorizontalShaftDoorResult.append(FREI30.value_of('FireResistanceSuccess'))
        FREI30.clear()
    for FR in HorizontalShaftWallList:
        FREI30.set_value('FireResistance', FR)
        HorizontalShaftWallResult.append(FREI30.value_of('FireResistanceSuccess'))
        FREI30.clear()

    if all(HorizontalShaftDoorResult):
        FireResistanceAllDoorSuccess30 = True
    else:
        FireResistanceAllDoorSuccess30 = False
    
    if all(HorizontalShaftWallResult):
        FireResistanceAllWallSuccess30 = True
    else:
        FireResistanceAllWallSuccess30 = False

    HorizontalShaft.set_value('FireResistanceAllDoorSuccess30', FireResistanceAllDoorSuccess30)
    HorizontalShaft.set_value('FireResistanceAllWallSuccess30', FireResistanceAllWallSuccess30)




BuildingElement="EI_60"



HorizontalShaft.set_value('VerticalScreenMaterialClass', "Class_A1")
HorizontalShaft.set_value('TechnicalShaftHasVerticalScreenAtCompartmentIntersection', True)
HorizontalShaft.set_value('VerticalScreenCoversFullTechnicalShaftCrossSection', True)

HorizontalShaft.set_value('DoesShaftPenetrateWall', True)

HorizontalShaft.set_value('FireResistancePenetratedWall', PenetratedWall)
HorizontalShaft.set_value('FireResistanceBuildingElementAtWallPenetration', BuildingElement)




#To propagate in the reverse direction
#VerticalShaft.set_value('VerticalTechnicalShaftRegulationSuccess', True)

HorizontalShaftResult = HorizontalShaft.model_expand()
print(HorizontalShaftResult)
