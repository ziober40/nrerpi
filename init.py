import time

__author__ = 'Bartek'

from webservice import DarwinLdbSession

darwin_sesh = DarwinLdbSession(wsdl="https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx",
                               api_key="yourkeyhere")


board = darwin_sesh.get_station_board('KDB', rows=40)

while 1:
    for b in board.train_services:
        service = darwin_sesh.get_service_details(b.service_id)
        delayed = ""
        if str(service.ata) != "None" and str(service.ata) != "On time":
                delayed = " DELAYED!!!"

        output = str(b.destination_text) + " - " + str(service.ata) + " - " + str(service.sta) + delayed
        print(output)
    time.sleep(2)
    print("---------------------")