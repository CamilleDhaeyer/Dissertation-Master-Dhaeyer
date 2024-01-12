from cdmn.API import DMN

#DSF stands for Double Skin Facade
PitchedRoof = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-6_PitchedRoofWindowOpeningRequirement.dmn',auto_propagate=True)
print("inputs:", PitchedRoof.get_inputs())
print("outputs:", PitchedRoof.get_outputs())
print("other:", PitchedRoof.get_intermediary())


RoofWallConnection = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-6_3-5-1-1_ConnectionCompartmentWallAndPitchedRoofRequirement.dmn',auto_propagate=True)
print("inputs:", RoofWallConnection.get_inputs())
print("outputs:", RoofWallConnection.get_outputs())
print("other:", RoofWallConnection.get_intermediary())


#define list of the fire resistances of the connection element between the pitched roof and comparmentwall(s)
ConnectionElementFR_list=["EI_60","EI_90","EI_60"]
Result_list=[]
for FR in ConnectionElementFR_list:
    RoofWallConnection.set_value('FireResistanceCompartmentWallConnectionToPitchedRoof', FR)
    Result_list.append(RoofWallConnection.value_of('FireResistanceCompartmentWallConnectionToPitchedRoofSuccess'))

if all(Result_list):
    AllCompartmentWallToPitchedRoofConnectionSuccess = True
else:
    AllCompartmentWallToPitchedRoofConnectionSuccess = False


PitchedRoof.set_value('AllCompartmentWallToPitchedRoofConnectionSuccess', AllCompartmentWallToPitchedRoofConnectionSuccess)
PitchedRoof.set_value('RoofType', "Pitched_Roof")

PitchedRoofResult =PitchedRoof.model_expand()
print(PitchedRoofResult)
