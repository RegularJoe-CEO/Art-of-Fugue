import math
import hashlib
import time

# V2: Uses float.hex() for bit-exact verification
# This eliminates "string formatting" drift arguments.

def voice_trig(start, count):
    """Voice 1: Trigonometric Identities"""
    val = float(start)
    results = []
    for i in range(count):
        # sin^2 + cos^2 = 1.0 (theoretically)
        val = math.sin(val) * math.sin(val) + math.cos(val) * math.cos(val)
        results.append(val)
    return results

def voice_log(start, count):
    """Voice 2: Logarithmic Decay"""
    val = float(start)
    results = []
    for i in range(count):
        if val <= 0: val = 1.2345
        val = math.log(val + 1.0)
        results.append(val)
    return results

def run_score():
    hasher = hashlib.sha256()
    
    # 3 Voices, 100,000 steps each
    v1 = voice_trig(123.456, 100000)
    v2 = voice_log(789.012, 100000)
    
    # Hash the HEX representation to capture raw bits
    for a, b in zip(v1, v2):
        hasher.update(a.hex().encode('utf-8'))
        hasher.update(b.hex().encode('utf-8'))
        
    return hasher.hexdigest()

if __name__ == "__main__":
    print("Running Art of Fugue (V2: Hex Mode)...")
    start_time = time.time()
    result = run_score()
    print(f"Computed Hash: {result}")
    
    # Save the hash to the file immediately
    with open("ART_OF_FUGUE_M1.txt", "w") as f:
        f.write(result + "\n")
