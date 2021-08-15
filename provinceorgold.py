myDict = {'Gold':3,
		  'Silver':2,
		  'Copper':1}
newDict = {'Province':8,
			'Duchy':5,
			'Estate':2}
cost = {'Gold':6,
		  'Silver':3,
		  'Copper':0
}
List = []
count = 0
cards = input().split(' ')
cards = list(map(int,cards))
count = cards[0]*myDict['Gold']+cards[1]*myDict['Silver']+cards[2]*myDict['Copper']
if count >= newDict['Province'] and count > newDict['Duchy'] and count > newDict['Estate']:
	List.append('Province')
if count < newDict['Province'] and count >= newDict['Duchy'] and count > newDict['Estate']:
	List.append('Duchy')
if count < newDict['Province'] and count < newDict['Duchy'] and count >= newDict['Estate']:
	List.append('Estate')

if count >=cost['Gold'] and count > cost['Silver'] and count > cost['Copper'] :
	List.append('Gold')
elif count < cost['Gold'] and count >=  cost['Silver'] and count > cost['Copper'] :
	List.append('Silver')
else:
	List.append('Copper')
if len(List) > 1:
	print(' or '.join(List))
else:
	for item in List:
		print(item)