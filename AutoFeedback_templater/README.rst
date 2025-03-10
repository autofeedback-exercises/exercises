======================
AutoFeedback_templater
======================

To grab the AutoFeedback exercises repository

.. code-block:: bash

    > git clone https://github.com/autofeedback-exercises/exercises

And install the new_exercises package

.. code-block:: bash

    > pip install autofeedback_templater 

This then provides you with a command line utility to set up your exercises.

.. code-block:: bash

    > new_exercise -l <path to location of exercises> -n <name of exercise>

so, for instance create a block of exercises called intro in a module directory, MTH1000, and within that create a new exercise called 'functions' I would execute

.. code-block:: bash

    > new_exercise -l MTH1000/intro -n functions

