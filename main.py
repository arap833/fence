from influxdb import InfluxDBClient


db_client = InfluxDBClient(host='127.0.0.1', port="8086")

db_client.switch_database('fence_dekut')

# voltage=7
# db_client.query('SELECT "duration" FROM "fence_dekut"."autogen"."fence_dekut" WHERE time > now() ')
result = db_client.query('select last("voltage") from "fence_dekut"')
voltage = list(result.get_points())[0]['last']

result = db_client.query('select last("current") from "fence_dekut"')
current = list(result.get_points())[0]['last']
#current=8
#voltage = result.get_points(tags={'user':'arap'})
#result = db_client.query('select last("Current") from "fence_dekut"')
#current=8
#current = result.get_points(tags={'user':'arap'})