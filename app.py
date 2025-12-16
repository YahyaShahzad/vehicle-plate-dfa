from flask import Flask, render_template, request
from datetime import datetime
from collections import Counter

app = Flask(__name__)

# Provinces and vehicle types
PROVINCES = ["Punjab", "Sindh", "Balochistan", "Khyber Pakhtunkhwa",
             "Gilgit Baltistan", "Azad Jammu & Kashmir", "Islamabad Capital Territory"]
VEHICLE_TYPES = ["2-Wheeler", "4-Wheeler"]

# DFA helper
LETTERS = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
DIGITS = set("0123456789")

def build_dfa_with_pattern(pattern: str):
    """
    pattern: string using 'L' for letters, 'D' for digits, '-' for dash
    e.g., 'L-DDDD' or 'LLL-DDDD'
    """
    states = [f'q{i}' for i in range(len(pattern)+1)]
    start = 'q0'
    accept = f'q{len(pattern)}'
    transitions = {}

    for i, ch in enumerate(pattern):
        if ch == 'L':
            for L in LETTERS:
                transitions[(f'q{i}', L)] = f'q{i+1}'
        elif ch == 'D':
            for D in DIGITS:
                transitions[(f'q{i}', D)] = f'q{i+1}'
        elif ch == '-':
            transitions[(f'q{i}', '-')] = f'q{i+1}'
        else:
            raise ValueError("Invalid pattern character")

    def validate(s):
        s = s.strip().upper()
        state = start
        for c in s:
            if (state, c) not in transitions:
                return False
            state = transitions[(state, c)]
        return state == accept

    return validate

# DFA map for all provinces
DFA_MAP = {
    ("Punjab","4-Wheeler"): build_dfa_with_pattern("L-DDDD"),
    ("Punjab","2-Wheeler"): build_dfa_with_pattern("LLL-DDDD"),
    ("Sindh","4-Wheeler"): build_dfa_with_pattern("LLL-DDD"),
    ("Sindh","2-Wheeler"): build_dfa_with_pattern("LLL-DDDD"),
    ("Balochistan","4-Wheeler"): build_dfa_with_pattern("LL-DDD"),
    ("Balochistan","2-Wheeler"): build_dfa_with_pattern("LL-DDDD"),
    ("Khyber Pakhtunkhwa","4-Wheeler"): build_dfa_with_pattern("LL-DDDD"),
    ("Khyber Pakhtunkhwa","2-Wheeler"): build_dfa_with_pattern("LL-DDD"),
    ("Gilgit Baltistan","4-Wheeler"): build_dfa_with_pattern("LL-DD"),
    ("Gilgit Baltistan","2-Wheeler"): build_dfa_with_pattern("LL-DDD"),
    ("Azad Jammu & Kashmir","4-Wheeler"): build_dfa_with_pattern("LL-DDD"),
    ("Azad Jammu & Kashmir","2-Wheeler"): build_dfa_with_pattern("LL-DDD"),
    ("Islamabad Capital Territory","4-Wheeler"): build_dfa_with_pattern("LLL-DDD"),
    ("Islamabad Capital Territory","2-Wheeler"): build_dfa_with_pattern("LLL-DD")
}

# Validation function
def dfa_validate_plate(plate: str, province: str, vehicle_type: str):
    key = (province, vehicle_type)
    if key not in DFA_MAP:
        return False
    return DFA_MAP[key](plate)

# History storage
history = []

@app.route("/", methods=["GET","POST"])
def index():
    plate = ""
    valid = None
    note = ""
    province = PROVINCES[0]
    vehicle_type = VEHICLE_TYPES[0]

    if request.method == "POST":
        plate = request.form.get("plate","").strip().upper()
        province = request.form.get("province", province)
        vehicle_type = request.form.get("vehicle_type", vehicle_type)

        if not plate:
            valid = False
            note = "Please enter a plate number."
        else:
            valid = dfa_validate_plate(plate, province, vehicle_type)
            if not valid:
                note = f"Plate does not match DFA rules for {province} {vehicle_type}."

        # Add to history
        history.insert(0, {
            "plate": plate,
            "province": province,
            "vehicle_type": vehicle_type,
            "result": "Valid" if valid else "Invalid",
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        if len(history) > 20:
            history.pop()

    # Chart data
    vehicleCounts = Counter(r["vehicle_type"] for r in history)
    provinceCounts = Counter(r["province"] for r in history)

    vehicle_labels = list(vehicleCounts.keys())
    vehicle_data = list(vehicleCounts.values())
    province_labels = list(provinceCounts.keys())
    province_data = list(provinceCounts.values())

    return render_template("index.html",
        plate=plate,
        valid=valid,
        note=note,
        province=province,
        vehicle_type=vehicle_type,
        history=history,
        provinces=PROVINCES,
        vehicle_types=VEHICLE_TYPES,
        vehicle_labels=vehicle_labels,
        vehicle_data=vehicle_data,
        province_labels=province_labels,
        province_data=province_data
    )

if __name__ == "__main__":
    app.run(debug=True)
