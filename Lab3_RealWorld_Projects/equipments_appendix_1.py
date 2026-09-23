import random
from functools import wraps

# Student-specific inputs
LAST_NAME = "PENA"
SEED_NUM = 14
FAVORITE_ARTIST = "SILENT SANCTUARY"


# Create a student-specific seed
def create_seed():
    return (
        SEED_NUM
        + sum(ord(c) for c in LAST_NAME)
        + sum(ord(c) for c in FAVORITE_ARTIST)
    )


# Generate student-specific equipment readings
def generate_readings():
    rng = random.Random(create_seed())

    readings = [rng.randint(40, 100) for _ in range(8)]

    # Add invalid readings to demonstrate exception handling
    readings.append("N/A")
    readings.append(-7)

    return readings


# Validate one reading
def validate_reading(reading):
    if not isinstance(reading, (int, float)) or isinstance(reading, bool):
        raise TypeError("Reading must be numeric.")

    if not 0 <= reading <= 100:
        raise ValueError("Reading must be between 0 and 100.")

    return True


# Calculate average
def calculate_average(readings):
    if not readings:
        return 0

    return sum(readings) / len(readings)


# Classify equipment condition
def classify_reading(reading):
    if reading <= 70:
        return "NORMAL"
    elif reading <= 85:
        return "WARNING"
    else:
        return "CRITICAL"


# Decorator for diagnostic process logging
def diagnostic_logger(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("[LOG] Diagnostic process started.")
        result = function(*args, **kwargs)
        print("[LOG] Diagnostic process completed.")
        return result

    return wrapper


@diagnostic_logger
def run_diagnostics(readings):
    valid_readings = []
    validation_results = []
    diagnostic_results = []

    for number, reading in enumerate(readings, start=1):
        try:
            validate_reading(reading)

            valid_readings.append(reading)
            condition = classify_reading(reading)

            validation_results.append(
                f"Reading {number}: VALID"
            )

            diagnostic_results.append(
                f"Reading {number}: {reading} -> {condition}"
            )

        except (TypeError, ValueError) as error:
            validation_results.append(
                f"Reading {number}: INVALID - {error}"
            )

    average = calculate_average(valid_readings)

    return (
        valid_readings,
        validation_results,
        diagnostic_results,
        average
    )


# Main program
equipment_data = generate_readings()

valid_readings, validation_results, diagnostic_results, average = \
    run_diagnostics(equipment_data)

critical_count = sum(
    1 for reading in valid_readings
    if classify_reading(reading) == "CRITICAL"
)

if critical_count > 0:
    overall_status = "CRITICAL CONDITION"
elif any(classify_reading(x) == "WARNING" for x in valid_readings):
    overall_status = "WARNING CONDITION"
else:
    overall_status = "NORMAL CONDITION"


print("\n=== EQUIPMENT DIAGNOSTIC SYSTEM ===")
print("Student:", LAST_NAME)
print("Seed Number:", SEED_NUM)
print("Favorite Artist:", FAVORITE_ARTIST)

print("\nGenerated Equipment Data:")
print(equipment_data)

print("\nValidation Results:")
for result in validation_results:
    print(result)

print("\nDiagnostic Results:")
for result in diagnostic_results:
    print(result)

print("\nDiagnostic Summary:")
print("Valid readings:", len(valid_readings))
print("Invalid readings:", len(equipment_data) - len(valid_readings))
print("Average:", round(average, 2))
print("Critical readings:", critical_count)
print("Overall Status:", overall_status)

print("\nFinal Output:")
print("Equipment diagnostic completed successfully.")