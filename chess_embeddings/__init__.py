from textwrap import wrap

from chess import (
    BB_KNIGHT_ATTACKS,
    BB_KING_ATTACKS,
    BB_PAWN_ATTACKS,
    BB_DIAG_ATTACKS,
    BB_RANK_ATTACKS,
    BB_FILE_ATTACKS,
)


class BitBoard(int):
    def __str__(self) -> str:
        return "\n".join(
            [" ".join(wrap(line[::-1], 1)) for line in wrap("{:064b}".format(self), 8)]
        )

    def __repr__(self) -> str:
        return f"BitBoard({self:d})"

    def __add__(self, other: "BitBoard") -> "BitBoard":
        return BitBoard(self | other)

    @property
    def indices(self) -> list[int]:
        return [
            index
            for index, char in enumerate("{:064b}".format(self)[::-1])
            if char == "1"
        ]


_BB_BLACK_PAWN_ATTACKS = [
    BitBoard(bb) for bb in BB_PAWN_ATTACKS[0][:56] + [0 for _ in range(56, 64)]
]
_BB_BLACK_PAWN_SINGLE_MOVES = [
    BitBoard(bb)
    for bb in [0 for _ in range(8)]
    + [2 ** (i - 8) for i in range(8, 56)]
    + [0 for _ in range(56, 64)]
]
_BB_BLACK_PAWN_DOUBLE_MOVES = [
    BitBoard(bb)
    for bb in [0 for _ in range(48)]
    + [2 ** (i - 16) for i in range(48, 56)]
    + [0 for _ in range(56, 64)]
]
BB_BLACK_PAWN_MOVES = [
    single + double + attacks
    for (single, double, attacks) in zip(
        _BB_BLACK_PAWN_SINGLE_MOVES, _BB_BLACK_PAWN_DOUBLE_MOVES, _BB_BLACK_PAWN_ATTACKS
    )
]
_BB_WHITE_PAWN_ATTACKS = [
    BitBoard(bb) for bb in [0 for _ in range(8)] + BB_PAWN_ATTACKS[1][8:]
]
_BB_WHITE_PAWN_SINGLE_MOVES = [
    BitBoard(bb)
    for bb in [0 for _ in range(8)]
    + [2 ** (i + 8) for i in range(8, 56)]
    + [0 for _ in range(56, 64)]
]
_BB_WHITE_PAWN_DOUBLE_MOVES = [
    BitBoard(bb)
    for bb in [0 for _ in range(8)]
    + [2 ** (i + 16) for i in range(8, 16)]
    + [0 for _ in range(16, 64)]
]
BB_WHITE_PAWN_MOVES = [
    single + double + attacks
    for (single, double, attacks) in zip(
        _BB_WHITE_PAWN_SINGLE_MOVES, _BB_WHITE_PAWN_DOUBLE_MOVES, _BB_WHITE_PAWN_ATTACKS
    )
]

BB_KNIGHT_MOVES = [BitBoard(bb) for bb in BB_KNIGHT_ATTACKS]
BB_KING_MOVES = [BitBoard(bb) for bb in BB_KING_ATTACKS]
BB_BISHOP_MOVES = [
    BitBoard(bb) for bb in [list(BB_DIAG_ATTACKS[i].values())[0] for i in range(64)]
]
_BB_RANK_MOVES = [
    BitBoard(bb) for bb in [list(BB_RANK_ATTACKS[i].values())[0] for i in range(64)]
]
_BB_FILE_MOVES = [
    BitBoard(bb) for bb in [list(BB_FILE_ATTACKS[i].values())[0] for i in range(64)]
]
BB_ROOK_MOVES = [bbr + bbf for (bbr, bbf) in zip(_BB_RANK_MOVES, _BB_FILE_MOVES)]
BB_QUEEN_MOVES = [bbb + bbr for (bbb, bbr) in zip(BB_BISHOP_MOVES, BB_ROOK_MOVES)]
