from datetime import datetime

GLASS_L = 0.25   # 1 glass = 0.25 litre

# Take input for morning/afternoon/evening
def take_three(msg):
    m = float(input("Morning " + msg + ": "))
    a = float(input("Afternoon " + msg + ": "))
    e = float(input("Evening " + msg + ": "))
    return m, a, e

# Hydration level
def hydration(total, target):
    if total < 0.5 * target: return "Very Low"
    if total < 0.8 * target: return "Low"
    if total < target:      return "Almost Reached"
    if total <= 1.2 * target: return "Target Achieved"
    return "Over Drinking"

# Save data
def save(tar, tot, status):
    today = datetime.now().date()
    f = open("water_history.txt", "a")
    f.write(f"{today} | Target:{tar} L | Total:{tot} L | Status:{status}\n")
    f.close()

# Show history
def show_history():
    print("----- Water History -----")
    f = open("water_history.txt", "r")
    data = f.read().strip()
    f.close()
    print(data if data else "No history yet!")

print("== Water Intake Tracker ==")

print("Select Mode:")
print("1. Glasses")
print("2. ml")
print("3. Litres")
mode = input("Enter choice (1/2/3): ")

# Wrong choice handling
if mode not in ["1","2","3"]:
    print("Invalid choice please enter correct choice.")
    exit()

if mode == "1":
    target_g = float(input("Daily target (in glasses): "))
    target_l = round(target_g * GLASS_L, 2)
    m, a, e = take_three("glasses")
    total = round((m + a + e) * GLASS_L, 2)

elif mode == "2":
    target_ml = float(input("Daily target (in ml): "))
    target_l = round(target_ml / 1000, 2)
    m, a, e = take_three("ml")
    total = round((m + a + e) / 1000, 2)

else:
    target_l = float(input("Daily target (in litres): "))
    m, a, e = take_three("litres")
    total = round(m + a + e, 2)

level = hydration(total, target_l)
save(target_l, total, level)

print("----- RESULT -----")
print("Target:", target_l, "L")
print("Total:", total, "L")
print("Status:", level)

see = input("Do you want to see your water history? (y/n): ")
if see.lower() == "y":
    show_history()
else:
    print("Stay hydrated! Stay focus ,goodbye")
