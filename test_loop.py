import person_generator
people = person_generator.data
keys = person_generator.keys


def main():
    for item in keys:
        print(people[item]["First Name"], people[item]["Last Name"], ",", people[item]["Age"],
              "years old , email:"+people[item]["Email"], ", phone:"+people[item]["Phone"])


main()
