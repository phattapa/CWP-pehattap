"""checkmate.py - Rush00 ex00

ตรวจว่า King ('K') บนกระดานสี่เหลี่ยมจัตุรัสถูก check หรือไม่
หมาก: K (King), P (Pawn), B (Bishop), R (Rook), Q (Queen)
ตัวอักษรอื่นทั้งหมดถือเป็นช่องว่าง
"""

KING = 'K'
PAWN = 'P'
BISHOP = 'B'
ROOK = 'R'
QUEEN = 'Q'
PIECES = (KING, PAWN, BISHOP, ROOK, QUEEN)

DIAGONALS = ((-1, -1), (-1, 1), (1, -1), (1, 1))
STRAIGHTS = ((-1, 0), (1, 0), (0, -1), (0, 1))


def parse_board(board):
    """คืน list ของแถว หรือ None ถ้า input ไม่ถูกต้อง (undefined behavior)"""
    if not isinstance(board, str):
        return None
    if board.endswith('\n'):
        board = board[:-1]
    grid = board.split('\n')
    size = len(grid)
    if size == 0:
        return None
    for row in grid:
        if len(row) != size:
            return None
    return grid


def find_king(grid):
    """คืนตำแหน่ง (row, col) ของ King หรือ None ถ้าไม่มี / มีมากกว่า 1 ตัว"""
    king = None
    for r, row in enumerate(grid):
        for c, square in enumerate(row):
            if square == KING:
                if king is not None:
                    return None
                king = (r, c)
    return king


def first_piece(grid, king, direction):
    """ยิงรังสีจาก King ไปทางเดียว คืน (หมากตัวแรกที่เจอ, ระยะห่าง)"""
    size = len(grid)
    r, c = king
    dr, dc = direction
    distance = 1
    r += dr
    c += dc
    while 0 <= r < size and 0 <= c < size:
        square = grid[r][c]
        if square in PIECES:
            return square, distance
        r += dr
        c += dc
        distance += 1
    return None


def is_check(grid, king):
    for direction in DIAGONALS:
        found = first_piece(grid, king, direction)
        if found is None:
            continue
        piece, distance = found
        if piece == BISHOP or piece == QUEEN:
            return True
        # Pawn กินทแยงขึ้นบน -> ตัวที่อยู่ "ล่าง" ของ King ติดกัน 1 ช่อง
        if piece == PAWN and distance == 1 and direction[0] == 1:
            return True
    for direction in STRAIGHTS:
        found = first_piece(grid, king, direction)
        if found is None:
            continue
        piece, _ = found
        if piece == ROOK or piece == QUEEN:
            return True
    return False


def checkmate(board):
    grid = parse_board(board)
    if grid is None:
        return
    king = find_king(grid)
    if king is None:
        return
    if is_check(grid, king):
        print("Success")
    else:
        print("Fail")