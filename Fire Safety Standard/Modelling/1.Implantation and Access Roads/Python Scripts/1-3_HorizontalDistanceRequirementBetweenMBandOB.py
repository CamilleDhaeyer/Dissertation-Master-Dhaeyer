from cdmn.API import DMN


#get all types of variables from each DMN
HorizontalDistance = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/1-3_HorizontalDistanceRequirementBetweenMBandOB.dmn',auto_propagate=True)

print("inputs:",HorizontalDistance.get_inputs())
print("outputs:", HorizontalDistance.get_outputs())
print("other:", HorizontalDistance.get_intermediary())

MBwallModule = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/1-3_MBWallFireResistanceModule.dmn',auto_propagate=True)

print("inputs:",MBwallModule.get_inputs())
print("outputs:", MBwallModule.get_outputs())
print("other:", MBwallModule.get_intermediary())


OBwallModule = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/1-3_OBWallFireResistanceModule.dmn',auto_propagate=True)

print("inputs:",OBwallModule.get_inputs())
print("outputs:", OBwallModule.get_outputs())
print("other:", OBwallModule.get_intermediary())


#set values for the module DMNs

MBwallModule.set_value('FireResistanceWallMB', "EI_60")
MBwallModule.set_value('IsWallMBLoadbearing', False )

MBwallModuleResult = MBwallModule.model_expand()
print(MBwallModuleResult)


OBwallModule.set_value('FireResistanceWallOB', "EI_60")
OBwallModule.set_value('IsWallOBLoadbearing', True )

OBwallModuleResult = OBwallModule.model_expand()
print(OBwallModuleResult)



#verify values of output variables from the modules
print(MBwallModule.value_of('ResistanceWallMB'))

print(OBwallModule.value_of('ResistanceWallOB'))


#set values of the main DMN model
HorizontalDistance.set_value('ResistanceWallMB', MBwallModule.value_of('ResistanceWallMB'))
HorizontalDistance.set_value('ResistanceWallOB', OBwallModule.value_of('ResistanceWallOB'))
HorizontalDistance.set_value('IsWallOBLoadbearing', True)
HorizontalDistance.set_value('IsWallMBLoadbearing', False)
#HorizontalDistance.set_value('MBdistanceOB', 5)




HorizontalDistanceResult = HorizontalDistance.model_expand()
print(HorizontalDistanceResult)

