
Inductive Nat : Type :=
| Zero
| S (n: Nat).

Inductive Int : Type :=
| minus (n: Nat)
| just (n: Nat).

Inductive Rati : Type :=
| div (z1: Int) (z2: Int).
