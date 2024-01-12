from cdmn.API import DMN


IntStairConstruction = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-2-3-1_InteriorStairConstructionRequirements_v2.dmn',auto_propagate=True)
RailingReg = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-2-3-1_InteriorStairConstructionRequirements_v2_railing.dmn',auto_propagate=True)

print("inputs:", IntStairConstruction.get_inputs())
print("outputs:", IntStairConstruction.get_outputs())
print("other:", IntStairConstruction.get_intermediary())


print("inputs:", RailingReg.get_inputs())
print("outputs:", RailingReg.get_outputs())
print("other:", RailingReg.get_intermediary())


print(RailingReg.possible_values_of('StairElementRailingPosition'))
#define a list of lists of the properties of stair elements (width, railingposition, etc)
StairElementList=[[1,"One_side_only","No_risk"],[1.2,"Two_sides","No_risk"]]
StairElementResult=[]

for element in StairElementList:
    RailingReg.set_value('StairElementEffectiveWidth', element[0])
    RailingReg.set_value('StairElementRailingPosition', element[1])
    RailingReg.set_value('DangerRiskIfOnlyOneRailing', element[2])
    StairElementResult.append(RailingReg.value_of('StairElementRailingSuccess'))

if all(StairElementResult):
    AllStairElementRailingSuccess = True
else:
    AllStairElementRailingSuccess = False
    


    
IntStairConstruction.set_value('StairType', "Straight_stair_type")
IntStairConstruction.set_value('StairSlope', 25)
IntStairConstruction.set_value('StairRiser', 0.15)
IntStairConstruction.set_value('StairRiserType', "Solid_riser")
IntStairConstruction.set_value('StairTread', 0.25)

IntStairConstruction.set_value('AllStairElementRailingSuccess', AllStairElementRailingSuccess)#module
IntStairConstruction.set_value('FireResistanceStair', "R_60")


IntStairConstructionResult = IntStairConstruction.model_expand()
print(IntStairConstructionResult)