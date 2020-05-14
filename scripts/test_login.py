import allure
import pytest


class TestLogin:

    @allure.step(title='测试1')
    def test_login001(self):
        print('点击放大镜')
        print('输入文字')
        print('点击返回')

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_login002(self):
        print('点击放大镜')
        print('点击返回')
