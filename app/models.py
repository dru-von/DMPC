from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///mpc.db')
Base = declarative_base()


class Config(Base):
    __tablename__ = 'config'
    id = Column(primary_key=True)
    horizon_len = Column(Integer, default=50)
    unit_time = Column(String, default='minute')


class CV(Base):
    __tablename__ = 'control_var'
    id = Column(primary_key=True)
    name = Column(String, default='CVx')
    noise_filter = Column(Float, default=0.75)


class MV(Base):
    __tablename__ = 'manip_var'
    id = Column(primary_key=True)
    name = Column(String, default='MVx')




