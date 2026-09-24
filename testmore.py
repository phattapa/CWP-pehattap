import io
import sys
from checkmate import checkmate


def run(board):
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        checkmate(board)
    except Exception as e:
        sys.stdout = old
        return "CRASH: %r" % (e,)
    sys.stdout = old
    return buf.getvalue().strip() or "(nothing)"


TESTS = [
    ("subject ex1 pawn", "R...\n.K..\n..P.\n....", "Success"),
    ("subject ex2 empty", "..\n.K", "Fail"),
    ("rook same row", "....\nR..K\n....\n....", "Success"),
    ("rook same col", "..R.\n....\n..K.\n....", "Success"),
    ("rook blocked by B", "R...\nB...\nK...\n....", "Fail"),
    ("N is empty square", "R...\nN...\nK...\n....", "Success"),
    ("bishop diag", "B...\n....\n..K.\n....", "Success"),
    ("bishop blocked", "B...\n.P..\n..K.\n....", "Fail"),
    ("bishop not on line", ".B..\n....\n..K.\n....", "Fail"),
    ("queen diag hit", "...Q\n....\n.K..\n....", "Success"),
    ("queen diag miss", "..Q.\n....\n.K..\n....", "Fail"),
    ("queen straight", "Q...\n....\nK...\n....", "Success"),
    ("queen behind pawn blocked", "Q...\nP...\nK...\n....", "Fail"),
    ("pawn below-left", "....\n.K..\nP...\n....", "Success"),
    ("pawn below-right", "....\n.K..\n..P.\n....", "Success"),
    ("pawn above (no check)", "....\n.P..\n..K.\n....", "Fail"),
    ("pawn same col", "....\n.P..\n.K..\n....", "Fail"),
    ("pawn distance 2", "....\nP...\n....\n..K.", "Fail"),
    ("pawn hits corner king", "K...\n.P..\n....\n....", "Success"),
    ("king corner pawn", "...K\n..P.\n....\n....", "Success"),
    ("1x1 king", "K", "Fail"),
    ("2x2 queen", "Q.\n.K", "Success"),
    ("8x8 nothing", "\n".join(["........"] * 7 + ["...K...."]), "Fail"),
    ("8x8 rook blocked", "R.......\n........\n........\nP.......\n"
                         "........\nK.......\n........\n........", "Fail"),
    ("8x8 rook open", "R.......\n........\n........\n........\n"
                      "........\nK.......\n........\n........", "Success"),
    ("not square", "....\n.K..", "(nothing)"),
    ("ragged rows", "....\n.K.\n....\n....", "(nothing)"),
    ("no king", "....\n....\n....\n....", "(nothing)"),
    ("two kings", "K...\n....\n..K.\n....", "(nothing)"),
    ("empty string", "", "(nothing)"),
    ("None", None, "(nothing)"),
    ("int", 42, "(nothing)"),
    ("list", ["....", ".K.."], "(nothing)"),
    ("trailing newline", "R...\n.K..\n..P.\n....\n", "Success"),
    ("junk chars empty", "abcd\nefKg\nhijk\nlmno", "Fail"),
    ("lowercase r not rook", "r...\nK...\n....\n....", "Fail"),
]

fails = 0
for name, board, expected in TESTS:
    got = run(board)
    ok = got == expected
    if not ok:
        fails += 1
    print("%-4s %-28s expected=%-10s got=%s"
          % ("OK" if ok else "KO", name, expected, got))
print("\n%d/%d passed" % (len(TESTS) - fails, len(TESTS)))