from cdmn.API import DMN


Mullion = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-5-1-1_CurtainWallFixationElementRequirement.dmn',auto_propagate=True)
Mullion.clear()


print("inputs:", Mullion.get_inputs())
print("outputs:", Mullion.get_outputs())
print("other:", Mullion.get_intermediary())



print(Mullion.possible_values_of('FireResistanceMullionFixationElement'))



Mullion.set_value('PresenceAutomaticExtinguishingSystem', True)




MullionResult = Mullion.model_expand()
print(MullionResult)

