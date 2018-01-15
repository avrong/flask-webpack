import pytest

from flask_webpack_current.tests.test_app.app import create_app, index


@pytest.yield_fixture(scope='session')
def app():
    """
    Setup our flask test app, this only gets executed once.

    :return: Flask app
    """
    params = {
        'DEBUG': False,
        'TESTING': True,
        'SERVER_NAME': 'localhost:5000',
        'WEBPACK_MANIFEST_PATH': 'build/public/manifest.json'
    }

    _app = create_app(settings_override=params)

    ctx = _app.app_context()
    ctx.push()

    _app.add_url_rule('/', 'index', index)

    yield _app

    ctx.pop()


@pytest.fixture(scope='function')
def client(app):
    """
    Setup an app client, this gets executed for each test function.

    :param app: Pytest fixture
    :return: Flask app client
    """
    return app.test_client()
