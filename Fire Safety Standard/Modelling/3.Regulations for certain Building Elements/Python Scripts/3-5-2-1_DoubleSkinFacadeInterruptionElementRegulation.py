from cdmn.API import DMN

#DSF stands for Double Skin Facade
DSFInterruption = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-5-2-1_DoubleSkinFacadeInterruptionElementRegulation.dmn',auto_propagate=True)


print("inputs:", DSFInterruption.get_inputs())
print("outputs:", DSFInterruption.get_outputs())
print("other:", DSFInterruption.get_intermediary())


print(DSFInterruption.possible_values_of('DoubleSkinFacadeCompartmentSuccess'))
#set (partial) input variable values
DSFInterruption.set_value('WidthInterruptionElement', 0.3)
DSFInterruption.set_value('WidthCavity', 0.3)
DSFInterruption.set_value('LengthInterruptionElement', 0.6)


#set value of output
#DSFInterruption.set_value('DoubleSkinFacadeCompartmentSuccess', True)

DSFInterruptionResult = DSFInterruption.model_expand()
print(DSFInterruptionResult)