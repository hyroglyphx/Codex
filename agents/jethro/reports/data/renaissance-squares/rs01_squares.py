#!/usr/bin/env python3
"""RS-01 reproducibility packet: Renaissance letter-square certificates.

Microset: SALOM + MILON + THIRAMA (French + German variant), Soyga as the
algorithmically anchored comparator.

What this script does (all from the constants below, no external input):
  1. Encodes the three witness squares + Soyga rule data.
  2. Enumerates coordinate orbits under G = {identity, transpose, half-turn,
     anti-diagonal reflection} and under transpose-only.
  3. Computes min-edit distances and majority reconstructions.
  4. Runs leave-one-cell-out masking with frequency-preserving and
     occupancy-preserving (permuted) controls.
  5. Verifies the Soyga recurrence against independently transcribed targets
     (SARTON ideal 10 rows + T1 opening, both from Reeds' paper) and runs
     boundary/seed sensitivity checks.
  6. Prints a JSON certificate + SHA-256 hashes of all inputs.

Evidence states: OBSERVED = letters as printed in the cited witness.
RECONSTRUCTED = letters supplied by orbit majority (never a witness reading).
PREDICTED = masking-test output. Nothing here is a historical-generation claim.

Run: python3 rs01_squares.py
"""
import hashlib, json, random
from collections import Counter

# ---------------------------------------------------------------- witnesses
# SALOM: Mathers, Abramelin Book III Ch. XIX No. 9 ("By a Maiden in general").
# Verified at sacred-texts.com/grim/abr/abr082.htm, 2026-10-13.
# German: Dehn/Guth, Book IV Ch. 19 No. 11 ("For peace in general") - same form.
SALOM = ["SALOM", "AREPO", "LEMEL", "OPERA", "MOLAS"]
# MILON: Mathers, Book III Ch. I No. 1. Rows from Mathers' notes (e),
# printed pp. 169-170 (sacred-texts abr047.htm). Complete double acrostic.
MILON = ["MILON", "IRAGO", "LAMAL", "OGARI", "NOLIM"]
# THIRAMA French line: Mathers, Book III Ch. I No. 2, notes (e).
THIRAMA_FR = ["THIRAMA", "HIGANAM", "IGOGANA", "RAGIGAR",
              "ANAGOGI", "MANAGIH", "AMARIHT"]
# THIRAMA German branch: same, except row 5 col 3 (0-indexed (4,2)) = O.
# Deduction: the orbit table gives German broken orbit {(2,4),(4,2)}: A:1, O:1;
# French has A at both; the lane records the variant in row 5, so O sits at (4,2).
THIRAMA_DE = ["THIRAMA", "HIGANAM", "IGOGANA", "RAGIGAR",
              "ANOGOGI", "MANAGIH", "AMARIHT"]
SQUARES = {"SALOM": SALOM, "MILON": MILON,
           "THIRAMA_FR": THIRAMA_FR, "THIRAMA_DE": THIRAMA_DE}

# ------------------------------------------------------------------- Soyga
# Reeds, "John Dee and the Magic Tables in the Book of Soyga" (1998).
ALPHA = "ABCDEFGHIKLMNOPQRSTUXYZ"  # 23 letters, no J, no V
F = {"A": 2, "B": 2, "C": 3, "D": 5, "E": 14, "F": 2, "G": 6, "H": 5,
     "I": 14, "K": 15, "L": 20, "M": 22, "N": 14, "O": 8, "P": 13, "Q": 20,
     "R": 11, "S": 8, "T": 8, "U": 15, "X": 15, "Y": 15, "Z": 2}
CODEWORDS = ["NISRAM", "ROELER", "IOMIOT", "ISIAPO", "ORRASE", "OSACUE",
             "XUAUIR", "RAOSAC", "RSADUA", "ATROGA", "SDUOLO", "ARICAA",
             "MARSIN", "RELEOR", "TOIMOI", "OPAISI", "ESARRO", "EUCASO",
             "RIUAUX", "CASOAR", "AUDASR", "AGORTA", "OLOUDS", "AACIRA",
             "OSRESO", "NIEBOA", "OIAIAE", "ITIABA", "ADAMIS", "REUELA",
             "UISEUA", "MERONF", "ILIOSU", "OYNIND", "IASULA", "MOYSES"]
# SARTON_IDEAL: first 10 rows as printed in Reeds' paper sec. 5.1.
# INDEPENDENTLY TRANSCRIBED from the paper (not produced by this implementation).
SARTON_IDEAL = [
    "SCFHNDIZBDIZBDIZBDIZBDIZBDIZBDIZBDIZ",
    "AEUZPRUPPRUPPRUPPRUPPRUPPRUPPRUPPRUP",
    "RQRLMQRCsbygxilmobygxilmobygxilmobyg".upper(),
    "TATTUHYSCE" + "NXNZNCRNNXNZNCRNNXNZNCRNNX",
    "OIKLRTGAETXndedhyedcquereDSFPNDHYEDC".upper(),
    "NZMKIKYQBXNDITMGETMBSETBGKKXGTMGETMB",
    "NOUBLGEGHCQALQIXULIQPSDGNAMUYLIXULIQ",
    "OYMANXUYZEGGRDOFYCMPEISPCDRHDQFZYCMP",
    "TGSIDCZABGNXISYXOLIFGPHUSMQESAHENRZR",
    "RSCMCFBCEXEMHZAZQHOOPEYMRZSNIPXUEHEH"]
# T1 opening: HELD-OUT check (not used in f recovery). From Reeds' paper.
T1_ROW1_PREFIX = "NDIZBDIZBDIZ"
T1_ROW2_PREFIX = "ISRL"

# ------------------------------------------------------------ orbit helpers
def orbits(n, group):
    """group: subset of {'I','T','R','A'} -> dict cell -> sorted orbit list."""
    def apply(op, r, c):
        if op == "I": return (r, c)
        if op == "T": return (c, r)
        if op == "R": return (n - 1 - r, n - 1 - c)
        if op == "A": return (n - 1 - c, n - 1 - r)
        raise ValueError(op)
    seen, out = set(), {}
    for r in range(n):
        for c in range(n):
            if (r, c) in seen:
                continue
            orb = sorted({apply(op, r, c) for op in group})
            for cell in orb:
                seen.add(cell)
                out[cell] = orb
    return out

FULL = ("I", "T", "R", "A")
TRANSPOSE_ONLY = ("I", "T")

def min_edit(grid, group):
    n = len(grid)
    orb = orbits(n, group)
    done, total, broken = set(), 0, []
    for cell, o in orb.items():
        key = tuple(o)
        if key in done:
            continue
        done.add(key)
        letters = [grid[r][c] for (r, c) in o]
        cnt = Counter(letters)
        maj, majn = cnt.most_common(1)[0]
        total += len(o) - majn
        if len(cnt) > 1:
            broken.append({"orbit": o, "letters": dict(cnt),
                           "majority": maj, "majority_count": majn})
    return total, broken

def leave_one_cell_out(grid, group):
    """Mask each cell in turn; predict from orbit-mates by majority.
    Returns (correct, wrong, undecidable, detail). Ties in the vote -> undecidable."""
    n = len(grid)
    orb = orbits(n, group)
    correct = wrong = undec = 0
    detail = []
    for r in range(n):
        for c in range(n):
            o = orb[(r, c)]
            mates = [(rr, cc) for (rr, cc) in o if (rr, cc) != (r, c)]
            if not mates:
                undec += 1
                detail.append({"cell": (r, c), "actual": grid[r][c], "outcome": "undecidable",
                               "reason": "orbit size 1 (no mates)"})
                continue
            votes = Counter(grid[rr][cc] for (rr, cc) in mates)
            top = votes.most_common(2)
            if len(top) > 1 and top[0][1] == top[1][1]:
                undec += 1
                detail.append({"cell": (r, c), "actual": grid[r][c], "outcome": "undecidable",
                               "reason": "tied vote", "votes": dict(votes)})
            elif top[0][0] == grid[r][c]:
                correct += 1
                detail.append({"cell": (r, c), "actual": grid[r][c], "outcome": "correct",
                               "predicted": top[0][0]})
            else:
                wrong += 1
                detail.append({"cell": (r, c), "actual": grid[r][c], "outcome": "wrong",
                               "predicted": top[0][0], "votes": dict(votes)})
    return correct, wrong, undec, detail

def frequency_control(grid):
    """Predict every cell by the square's most frequent letter (no symmetry)."""
    cnt = Counter("".join(grid))
    maj = cnt.most_common(1)[0][0]
    correct = sum(1 for row in grid for ch in row if ch == maj)
    return maj, correct, len(grid) * len(grid[0])

def permuted_control(grid, group, seeds=(1, 2, 3)):
    """Same letter multiset + same occupancy, randomly permuted: run the
    leave-one-cell-out symmetry prediction on the permuted grid."""
    n = len(grid)
    letters = list("".join(grid))
    totals = []
    for s in seeds:
        rng = random.Random(s)
        rng.shuffle(letters)
        perm = ["".join(letters[i * n:(i + 1) * n]) for i in range(n)]
        c, w, u, _ = leave_one_cell_out(perm, group)
        totals.append({"seed": s, "correct": c, "wrong": w, "undecidable": u})
    return totals

# --------------------------------------------------------------- Soyga gen
def v(ch):
    return ALPHA.index(ch) + 1

def l(n):
    return ALPHA[(n - 1) % 23]

def soyga_generate(code, f_table=None, reverse_col=True):
    f = f_table or F
    g = [[""] * 36 for _ in range(36)]
    # First column: code word, then its reversal, repeated.
    col = []
    while len(col) < 36:
        col.extend(list(code))
        if reverse_col:
            col.extend(list(code[::-1]))
        # if reverse_col is False the loop still terminates via code repeats
    for r in range(36):
        g[r][0] = col[r]
    # First row: X = P + f(P) mod 23.
    for c in range(1, 36):
        g[0][c] = l(v(g[0][c - 1]) + f[g[0][c - 1]])
    # Interior: X = N + f(W) mod 23.
    for r in range(1, 36):
        for c in range(1, 36):
            g[r][c] = l(v(g[r - 1][c]) + f[g[r][c - 1]])
    return ["".join(row) for row in g]

def anagram_pairs(words):
    """All anagram pairs among the 36 code words (first-column seeds)."""
    pairs = []
    for i in range(36):
        for j in range(i + 1, 36):
            if sorted(words[i]) == sorted(words[j]):
                pairs.append((i + 1, j + 1))
    return pairs

# -------------------------------------------------------------------- main
def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()

def main():
    cert = {"squares": {}, "soyga": {}, "hashes": {}}
    for name, grid in SQUARES.items():
        n = len(grid)
        full_d, full_broken = min_edit(grid, FULL)
        t_d, t_broken = min_edit(grid, TRANSPOSE_ONLY)
        c, w, u, detail = leave_one_cell_out(grid, FULL)
        maj, fcorr, tot = frequency_control(grid)
        perm = permuted_control(grid, FULL)
        cert["squares"][name] = {
            "n": n, "cells": grid,
            "min_edit_full": full_d, "broken_orbits_full": full_broken,
            "min_edit_transpose_only": t_d, "broken_orbits_transpose_only": t_broken,
            "leave_one_cell_out": {"correct": c, "wrong": w, "undecidable": u,
                                   "detail": detail},
            "frequency_control": {"most_frequent": maj, "correct": fcorr,
                                  "total": tot},
            "permuted_control": perm,
        }
        cert["hashes"][name] = sha("\n".join(grid))
    # Soyga
    tables = [soyga_generate(cw) for cw in CODEWORDS]
    sarton = soyga_generate("SARTON")
    sarton_match = sum(1 for i in range(10) if sarton[i] == SARTON_IDEAL[i])
    t1 = soyga_generate("NISRAM")
    t1_ok = t1[0].startswith(T1_ROW1_PREFIX) and t1[1].startswith(T1_ROW2_PREFIX)
    pairs = anagram_pairs(CODEWORDS)
    expected_pairs = [(i + 1, i + 13) for i in range(12)]
    # sensitivity: no-reversal first column; f=0 (no lookup)
    sarton_norev = soyga_generate("SARTON", reverse_col=False)
    norev_match = sum(1 for i in range(10) if sarton_norev[i] == SARTON_IDEAL[i])
    zero_f = {k: 0 for k in F}
    sarton_zerof = soyga_generate("SARTON", f_table=zero_f)
    zerof_match = sum(1 for i in range(10) if sarton_zerof[i] == SARTON_IDEAL[i])
    cert["soyga"] = {
        "tables_generated": 36, "cells_per_table": 1296,
        "total_cells": 36 * 1296,
        "sarton_ideal_rows_matched": sarton_match, "sarton_ideal_rows_total": 10,
        "t1_held_out_opening_ok": t1_ok,
        "t1_row1_prefix": T1_ROW1_PREFIX, "t1_row2_prefix": T1_ROW2_PREFIX,
        "anagram_pairs_found": pairs, "anagram_pairs_expected": expected_pairs,
        "anagram_pairs_exact": pairs == expected_pairs,
        "sensitivity_no_reversal_sarton_rows_matched": norev_match,
        "sensitivity_f_zero_sarton_rows_matched": zerof_match,
        "target_provenance": ("SARTON 10 rows + T1 opening independently transcribed "
                              "from Reeds 1998. All other tables are implementation "
                              "output from code words + recurrence, not independent targets."),
    }
    cert["hashes"]["soyga_f_table"] = sha(json.dumps(F, sort_keys=True))
    cert["hashes"]["soyga_codewords"] = sha("\n".join(CODEWORDS))
    cert["hashes"]["sarton_ideal"] = sha("\n".join(SARTON_IDEAL))
    print(json.dumps(cert, indent=1))
    return cert

if __name__ == "__main__":
    main()
