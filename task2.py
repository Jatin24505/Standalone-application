import os

FILE_NAME = "employees.txt"

def create_employee():
    try:
        name = input("Enter your name: ").strip()
        age = int(input("Enter your age (18-60): "))
        if age < 18 or age > 60:
            raise ValueError("Age must be between 18 and 60.")

        print("Enter designation code (p25 for Programmer, m30 for Manager, t20 for Tester):")
        designation = input("Designation: ").strip().lower()

        salary = 0
        if designation == 'p25':
            salary = 25000
        elif designation == 'm30':
            salary = 30000
        elif designation == 't20':
            salary = 20000
        else:
            raise ValueError("Invalid designation code.")

        with open(FILE_NAME, "a") as file:
            file.write(f"{name},{age},{salary},{designation}\n")

        print("✅ Employee record created successfully!\n")

    except ValueError as ve:
        print(f"❌ Error: {ve}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def display_employees():
    if not os.path.exists(FILE_NAME):
        print("❌ No employee records found.\n")
        return

    print("\n📋 Employee Records:")
    print("Name\tAge\tSalary\tDesignation")
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, age, salary, designation = line.strip().split(',')
                designation_name = {
                    "p25": "Programmer",
                    "m30": "Manager",
                    "t20": "Tester"
                }.get(designation, "Unknown")
                print(f"{name}\t{age}\t{salary}\t{designation_name}")
        print()
    except Exception as e:
        print(f"❌ Error reading file: {e}")


def raise_salary():
    if not os.path.exists(FILE_NAME):
        print("❌ No employee records to update.\n")
        return

    try:
        emp_name = input("Enter the name of the employee to raise salary: ").strip()
        percent = float(input("Enter percentage raise (1-30): "))
        if percent < 1 or percent > 30:
            raise ValueError("Percentage must be between 1 and 30.")

        updated = False
        lines = []
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, age, salary, designation = line.strip().split(',')
                if name.lower() == emp_name.lower():
                    new_salary = int(float(salary) + (float(salary) * percent / 100))
                    lines.append(f"{name},{age},{new_salary},{designation}\n")
                    updated = True
                else:
                    lines.append(line)

        if updated:
            with open(FILE_NAME, "w") as file:
                file.writelines(lines)
            print("✅ Salary updated successfully!\n")
        else:
            print("❌ Employee not found.\n")

    except ValueError as ve:
        print(f"❌ Error: {ve}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def main():
    while True:
        print("==== Employee Management System ====")
        print("1. Create Employee")
        print("2. Display Employees")
        print("3. Raise Salary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            create_employee()
        elif choice == '2':
            display_employees()
        elif choice == '3':
            raise_salary()
        elif choice == '4':
            print("🙏 Thank you for using the application!")
            break
        else:
            print("❌ Invalid choice. Please enter between 1 and 4.\n")

if __name__ == "__main__":
    main()
