# STUDENT: PENA | SEED: 14 | ARTIST: SILENT SANCTUARY
SURNAME = "PENA"
SEED = 14
ARTIST = "SILENT SANCTUARY"

raw_stream = [21, 24, 27, -999, 33, 36, 39, 42, 45, 48]
print(f"--- EXERCISE 3 PIPELINE - {SURNAME}/{SEED}/{ARTIST} ---")
print(f"Raw Stream: {raw_stream}")

def validate(data):
    print("[DIAG] Checking validate")
    valid = [x for x in data if x != -999]
    print(f"Valid: {len(valid)}, Invalid: {len(data)-len(valid)}")
    return valid

def calibrate(data):
    print("[DIAG] Checking calibrate")
    add = SEED % 5  # 14 % 5 = 4
    calibrated = [x + add for x in data]
    print(f"Calibrated (+{add}): {calibrated}")
    return calibrated

def analyze(data):
    avg = round(sum(data)/len(data), 2)
    status = "WARNING" if avg > 35 else "NORMAL"
    print(f"Final Sequence: {data}")
    print(f"FINAL OUTPUT: Avg={avg}, Status={status}")
    return avg, status

cleaned = validate(raw_stream)
calibrated = calibrate(cleaned)
analyze(calibrated)