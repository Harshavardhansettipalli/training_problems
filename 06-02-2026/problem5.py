newsletter_a = set()

n = int(input("Enter number of subscribers for Newsletter A: "))
for i in range(n):
    email = input("Enter email ID: ")
    newsletter_a.add(email)

newsletter_b = set()

m = int(input("\nEnter number of subscribers for Newsletter B: "))
for i in range(m):
    email = input("Enter email ID: ")
    newsletter_b.add(email)

new_email = input("\nEnter new email to subscribe to Newsletter A: ")
newsletter_a.add(new_email)

remove_email = input("Enter email to unsubscribe from Newsletter A: ")
newsletter_a.discard(remove_email)

common_users = newsletter_a & newsletter_b

print("\nNewsletter A Subscribers:", newsletter_a)
print("Newsletter B Subscribers:", newsletter_b)
print("Subscribed to BOTH newsletters:", common_users)
