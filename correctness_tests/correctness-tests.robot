*** Settings ***
Library                       HttpLibrary.HTTP
Library                       OperatingSystem
Test Setup                    Create API Context
 
*** Variables ***
${API_ENDPOINT}               http://api.kaiworship.xyz/

*** Keywords ***
Create API Context
  Create Http Context                   api.kaiworship.xyz   http

*** Test Cases ***
M.1.1 Merch All Variables No Dates

	${stats_area} =   Set Variable	MerchandiseExports
	${categories} = 	Set Variable  Total,FoodAndLiveAnimals,BeveragesAndTobacco,CrudeMaterialAndInedible,MineralFuelLubricantAndRelatedMaterial,AnimalAndVegetableOilFatAndWaxes,ChemicalsAndRelatedProducts,ManufacturedGoods,MachineryAndTransportEquipments,OtherManufacturedArticles,Unclassified
	${states} =  			Set Variable 	Total,NSW,WA,SA,ACT,VIC,TAS,QLD,NT
	${params} =  			Set Variable  ignoreHeader=True

	${expected} = 		Set Variable  M.1.1.expected.json

  Create API Context
  GET  							/v4/${stats_area}/${categories}/${states}?${params}
  ${resp} =  				Get Response Body
  ${resp_json} =  	Parse Json  	${resp}
  Log  							${resp_json}
  ${exp_file} =     Get File    	expected_outputs/${expected}
  ${exp_json} =     Parse Json    ${exp_file}
  Should Be Equal  	${resp_json}  ${exp_json}

 
R.1.1 Retail All Variables No Dates

	${stats_area} =   Set Variable	Retail
	${categories} = 	Set Variable  Total,Food,HouseholdGood,ClothingFootwareAndPersonalAccessory,DepartmentStores,CafesRestaurantsAndTakeawayFood,Other
	${states} =  			Set Variable 	Total,NSW,WA,SA,ACT,VIC,TAS,QLD,NT
	${params} =  			Set Variable  ignoreHeader=True

	${expected} = 		Set Variable  R.1.1.expected.json

  Create API Context
  GET  							/v4/${stats_area}/${categories}/${states}?${params}
  ${resp} =  				Get Response Body
  ${resp_json} =  	Parse Json  	${resp}
  Log  							${resp_json}
  ${exp_file} =     Get File    	expected_outputs/${expected}
  ${exp_json} =     Parse Json    ${exp_file}
  Should Be Equal  	${resp_json}  ${exp_json}



