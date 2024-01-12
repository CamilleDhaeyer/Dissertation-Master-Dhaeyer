from cdmn.API import DMN

#DSF stands for Double Skin Facade
Roof = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-6_RoofGeneralRegulation.dmn',auto_propagate=True)
print("inputs:", Roof.get_inputs())
print("outputs:", Roof.get_outputs())
print("other:", Roof.get_intermediary())


Roof.set_value('FireResistanceRoofSuccess', True)#module
Roof.set_value('RoofSpaceEmpty', False)
Roof.set_value('FireResistanceRoofSubFloorSuccess', True)#module
Roof.set_value('FireResistanceAccesOpeningToRoofSuccess', False)#module


RoofResult =Roof.model_expand()
print(RoofResult)


