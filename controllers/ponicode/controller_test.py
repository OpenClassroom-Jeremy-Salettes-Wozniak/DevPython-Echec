import controller
import pytest

class Test_Controller_All_table_tournaments:
    
    @pytest.fixture()
    def controller(self):
        return controller.Controller()
    

    def test_all_table_tournaments_1(self, controller):
        controller.all_table_tournaments({ "tournaments": True })

    def test_all_table_tournaments_2(self, controller):
        controller.all_table_tournaments({ "tournaments": False })

    def test_all_table_tournaments_3(self, controller):
        controller.all_table_tournaments(None)


class Test_Controller_Rapport_tournoi:
    
    @pytest.fixture()
    def controller(self):
        return controller.Controller()
    

    def test_rapport_tournoi_1(self, controller):
        result = controller.rapport_tournoi()

