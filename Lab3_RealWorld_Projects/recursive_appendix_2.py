# ==========================================
# EXERCISE 2: RECURSIVE FAULT TRACE
# ==========================================

LAST_NAME = "PENA"
SEED_NUM = 14
FAVORITE_ARTIST = "SILENT SANCTUARY"


# Generate the fault data
def generate_fault_data():
    return 75


# Recursive function
def trace_fault(fault_code, trace=None):

    if trace is None:
        trace = []

    # Base condition
    if fault_code <= 3:
        trace.append(fault_code)
        return trace

    trace.append(fault_code)

    # Recursive call
    return trace_fault(fault_code - 6, trace)


# Main program
fault_data = generate_fault_data()

recursive_trace = trace_fault(fault_data)

recursive_calls = len(recursive_trace)

termination_point = recursive_trace[-1]


# ==========================================
# OUTPUT
# ==========================================

print("==========================================")
print("        EXERCISE 2: RECURSIVE TRACE")
print("==========================================")

print("\nStudent-Specific Input:")
print("LAST_NAME:", LAST_NAME)
print("SEED_NUM:", SEED_NUM)
print("FAVORITE_ARTIST:", FAVORITE_ARTIST)

print("\nGenerated Fault Data:")
print("Fault Data:", fault_data)

print("\nRecursive Fault Trace:")

for number, fault_code in enumerate(recursive_trace, start=1):

    if fault_code == termination_point:
        print(
            f"Trace {number}: Fault Code {fault_code}"
        )
    else:
        print(
            f"Trace {number}: Fault Code {fault_code}"
        )


print(
    f"\nLevel {recursive_calls}: "
    f"Fault code {termination_point} reached termination. "
    f"Diagnostic Complete."
)


print("\n==========================================")
print("          FINAL TRACE SUMMARY")
print("==========================================")

print("Generated Fault Data:", fault_data)

print("Trace Summary:", recursive_trace)

print("Recursive Calls:", recursive_calls)

print("Termination Point:", termination_point)


print("\nExecution Log:")
print("Fault data generated successfully.")
print("Recursive fault analysis started.")
print("Fault code decreased by 6 during each recursive call.")
print("Base condition reached at fault code 3.")
print("Diagnostic analysis completed successfully.")


print("\nFinal Output:")
print(
    f"Fault Data {fault_data} processed successfully "
    f"through recursive analysis."
)