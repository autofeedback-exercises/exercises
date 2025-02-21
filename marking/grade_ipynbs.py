from canvasapi import Canvas
from APIKEY import API_KEY, API_URL
from test_exercises import studentTest
from tqdm import tqdm

canvas = Canvas(API_URL, API_KEY)


def select_course(courseList, enrollment_term_id=None):

    if enrollment_term_id:
        courses = [course for course in courseList
                   if enrollment_term_id in course.name]
    else:
        courses = courseList

    answers = choose_one(courses, obj="course")

    return answers


def read_command_line():
    from argparse import ArgumentParser as AP
    parser = AP()
    parser.add_argument('-c', '--course', help="Canvas courseID",
                        default=None)
    parser.add_argument('-a', '--assignment', help='assignment id',
                        default=None)
    parser.add_argument('--all', help='get all assignments',
                        action='store_true', default=False)

    args = parser.parse_args()
    if not args.course:
        args.course = choose_course(canvas)
    else:
        args.course = canvas.get_course(args.course)

    asses = args.course.get_assignments(include="assignment")
    if args.all:
        args.asses = asses
    else:
        if not args.assignment:
            args.assignment = choose_many(asses, obj="assignment")
            args.asses = [args.course.get_assignment(x)
                          for x in args.assignment]
        else:
            args.asses = [args.course.get_assignment(args.assignment)]

    return args


def choose_many(pagList, obj="course"):
    from inquirer import Checkbox, prompt

    questions = [Checkbox(obj, message=f" Which {obj} do you want to use? \
(<up>/<down> to navigate, \
<space> to check/uncheck, \
<enter> to confirm)", choices=pagList)]

    answers = prompt(questions)

    return answers[obj]


def choose_one(pagList, obj="course"):
    from inquirer import List, prompt

    questions = [List(obj, message=f" Which {obj} do you want to use? \
(<up>/<down> to navigate, \
<space> to check/uncheck, \
<enter> to confirm)", choices=pagList)]

    answers = prompt(questions)

    return answers[obj]


def choose_course(canvas):
    return choose_one(canvas.get_courses(state='available'))


def mkdir(ass_id):
    import os
    if os.path.isdir(str(ass_id)):
        return
    else:
        os.mkdir(str(ass_id))


def nameFile(sub):
    thefile = sub.attachments[-1]
    fname = thefile.__str__().replace(' ', '_')
    return f"{sub.assignment_id}/u{sub.user_id}_{fname}"


def download_ungraded(sub):

    if len(sub.attachments) > 0:
        mkdir(sub.assignment_id)
        thefile = sub.attachments[-1]
        downname = nameFile(sub)
        if downname.endswith(".ipynb"):
            thefile.download(downname)


def mark_ungraded(sub, ass):
    if len(sub.attachments) > 0:
        downname = nameFile(sub)
        mark = int(ass.points_possible) * studentTest(downname)
        sub.mark_read()
        if sub.grade:
            if mark > int(sub.grade):
                update_grade(sub, mark)
        else:
            update_grade(sub, mark)
        return mark


def clear_testsrc():
    """ check if testsrc is installed, and if so, use pip to
    uninstall it"""
    from importlib.util import find_spec
    installed = find_spec('testsrc') is not None
    if installed:
        import subprocess
        import sys
        subprocess.check_call(
            [sys.executable, "-m", "pip", "uninstall", "-y", "testsrc"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT)
    return


def cleanup(ass):
    import shutil
    clear_testsrc()
    shutil.rmtree(str(ass.id))


def get_submissions(ass):

    marks = []
    subs = ass.get_submissions()

    ungraded = [sub for sub in subs if len(sub.attachments) > 0 and
                (sub.grade == "0" or sub.grade is None)]
    for sub in tqdm(ungraded, desc=f"Downloading {ass.name}", ascii=True):
        download_ungraded(sub)
    for sub in tqdm(ungraded, desc=f"Grading     {ass.name}", ascii=True):
        marks.append(mark_ungraded(sub, ass))
    num_zeros = sum(x == 0 for x in marks)
    print(f"{num_zeros} out of {len(marks)} students scored zero")


def update_grade(sub, newgrade):
    sub.edit(submission={'posted_grade': str(newgrade)})


if __name__ == '__main__':
    args = read_command_line()

    for ass in args.asses:
        get_submissions(ass)
        cleanup(ass)
