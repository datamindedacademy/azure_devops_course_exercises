# Hands On YAML Pipelines



## Hello World Azure Functions

This exercise is a compound one, where we will address several basic and advanced topic of YAML pipelines.
In this documentation the steps are discussed in some more detail.

The exercise here represents a real life scenario where we have an API defined using azure functions. 
These functions execute some basic code when triggered trough HTTPS.
The goal is to build the code, test it, deploy it to a development environment
and afterwards to a production environment.

### Build

In this first section we will create the first part of our pipeline, the build.
Open the empty file: `my_first_pipeline.yml` and complete the steps below. 
You can edit the pipeline in browser or locally in an IDE.

**NOTE** Make sure you are working on YOUR (forked) BRANCH.

**Name the pipeline RUNS:**  including the current date (use a variable)

**Use the correct pool:** 
The name of the agent you can use is: `DMLaptop` ot `Azure Pipelines` with the latest `ubuntu`image.
One is a self-hosted agent (my own computer), the latter one is hosted by azure.

**Create a param:** Define a parameter named `python` and where the default value is `3.6`

**Create a first stage `Build`:**
This stage should contain one job and two steps.
1. The first step includes building the 
`zip` file of the directory `src/hello_world/azure_functions`.
The zip should contain all files in there but not the root dir itself (not`azure_functions`). There are several manners on 
how to create this zip, one could use bash script or another hint is using the `ArchiveFiles` task. 
2. The second step is to publish this zip file as an artifact. Make sure to publish it in the artifacts' directory of the Build.
Tip: take a look at the system and build environment variable and there might be one related to this.

### Test

The second stage we introduce is the test stage.
For now, we only have a single test.
Since we are working with a python project we use the package `pytest`
to test/execute our code.
In general there are often libraries or package needed to execute the pipeline.
In this part we will also learn how we can install some requirements (python).
There are several ways to execute the steps, if in doubt: use Google!


**Create a second stage `Test`**

In this stage we will need to perform 3 steps.
1. A step that makes sure we use the correct python version. Tip: take a look at `UsePythonVersion@0`.
2. A step that executes the python command: `pip install -r *PATH_TO_REQUIREMENTSFILE*`.
This command will install all packages needed and defined in the requirements file `requirements.txt`.
3. A step that executes the actual tests. This can done via the command `pytest *PATH_DIR_FUNCTIONS_OR_TESTS*`

Make sure that all steps have a clear `displayName`

### Deploy

Now we have built and tested our code. It is time to deploy!
As it is often the case in software development, there are several pillars or environment.
This project is no different and we are working with a `DEV` and `PRD` environment.
In this part you should define two stages, a deployment both environments.

There are two steps that should be defined in each stage.
1. Download the artifact you created in the `Build` stage.
2. Define the deployment of the artifact. For this use the following code:
```
- task: AzureFunctionApp@1
            inputs:
              azureSubscription: "service_student$YOURNUMBER$"
              appType: functionAppLinux
              appName: "functionapp-student*the number assigned to you*-*dev or prd depedning on the environment*"
              package: *The downloaded articaft. Tip: try to find out where they are downloaded*
```

Make sure your deployment succeeds.

### Triggers
Currently our pipeline is only confgured to run manually.
This is not exactly agile...
Lets define a new trigger! 

**Define a trigger** when:
1. There is a push on the main branch
2. There are changes in the `/azure_functions` folder

Make a change that should trigger the pipeline and check it runs.

### Templates & Environments

We have seen in the slides it is possible to remove some code duplication.
Create a new folder `templates` in the `pipelines` folder.
Here define a template that deploys to a pillar.


Use environments: `hello_world_*YOURNAME*_*ENVIRONMENT*`.

### Caching
We saw that installing the lots od dependencies again and again, might have som impact on performance.
In our `Test` stage, we install som dependencies.

**Use Caching in Test stage**
1. Cache the requirements file/pip dependencies.
2. Make sure we don't install the requirements if there was a hit


### Validation

Since we have a working environment for both `DEV` and `PRD` it is a good idea
to add an approval check to the deployment of this environment.

**Add Manual approval for YOUR `PRD` environment**
Go to the environments tab and find your `PRD` environment.
From here go to the checks settings and add a manual approval.












