from urlshort import create_app

def test_shorten(client):
    ''' testing if we can find the Shorten word on home page '''
    response = client.get('/')
    assert b'Shorten' in response.data