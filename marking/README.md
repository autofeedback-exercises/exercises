# Grading student submissions

## APIKEY

To interact directly with Canvas, you need to add the API information to a file called `APIKEY.py` in this directory.

The file should look like
```python
API_URL = "https://canvas.qub.ac.uk"

API_KEY = "14830~xadfs9asfdljl9eefioajafl0-paopfjdsfa0gi0"
```
where the `API_KEY` entry is your user-generated API access token from Canvas. To generate a token, navigate to canvas, click on your "Account" in the left hand menubar, scroll to "Approved integrations", and click on "New access token". Put in the requested details, and then copy the generated token into `APIKEY.py`.

## Running with docker

In order to safely download and run student-written code, we recommend that you use a virtual machine (docker image) to ensure no nefarious code is executed with access to your local data. 

### Installing docker (macOS)

Docker can be installed via macports:

```bash
> sudo port install docker docker-credential-helper-osxkeychain colima
```

You may already have, or be tempted to install, the Docker Desktop app. While it is "free to download" is it not at all clear that use within QUB is permitted without a license. QUB does not have such a license. 

Once installed, you start the docker daemon with 

```bash
> colima start
INFO[0002] starting colima
INFO[0002] runtime: docker
INFO[0004] starting ...                   context=vm
INFO[0016] provisioning ...               context=docker
INFO[0017] starting ...                   context=docker
INFO[0017] done
```

### Building the docker image

The docker image is built with

```bash
> docker build --tag 'gradepython' .
```

This only needs to be done once.

### Running the docker image

To run the docker image (which you will do everytime you want to mark student submissions)

```bash 
> docker run -it gradepython "/bin/bash"
```
This will open a bash shell in the docker image.

### Executing the grading

```bash
> grade_ipynbs.py
```
will bring up a list of your available Canvas courses. Navigate to the correct course with the up/down arrow keys, and press Enter to select. This in turn will bring up a list of all available assignments on the module (NB not just the programming assignments). You can select as many assignments as you wish to grade- use the up/down arrow keys, and then the right arrow or space bar to select. When you have selected all the assignments, press Enter.

If you know the course ID and/or the assignment IDs you can avoid this selection process and execute `grade_ipynbs.py` with the command line options:

```bash
> grade_ipynbs.py -c <course ID> -a <ass ID1> <ass ID2> ...
```

The script downloads those submissions which are currently unmarked, or which have received a grade of 0, marks them, and updates the grade on canvas. It will also give a summary of the number of those assignments marked which scored zero. This can be useful to show up errors in the marking- if everyone got zero, there may be a problem with the way the AutoFeedback tests are set up.