# -*- coding: utf-8 -*-
"""
Post model for db test
"""
from sqlalchemy import Column, BigInteger, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PostModel(Base):
    __tablename__ = 'posts'

    post_id = Column(BigInteger, primary_key=True)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
