# COR-ES-005 — A Constant-Divisor Section on n ≡ 97 (mod 840)
**Date:** 2026-11-22
**Lineage:** THM-ES-001 → SIV-ES-004 → COR-ES-005
**Status:** exact proved infinite family, extending this construction's residual coverage from 30 to 31 of 48 classes. No claim of novel global Erdős–Straus resolution.

For every integer t≥0, set n=840t+97, x=210t+28=(n+15)/4, and d=14. Then m=4x−n=15, q=nx. Modulo 15, n≡7, x≡13, so nx≡7·13≡1 mod15 and gcd(15,nx)=1. Hence primitive μ=15 and ν=nx, and d≡14≡−ν mod15. Since x=14(15t+2), d=14 divides ν². Further, n≥97>15 ensures μx−ν=(15−n)x<0, so the chamber lower bound is 1; d≤ν trivially. Thus d∈C_n(x) for all t≥0. THM-ES-001 reconstructs y=(ν+14)/15, z=(ν²/14+ν)/15, with x≤y≤z and 4/n=1/x+1/y+1/z.

At t=0, n=97, x=28, ν=2716, e=526904, y=182, z=35308. Exact fractions give 4/97=1/28+1/182+1/35308.

**Search scope:** Exhaustive finite candidate scan of fixed d≤999 and m≡3 mod4, 7≤m<200, over 12 successive n in each of the 18 residual classes. It yielded this candidate for class 97 and no other uniform fixed-d candidate under these limits. This finite scan is NOT a nonexistence proof for the remaining 17 classes, nor does it exclude periodic d selectors or larger m,d. The symbolic proof above, not the scan, establishes the class 97 section.

**Remaining residual classes modulo 840 for the present proven construction:** 1,121,169,241,289,337,361,409,457,481,529,577,601,649,697,769,817.

**Next:** Search periodic finite-state selectors rather than fixed d; isolate moduli of gcd(m,nx), and seek an exact symbolic rule covering multiple residual classes at once. Compare all results against classical Egyptian fraction congruence coverage.
