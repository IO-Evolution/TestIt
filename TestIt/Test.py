import os
import jinja2

from Exam import Exam

ex = Exam("./input/TestInformatica.json")

env = jinja2.Environment(loader=jinja2.loaders.FileSystemLoader('./templates'),
                         variable_start_string='\PYEXP{',
                         variable_end_string='}',
                         line_statement_prefix='%%',
                         comment_start_string='{=',
                         comment_end_string='=}',
                         )
template = env.get_template("base.tex")

data = ex.to_dict()
test = template.render(data=data)
corrected = template.render(data=data, correction=True)

compiled_file_name = data['heading'].replace('-', '').replace(' ', '_')

# COMPILATION
# Students
with open('output/' + compiled_file_name + '_student.tex', 'w') as out:
    out.write(test)
# Teacher
with open('output/' + compiled_file_name + '_teacher.tex', 'w') as out:
    out.write(test)

pwd = os.getcwd()
os.system(f"pdflatex -shell-escape -interaction=nonstopmode -output-directory={pwd}/output {pwd}/output/{compiled_file_name}_student.tex")
os.system(f"pdflatex -shell-escape -interaction=nonstopmode -output-directory={pwd}/output {pwd}/output/{compiled_file_name}_teacher.tex")

os.system(f"rm {pwd}/output/*.aux {pwd}/output/*.log {pwd}/output/*.tex")
os.system(f"rm -R {pwd}/_*")
