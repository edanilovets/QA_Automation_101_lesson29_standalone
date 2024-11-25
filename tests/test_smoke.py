import pytest


class TestSmoke:

    @pytest.mark.smoke
    def test_smoke(self):
        assert True
