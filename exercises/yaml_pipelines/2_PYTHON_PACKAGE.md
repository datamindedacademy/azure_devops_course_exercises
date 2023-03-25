# Python Package

In this exercise we are going to create a pipeline that publishes a python package as an azure artifact using poetry.

## Fork the repo

We don't want you to work on the same repo, so please make sure you fork the `python_pacakge` first and 
use your name in the forked repo.

## Let's build it!
There are a bucnh of steps in this pipeline.

- [ ] Install poetry, you will ahve to use curl for this.

- [ ] Configure Poetry, here I will give you a helping hand the commands that need to be executred are:
```bash
poetry config virtualenvs.in-project true
poetry config virtualenvs.path $(venv)
poetry lock
```

- [ ] Install the dependencies using poetry
- [ ] Make use linting is in order by using the pacakge `black`.
Note it is included in the requirements so you don't have to install it seperatly.
- [ ] There are some steps included in the project, make sure you run them!
- [ ] Actually build the project using poetry
- [ ] Authenticate with twine on the artifact feed:
`'Data Minded Azure Devops Workshop/$(MYOWNORIGINALNAME)'`
Make sure to use a variable here.
- [ ] And ofcourse, deploy! I will give you a helping hand again:
`poetry run twine upload -r $(MYOWNORIGINALNAME) --config-file $(PYPIRC_PATH) dist/*.whl`



### Caching
We saw that installing the lots od dependencies again and again, might have som impact on performance.
Make sure that we cache our virtual environment.

For this you will need to use google a bit

