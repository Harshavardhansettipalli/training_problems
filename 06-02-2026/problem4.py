event_a = set()

n = int(input("Enter number of students registered for Event A: "))
for i in range(n):
    sid = int(input("Enter student ID: "))
    event_a.add(sid)  
event_b = set()
m = int(input("\nEnter number of students registered for Event B: "))
for i in range(m):
    sid = int(input("Enter student ID: "))
    event_b.add(sid)
print("\nTotal unique participants in Event A:", len(event_a))
common_students = event_a.intersection(event_b)
print("Common participants in both events:", common_students)
cancel_id = int(input("Enter student ID to cancel registration from Event A: "))
event_a.discard(cancel_id)  

print("Updated Event A registrations:", event_a)
