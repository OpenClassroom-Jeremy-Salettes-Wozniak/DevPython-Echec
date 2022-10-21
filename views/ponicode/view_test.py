import view
import pytest

class Test_View_Header:
    
    @pytest.fixture()
    def view(self):
        return view.View()
    

    def test_header_1(self, view):
        view.header("Unknown error")

    def test_header_2(self, view):
        view.header("Ran out of iterations")

    def test_header_3(self, view):
        view.header("Unable to allocate address")

    def test_header_4(self, view):
        view.header("No response")

    def test_header_5(self, view):
        view.header("Error in retrieving email.")

    def test_header_6(self, view):
        view.header("")


class Test_View_Modifier_tournoi:
    
    @pytest.fixture()
    def view(self):
        return view.View()
    

    def test_modifier_tournoi_1(self, view):
        result = view.modifier_tournoi("http://www.example.com/route/123?foo=bar")

    def test_modifier_tournoi_2(self, view):
        result = view.modifier_tournoi("https://api.telegram.org/bot")

    def test_modifier_tournoi_3(self, view):
        result = view.modifier_tournoi("http://www.croplands.org/account/confirm?t=")

    def test_modifier_tournoi_4(self, view):
        result = view.modifier_tournoi("ponicode.com")

    def test_modifier_tournoi_5(self, view):
        result = view.modifier_tournoi("www.google.com")

    def test_modifier_tournoi_6(self, view):
        result = view.modifier_tournoi("")

