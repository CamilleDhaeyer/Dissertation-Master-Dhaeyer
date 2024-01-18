import rdflib

g = rdflib.Graph()
g.parse("C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/Overleaf/Proof Of Concept/IFC to RDF/Hotel_Model.ttl")

knows_query = """
    SELECT ?wallId ?fireRatingValue
    WHERE {
        ?relDefByProp ifc:relatingPropertyDefinition_IfcRelDefinesByProperties ?propSet .
        ?relDefByProp ifc:relatedObjects_IfcRelDefines ?wall .
        
        ?propSet ifc:name_IfcRoot inst:IfcLabel_40400 .
        ?propSet ifc:hasProperties_IfcPropertySet ?propSingleValue .
        
        ?propSingleValue ifc:name_IfcProperty inst:IfcIdentifier_40397 .
        ?propSingleValue ifc:nominalValue_IfcPropertySingleValue ?label .
        
        ?label express:hasString ?fireRatingValue .

        ?wall rdf:type ifc:IfcWallStandardCase .
        ?wall ifc:globalId_IfcRoot ?globalId .
        ?globalId express:hasString ?wallId .
        
    }"""
    
# Execute the SPARQL query
qres = g.query(knows_query)
print(qres)
# Print the variable names
print("Variables:", qres.vars)

for row in qres:
    print(row)
    print(type(row))

# Print the results
wallId_list = [str(row['wallId']) for row in qres]
FR_list = [str(row['fireRatingValue']) for row in qres]


print(wallId_list)
print(FR_list)

#DMN import
from cdmn.API import DMN

#get all types of variables from each DMN
FRwallEI60 = DMN('C:/Users/camil/OneDrive - UGent/Ugent/AJ/23-24/Masterthesis/MODELS/DMN/1.Inplanting en toegangswegen/final/FireResistanceWallModuleEI60.dmn',auto_propagate=True)

FRWallResult_list = []
i=0
for FR in FR_list:
    FRwallEI60.set_value('FireResistanceWall', FR)
    FRWallResult_list.append([wallId_list[i], FRwallEI60.value_of('FireResistanceWallSuccess')])
    FRwallEI60.clear()
    i += 1

print(FRWallResult_list)


