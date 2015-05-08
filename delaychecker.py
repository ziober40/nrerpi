__author__ = 'Bartek'

from webservice import DarwinLdbSession


class CheckDelay(object):
    def __init__(self):
        self.darwin_sesh = DarwinLdbSession(wsdl="https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx",
                                            api_key="1696aa2c-a886-44d2-8826-dfae56d95d9f")

    def get_delayed_trains(self, station_name='KDB', rows=40):
        board = self.darwin_sesh.get_station_board(station_name, rows)
        delayed_trains = []
        for b in board.train_services:
            try:
                service = self.darwin_sesh.get_service_details(b.service_id)
                if str(service.ata) != "None" and str(service.ata) != "On time":
                    delayed_trains.push(str(b.destination_text) + " - " + str(service.ata) + " - " + str(service.sta))
            except:
                print('connection downtime')
                return delayed_trains
        return delayed_trains