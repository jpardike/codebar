class Member:
    def __init__(self, full_name, introduce='Hi!'):
        self.full_name = full_name
        self.introduce = introduce


class Student(Member):
    def __init__(self, full_name, reason, introduce='Hi!'):
        super().__init__(full_name, introduce)

        self.reason = reason


class Instructor(Member):
    def __init__(self, full_name, bio, introduce='Hi!'):
        super().__init__(full_name, introduce)

        self.bio = bio
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)


class Workshop:
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.instructors = []
        self.students = []

    def add_participant(self, participant):
        if type(participant) == Student:
            self.students.append(participant)
        else:
            self.instructors.append(participant)

    def __print_date_subject(self):
        print(f'Workshop - {self.date} - {self.subject}')

    def __print_students(self):
        print('\nStudents')
        for i in range(1, len(self.students) + 1):
            print(f'{i}. {self.students[i - 1].full_name} - {self.students[i - 1].reason} ')

    def __print_instructors(self):
        print('\nInstructors')
        for i in range(1, len(self.instructors) + 1):
            print(f'{i}. {self.instructors[i - 1].full_name} - {self.instructors[i - 1].skills} \n {self.instructors[i -1].bio} ')

    def print_details(self):
        self.__print_date_subject()
        self.__print_students()
        self.__print_instructors()


workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()
