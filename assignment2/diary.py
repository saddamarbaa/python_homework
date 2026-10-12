
# Task 1
try:
    with open("diary.txt", "a") as file:
        first_entry = True

        while True:
            if first_entry:
                entry = input("What happened today? ")
            else:
                entry = input("What else? ")

            file.write(entry + "\n")

            if entry == "done for now":
                break

            first_entry = False

except Exception as e:
    print("An exception occurred.", type(e).__name__)