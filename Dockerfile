FROM python:3

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir  jupyter \
  && pip install --no-cache-dir  AutoFeedback \
  && pip install --no-cache-dir pytest \
  && pip install --no-cache-dir pandas \
  && pip install --no-cache-dir inquirer \
  && pip install --no-cache-dir canvas_selector


COPY marking/.canvasapirc ./root/
COPY marking/grade_ipynbs.py ./bin/
COPY tests/test_exercises.py ./bin/
RUN chmod +x ./bin/grade_ipynbs.py
