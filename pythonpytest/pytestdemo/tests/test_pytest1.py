import pytest

from pytestdemo.common.common import CommonUtil
@pytest.fixture(scope='function')
def exe_database_sql():
    print('执行sql查询')
    yield
    print("\nyoure done")

class TestApi(CommonUtil):

    # workage = 10
    # @pytest.mark.skip(reason='无理由')
    def test_01_qa(self):
        print('牛牛又比比')
    # @pytest.mark.skipif(workage<12,reason='工龄太低')
    def test_02_sahzi(self):
        print('天下无双')


    def test_03_sakhzi(self):
        print('天下无yi')
        # raise Exception("天下无敌")
    def test_04_saihzi(self,exe_database_sql):
        print('天下weigong')
