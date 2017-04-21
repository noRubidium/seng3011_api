*** Settings ***
Library                       HttpLibrary.HTTP
Library                       OperatingSystem
Test Setup                    Create API Context
 
*** Variables ***
${API_ENDPOINT}               http://api.kaiworship.xyz
${VERSION}										v4

*** Keywords ***
Create API Context
  Create Http Context         api.kaiworship.xyz   http

*** Test Cases ***
M.1.1 Merch All Variables No Dates

	[Tags]  happy-day 

	${stats_area} =   Set Variable	MerchandiseExports
	${categories} = 	Set Variable  Total,FoodAndLiveAnimals,BeveragesAndTobacco,CrudeMaterialAndInedible,MineralFuelLubricantAndRelatedMaterial,AnimalAndVegetableOilFatAndWaxes,ChemicalsAndRelatedProducts,ManufacturedGoods,MachineryAndTransportEquipments,OtherManufacturedArticles,Unclassified
	${states} =  			Set Variable 	Total,NSW,WA,SA,ACT,VIC,TAS,QLD,NT
	${params} =  			Set Variable  ignoreHeader=True

	${expected} = 		Set Variable  M.1.1.expected.json

  Create API Context
  GET  							/v4/${stats_area}/${categories}/${states}?${params}
  Log								${API_ENDPOINT}/v4/${stats_area}/${categories}/${states}?${params}

  Response Status Code Should Equal		200

  ${resp_body} =  	Get Response Body
  ${resp_json} =  	Parse Json  	${resp_body}
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
  Log								${API_ENDPOINT}/v4/${stats_area}/${categories}/${states}?${params}

  Response Status Code Should Equal		200

  ${resp_body} =  	Get Response Body
  ${resp_json} =  	Parse Json  	${resp_body}
  Log  							${resp_json}
  ${exp_file} =     Get File    	expected_outputs/${expected}
  ${exp_json} =     Parse Json    ${exp_file}
  Should Be Equal  	${resp_json}  ${exp_json}


M.1.2 Merch All Variables Entire Date Range

	${stats_area} =   Set Variable	MerchandiseExports
	${categories} = 	Set Variable  Total,FoodAndLiveAnimals,BeveragesAndTobacco,CrudeMaterialAndInedible,MineralFuelLubricantAndRelatedMaterial,AnimalAndVegetableOilFatAndWaxes,ChemicalsAndRelatedProducts,ManufacturedGoods,MachineryAndTransportEquipments,OtherManufacturedArticles,Unclassified
	${states} =  			Set Variable 	Total,NSW,WA,SA,ACT,VIC,TAS,QLD,NT

	${start_date} = 	Set Variable 	1995-07-01
	${end_date} = 		Set Variable 	2017-02-01
	${params} =  			Set Variable  startDate=${start_date}&endDate=${end_date}&ignoreHeader=True

	${expected} = 		Set Variable  M.1.2.expected.json

  Create API Context
  GET  							/v4/${stats_area}/${categories}/${states}?${params}
  Log								${API_ENDPOINT}/v4/${stats_area}/${categories}/${states}?${params}

  Response Status Code Should Equal		200

  ${resp_body} =  	Get Response Body
  ${resp_json} =  	Parse Json  	${resp_body}
  Log  							${resp_json}
  ${exp_file} =     Get File    	expected_outputs/${expected}
  ${exp_json} =     Parse Json    ${exp_file}
  Should Be Equal  	${resp_json}  ${exp_json}


R.1.2 Retail All Variables Entire Date Range

	${stats_area} =   Set Variable	Retail
	${categories} = 	Set Variable  Total,Food,HouseholdGood,ClothingFootwareAndPersonalAccessory,DepartmentStores,CafesRestaurantsAndTakeawayFood,Other
	${states} =  			Set Variable 	Total,NSW,WA,SA,ACT,VIC,TAS,QLD,NT

	${start_date} = 	Set Variable 	1995-07-01
	${end_date} = 		Set Variable 	2017-02-01
	${params} =  			Set Variable  startDate=${start_date}&endDate=${end_date}&ignoreHeader=True

	${expected} = 		Set Variable  R.1.2.expected.json

  Create API Context
  GET  							/v4/${stats_area}/${categories}/${states}?${params}
  Log								${API_ENDPOINT}/v4/${stats_area}/${categories}/${states}?${params}

  Response Status Code Should Equal		200

  ${resp_body} =  	Get Response Body
  ${resp_json} =  	Parse Json  	${resp_body}
  Log  							${resp_json}
  ${exp_file} =     Get File    	expected_outputs/${expected}
  ${exp_json} =     Parse Json    ${exp_file}
  Should Be Equal  	${resp_json}  ${exp_json}


M.1.3 Merch All Variables Date Range Beyond All Data

	${stats_area} =   Set Variable	MerchandiseExports
	${categories} = 	Set Variable  Total,FoodAndLiveAnimals,BeveragesAndTobacco,CrudeMaterialAndInedible,MineralFuelLubricantAndRelatedMaterial,AnimalAndVegetableOilFatAndWaxes,ChemicalsAndRelatedProducts,ManufacturedGoods,MachineryAndTransportEquipments,OtherManufacturedArticles,Unclassified
	${states} =  			Set Variable 	Total,NSW,WA,SA,ACT,VIC,TAS,QLD,NT

	${start_date} = 	Set Variable 	1990-01-01
	${end_date} = 		Set Variable 	2018-01-01
	${params} =  			Set Variable  startDate=${start_date}&endDate=${end_date}&ignoreHeader=True

	${expected} = 		Set Variable  M.1.3.expected.json

  Create API Context
  GET  							/v4/${stats_area}/${categories}/${states}?${params}
  Log								${API_ENDPOINT}/v4/${stats_area}/${categories}/${states}?${params}

  Response Status Code Should Equal		200

  ${resp_body} =  	Get Response Body
  ${resp_json} =  	Parse Json  	${resp_body}
  Log  							${resp_json}
  ${exp_file} =     Get File    	expected_outputs/${expected}
  ${exp_json} =     Parse Json    ${exp_file}
  Should Be Equal  	${resp_json}  ${exp_json}


R.1.3 Retail All Variables Date Range Beyond All Data

	${stats_area} =   Set Variable	Retail
	${categories} = 	Set Variable  Total,Food,HouseholdGood,ClothingFootwareAndPersonalAccessory,DepartmentStores,CafesRestaurantsAndTakeawayFood,Other
	${states} =  			Set Variable 	Total,NSW,WA,SA,ACT,VIC,TAS,QLD,NT

	${start_date} = 	Set Variable 	1990-01-01
	${end_date} = 		Set Variable 	2018-01-01
	${params} =  			Set Variable  startDate=${start_date}&endDate=${end_date}&ignoreHeader=True

	${expected} = 		Set Variable  R.1.3.expected.json

  Create API Context
  GET  							/v4/${stats_area}/${categories}/${states}?${params}
  Log								${API_ENDPOINT}/v4/${stats_area}/${categories}/${states}?${params}

  Response Status Code Should Equal		200

  ${resp_body} =  	Get Response Body
  ${resp_json} =  	Parse Json  	${resp_body}
  Log  							${resp_json}
  ${exp_file} =     Get File    	expected_outputs/${expected}
  ${exp_json} =     Parse Json    ${exp_file}
  Should Be Equal  	${resp_json}  ${exp_json}







M.E.1.1 Merch Error Incorrect Stats Area

	[Tags]  error 

	${stats_area} =   Set Variable	MerchandiseExport
	${categories} = 	Set Variable  Total,FoodAndLiveAnimals,BeveragesAndTobacco,CrudeMaterialAndInedible,MineralFuelLubricantAndRelatedMaterial,AnimalAndVegetableOilFatAndWaxes,ChemicalsAndRelatedProducts,ManufacturedGoods,MachineryAndTransportEquipments,OtherManufacturedArticles,Unclassified
	${states} =  			Set Variable 	Total,NSW,WA,SA,ACT,VIC,TAS,QLD,NT

	${start_date} = 	Set Variable 	1990-01-01
	${end_date} = 		Set Variable 	2018-01-01
	${params} =  			Set Variable  startDate=${start_date}&endDate=${end_date}&ignoreHeader=True

	${expected} = 		Set Variable  M.E.1.1.expected.json

  Create API Context
  Next Request May Not Succeed
  GET 							/v4/${stats_area}/${categories}/${states}?${params}
  Log								${API_ENDPOINT}/v4/${stats_area}/${categories}/${states}?${params}

  Response Status Code Should Equal		404

  ${resp_body} =  	Get Response Body
  ${resp_json} =  	Parse Json  	${resp_body}
  Log  							${resp_json}
  ${exp_file} =     Get File    	expected_outputs/${expected}
  ${exp_json} =     Parse Json    ${exp_file}
  Should Be Equal  	${resp_json}  ${exp_json}


R.E.1.1 Retail Error Incorrect Stats Area

	[Tags]  error 

	${stats_area} =   Set Variable	Retails
	${categories} = 	Set Variable  Total,Food,HouseholdGood,ClothingFootwareAndPersonalAccessory,DepartmentStores,CafesRestaurantsAndTakeawayFood,Other
	${states} =  			Set Variable 	Total,NSW,WA,SA,ACT,VIC,TAS,QLD,NT

	${start_date} = 	Set Variable 	1990-01-01
	${end_date} = 		Set Variable 	2018-01-01
	${params} =  			Set Variable  startDate=${start_date}&endDate=${end_date}&ignoreHeader=True

	${expected} = 		Set Variable  R.E.1.1.expected.json

  Create API Context
  Next Request May Not Succeed
  GET 							/v4/${stats_area}/${categories}/${states}?${params}
  Log								${API_ENDPOINT}/v4/${stats_area}/${categories}/${states}?${params}

  Response Status Code Should Equal		404

  ${resp_body} =  	Get Response Body
  ${resp_json} =  	Parse Json  	${resp_body}
  Log  							${resp_json}
  ${exp_file} =     Get File    	expected_outputs/${expected}
  ${exp_json} =     Parse Json    ${exp_file}
  Should Be Equal  	${resp_json}  ${exp_json}



M.E.1.2 Merch Error Incorrect Commodities

	[Tags]  error 

	${stats_area} =   Set Variable	MerchandiseExports
	${categories} = 	Set Variable  Total,FoodAndLiveAnimals,BeveragesAndTobacco,CrudeMaterialAndInedible,MineralFuelLubricantAndRelatedMaterial,AnimalAndVegetableOilFat,,
	${states} =  			Set Variable 	Total,NSW,WA,SA,ACT,VIC,TAS,QLD,NT

	${start_date} = 	Set Variable 	1990-01-01
	${end_date} = 		Set Variable 	2018-01-01
	${params} =  			Set Variable  startDate=${start_date}&endDate=${end_date}&ignoreHeader=True

	${expected} = 		Set Variable  M.E.1.2.expected.json

  Create API Context
  Next Request May Not Succeed
  GET 							/v4/${stats_area}/${categories}/${states}?${params}
  Log								${API_ENDPOINT}/v4/${stats_area}/${categories}/${states}?${params}

  Response Status Code Should Equal		404

  ${resp_body} =  	Get Response Body
  ${resp_json} =  	Parse Json  	${resp_body}
  Log  							${resp_json}
  ${exp_file} =     Get File    	expected_outputs/${expected}
  ${exp_json} =     Parse Json    ${exp_file}
  Should Be Equal  	${resp_json}  ${exp_json}


R.E.1.2 Retail Error Incorrect Categories

	[Tags]  error 

	${stats_area} =   Set Variable	Retail
	${categories} = 	Set Variable  Total,Food,HouseholdGood,ClothingAccessory,DepartmentStores,CafesRestaurantsAndTakeawayFood,Other
	${states} =  			Set Variable 	Total,NSW,WA,SA,ACT,VIC,TAS,QLD,NT

	${start_date} = 	Set Variable 	1990-01-01
	${end_date} = 		Set Variable 	2018-01-01
	${params} =  			Set Variable  startDate=${start_date}&endDate=${end_date}&ignoreHeader=True

	${expected} = 		Set Variable  R.E.1.2.expected.json

  Create API Context
  Next Request May Not Succeed
  GET 							/v4/${stats_area}/${categories}/${states}?${params}
  Log								${API_ENDPOINT}/v4/${stats_area}/${categories}/${states}?${params}

  Response Status Code Should Equal		404

  ${resp_body} =  	Get Response Body
  ${resp_json} =  	Parse Json  	${resp_body}
  Log  							${resp_json}
  ${exp_file} =     Get File    	expected_outputs/${expected}
  ${exp_json} =     Parse Json    ${exp_file}
  Should Be Equal  	${resp_json}  ${exp_json}



M.E.1.3 Merch Error Incorrect States

	[Tags]  error 

	${stats_area} =   Set Variable	MerchandiseExports
	${categories} = 	Set Variable  Total,FoodAndLiveAnimals,BeveragesAndTobacco,CrudeMaterialAndInedible,MineralFuelLubricantAndRelatedMaterial,AnimalAndVegetableOilFatAndWaxes,ChemicalsAndRelatedProducts,ManufacturedGoods,MachineryAndTransportEquipments,OtherManufacturedArticles,Unclassified
	${states} =  			Set Variable 	NZ,WA

	${start_date} = 	Set Variable 	1990-01-01
	${end_date} = 		Set Variable 	2018-01-01
	${params} =  			Set Variable  startDate=${start_date}&endDate=${end_date}&ignoreHeader=True

	${expected} = 		Set Variable  M.E.1.3.expected.json

  Create API Context
  Next Request May Not Succeed
  GET 							/v4/${stats_area}/${categories}/${states}?${params}
  Log								${API_ENDPOINT}/v4/${stats_area}/${categories}/${states}?${params}

  Response Status Code Should Equal		404

  ${resp_body} =  	Get Response Body
  ${resp_json} =  	Parse Json  	${resp_body}
  Log  							${resp_json}
  ${exp_file} =     Get File    	expected_outputs/${expected}
  ${exp_json} =     Parse Json    ${exp_file}
  Should Be Equal  	${resp_json}  ${exp_json}


R.E.1.3 Retail Error Incorrect States

	[Tags]  error 

	${stats_area} =   Set Variable	Retail
	${categories} = 	Set Variable  Total,Food,HouseholdGood,ClothingFootwareAndPersonalAccessory,DepartmentStores,CafesRestaurantsAndTakeawayFood,Other
	${states} =  			Set Variable 	NZ,WA

	${start_date} = 	Set Variable 	1990-01-01
	${end_date} = 		Set Variable 	2018-01-01
	${params} =  			Set Variable  startDate=${start_date}&endDate=${end_date}&ignoreHeader=True

	${expected} = 		Set Variable  R.E.1.3.expected.json

  Create API Context
  Next Request May Not Succeed
  GET 							/v4/${stats_area}/${categories}/${states}?${params}
  Log								${API_ENDPOINT}/v4/${stats_area}/${categories}/${states}?${params}

  Response Status Code Should Equal		404

  ${resp_body} =  	Get Response Body
  ${resp_json} =  	Parse Json  	${resp_body}
  Log  							${resp_json}
  ${exp_file} =     Get File    	expected_outputs/${expected}
  ${exp_json} =     Parse Json    ${exp_file}
  Should Be Equal  	${resp_json}  ${exp_json}

