from cdmn.API import DMN


DisposalChute = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/5.Constructievoorschriften voor sommige lokalen en technische ruimten/final/5-1-4-1_WasteDisposalRoomChuteRegulation.dmn',auto_propagate=True)

print("inputs:", DisposalChute.get_inputs())
print("outputs:", DisposalChute.get_outputs())
print("other:", DisposalChute.get_intermediary())


DisposalChuteResult = DisposalChute.model_expand()
print(DisposalChuteResult)