# sunycsc485
## Github Actions, Checks Made on Creating a Pull Request
Github supports workflow actions, instructions to perform various code-related steps and checks when certain things happen. For more info, see [GitHub Actions documentation](https://docs.github.com/en/actions).

We will build instructions to:
1. run our tests when we create a pull request; these tests will run against that pull request's branch, and will exclude tests that require an API server to be running (because  those will fail)
2. generate a coverage report for the tests that were run.


### Setting up our actions
To configure this, we need to have a new directory structure in the project route; this will look like this:
```text
suny485 (project root)
  |- suny48 (package)
  |- .gitignore
  |- requirements.txt
  |- setup.cfg
  |- setup.py     <-- create this file
  |- README.md
  |- pytest.ini
  |- .github      <-- create this folder
    |- workflows  <-- create this folder
      |- push.yml <-- create this file
```

The push.yml file contains the instructions that github will use to configure and launch a docker container and the specific actions to perform on that container:
```yaml
name: Run pytest on PR

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Switch to Current Branch
      run: |
        git checkout ${{ env.BRANCH }}

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: 3.9

    - name: Install dependencies
      run: |
        python -m pip install -U pip
        pip install -r requirements.txt
        pip install -e .
        python setup.py install
        echo "[pwd]: ${PWD}"

    - name: Display Troubleshooting Information
      run: |
        echo "[workspace]: ${{ github.workspace }}"
        echo "[pwd]: ${PWD}"
        echo "[LS]: $(ls -al)"

    - name: Run tests and coverage report
      run: |
        # Note: the following commands have three entirely different instances
        # of the "-m" flag. These are positionally required!
        echo "[pwd]: ${PWD}"
        export PYTHONPATH=$PWD/suny485
        echo "[pythonpath]: ${PYTHONPATH}"
        echo "!! run pytest and exclude any live API tests !!"
        coverage run -m pytest -m 'not live_api' --tb=short
        echo "!! run coverage report"
        coverage report -m
```

### Using the actions
You will still create a pull request exactly as you have been doing. Your worklow is:
1. on your local main branch, pull from origin main to get the latest version of code from github.
2. from local main, create a feature branch. This is where you will make your changes.
3. check out your feature branch!
4. write your new code
5. commit your changes
6. push your code to a feature branch on github
7. look at your new branch on github, then click the "create pull request" button
8. Blam! now github runs your action, and you will see status indicator saying that it is in process
9. If you have no syntax errors, the actions will complete and you will get the prompt to rebase your PR. You can choose to review the logs from your actions, which will show your test results and your coverage report.