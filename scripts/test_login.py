import allure
import pytest


class TestLogin:

    @allure.step(title='测试1')
    def test_login001(self):
		assert 0

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_login002(self):
		assert 1
