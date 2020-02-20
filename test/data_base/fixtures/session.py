# -*- coding: utf-8 -*-
"""
Fixtures for db test
"""
import os
import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data_base.factories.post_factory import PostFactory

engine = create_engine(os.getenv("DATABASE_URL"))
Session = sessionmaker()


@pytest.fixture(scope='function')
def session(connection):
    transaction = connection.begin()
    session = Session(bind=connection)
    PostFactory._meta.sqlalchemy_session = session
    yield session
    session.close()
    transaction.rollback()


@pytest.fixture(scope='module')
def connection():
    connection = engine.connect()
    yield connection
    connection.close()
