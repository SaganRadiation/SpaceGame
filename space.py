import re, sys, random, math

DESCRIPTORS = dict()
ATTRIBUTES = set()

class Ship:
	def __init__(self,stats):
		self.stats = stats
		
def getShipStats(ship):
	return '\n'.join([attribute + ':\t' + str(ship.stats[attribute]) for attribute in ATTRIBUTES])

def getShipTexts(ship):
	return '\n'.join([getText(attribute, ship.stats[attribute]) for attribute in ATTRIBUTES])

def makeRandomSpaceShip():
	stats = {}
	for attribute in ATTRIBUTES:
		max = DESCRIPTORS[attribute][-1][0] * 1.2
		stats[attribute] = math.floor(random.random()*max*1.5)
	return Ship(stats)
		

def getText(attribute,val):
	list = DESCRIPTORS[attribute]
	previousDescriptor = None
	for descriptor in list:
		if descriptor[0] > val:
			return previousDescriptor[1]
		previousDescriptor = descriptor
	return list[-1][1]
		
def load():
	try:
		with open('Descriptors.txt') as f:
			data = f.read()
	except:
		print('Failed to open file.')
		sys.exit()
		
	try:
		data = re.sub('[\t ]*#.*?\n','',data)
		data = re.sub('^[\n \t]*','',data)
		data = re.sub('[\n \t]*$','',data)
		for attribute in re.split('\n\D',data):
			if attribute != '':
				attribute = attribute.split('\n')
				name = attribute[0]
				name = re.sub('[\t ]*$','',name)
				list = []
				for descriptor in attribute[1:]:
					match = re.match('(\d+) (.+)',descriptor)
					number = int(match.group(1))
					text = match.group(2)
					text = re.sub('[\t ]*$','',text)
					list += [[number, text]]
				ATTRIBUTES.add(name)
				DESCRIPTORS[name] = list
	except:
		print('Improperly formatted data.')
		sys.exit()
	
def main():
	load()
	print ('\nGenerating random ship...\n')
	myShip = makeRandomSpaceShip()
	print ('Ship stats:')
	print (getShipStats(myShip))
	print ('\nShip description:')
	print (getShipTexts(myShip))
	print ('\n')

if __name__ == '__main__':
	main()