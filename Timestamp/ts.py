import sys
import json
import math
from datetime import datetime, timedelta, timezone

kst = timezone(timedelta(hours=9))
gmt = timezone(timedelta(hours=0))
item = {}
query = sys.argv[1]

if query == 'now':
	item = {
		"items": [
			{
				"uid" : "1",
				"title" : "",
				"subtitle" : "timestamp",
				"arg" : "arg1",
			},
			{
				"uid" : "2",
				"title" : "",
				"subtitle" : "timestamp-ms",
				"arg" : "arg1",
			},
			{
				"uid" : "3",
				"title" : "",
				"subtitle" : "KST +09:00",
				"arg" : "arg3",
			},
			{
				"uid" : "4",
				"title" : "",
				"subtitle" : "GMT +-00:00",
				"arg" : "arg4",
			}
		]
	}

	now = datetime.now()
	datetime_kst = now.astimezone(kst)
	datetime_gmt = now.astimezone(gmt)
	item['items'][0]['title'] = int(now.timestamp())
	item['items'][1]['title'] = int(now.timestamp()) * 1000
	item['items'][2]['title'] = datetime_kst.isoformat()
	item['items'][3]['title'] = datetime_gmt.isoformat()
	item['items'][0]['arg'] = int(now.timestamp())
	item['items'][1]['arg'] = int(now.timestamp()) * 1000
	item['items'][2]['arg'] = datetime_kst.isoformat()
	item['items'][3]['arg'] = datetime_gmt.isoformat()

else:
	digits = len(query)
	item = {
		"items": [
			{
				"uid" : "1",
				"title" : "",
				"subtitle" : "",
				"arg" : "",
			},
			{
				"uid" : "2",
				"title" : "",
				"subtitle" : "",
				"arg" : "",
			},
		]
	}

	if digits == 8:		# YYYYmmdd
		dateObj = datetime.strptime(query, '%Y%m%d')
		datetime_kst = dateObj.astimezone(kst)

		item['items'][0]['title'] = datetime_kst.timestamp()
		item['items'][1]['title'] = datetime_kst.timestamp() * 1000

		item['items'][0]['arg'] = datetime_kst.timestamp()
		item['items'][1]['arg'] = datetime_kst.timestamp() * 1000

		item['items'][0]['subtitle'] = "timestamp"
		item['items'][1]['subtitle'] = "timestamp - microseconds"
	elif digits == 14:	# YYYYmmddHHMMSS
		dateObj = datetime.strptime(query, '%Y%m%d%H%M%S')
		datetime_kst = dateObj.astimezone(kst)

		item['items'][0]['title'] = datetime_kst.timestamp()
		item['items'][1]['title'] = datetime_kst.timestamp() * 1000

		item['items'][0]['arg'] = datetime_kst.timestamp()
		item['items'][1]['arg'] = datetime_kst.timestamp() * 1000

		item['items'][0]['subtitle'] = "timestamp"
		item['items'][1]['subtitle'] = "timestamp - microseconds"
	elif digits == 10:	# timestamp
		timestamp = int(query)
		datetime_kst = datetime.fromtimestamp(timestamp).astimezone(kst)
		datetime_gmt = datetime.fromtimestamp(timestamp).astimezone(gmt)
		item['items'][0]['title'] = datetime_kst.isoformat()
		item['items'][1]['title'] = datetime_gmt.isoformat()

		item['items'][0]['arg'] = datetime_kst.isoformat()
		item['items'][1]['arg'] = datetime_gmt.isoformat()

		item['items'][0]['subtitle'] = "KST +09:00"
		item['items'][1]['subtitle'] = "GMT +00:00"
	elif digits == 13:	# timestamp-ms
		timestamp = int(query)
		datetime_kst = datetime.fromtimestamp(timestamp // 1000).astimezone(kst)
		datetime_gmt = datetime.fromtimestamp(timestamp // 1000).astimezone(gmt)
		item['items'][0]['title'] = datetime_kst.isoformat()
		item['items'][1]['title'] = datetime_gmt.isoformat()

		item['items'][0]['arg'] = datetime_kst.isoformat()
		item['items'][1]['arg'] = datetime_gmt.isoformat()

		item['items'][0]['subtitle'] = "KST +09:00"
		item['items'][1]['subtitle'] = "GMT +00:00"
print(json.dumps(item))

