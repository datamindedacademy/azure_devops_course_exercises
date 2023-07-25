# Hands On Classic Pipelines

## Introduction

The goal of this exercise is to create a build pipelines where we build and
test our code. The project at hand is one where we create an API and we want
to make sure we get the correct http response.  The code is already there so it
is just a matter of building it and testing it.

For this exercise you can use the pool `Azure Pipelines` with the latest ubuntu
image.

## Build

The first stage in this exercise is the build. Here we want to create an
archive file (`zip`) and publish it as an artifact. These are thus the two
exact steps in our job:

1. The first step includes building the `zip` file of the directory
   `src/hello_world/azure_functions`. The zip should contain all files in there
   but not the root dir itself (not`azure_functions`).
2. The second step is to publish this zip file as an artefact. Make sure to
   publish it in the artifacts' directory of the Build. Tip: take a look at the
   system and build environment variable and there might be one related to
   this.

Use at least 1 variable in the process!

## Test

Add another agent job and call this one `Test`. The steps in this stage are as
follows:

1. Make sure we use the correct Python version which is `3.6`.
2. Install the requirements that we need. The command for this is `pip install
   -r *PATH_TO_REQUIREMENTSFILE*`.
3. Run the tests themself. This can be done by executing the command: `pytest
   *PATH_DIR_FUNCTIONS_OR_TESTS*`.

Please make sure this stage is executed before the build stage. 

### Release to DEV

The goal of this exercise is to create a release pipeline from the artifact we
created in the previous one.  The artifact will be released in two separate
pillars/environments, `$YOURNAME$_DEV` and `$YOURNAME$_PRD`


1. Create a new release pipeline
2. Give it a unique name, and use your name in the pipeline.
3. Select the artifact from YOUR build pipeline
4. Rename the first stage and select `Deploy Azure Function App`
5. Edit the stage and select the correct azure subscription.  The one you
   should use will be shared from the trainer.
6. Select the correct `App Type`: `Function App on Linux`
7. Select the correct service name.

Now it is time to save, and release. Make sure the pipeline succeeds and
afterwards check the results by going to the URL:
`https://functionapp-student$YOURNUMBER$-dev.azurewebsites.net/api/hello_world`
If this is your personal greeting, then well done!

## Release to PRD

1. Please repeat the previous steps and add another stage that does the same
   except release to the `PRD` function app.
2. Make sure this one depends on the `DEV` release.
3. Add a gate to the `PRD` release and make sure it needs your approval.
4. Add a scheduled release trigger. This should be released once a week.  The
   other params I leave to you!

Time again to save, and release. Again check that:

1. The pipeline succeeds.
2. The Correct anonymous greeting is shown when you go to
   `https://functionapp-student$YOURNUMBER$-prd.azurewebsites.net/api/hello_world`

Well done!
