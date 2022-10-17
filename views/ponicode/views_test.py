import views
import pytest

class Test_View_Round:
    
    @pytest.fixture()
    def view(self):
        return views.View()
    

    def test_round_1(self, view):
        result = view.round(100, "user@host:300")

    def test_round_2(self, view):
        result = view.round(1, "user1+user2@mycompany.com")

    def test_round_3(self, view):
        result = view.round(0, "something.example.com")

    def test_round_4(self, view):
        result = view.round(0, "email@Google.com")

    def test_round_5(self, view):
        result = view.round(100, "email@Google.com")

    def test_round_6(self, view):
        result = view.round(0, "")

