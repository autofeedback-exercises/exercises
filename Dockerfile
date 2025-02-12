FROM python:3

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir  jupyter \
  && pip install --no-cache-dir  AutoFeedback \
  && pip install --no-cache-dir pytest \
  && pip install --no-cache-dir pandas \
  && pip install --no-cache-dir inquirer \
  && pip install --no-cache-dir tqdm \
  && pip install --no-cache-dir canvasapi 

COPY marking/APIKEY.py ./bin/
COPY marking/grade_ipynbs.py ./bin/
COPY tests/test_exercises.py ./bin/

