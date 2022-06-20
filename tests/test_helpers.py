from angelou.helpers import fibo


class TestHelpers(object):

    def test_fibo(self):
        assert (fibo(10) == 55)
