from pytest  import fixture
from cdm.testing import get_context, get_installer

# returns a sample application
@fixture(scope="session")
def sample():
    context = get_context()


def test_simple_cql_schema():
    installer = get_installer("sample")
    import ipdb; ipdb.set_trace()
