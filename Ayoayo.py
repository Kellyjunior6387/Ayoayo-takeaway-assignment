class Player:
    """Class to implement a player of the game"""
    def __init__(self, name: str, player_num: int) -> None:
        """
        Args:
            name: Player's name
            player_num: player 1 for 1, and 2 for 2
        """
        self.__name = name
        self.__player_num = player_num

    @property
    def get_name(self) -> str:
        return self.__name
    
    @property
    def get_player_numm(self) -> str:
        return self.__player_num
    

class Ayoayo:
    """The main Ayoayo class to implement the game"""
    def __init__(self) -> None:
        self.__player1: Player | None = None
        self.__player2: Player | None = None
        self.__board: dict[str, list[int] | int] = {
            'player1': [4] * 6,
            'player2': [4] * 6,
            'store1': 0,
            'store2': 0
        }
        self.__game_ended: bool = False
    def createPlayer(self, name) -> Player | None:
        """Creates a player and assigns them to the game
        Args:
            name: The player's name
        Return
            Player object or None if he already exista
        """
        if not self.__player1:
            self.__player1 = Player(name, 1)
            return self.__player1
        elif not self.__player2:
            self.__player2 = Player(name, 2)
            return self.__player2
        return None
    def printBoard(self) -> None:
        """Prints the board"""
        print('player1:')
        print(f"store: {self.__board['store1']}")
        print(self.__board['player1'])
        print('player2')
        print(f"store: {self.__board['store2']}")
        print(self.__board['player2'])
    def returnWinner(self) -> str:
        """
        Function to determine if game is ended
        and determine winner
        Returns:
            A message indicating status of the game
        """
        if not self.__game_ended:
            return "Game has not ended"
        
        if self.__board['store1'] > self.__board['store2']:
            return f"Winner is player 1: {self.__player1.name}"
        elif self.__board['store2'] > self.__board['store1']:
            return f"Winner is player 2: {self.__player2.name}"
        return "Its a tie"
    def playGame():
        pass


if __name__ == "__main__":
    ayoayo = Ayoayo()
    ayoayo.createPlayer('kelvin')
    ayoayo.createPlayer('brian')
    ayoayo.printBoard()