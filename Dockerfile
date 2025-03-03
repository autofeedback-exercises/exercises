FROM python:3

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir AutoFeedback_grader


COPY .canvasapirc ./root/

ENTRYPOINT ["grade_ipynbs"]

CMD []
