# SIV-ES-004 — A 30/48 Residual-Class Chamber Cover with Fixed m=7
**Timeline branch:** Diophantine Certificate Geometry; derived from audited THM-ES-001 and COR-ES-002/003.
**Date:** 2026-11-22.
**Status:** Symbolically proved infinite-family coverage theorem; does NOT prove global Erdős–Straus. Coverage means residue classes modulo 840, not 30 arbitrary numerical samples.

## Residual domain
Scaling by known solutions at 2,3,5,7 handles gcd(n,210)>1. COR-ES-002 handles n≡3 (mod4). COR-ES-003 handles n≡5 (mod8). Therefore only gcd(n,210)=1 and n≡1 (mod8) remain. This consists of φ(210)=48 classes mod840.

## Fixed-gate theorem
For any n≥2 with gcd(n,210)=1 and n≡1 (mod8), choose x=(n+7)/4 (an even integer). Then m=4x−n=7, q=nx, gcd(7,q)=1 (because 7∤n and x≡n/4 mod7), so μ=7 and ν=q=nx.
Modulo7, ν≡n²/4≡2n²∈{1,2,4}, since nonzero squares mod7 are {1,2,4}.
Let
D_3={3,6,12}, D_5={5,10,20}.
The negatives of D_3 mod7 are {4,1,2}, each exactly once; likewise negatives of D_5 mod7 are {2,4,1}. Hence for every ν mod7 in {1,2,4}, there is a unique d in each D_t with d≡−ν (mod7).

If 3|x, choose d from D_3. Because n is odd and x even, ν=nx is divisible by6, so d∈{3,6,12} divides ν² (indeed 36|ν²). Similarly if 5|x, ν divisible by10, and d∈{5,10,20} divides ν² (100|ν²). In both cases ν=nx≥17x for all qualifying n (the first qualifying n is ≥17), so 7x−ν=(7−n)x≤0 and lower chamber bound is 1. Also d≤20≤ν for the eligible n (for the 3-family n≥17,x≥6, ν≥102; for the 5-family n≥33,x≥10, ν≥330). Thus d∈C_n(x).
Decode e=ν²/d, y=(d+ν)/7, z=(e+ν)/7. THM-ES-001 proves the resulting ordered integer solution.

## Count of covered residual classes modulo 840
For residual n≡1 (mod8), x=(n+7)/4 is even.
3|x iff n≡17 (mod24). Within the 48 residual classes mod840, this selects 24 classes (one of the two allowed nonzero residues mod3, all four nonzero mod5 and all six nonzero mod7).
5|x iff n≡33 (mod40). This selects 12 classes (one of the four nonzero residues mod5, both nonzero mod3, all six nonzero mod7).
Their intersection selects 6 classes. Inclusion-exclusion gives 24+12−6=30 of 48.
These congruence conditions and d selectors are periodic mod840, because 840 is divisible by 24,40,7 and x(n+840)=x(n)+210; divisibility by 3 and 5 and ν mod7 persist. Therefore the proof applies to every positive member of each selected residue class.

## Exact covered classes
[17,41,73,89,113,137,193,209,233,257,281,313,353,377,401,433,449,473,521,569,593,617,641,673,689,713,737,761,793,809]

## Exact remaining classes after this m=7 selector
[1,97,121,169,241,289,337,361,409,457,481,529,577,601,649,697,769,817]
The residue r=1 means positive n≡1 mod840 with n≥2 (first n=841); n=1 is outside the conjecture domain.
These are **uncovered by the present m=7, d∈D_3∪D_5 construction**, not asserted to be insoluble or unhandled by other known formulas.

## Example
n=17: x=6, ν=102≡4 mod7; d=3∈D_3 and d≡−4 mod7. e=102²/3=3468; y=(3+102)/7=15, z=(3468+102)/7=510; 4/17=1/6+1/15+1/510.

## Next task
For the 18 explicit residual classes, search other bounded m≡3 mod4 (11,15,19,23,27,...) and small divisor selector sets, while retaining symbolic chamber-membership proofs for every n in each class. Report overlap with existing classical congruence identities separately.
