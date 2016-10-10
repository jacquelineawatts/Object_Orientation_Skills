"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Abstraction
   Abstraction allows chunks of code to be hidden, enabling users of the code to
   access the functionality but not requiring that they understand the underlying
   nuts and bolts.

   Encapsulation
   Encapsulation is when data and functionality are kept side-by-side, rather than a
   function being completely distinct from the type of object it is acting on. This
   allows us to create functionality that is both specific and unique to those
   types of objects (or of objects in related child classes).

   Polymorphism
   Polymorphism allows different types of classes to have a consistant interface
   with users, bringing together multiple subclasses to use a generalized 'template'
   of attributes and methods. Making your code polymorphic means bringing together
   those elements that are the same between Classes to live in a parent class, and
   shifting anything that is unique to an object into a child class.


2. What is a class?

    A class allows you to group together similar objects (instances) under an umbrella
    with defined data points (attributes) and behaviors (methods) that all instances
    of that class will share.

3. What is an instance attribute?

    A piece of data about an object of a class that is assigned at the individual
    level, not the class level.

4. What is a method?

    A piece of code that defines the behavior that an instance of that class is
    able to do.

5. What is an instance in object orientation?

    An instance is an object of a particular class. The class defines the specific
    data points that object will have (the attributes) and behavior that that object
    can do (the methods). If an instance's class is a child class, the instance will
    inherit attributes and methods from its parent classes as well.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A attribute that is defined at the class level (a class attribute) will be the
   same for all objects which are instantiated as part of that Class, whereas an
   instance attribute is defined at the individual level and will be assigned for
   only that instance of an object, not for other objects of that Class.

"""

# ----------------------------- Defining Classes -------------------------------
class Student(object):
    """Creates a class for Students"""

    def __init__(self, f_name, l_name, address):
        """Initialize a student"""

        self.f_name = f_name
        self.l_name = l_name
        self.address = address


class Question(object):
    """Creates a class for Questions"""

    def __init__(self, question, correct_answer):
        """Initialize a new question"""
        self.question = question
        self.correct_answer = correct_answer.lower()

    def ask_and_evaluate(self):
        """Prompts user with a question and evaluates user input.

        If answer provided by user is the correct answer, function return True."""

        print self.question
        return self.correct_answer == raw_input('>> ').lower()


class Exam(object):
    """Creates a class for Questions"""

    def __init__(self, name):
        """Initialize a new exam"""
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Instantiates a new question and adds to exam questions list"""

        self.questions.append(Question(question, correct_answer))

    def administer(self):
        """Administers questions, evaluates answers, and calculates score in %"""

        score = 0.0
        for question in self.questions:
            if question.ask_and_evaluate() is True:
                score += 1
        return (score / len(self.questions)) * 100

class Quiz(Exam):
    """Creates class for Quiz which inherits from parent class, Exam"""

    def administer(self):
        """Builds on exam.administer() method by returning score as Boolean"""

        score = super(Quiz, self).administer()
        return score >= 50

# ----------------------------- Defining Functions -----------------------------
def take_test(exam, student):
    """Administers exam and assigns score to new student instance attribute."""

    student.score = exam.administer()


def example(exam_name, question_set, student):
    """Conducts sample quiz, and returns student and exam instances

    Expected input includes...
        exam_name: Give your exam/quiz a name
        question_set: A dictionary of sample questions (keys) + answers (values)
        student: A dictionary of a sample student's information
    """

    exam = Exam(exam_name)
    for question in question_set:
        exam.add_question(question, question_set[question])
    student = Student(student['f_name'], student['l_name'], student['address'])
    take_test(exam, student)
    return student, exam

# ------------------------ Dictionaries of Sample Content ----------------------

weird_state_facts = {
    'It\'s illegal in Georgia to do what with a fork?': 'Eat fried chicken',
    'In South Dakota it\'s illegal to fall down and sleep where?': 'In a cheese factory',
    'In Kansas it\'s illegal to eat cherry pie with what?': 'Ice cream',
    'It\'s illegal in Texas to put what on your neighbor\'s cow?': 'Graffiti'
}

watts_jacqui = {
    'f_name': 'Jacqui',
    'l_name': 'Watts',
    'address': 'San Francisco'
}

# ------------------------------ Executable Code -------------------------------

jacqui, state_facts = example('Weird State Facts', weird_state_facts, watts_jacqui)

if jacqui.score is True or jacqui.score >= 50:
    passed = 'passed'
else:
    passed = 'did not pass'

print "{} {} took a quiz on {} and she {}!".format(jacqui.f_name, jacqui.l_name,
                            state_facts.name, passed)
