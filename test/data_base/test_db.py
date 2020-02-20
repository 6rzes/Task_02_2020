from data_base.factories.post_factory import PostFactory, PostModel
from data_base.model.post import PostModel
from data_base.fixtures.session import connection, session


def test_create_posts(session):
    __create_batch()
    db_rows_count = len(session.query(PostModel).all())
    assert 10 == db_rows_count


def test_delete_last_post(session):
    __create_batch()
    db_rows_count_before_del = len(session.query(PostModel).all())
    session.query(PostModel).filter(PostModel.post_id == db_rows_count_before_del).delete()
    db_rows_count_after_del = len(session.query(PostModel).all())
    assert db_rows_count_before_del - 1, db_rows_count_after_del


def test_select_post_by_id(session):
    __create_batch()
    first_post_id = session.query(PostModel).all()[0].post_id
    for post_id in [first_post_id]:
        assert session.query(PostModel).filter_by(post_id=post_id).one()


def test_update_first_post(session):
    __create_batch()
    first_post = session.query(PostModel).with_for_update().first()
    first_post.title = "new title"
    first_post.body = "new body"
    session.flush()
    first_post_modified = session.query(PostModel).with_for_update().first()
    assert first_post_modified.title == first_post.title
    assert first_post_modified.body == first_post.body


def __create_batch():
    expected_user_count = 10
    PostFactory.create_batch(expected_user_count)