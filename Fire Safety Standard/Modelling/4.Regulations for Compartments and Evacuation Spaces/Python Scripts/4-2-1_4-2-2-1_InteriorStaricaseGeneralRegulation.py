from cdmn.API import DMN

#get all types of variables from each DMN
IntStaircaseGeneral = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-2-1_4-2-2-1_InteriorStaricaseGeneralRegulation.dmn',auto_propagate=True)

print("inputs:", IntStaircaseGeneral.get_inputs())
print("outputs:", IntStaircaseGeneral.get_outputs())
print("other:", IntStaircaseGeneral.get_intermediary())


#define list of fire resistances from the interior walls
FRintwall_list=["EI_60","EI_60","EI_90","EI_30"]


#Define empty result list
IntWallResults=[]


#Call general wall EI 60 DMN
FRwallEI60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceWallModuleEI60.dmn',auto_propagate=True)


for FR in FRintwall_list:
    FRwallEI60.set_value('FireResistanceWall', FR)
    FRwallEI60.propagate()#niet per se nodig want staat al op autopropagate
    IntWallResults.append(FRwallEI60.value_of('FireResistanceWallSuccess'))
    FRwallEI60.clear()


print(IntWallResults)

#Map to AirlockAllWallSuccess

if all(IntWallResults):
    AllFireResistanceInteriorWallOfInteriorStaircaseSuccess = True
else: 
    AllFireResistanceInteriorWallOfInteriorStaircaseSuccess = False

print(AllFireResistanceInteriorWallOfInteriorStaircaseSuccess)

IntStaircaseGeneral.set_value('AllFireResistanceInteriorWallOfInteriorStaircaseSuccess', AllFireResistanceInteriorWallOfInteriorStaircaseSuccess)

IntStaircaseGeneralResult = IntStaircaseGeneral.model_expand()
print(IntStaircaseGeneralResult)