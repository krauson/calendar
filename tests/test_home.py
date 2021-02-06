<<<<<<< HEAD
=======
from fastapi import status


>>>>>>> 7f38da98a7122787cdd981344ce2f6a116f96e10
class TestHome:
    URL = "/"

    def test_get_page(self, client):
        resp = client.get(self.URL)
<<<<<<< HEAD
        assert resp.status_code == 200
=======
        assert resp.status_code == status.HTTP_200_OK
>>>>>>> 7f38da98a7122787cdd981344ce2f6a116f96e10
