import players
import pytest

class Test_Player_Player_load:
    
    @pytest.fixture()
    def player(self):
        return players.Player()
    

    def test_player_load_1(self, player):
        result = player.player_load("a85a8e6b-348b-4011-a1ec-1e78e9620782")

    def test_player_load_2(self, player):
        result = player.player_load("7289708e-b17a-477c-8a77-9ab575c4b4d8")

    def test_player_load_3(self, player):
        result = player.player_load("03ea49f8-1d96-4cd0-b279-0684e3eec3a9")

    def test_player_load_4(self, player):
        result = player.player_load("")

