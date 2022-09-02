
# coding: utf-8

# In[ ]:


# coding: utf-8

# In[ ]:


# Install below packages
'''
sudo pip3 install azure-iot-device
sudo pip3 install azure-iot-hub
sudo pip3 install azure-iothub-service-client
sudo pip3 install azure-iothub-device-client
'''

# Run below on Azure CLI
'''
#### below to add extension
az extension add --name azure-cli-iot-ext

### Below to start device monitor to check incoming telemetry data
az iot hub monitor-events --hub-name YourIoTHubName --device-id MyPythonDevice

'''

# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import random
import time

# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
from azure.iot.device import IoTHubDeviceClient, Message

# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table
CONNECTION_STRING = "HostName=IotProjectEcg.azure-devices.net;DeviceId=IOT;SharedAccessKey=dIPmzJZPtbko32OxxYHCfo/Naqyz699lU/ljQejwpug="

# Define the JSON message to send to IoT Hub.
BP = 5.0
PULSE = 0.5
PRESSURE = 2
PRESSURE1 = 6.5
MSG_TXT = '{{"BP": {BP},"PULSE": {PULSE},"PRESSURE":{PRESSURE},"PRESSURE1": {PRESSURE1}}}'

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
            bp = BP + (random.random() * 15)
            pulse = PULSE + (random.random() * 15)
            pressure= PRESSURE + (random.random() * 15)
            pressure1 =PRESSURE1 + (random.random() * 15)
            msg_txt_formatted = MSG_TXT.format(bp=bp, pulse=pulse,pressure=pressure , pressure1=pressure1)
            message = Message(msg_txt_formatted)

            # Add a custom application property to the message.
            # An IoT hub can filter on these properties without access to the message body.
            #if temperature > 30:
              #message.custom_properties["temperatureAlert"] = "true"
            #else:
              #message.custom_properties["temperatureAlert"] = "false"

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

