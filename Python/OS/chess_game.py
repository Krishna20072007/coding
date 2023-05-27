import chess
import chess.svg

def main():
    board = chess.Board()

    while not board.is_game_over():
        print(board)
        print("\n")
        move = input("Enter your move (in algebraic notation): ")
        
        try:
            chess.Move.from_uci(move)  # Validate the move format
            board.push_san(move)
        except ValueError:
            print("Invalid move! Try again.")

    print("Game over.")
    print("Result: " + board.result())
    
if __name__ == "__main__":
    main()
