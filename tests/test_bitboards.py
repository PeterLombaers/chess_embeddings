from chess_embeddings import (
    BB_BLACK_PAWN_MOVES,
    BB_WHITE_PAWN_MOVES,
    BB_KNIGHT_MOVES,
    BB_BISHOP_MOVES,
    BB_ROOK_MOVES,
    BB_QUEEN_MOVES,
    BB_KING_MOVES,
    board_to_tensor,
)
import chess


def test_black_pawn_moves():
    print(BB_BLACK_PAWN_MOVES[0].indices)
    assert set(BB_BLACK_PAWN_MOVES[0].indices) == set()
    assert set(BB_BLACK_PAWN_MOVES[10].indices) == {1, 2, 3}
    assert set(BB_BLACK_PAWN_MOVES[17].indices) == {8, 9, 10}
    assert set(BB_BLACK_PAWN_MOVES[29].indices) == {20, 21, 22}
    assert set(BB_BLACK_PAWN_MOVES[39].indices) == {30, 31}
    assert set(BB_BLACK_PAWN_MOVES[53].indices) == {44, 45, 46, 37}
    assert set(BB_BLACK_PAWN_MOVES[63].indices) == set()


def test_white_pawn_moves():
    assert set(BB_WHITE_PAWN_MOVES[0].indices) == set()
    assert set(BB_WHITE_PAWN_MOVES[12].indices) == {19, 20, 21, 28}
    assert set(BB_WHITE_PAWN_MOVES[26].indices) == {33, 34, 35}
    assert set(BB_WHITE_PAWN_MOVES[43].indices) == {50, 51, 52}
    assert set(BB_WHITE_PAWN_MOVES[55].indices) == {62, 63}
    assert set(BB_WHITE_PAWN_MOVES[57].indices) == set()


def test_knight_moves():
    assert set(BB_KNIGHT_MOVES[1].indices) == {16, 18, 11}
    assert set(BB_KNIGHT_MOVES[12].indices) == {2, 18, 27, 29, 22, 6}
    assert set(BB_KNIGHT_MOVES[27].indices) == {10, 17, 33, 42, 44, 37, 21, 12}
    assert set(BB_KNIGHT_MOVES[56].indices) == {41, 50}
    assert set(BB_KNIGHT_MOVES[46].indices) == {29, 36, 52, 61, 63, 31}


def test_bishop_moves():
    assert set(BB_BISHOP_MOVES[1].indices) == {8, 10, 19, 28, 37, 46, 55}
    assert set(BB_BISHOP_MOVES[34].indices) == {
        16,
        25,
        48,
        41,
        61,
        52,
        43,
        27,
        20,
        13,
        6,
    }


def test_rook_moves():
    assert set(BB_ROOK_MOVES[9].indices) == {
        8,
        1,
        17,
        25,
        33,
        41,
        49,
        57,
        10,
        11,
        12,
        13,
        14,
        15,
    }


def test_queen_moves():
    assert set(BB_QUEEN_MOVES[53].indices) == {
        61,
        60,
        62,
        54,
        55,
        46,
        39,
        45,
        37,
        29,
        21,
        13,
        5,
        44,
        35,
        26,
        17,
        8,
        52,
        51,
        50,
        49,
        48,
    }


def test_king_moves():
    assert set(BB_KING_MOVES[3].indices) == {2, 10, 11, 12, 4}
    assert set(BB_KING_MOVES[30].indices) == {21, 22, 23, 31, 39, 38, 37, 29}


def test_board_to_tensor():
    board = chess.Board()
    assert board_to_tensor(board).tolist() == (
        # WHITE PAWNS
        [0 for _ in range(8)]
        + [1 for _ in range(8, 16)]
        + [0 for _ in range(16, 64)]
        # WHITE KNIGHTS
        + [0]
        + [1]
        + [0 for _ in range(2, 6)]
        + [1]
        + [0 for _ in range(7, 64)]
        # WHITE BISHOPS
        + [0 for _ in range(2)]
        + [1]
        + [0 for _ in range(3, 5)]
        + [1]
        + [0 for _ in range(6, 64)]
        # WHITE ROOKS
        + [1]
        + [0 for _ in range(1, 7)]
        + [1]
        + [0 for _ in range(8, 64)]
        # WHITE QUEEN
        + [0 for _ in range(3)]
        + [1]
        + [0 for _ in range(4, 64)]
        # WHITE KING
        + [0 for _ in range(4)]
        + [1]
        + [0 for _ in range(5, 64)]
        # BLACK PAWNS
        + [0 for _ in range(48)]
        + [1 for _ in range(48, 56)]
        + [0 for _ in range(56, 64)]
        # BLACK KNIGHTS
        + [0 for _ in range(57)]
        + [1]
        + [0 for _ in range(58, 62)]
        + [1]
        + [0]
        # BLACK BISHOPS
        + [0 for _ in range(58)]
        + [1]
        + [0 for _ in range(59, 61)]
        + [1]
        + [0 for _ in range(62, 64)]
        # BLACK ROOKS
        + [0 for _ in range(56)]
        + [1]
        + [0 for _ in range(57, 63)]
        + [1]
        # BLACK QUEEN
        + [0 for _ in range(59)]
        + [1]
        + [0 for _ in range(60, 64)]
        # BLACK KING
        + [0 for _ in range(60)]
        + [1]
        + [0 for _ in range(61, 64)]
    )
