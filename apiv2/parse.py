#!/usr/bin/python
import sys, json

jess = json.loads('{"header":{"id":"76fffc29-008f-4639-82ef-956b9119130e","test":false,"prepared":"2017-03-28T08:40:58.6089066Z","sender":{"id":"ABS","name":"Australian Bureau of Statistics"},"links":[{"href":"http://stat.data.abs.gov.au:80/sdmx-json/data/MERCH_EXP/1+4.1+6.-1.-.M/all?endTime=2014-05&dimensionAtObservation=allDimensions&startTime=2014-02","rel":"request"}]},"dataSets":[{"action":"Information","observations":{"0:0:0:0:0:0":[36053.845,0,null],"0:0:0:0:0:1":[35558.589,0,null],"0:0:0:0:0:2":[37975.071,0,null],"0:0:0:0:0:3":[44953.016,0,null],"0:1:0:0:0:0":[193473.083,0,null],"0:1:0:0:0:1":[259435.32,0,null],"0:1:0:0:0:2":[267763.476,0,null],"0:1:0:0:0:3":[267756.105,0,null],"1:0:0:0:0:0":[91358.087,0,null],"1:0:0:0:0:1":[96998.913,0,null],"1:0:0:0:0:2":[83416.81,0,null],"1:0:0:0:0:3":[114941.179,0,null],"1:1:0:0:0:0":[177304.745,0,null],"1:1:0:0:0:1":[205721.564,0,null],"1:1:0:0:0:2":[194670.073,0,null],"1:1:0:0:0:3":[193112.341,0,null]}}],"structure":{"links":[{"href":"http://stat.data.abs.gov.au/sdmx-json/dataflow/MERCH_EXP/all","rel":"dataflow"}],"name":"Merchandise Exports - ($ Thousands)","description":"Merchandise Exports - ($ Thousands)","dimensions":{"observation":[{"keyPosition":0,"id":"REGION","name":"State of Origin","values":[{"id":"1","name":"New South Wales"},{"id":"4","name":"South Australia"}]},{"keyPosition":1,"id":"SITC_REV3","name":"Commodity by SITC","values":[{"id":"1","name":"Beverages and tobacco"},{"id":"6","name":"Manufactured goods classified chiefly by material"}]},{"keyPosition":2,"id":"INDUSTRY","name":"Industry of Origin (ANZSIC06)","values":[{"id":"-1","name":"Total"}]},{"keyPosition":3,"id":"COUNTRY","name":"Country of Destination","values":[{"id":"-","name":"Total"}]},{"keyPosition":4,"id":"FREQUENCY","name":"Frequency","values":[{"id":"M","name":"Monthly"}],"role":"FREQ"},{"id":"TIME_PERIOD","name":"Time","values":[{"id":"2014-02","name":"Feb-2014"},{"id":"2014-03","name":"Mar-2014"},{"id":"2014-04","name":"Apr-2014"},{"id":"2014-05","name":"May-2014"}],"role":"TIME_PERIOD"}]},"attributes":{"dataSet":[],"series":[],"observation":[{"id":"TIME_FORMAT","name":"Time Format","values":[{"id":"P1M","name":"Monthly"}]},{"id":"OBS_STATUS","name":"Observation Status","values":[]}]},"annotations":[{"title":"Statistical usage warning","uri":"","text":"ABS.Stat beta is continuing to be developed.  Data will be updated as soon as possible following its 11:30 am release on the ABS website."}]}}')

lookup = jess['structure']['dimensions']['observation']

states = {}
commodities = {}
months = {}

for i in lookup:
	id = i['id']
	if id == 'REGION':
		index = 0
		for state in i['values']:
			states[index] = state['name']
			index += 1
	if id == 'SITC_REV3':
		index = 0
		for commodity in i['values']:
			commodities[index] = commodity['name']
			index += 1
	if id == 'TIME_PERIOD':
		index = 0
		for month in i['values']:
			months[index] = month['name']
			index += 1

result = {}
result['MonthlyCommodityExportData'] = [{} for i in range(0,len(commodities))]
export_data = result['MonthlyCommodityExportData']

for dataset in jess['dataSets']:
	for observation, item in dataset['observations'].items():
		value = item[0]
		(state, commodity, _, _, _, month) = observation.encode().split(':')
		state = int(state)
		commodity = int(commodity)
		month = int(month)

		table = export_data[commodity]
		if 'commodity' not in table:
			table['commodity'] = str(commodities[commodity])
		if 'regional_data' not in table:
			table['regional_data'] = [{} for i in range(0, len(states))]

		regional_data = table['regional_data'][state]
		if 'state' not in regional_data:
			regional_data['state'] = str(states[state])
		if 'data' not in regional_data:
			regional_data['data'] = [{} for i in range(0, len(months))]

		export = regional_data['data'][month]
		export['date'] = str(months[month])
		export['value'] = value


print(json.dumps(result))






