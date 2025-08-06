name="Karma Wangchuk"
age=20
height=1.82
is_student=True

person_info={
    "Name":name,
    "Age":age,
    "Height":height,
    "Is_Student":is_student
}
print(person_info)

person_info["Favourite_color"]="Blue"
print(person_info)

try:
    print(person_info["Weight"])
except KeyError as e:
    print(f"Error:{e}")

    
