# STUDENT: PENA | SEED: 14 | ARTIST: SILENT SANCTUARY
SURNAME = "PENA"
SEED = 14
ARTIST = "SILENT SANCTUARY"

equipment_data = [21, 24, 27, 33, 36, 39, 42, 45, 48]

def diagnostic_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"--- Equipment Diagnostic: {SURNAME}/{SEED}/{ARTIST} ---")
        result = func(*args, **kwargs)
        print("[LOG] decorator recorded calculation and classification")
        return result
    return wrapper

@diagnostic_decorator
def analyze_equipment(data):
    avg = sum(data) / len(data)
    critical = len([x for x in data if x > 40])
    status = "WARNING" if avg > 35 else "NORMAL"
    print(f"Valid readings: {len(data)}")
    print(f"Average: {round(avg, 2)}")
    print(f"Critical readings: {critical}")
    print(f"Overall Status: {status}")
    return avg, status

analyze_equipment(equipment_data)