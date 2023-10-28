
from .handler_models import request_from_dict


def test_request_from_dict():
    d = {'oper': 'some-oper', 'body': {'some-prop': 1}}
    r = request_from_dict(d)
    assert 'some-oper' == r.oper
    assert {'some-prop': 1} == r.body
