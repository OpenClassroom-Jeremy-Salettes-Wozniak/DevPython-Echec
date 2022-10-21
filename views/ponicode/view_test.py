import view
import pytest

class Test_View_Header:
    
    @pytest.fixture()
    def view(self):
        return view.View()
    

    def test_header_1(self, view):
        result = view.header("Unknown error")

    def test_header_2(self, view):
        result = view.header("Ran out of iterations")

    def test_header_3(self, view):
        result = view.header("Unable to allocate address")

    def test_header_4(self, view):
        result = view.header("No response")

    def test_header_5(self, view):
        result = view.header("Error in retrieving email.")

    def test_header_6(self, view):
        result = view.header("")

