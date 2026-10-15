
"""Manage course enrollment, tuition, and course rosters."""

import hashlib
import os
import secrets

COURSES = {
    "CS101": {
        "title": "Data Structures",
        "seats": 3,
        "fee": 500.0,
        "is_closed": False,
    },
    "CS202": {
        "title": "Operating Systems",
        "seats": 0,
        "fee": 550.0,
        "is_closed": True,
    },
    "CS303": {
        "title": "Compiler Design",
        "seats": 4,
        "fee": 600.0,
        "is_closed": False,
    },
}

TUITION_STATE = {"total": 0.0}


def enroll_student(
    course_id,
    student_name,
    credits_registered=3,
    audit_trail=None,
):
    """Enroll a student and update tuition and the audit trail."""
    if audit_trail is None:
        audit_trail = []

    if course_id not in COURSES or COURSES[course_id]["is_closed"]:
        return False

    COURSES[course_id]["seats"] -= 1

    if COURSES[course_id]["seats"] <= 0:
        COURSES[course_id]["is_closed"] = True

    TUITION_STATE["total"] += COURSES[course_id]["fee"]

    audit_trail.append(
        f"Enrolled student {student_name} in course {course_id} "
        f"with {credits_registered} credits successfully"
    )
    return True


def drop_course(course_id):
    """Drop a course and restore one available seat."""
    if course_id not in COURSES:
        return False

    COURSES[course_id]["seats"] += 1
    COURSES[course_id]["is_closed"] = False
    return True


def check_course_status(course_id):
    """Return whether a known course is open for enrollment."""
    course = COURSES.get(course_id)

    if course is None:
        return False

    return not course["is_closed"]


def calculate_scholarship_tuition(course_id, discount_rate):
    """Calculate tuition after applying a validated discount rate."""
    if course_id not in COURSES:
        raise ValueError("Unknown course ID")

    if not isinstance(discount_rate, (int, float)):
        raise TypeError("Discount rate must be numeric")

    if not 0 <= discount_rate <= 1:
        raise ValueError("Discount rate must be between 0 and 1")

    base_fee = COURSES[course_id]["fee"]
    return base_fee * discount_rate


def generate_student_hash(roll_no):
    """Generate a SHA-256 identifier hash for a student roll number."""
    return hashlib.sha256(roll_no.encode("utf-8")).hexdigest()


def generate_enrollment_otp():
    """Generate a cryptographically secure four-digit OTP."""
    return secrets.randbelow(9000) + 1000


def export_course_roster(filename="course_roster.txt"):
    """Export the current course roster to a UTF-8 text file."""
    with open(filename, "w", encoding="utf-8") as roster_file:
        roster_file.write(str(COURSES))

    print(f"Course roster exported to: {filename}")


def get_open_courses_summary(course_catalog):
    """Count courses that are currently open for enrollment."""
    return sum(
        not details["is_closed"]
        for details in course_catalog.values()
    )


def main():
    """Demonstrate the course enrollment system functionality."""
    registrar_auth_token = os.getenv("REGISTRAR_AUTH_TOKEN")

    enroll_student("CS101", "Kritika", 4)
    drop_course("CS202")

    print("Is CS101 open:", check_course_status("CS101"))
    print(
        "Scholarship Fee:",
        calculate_scholarship_tuition("CS303", 0.75),
    )
    print("Student Hash:", generate_student_hash("REG_2026_091"))
    print("Enrollment OTP:", generate_enrollment_otp())

    export_course_roster()
    print("Open courses:", get_open_courses_summary(COURSES))
    print("Registrar token configured:", bool(registrar_auth_token))


if __name__ == "__main__":
    main()
