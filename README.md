Mancala capstone project files

General structure:
    For each game, we have a game_driver object which has two players and a game_state
    can have multiple player strategies, and the game driver will receive whose
        turn it is from state and query that player appropriately
    Game driver will understand when the game is over and react accordingly
        (for now will just print to console)
    Game state will always know whose turn it is (ex if someone has no legal
        moves, repeat moves, etc)