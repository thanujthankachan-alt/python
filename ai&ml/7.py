def get_report(name, marks):
    total = sum(marks)
    percent = (total / (len(marks) * 100)) * 100
    grade = "F"
    for score, g in [(90, "A+"), (80, "A"), (70, "B"), (60, "C"), (50, "D")]:
        if percent >= score:
            grade = g
            break

    print(f"\n--- {name}'s Report ---")
    print(f"Total: {total} | Percentage: {percent:.2f}% | Grade: {grade}")

get_report("titus sony markose", [85, 92, 78, 89, 95])