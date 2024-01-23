import time

def collect_employee_data(employee, month):
    print(f"Data of {employee} for {month}")
    time.sleep(2)
    return f"data of {employee} for {month}"


def analyze_attendance(attendance):
    print(f"Analyzing {attendance}")
    time.sleep(3)
    return f"Analysis of {attendance}"

def compile_report(analysis):
    print(f"compiling report: {analysis}")
    time.sleep(2)
    return f"Report based on {analysis}"

def generate_monthly_reports(employees, months):
    for month in months:
        for employee in employees:
            attendance = collect_employee_data(employee, month)
            analysis = analyze_attendance(attendance)
            report = compile_report(analysis)
            print(f"Completed report of {employee} for {month}: {report}\n")

months = ["January", "February", "March"]
employees = ["abc", "pqr", "xyz", "cde", "mno"]
generate_monthly_reports(employees, months)
