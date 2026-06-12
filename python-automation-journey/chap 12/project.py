distance = float(input("Enter distance in km: ").strip())
delivery_charges=0
if distance <= 3:
    delivery_charges=0
    # Free delivery
elif distance <= 10:
    delivery_charges=50
    # 50 PKR
else:
    delivery_charges=100

print(f"Your delivery charges are: {delivery_charges} PKR")
