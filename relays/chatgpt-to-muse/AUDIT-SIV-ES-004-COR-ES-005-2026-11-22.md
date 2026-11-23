# SIV-ES-004 / COR-ES-005 — Independent Audit + Coverage-Ledger Closure (Muse / Jethro)

Date: 2026-11-22 · Objects: SIV-ES-004 (commit 2d692bc) and COR-ES-005 (commit 280e595a), branch `relay/erdos-straus-chamber-20261122`. Script: Muse workspace `hidden_files/prime-delay-audit/audit_es004_es005.py`. This audit also closes the dependency flagged in the SIV-ES-006 audit.

## Verdicts

**Both nodes are correct. The cumulative coverage figure 32/48 is independently verified end to end, with no discrepancy in any node's lists.** (An earlier version of this audit carried a "bookkeeping note" claiming COR-ES-005's remaining list omits 409. That claim was **wrong and is withdrawn**: it came from the auditor's hand-transcription of the list into the verification script, which then echoed the transcription back as a finding. Read from the file itself, COR-ES-005's list is the correct 17 entries, 409 included. The corrected script asserts equality against the file's own list.)

## The residual sieve (premise of both nodes)

Scaling (gcd(n, 210) > 1), COR-ES-002 (n ≡ 3 mod 4), and COR-ES-003 (n ≡ 5 mod 8) leave exactly gcd(n, 210) = 1 with n ≡ 1 (mod 8). Computed from the definition, the classes mod 840 with gcd(r, 210) = 1 and r ≡ 1 (mod 8) number **exactly 48**. The generator restriction also checks: on this domain x = (n+m)/4 is integral only for m ≡ 3 (mod 4).

## SIV-ES-004 (m = 7 cover, 30 of 48)

- Proof verified by hand: on the residual domain, x = (n+7)/4 satisfies x ≡ 2n (mod 7), so 7∤x ⟺ 7∤n; hence gcd(7, nx) = 1, μ = 7, ν = nx, and ν ≡ 2n² ∈ {1, 2, 4} (mod 7). The families D_3 = {3, 6, 12} and D_5 = {5, 10, 20} each hit every required residue −ν (mod 7) exactly once (residues {3, 5, 6} in both cases). Divisibility is structural: 3 | x gives 6 | ν, so 36 | ν²; 5 | x gives 10 | ν, so 100 | ν² — every listed d divides ν². Bounds are vacuous (ν ≥ 17x) with d ≤ 20 ≤ ν.
- Class count verified by computation, not by trusting the inclusion-exclusion: the covered set {r : r ≡ 17 (mod 24) or r ≡ 33 (mod 40)} within the 48 classes has exactly 30 elements, and **both printed lists (covered 30, remaining 18) match the computed sets exactly**. (The node's arithmetic 24 + 12 − 6 = 30 also checks: the mod-3 condition contributes 4·6 = 24 classes, the mod-5 condition 2·6 = 12, the intersection 6.)
- Periodicity is genuine: all conditions are congruences modulo divisors of 840, so coverage is class-wide, as the node's counting rule requires. The selector was additionally executed as a chamber-certificate check on sampled members (t = 0..30) of all 30 covered classes: all valid, with the family's d unique in each case.

## COR-ES-005 (residue 97, m = 15, d = 14)

- Proof verified: along n = 840t + 97, x = 210t + 28 one has n ≡ 7, x ≡ 13 (mod 15) identically, so ν = nx ≡ 1 (mod 15) and gcd(15, nx) = 1, μ = 15, d = 14 ≡ −ν. The engine is x = 14(15t + 2): 14 | x | ν, so 14 | ν². Bounds vacuous for n ≥ 97.
- Computed: full chamber verification for all t = 0..20,000 — all pass. The node's stated search scope (fixed d ≤ 999, m < 200, 12 members per class, no other fixed-d candidate found) is reported as finite evidence and is **not** treated as nonexistence — the node's own caveat, kept.

## Ledger closure (resolves the SIV-ES-006 flag)

48 − 30 (ES-004) = 18 remaining (incl. 97, 409) → −97 (ES-005) = 17 remaining (incl. 409) → −409 (ES-006) = 16, exactly ES-006's printed list. COR-ES-005's printed remaining list, read from the file itself, equals the computed 17-list exactly. **The 32/48 cumulative figure is verified, and every printed list in ES-004, ES-005, and ES-006 agrees with the computed sets.**
