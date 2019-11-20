d1 = {'byteOP': 'dan', 'python': 'judo', "advpython": 'judo', 'cbasic': 'ransom'}

d2={}
d2 = {v:[] for k,v in d1.items()}
{d2[v].append(k) for k,v in d1.items()}
print(d2)


print(sorted(d1.items(),key=lambda x:x[1]))

d = {
	'vgs': [{
		'name': 'nsulateTestArray',
		'status': 'RUNNING',
		'health': 'OPTIMAL',
		'uuid': 'c7e94aeb-81b2-4ee8-ba18-48e25566ce24',
		'k': '1',
		'm': '1',
		'nSpans': '1',
		'sizeBytes': '30895312896',
		'freeBytes': '30895312896',
		'reservedBytes': '264241152',
		'erasure': 'ISAL',
		'checksum': 'SHA-256',
		'encryption': 'NONE',
		'platform': 'GPU',
		'creationTimestamp': '1567686695',
		'uptimeSeconds': '28',
		'spans': [{
			'spanSizeBytes': '63308808192',
			'isRowdb': True,
			'pvs': [{
				'path': '/dev/sdd',
				'serial': '987041930082',
				'model': 'V-32',
				'type': 'SSD',
				'sizeBytes': '31675383808',
				'state': 'OK',
				'TDW': 0.00384288724
			}, {
				'path': '/dev/sde',
				'serial': '987042030651',
				'model': 'V-32',
				'type': 'SSD',
				'sizeBytes': '31675383808',
				'state': 'OK',
				'TDW': 0.00384288724
			}]
		}, {
			'spanId': '1',
			'spanSizeBytes': '63308808192',
			'pvs': [{
				'path': '/dev/sdb',
				'serial': '987042030674',
				'model': 'V-32',
				'type': 'SSD',
				'sizeBytes': '31675383808',
				'state': 'OK'
			}, {
				'path': '/dev/sdc',
				'serial': '987042030263',
				'model': 'V-32',
				'type': 'SSD',
				'sizeBytes': '31675383808',
				'state': 'OK'
			}, {
				'path': '/dev/sdf',
				'serial': '987042030659',
				'model': 'V-32',
				'type': 'SSD',
				'sizeBytes': '31675383808',
				'state': 'SPARE'
			}]
		}],
		'rowK': '1',
		'rowM': '1',
		'maxDriveTDW': 0.00384288724,
		'freeNvpoolBytes': '3797942272',
		'totalNvpoolBytes': '4871684096',
		'reservedNvpoolBytes': '1073741824',
		'volatileCache': '1',
		'stripSize': '262144'
	}],
	'customerId': 'nyriad-developer-calsoft-spot1',
	'hardware': {
		'cpu': [{
			'model': 'Intel(R) Core(TM) i5-8400 CPU @ 2.80GHz'
		}],
		'ram': {
			'totalBytes': '23105392640',
			'nsulateUsageBytes': '610725888'
		},
		'gpu': [{
			'name': 'GeForce GTX 1050 Ti',
			'uuid': 'GPU-bb9d4de3-3016-2d88-04e3-11885db7c62e'
		}],
		'os': {
			'distro': 'Ubuntu 18.04.2 LTS',
			'kernel': '4.15.0-60-generic GNU/Linux'
		},
		'network': {
			'macAddress': 'e0:d5:5e:b0:db:64'
		}
	}
}
print(d)