from app import app # Flask instance of the API
from unittest import mock


#Bad Request Test Case with no parameters
def test_rates_to_expect_BAD_REQUEST():
    response = app.test_client().get('/rates', query_string=dict())
    assert response.status_code == 400


#Bad Request Test Case with invcalid date range
def test_rates_with_invalid_dates():
    response = app.test_client().get('/rates', query_string=dict(date_from='2016-11-01', date_to='2016-01-07',origin='CNSGH',destination='EETLL'))
    assert response.status_code == 400
