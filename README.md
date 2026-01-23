# 🎼 The Art of Fugue: A Determinism Benchmark

**"Standard benchmarks play scales. We needed one that plays a symphony."**

This repository contains the validation suite used by [LuxiEdge](https://luxiedge.com) to prove **Cross-Platform Determinism** (Bit-Exactness) across heterogeneous hardware.

## The Concept

In High-Performance Computing (HPC), most benchmarks test isolated operations (e.g., `sin(x)` in a loop). This is like playing a single note on a piano. It is easy to get right.

A **Fugue** (specifically Bach’s *The Art of Fugue*) involves multiple complex voices weaving together simultaneously. If a player misses a single note, the harmonic structure collapses.

## The Test

`art_of_fugue.py` simulates a "polyphonic" mathematical workload. It does not test speed; it tests **Identity**.

It launches multiple "Voices" (threads) of conflicting mathematical intensity:
*   **Voice 1:** Trigonometric Identities
*   **Voice 2:** Logarithmic Decay
*   **Voice 3:** Discontinuous Transcendentals

## The Verification: Bit-Exact Identity

The benchmark captures the output of this chaotic mix into a single **SHA-256 Hash**.

*   **Goal:** The hash should be identical on a Raspberry Pi, an Apple M1, and an NVIDIA H100.
*   **Reality:** On most engines, these hashes drift due to scheduler improvisation and floating-point non-associativity.
*   **LuxiEdge:** Produces the exact same hash across all platforms.

When the hash matches across your edge device and your hyperscale cluster, you have truth.
