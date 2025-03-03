FROM python:3

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir  jupyter \
  && pip install --no-cache-dir  AutoFeedback \
  && pip install --no-cache-dir pytest \
  && pip install --no-cache-dir pandas \
  && pip install --no-cache-dir inquirer \
  && pip install --no-cache-dir canvas_selector \ 
  && pip install --no-cache-dir AutoFeedback_grader


COPY .canvasapirc ./root/

CMD ["grade_ipynbs", "-s", "2241_SPR"]