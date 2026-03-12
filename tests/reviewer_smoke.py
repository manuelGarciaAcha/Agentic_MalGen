import sys
sys.path.append('')

# JSON testing:

from agents.reviewer import Reviewer

reviewer = Reviewer()

goal = """
Write a Python program that loads student grade data from a CSV-style string.
Each line has: name,score
The program should:
1. Ignore empty lines
2. Skip malformed rows
3. Convert scores to integers
4. Return a dictionary with:
   - "average"
   - "highest"
   - "lowest"
   - "passed_students" (score >= 60)
If there are no valid students, return average=0, highest=None, lowest=None, passed_students=[].
"""

test_code = """
def parse_students(data):
    students = []
    lines = data.split("\\n")

    for line in lines:
        parts = line.split(",")
        if len(parts) != 2:
            continue

        name = parts[0].strip()
        score = int(parts[1].strip())
        students.append({"name": name, "score": score})

    return students


def compute_average(students):
    total = 0
    for s in students:
        total += s["score"]
    return total / len(students)


def find_highest(students):
    highest = students[0]
    for s in students:
        if s["score"] > highest["score"]:
            highest = s
    return highest["name"]


def find_lowest(students):
    lowest = students[0]
    for s in students:
        if s["score"] < lowest["score"]:
            lowest = s
    return lowest["name"]


def get_passed_students(students):
    passed = []
    for s in students:
        if s["score"] > 60:
            passed.append(s["name"])
    return passed


def summarize_grades(data):
    students = parse_students(data)

    return {
        "average": compute_average(students),
        "highest": find_highest(students),
        "lowest": find_lowest(students),
        "passed_students": get_passed_students(students)
    }
"""

result = reviewer.review(
    goal=goal,
    code=test_code,
    fix_items=[],
    iteration=1,
)

print(result)