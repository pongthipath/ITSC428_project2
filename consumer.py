# Import KafkaConsumer from Kafka library
from kafka import KafkaConsumer
# Import sys module
import sys, json

# Define server with port
bootstrap_servers = ['localhost:9092']
data_list = list()

def get_JSON(data_l):
    with open('data.json', 'w') as file_write:
        raw_data = {
            "data": data_l
        }
        json.dump(raw_data, file_write)

# Define topic name from where the message will recieve
topicName = 'traffic'

# Initialize consumer variable
consumer = KafkaConsumer (topicName, group_id ='group1',bootstrap_servers = bootstrap_servers)

# Read and print message from consumer
for msg in consumer:
    print("Topic Name=%s,Message=%s"%(msg.topic,msg.value))
    dec = str(msg.value, 'utf-8')
    data = dec.split(",")
    json_file = {
        'time': data[0].split('"')[1],
        'profile': data[3].split('"')[0],
        'total_traffic': data[1],
        'length': data[2]
    }                                                                                                                                                                                                                                                                                                                                                                                               
    data_list.append(json_file)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    print("\n")
    print(data_list)
    get_JSON(data_list)                                                                                                          

# Terminate the script
sys.exit()

