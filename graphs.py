
import matplotlib.pyplot as plt

# Average salary per department
departments = ["IT", "HR", "Sales", "Finance"]
avg_salary = [45000, 35000, 40000, 42000]

plt.figure(figsize=(8, 5))
bars = plt.bar(departments, avg_salary)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.bar_label(bars)
plt.tight_layout()
plt.savefig("salary_chart.png")
plt.show()
