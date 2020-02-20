# -*- coding: utf-8 -*-
"""
Factory for posts, using factory boy
"""

import factory

from data_base.model.post import PostModel


# pylint: disable=missing-class-docstring
class PostFactory(factory.alchemy.SQLAlchemyModelFactory):
    post_id = factory.Sequence(lambda n: n)
    title = factory.Faker('word')
    body = factory.Faker('sentence')

    class Meta:
        model = PostModel
        sqlalchemy_session_persistence = 'commit'
