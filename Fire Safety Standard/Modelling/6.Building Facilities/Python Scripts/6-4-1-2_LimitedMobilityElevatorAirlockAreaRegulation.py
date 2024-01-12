from cdmn.API import DMN

#For limited mobility elevators 
#This script is additional to DMNs of 6-1-2

AirlockArea = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/6.Uitrusting van de gebouwen/final/6-4-1-2_LimitedMobilityElevatorAirlockAreaRegulation.dmn',auto_propagate=True)

print("inputs:", AirlockArea.get_inputs())
print("outputs:", AirlockArea.get_outputs())
print("other:", AirlockArea.get_intermediary())


AirlockAreaResult =AirlockArea.model_expand()
print(AirlockAreaResult)