from kafka import KafkaProducer # pip install kafka-python
import numpy as np              # pip install numpy
from sys import argv, exit
from time import time, sleep
import json

# different device "profiles" with different 
# distributions of values to make things interesting
# tuple --> (mean, std.dev)
DEVICE_PROFILES = {
	"North": {'totaltraffic': (51.3, 17.7), 'length': (77.4, 18.7)},
	"South": {'totaltraffic': (49.5, 19.3), 'length': (33.0, 13.9)},
	"West": {'totaltraffic': (63.9, 11.7), 'length': (62.8, 21.8)},
	"East": {'totaltraffic': (63.9, 11.7), 'length': (62.8, 21.8)}
}

# check for arguments, exit if wrong
if len(argv) != 2 or argv[1] not in DEVICE_PROFILES.keys():
	print("please provide a valid device name:")
	for key in DEVICE_PROFILES.keys():
		print(f"  * {key}")
	print(f"\nformat: {argv[0]} DEVICE_NAME")
	exit(1)

profile_name = argv[1]
profile = DEVICE_PROFILES[profile_name]

# set up the producer
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

count = 1

# until ^C
while True:
	# get random values within a normal distribution of the value
	totaltraffic = np.random.normal(profile['totaltraffic'][0], profile['totaltraffic'][1])
	length = max(0, min(np.random.normal(profile['length'][0], profile['length'][1]), 100))
	
	# create CSV structure in String Format
	msg = f'{time()},{length},{totaltraffic},{profile_name}'
    # msg = {
    #     'time': time(),
    #     'profile': profile_name,
    #     'total_traffic': totaltraffic,
    #     'length': length
    # }																																																																																																																																																																															
	# send to Kafka
	producer.send('traffic', msg) #convert string to byte and send 
	print(f'sending data to kafka, #{count}')

	count += 1
	sleep(1)