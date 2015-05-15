__author__ = 'Bartek'

import datetime
from pymongo import MongoClient
from webservice import DarwinLdbSession
from logger import Logger


class CheckDelay(object):
    def __init__(self):
        self.darwin_sesh = DarwinLdbSession(wsdl="https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx",
                                            api_key="1696aa2c-a886-44d2-8826-dfae56d95d9f")
        self.logger = Logger()
        client = MongoClient()
        self.db = client.nrerpi
        self.collection = self.db.TrainServices

    def get_delayed_trains(self, station_name='KDB', rows=4):
        board = self.darwin_sesh.get_station_board(station_name, rows)
        delayed_trains = []
        for b in board.train_services:
            service = self.darwin_sesh.get_service_details(b.service_id)
            try:
                service = self.darwin_sesh.get_service_details(b.service_id)
                if str(service.ata) != "None" and str(service.ata) != "On time":
                    delayed_trains.append(b.destination_text)
                self.save_in_database(b, service)
                self.logger.log(str(b.destination_text) + " -  ata:" + str(service.ata) + " - atd:" + str(
                    service.atd) + " - crs:" + str(service.crs) + " - disruption reason:" + str(
                    service.disruption_reason) + " - eta:" + str(service.eta) + " - etd:" + str(
                    service.etd) + " - is cancelled:" + str(service.is_cancelled) + " - overdue message:" + str(
                    service.overdue_message) + " - platform:" + str(service.platform))
            except BaseException as e:
                self.logger.log('connection downtime or different error' + str(e))
                return delayed_trains
        return delayed_trains

    def save_in_database(self, service, details):

        train_information = {
            "InputDate": datetime.datetime.utcnow(),
            "EstimatedTimeArrival": str(service.eta),
            "EstimatedTimeDeparture": str(service.etd),
            "Destination": str(service.destination_text),
            "Origin": str(service.origin_text),
            "Platform": str(service.platform),
            "ScheduledTimeArrival": str(service.sta),
            "ScheduledTimeDeparture": str(service.std),

        }
        self.collection.insert(train_information)