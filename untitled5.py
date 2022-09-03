import random
import time

# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
from azure.iot.device import IoTHubDeviceClient, Message

# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table
CONNECTION_STRING = "HostName=Amrutha1.azure-devices.net;DeviceId=123;SharedAccessKey=/R43I3o2PXonGO2gJLv69rxpPx6keI1xXoQDghzzCQk="

# Define the JSON message to send to IoT Hub.
PRESSURE = 20.0
PRESSURE1 = 60
MSG_TXT = '{{"pressure": {pressure},"pressure1": {pressure1}}}'

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def iothub_client_telemetry_sample_run():

    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )
        while True:
            # Build the message with simulated telemetry values.
            pressure = PRESSURE + (random.random() * 15)
            pressure1 = PRESSURE1 + (random.random() * 20)
            msg_txt_formatted = MSG_TXT.format(pressure=pressure, pressure1=pressure1)
            message = Message(msg_txt_formatted)

            # Add a custom application property to the message.
            # An IoT hub can filter on these properties without access to the message body.
            #if pressure > 40:
              #message.custom_properties["pressureAlert"] = "true"
            #else:
              #message.custom_properties["pressureAlert"] = "false"

            # Send the message.
            print( "Sending message: {}".format(message) )
            client.send_message(message)
            print ( "Message successfully sent" )
            time.sleep(3)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "IoT Hub Quickstart #1 - Simulated device" )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()
