import json


class Question:
    def __init__(self, data):
        self.data = data

        self.type = data['type']
        self.text = data['text']
        self.points = data['points']

        self.answers = []
        for answer_data in data['answers']:
            try:
                self.answers.append((answer_data['text'], answer_data['status']))
            except:
                self.answers.append((answer_data['text'], 'wrong'))

    def to_dict(self):
        ret = {
            'type': self.type,
            'text': self.text,
            'points': self.points,
            'answers': [{'text': answer[0], 'status': answer[1]} for answer in self.answers]
        }
        return ret


class Section:
    def __init__(self, data):
        self.data = data

        self.title = data['title']

        self.questions = []
        for question_data in data['questions']:
            self.questions.append(Question(question_data))

    def to_dict(self):
        ret = {
            'title': self.title,
            'questions': [question.to_dict() for question in self.questions]
        }
        return ret


class Exam:
    def __init__(self, input_file):
        self.input_file = input_file

        self.sections = []
        with open(self.input_file, 'r') as input_file:
            data = json.load(input_file)

            self.heading = data['heading']
            self.sub_heading = data['sub_heading']
            self.teacher = data['teacher']
            self.duration = data['duration']

            for section_data in data['sections']:
                self.sections.append(Section(section_data))

    def to_dict(self):
        ret = {
            'heading': self.heading,
            'sub_heading': self.sub_heading,
            'teacher': self.teacher,
            'duration': self.duration,
            'sections': [section.to_dict() for section in self.sections]
        }
        return ret
