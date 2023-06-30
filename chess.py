import chess.chess_class as ch
import user_ex.user_except as uex

if __name__ == '__main__':
    positions = [
        [(0, 3), (1, 7), (2, 0), (3, 4), (4, 6), (5, 1), (6, 5), (7, 2)],
        [(0, 4), (1, 7), (2, 0), (3, 4), (4, 6), (5, 1), (6, 5), (7, 2)],
        [(0, 4), (1, 7), (2, 0), (3, 4), (4, 6), (5, 1), (6, 5), (7, 2), (4, 5)],
    ]

    games = ch.ChessGame()

    for pos in positions:
        try:
            print(f"{pos} - {games.check_queen(pos)}")
        except Exception as e:
            print(e)
