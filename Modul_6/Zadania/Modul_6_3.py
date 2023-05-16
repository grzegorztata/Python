import csv
from sqlalchemy import ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
clean_station_file = "KursPython/Modul_6/Zadania/Files/clean_stations.csv"
clean_measure_file = "KursPython/Modul_6/Zadania/Files/clean_measure.csv"

engine = create_engine('sqlite:///Zadanie_6_3.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class CleanStation(Base):
    __tablename__ = 'clean_stations'
    id = Column(Integer, primary_key=True)
    station = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    elevation = Column(String)
    name = Column(String)
    country = Column(String)
    state = Column(String)
    
    @classmethod
    def add_clean_stations(cls, filename):
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                station = CleanStation(
                    station=row['station'],
                    latitude=row['latitude'],
                    longitude=row['longitude'],
                    elevation=row['elevation'],
                    name=row['name'],
                    country=row['country'],
                    state=row['state']
                )
                session.add(station)
        session.commit()
    
class CleanMeasure(Base):
    __tablename__ = 'clean_measure'
    id = Column(Integer, primary_key=True)
    station = Column(String, ForeignKey('clean_stations.station'))
    date = Column(String)
    precip = Column(String)
    tobs = Column(String)
    
    @classmethod
    def add_clean_measure(cls, filename):
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                measure = CleanMeasure(
                    station=row['station'],
                    date=row['date'],
                    precip=row['precip'],
                    tobs=row['tobs']
                )
                session.add(measure)
        session.commit()
    
    station_data = relationship("CleanStation", backref="measurements")

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    CleanStation.add_clean_stations(clean_station_file)
    CleanMeasure.add_clean_measure(clean_measure_file)