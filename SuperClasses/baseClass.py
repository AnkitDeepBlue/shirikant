import pytest

@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("takeScreenShot")
class baseclass:
    pass