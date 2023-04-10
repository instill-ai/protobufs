#!/bin/bash 

# Setup swagger file name
filename="../openapiv2/openapiv2.swagger.yaml"
echo "Post-Processing $filename" 

# --- standard conversion for naming scheme following Google AIP-122 ---
##
# This converts 
# "v1alpha/{____Name}" to "v1alpha/____s/{id}", and
# "v1alpha/{____Permalink}" to "v1alpha/____s/{uid}",
# where "____" denotes the names in the name_list
name_list=(
    "pipeline"
    "token"
    "user"
    "model"
    "operation"
)

# This converts 
# "v1alpha/{____Name}" to "v1alpha/****/{id}", and
# "v1alpha/{____Permalink}" to "v1alpha/****/{uid}"
# array in name_hyphen_list is [____,****]
definition_list=(
    "sourceConnector source-connector"
    "destinationConnector destination-connector"
    "sourceConnectorDefinition source-connector-definition"
    "destinationConnectorDefinition destination-connector-definition"
    "modelDefinition model-definition"
)

# This converts 
# "v1alpha/{____Name}" to "v1alpha/____s/{id}/****s/{type}",
# where each subarray in model_card_list is [____,****]
controller_list=(
    "resource type"
)

# --- customised conversion for naming schemes for VDP (needs updates) ---
##
# This is special list for connector and model operations.
# Should be merged to other conversions once they are refactored.
# Here `name` consist of {uid} instead of {id}.
# This converts 
# "v1alpha/{____Name}" to "v1alpha/****/{uid}"
# array in name_hyphen_list is [____,****]
operation_list=(
    "connectorOperation connector-operation"
    "modelOperation model-operation"
)

# This is a special list for model cards
# This converts 
# "v1alpha/{____Name}" to "v1alpha/****s/{id}/++++",
# where each subarray in model_card_list is [____,****,++++]
model_card_list=(
    "modelCard model readme"
)

# ---Find and Replace
##
# name_list
echo "Replacing name_list:"
for name in "${name_list[@]}"; do 
    # Replace name with ID
	# Split the pair into the find and replace strings 
	findstring="/{${name}Name}" 
	replacestring="/${name}s/{id}" 

	echo "  $findstring --> $replacestring"

	# Use sed to replace the string in the file 
	sed -i '' -e "s#$findstring#$replacestring#g" $filename 

    # Replace permalink with UID
    # Split the pair into the find and replace strings 
	findstring="/{${name}Permalink}" 
	replacestring="/${name}s/{uid}" 
	
    echo "  $findstring --> $replacestring"

	# Use sed to replace the string in the file 
	sed -i '' -e "s#$findstring#$replacestring#g" $filename 
done 

##
# definition_list
echo "Replacing definition_list:"
for pair in "${definition_list[@]}"; do 
	# Replace name with ID
	# Split the pair into the find and replace strings 
	findstring="/{$(echo $pair | cut -d ' ' -f 1)Name}" 
	replacestring="/$(echo $pair | cut -d ' ' -f 2)s/{id}" 
	
    echo "  $findstring --> $replacestring"

	# Use sed to replace the string in the file 
	sed -i '' -e "s#$findstring#$replacestring#g" $filename 

    # Replace permalink with UID
    # Split the pair into the find and replace strings 
	findstring="/{$(echo $pair | cut -d ' ' -f 1)Permalink}" 
	replacestring="/$(echo $pair | cut -d ' ' -f 2)s/{uid}" 
	
    echo "  $findstring --> $replacestring"

	# Use sed to replace the string in the file 
	sed -i '' -e "s#$findstring#$replacestring#g" $filename 
done 

##
# controller_list
echo "Replacing controller_list:"
for pair in "${controller_list[@]}"; do 
	# Replace name with ID
	# Split the pair into the find and replace strings 
	findstring="/{$(echo $pair | cut -d ' ' -f 1)Name}" 
	replacestring="/$(echo $pair | cut -d ' ' -f 1)s/{id}/$(echo $pair | cut -d ' ' -f 2)s/{type}" 
	
    echo "  $findstring --> $replacestring"

	# Use sed to replace the string in the file 
	sed -i '' -e "s#$findstring#$replacestring#g" $filename 
done 

##
# operation_list
echo "Replacing operation_list:"
for pair in "${operation_list[@]}"; do 
	# Replace name with UID
	# Split the pair into the find and replace strings 
	findstring="/{$(echo $pair | cut -d ' ' -f 1)Name}" 
	replacestring="/$(echo $pair | cut -d ' ' -f 2)s/{uid}" 
	
    echo "  $findstring --> $replacestring"

	# Use sed to replace the string in the file 
	sed -i '' -e "s#$findstring#$replacestring#g" $filename 
done 

##
# model_card_list
echo "Replacing model_card_list:"
for pair in "${model_card_list[@]}"; do 
	# Replace name with ID and "readme"
	# Split the pair into the find and replace strings 
	findstring="/{$(echo $pair | cut -d ' ' -f 1)Name}" 
	replacestring="/$(echo $pair | cut -d ' ' -f 2)s/{id}/$(echo $pair | cut -d ' ' -f 3)" 
	
    echo "  $findstring --> $replacestring"

	# Use sed to replace the string in the file 
	sed -i '' -e "s#$findstring#$replacestring#g" $filename 
done 

echo "Done!"