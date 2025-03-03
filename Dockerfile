FROM python:3

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir  jupyter \
  && pip install --no-cache-dir  AutoFeedback \
  && pip install --no-cache-dir pytest \
  && pip install --no-cache-dir pandas \
  && pip install --no-cache-dir inquirer \
  && pip install --no-cache-dir canvas_selector \ 
  && pip install "git+https://github.com/autofeedback-exercises/exercises.git@add_marking_utilities"


COPY .canvasapirc ./root/
