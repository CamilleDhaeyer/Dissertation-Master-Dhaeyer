from cdmn.API import DMN
import pandas as pd

sheet_name = "FR_GL2"
excel_file = pd.read_excel('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/Overleaf/Proof Of Concept/Dynamo/Fire_Resistance_Rating.xlsx', sheet_name=sheet_name)
variable_columns = ['ifcGUID', 'Fire Resistance Rating', 'SpaceType', 'WallClass']

wall_list = excel_file[variable_columns].values.tolist()
print(wall_list)

#get all types of variables from each DMN
FROuterWall = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/4.Voorschriften inzake constructie van compartimenten en evacuatieruimten/final/4-1_FireResistanceOuterWallTypesRegulation.dmn',auto_propagate=True)

FROuterWallResult_List = []
for wall in wall_list:
    FROuterWall.set_value('FireResistanceWall', wall[1])
    FROuterWall.set_value('SpaceType', wall[2])
    FROuterWall.set_value('WallClass', wall[3])
    FROuterWallResult_List.append([wall[0],FROuterWall.value_of('FireResistanceWallSuccess'),FROuterWall.value_of('FacadeMessage')])
    FROuterWall.clear()

print(FROuterWallResult_List)

