from cdmn.API import DMN


VerticalElement = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/3.Voorschriften voor sommige bouwelementen/final/3-5-1-1_FireExpansionAlongFacade_VerticalProtectionModule.dmn',auto_propagate=True)

print("inputs:", VerticalElement.get_inputs())
print("outputs:", VerticalElement.get_outputs())
print("other:", VerticalElement.get_intermediary())


VerticalElement.set_value('WidthWall', 0.2)
VerticalElement.set_value('WidthOfWallExtensionLeftFromCenterOfWall', 0.5)
VerticalElement.set_value('WidthOfWallExtensionRightFromCenterOfWall', 0.5)

VerticalElement.set_value('DistanceFacadePlaneToWindowPlaneLeft', 0.25)
VerticalElement.set_value('DistanceFacadePlaneToWindowPlaneRight', 0.25)

VerticalElement.set_value('FireResistanceExtensionElement', "E_60")

VerticalElement.set_value('PresenceWallExtensionInPlaneOfFacade', True)
VerticalElement.set_value('PresenceWallExtensionPastFacade', False)

VerticalElement.set_value('WallClass', "Outer_wall")
VerticalElement.set_value('SpaceType', "Building")

VerticalElementResult = VerticalElement.model_expand()
print(VerticalElementResult)
print(VerticalElement.value_of('VerticalFireProtectionElementSuccess'))

