current_location = (17.3850, 78.4867)  

print("Current GPS Location:")
print("Latitude:", current_location[0])
print("Longitude:", current_location[1])
previous_location = (17.3850, 78.4867)

if current_location == previous_location:
    print("Vehicle has NOT moved.")
else:
    print("Vehicle has moved.")
