# Implement any one of the following Expert System --> Employee performance evaluation

class Employee:
    def __init__(self, name, productivity, quality, teamwork, communication):
        self.name = name
        self.productivity = productivity
        self.quality = quality
        self.teamwork = teamwork
        self.communication = communication
        self.performance_rating = None

def evaluate_performance(employee):
    productivity_score = calculate_productivity_score(employee.productivity)
    quality_score = calculate_quality_score(employee.quality)
    teamwork_score = calculate_teamwork_score(employee.teamwork)
    communication_score = calculate_communication_score(employee.communication)
    
    overall_score = (productivity_score + quality_score + teamwork_score + communication_score) / 4
    
    if overall_score >= 80:
        employee.performance_rating = "Exceeds Expectations"
    elif overall_score >= 70:
        employee.performance_rating = "Meets Expectations"
    else:
        employee.performance_rating = "Below Expectations"

def calculate_productivity_score(productivity):
    # Dummy implementation, replace with actual scoring logic
    return productivity * 10

def calculate_quality_score(quality):
    # Dummy implementation, replace with actual scoring logic
    return quality * 10

def calculate_teamwork_score(teamwork):
    # Dummy implementation, replace with actual scoring logic
    return teamwork * 10

def calculate_communication_score(communication):
    # Dummy implementation, replace with actual scoring logic
    return communication * 10

# Example usage
employees = [
    Employee("John", 8, 9, 7, 8),
    Employee("Alice", 7, 8, 9, 9),
    Employee("Bob", 9, 7, 8, 7)
]

for emp in employees:
    evaluate_performance(emp)
    print(f"{emp.name}: {emp.performance_rating}")
