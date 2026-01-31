# Art of Fugue: Cross-Platform Floating-Point Determinism Test

## The Problem

When you run the same floating-point math on different hardware, you often get different results. This is not a bug. It is how IEEE 754 floating-point arithmetic works in practice.

Different CPUs (Intel, AMD, ARM) and GPUs (NVIDIA, AMD) use different:

- Instruction scheduling
- Fused multiply-add implementations
- Rounding behavior at microarchitecture level
- SIMD vectorization strategies

The result: identical code produces different outputs on different machines. For most applications, this does not matter. For auditable finance, deterministic simulation replay, and reproducible ML training, it breaks everything.

## What This Test Does

This script runs 200,000 floating-point operations (trigonometric and logarithmic) and hashes all results using their exact binary representation via Python float.hex() method. The output is a single SHA-256 hash.

If two machines produce the same hash, they computed bit-identical results. If the hashes differ, the floating-point results drifted.

## How to Run the Test

Requirements: Python 3.x (no external dependencies)

Step 1: Download the script

    curl -O https://raw.githubusercontent.com/RegularJoe-CEO/Art-of-Fugue/main/art_of_fugue.py

Step 2: Run it

    python3 art_of_fugue.py

## Expected Results

Run this on two different machines. For example, a Mac with an ARM CPU and a Linux server with an Intel CPU or NVIDIA GPU.

You will likely see different hashes:

| Platform | Hash |
|----------|------|
| macOS ARM64 (M1/M2/M3) | b02237875da129b90b6355d5918b38657e4bb2e697e413124c661acd0899eb19 |
| Linux x86_64 (NVIDIA GPU) | c060c5031b1bdb7b730ad6de7639ca87fd3257009a3e3580b71b4f116158c9d6 |

These hashes are different because Python math module calls the platform native C library (libm), which is implemented differently on each architecture.

## Why This Matters

In regulated industries, reproducibility is mandatory:

- Quantitative Finance: Regulatory audits require exact replay of historical calculations
- Defense Systems: Simulation results must be reproducible for certification
- Machine Learning: Training runs must be reproducible for debugging and validation

If your math engine cannot guarantee identical results across platforms, you cannot meet these requirements.

## How LuxiEdge Solves This

LuxiEdge is a deterministic computation engine that produces bit-exact results regardless of hardware. The same inputs always produce the same outputs, whether running on ARM, x86, CPU, or GPU.

Example using LuxiEdge with inputs [123.456, 789.012]:

| Platform | LuxiEdge Hash |
|----------|---------------|
| macOS ARM64 CPU | 781ae6b19ca58f36bfaaedde6e605f6fc8a766701d69175cbbcd39fe20efd610 |
| Linux x86_64 GPU | 781ae6b19ca58f36bfaaedde6e605f6fc8a766701d69175cbbcd39fe20efd610 |

Identical hashes. Bit-for-bit determinism across architectures.

Learn more at https://github.com/RegularJoe-CEO/LuxiDemo

## License

MIT

## Copyright

Copyright 2025 Eric Waller. All rights reserved.
