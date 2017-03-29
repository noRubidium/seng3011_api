#!/usr/bin/python
import sys, json
from utils import lookup, get_state_abbrev, get_date_end

jess = json.loads('{"header":{"id":"48fc0e79-a3e1-4045-9bec-c8e1b1a3f242","test":false,"prepared":"2017-03-29T04:04:17.9217437Z","sender":{"id":"ABS","name":"Australian Bureau of Statistics"},"links":[{"href":"http://stat.data.abs.gov.au:80/sdmx-json/data/RT/1+4.2.41+44.10.M/all?endTime=2014-05&dimensionAtObservation=allDimensions&startTime=2014-02","rel":"request"}]},"dataSets":[{"action":"Information","observations":{"0:0:0:0:0:0":[2599.8,0,null],"0:0:0:0:0:1":[2862.7,0,null],"0:0:0:0:0:2":[2754.1,0,null],"0:0:0:0:0:3":[2820.7,0,null],"0:0:1:0:0:0":[336.2,0,null],"0:0:1:0:0:1":[410.2,0,null],"0:0:1:0:0:2":[472.2,0,null],"0:0:1:0:0:3":[451.9,0,null],"1:0:0:0:0:0":[630.2,0,null],"1:0:0:0:0:1":[690.6,0,null],"1:0:0:0:0:2":[679.9,0,null],"1:0:0:0:0:3":[686.4,0,null],"1:0:1:0:0:0":[80.4,0,null],"1:0:1:0:0:1":[99.2,0,null],"1:0:1:0:0:2":[108.2,0,null],"1:0:1:0:0:3":[106.8,0,null]}}],"structure":{"links":[{"href":"http://stat.data.abs.gov.au/sdmx-json/dataflow/RT/all","rel":"dataflow"}],"name":"Retail Trade","description":"Retail Trade","dimensions":{"observation":[{"keyPosition":0,"id":"ASGC_2010","name":"Region","values":[{"id":"1","name":"New South Wales"},{"id":"4","name":"South Australia"}]},{"keyPosition":1,"id":"DT","name":"Data Type","values":[{"id":"2","name":"Current Prices ($ Million)"}]},{"keyPosition":2,"id":"IND_R","name":"Retail Industry","values":[{"id":"41","name":"Food retailing"},{"id":"44","name":"Department stores"}]},{"keyPosition":3,"id":"TSEST","name":"Adjustment Type","values":[{"id":"10","name":"Original"}]},{"keyPosition":4,"id":"FREQUENCY","name":"Frequency","values":[{"id":"M","name":"Monthly"}],"role":"FREQ"},{"id":"TIME_PERIOD","name":"Time","values":[{"id":"2014-02","name":"Feb-2014"},{"id":"2014-03","name":"Mar-2014"},{"id":"2014-04","name":"Apr-2014"},{"id":"2014-05","name":"May-2014"}],"role":"TIME_PERIOD"}]},"attributes":{"dataSet":[],"series":[],"observation":[{"id":"TIME_FORMAT","name":"Time Format","values":[{"id":"P1M","name":"Monthly"}]},{"id":"OBS_STATUS","name":"Observation Status","values":[]}]},"annotations":[{"title":"Statistical usage warning","uri":"","text":"ABS.Stat beta is continuing to be developed.  Data will be updated as soon as possible following its 11:30 am release on the ABS website."}]}}')
lookup = jess['structure']['dimensions']['observation']

states = {}
categories = {}
months = {}

for i in lookup:
	id = i['id']
	if id == 'ASGC_2010':
		index = 0
		for state in i['values']:
			states[index] = state['name']
			index += 1
	if id == 'IND_R':
		index = 0
		for category in i['values']:
			categories[index] = category['name']
			index += 1
	if id == 'TIME_PERIOD':
		index = 0
		for month in i['values']:
			months[index] = month['name']
			index += 1

result = {}
result['MonthlyRetailData'] = [{} for i in range(0,len(categories))]
retail_data = result['MonthlyRetailData']

for dataset in jess['dataSets']:
	for observation, item in dataset['observations'].items():
		turnover = item[0]
		(state, _, category, _, _, month) = observation.encode().split(':')
		state = int(state)
		category = int(category)
		month = int(month)

		table = retail_data[category]
		if 'category' not in table:
			table['category'] = str(categories[category])
		if 'regional_data' not in table:
			table['regional_data'] = [{} for i in range(0, len(states))]

		regional_data = table['regional_data'][state]
		if 'state' not in regional_data:
			regional_data['state'] = get_state_abbrev(states[state])
		if 'data' not in regional_data:
			regional_data['data'] = [{} for i in range(0, len(months))]

		export = regional_data['data'][month]
		export['date'] = get_date_end(str(months[month]))
		export['turnover'] = turnover



print(json.dumps(result))
