# Hello World Azure Functions

This exercise is a compound one, where we will address several basic and
advanced topic of YAML pipelines. In this documentation the steps are
discussed in some more detail.

The exercise here represents a real life scenario where we have an API defined
using Azure Functions. This is an Azure service where one uploads some code to,
and a configuration file, so that the code is triggered by certain external
events. For example, whenever someone visits a certain web address, the code
gets triggered and a certain website is shown. Azure Functions can be used for
a whole lot more, but we'll limit ourselves to this "serverless" functionality.
The goal is to build the code, test it, deploy it to a development environment
and afterwards to a production environment.

## Building the pipeline artifact

In this first section we will create the first part of our pipeline, the build
stage. Open the empty file: `my_first_pipeline.yml` and complete the steps
below. You can edit the pipeline from within the Azure DevOps interface or
locally in an IDE, if you cloned the repository.

**NOTE** Before you begin, make sure you are working on YOUR (forked) BRANCH.

1. Assign a name to the pipeline runs. Include the date at which the pipeline
   runs. Because this can change from day to day, you'll want to use a [system
   variable].
2. Configure the agent pool the pipeline should use. The name of the agent you
   can use is: `DMLaptop` or `Azure Pipelines` with a recent `ubuntu` image.
   The former is a self-hosted agent (my own computer), the latter is provided
   by Azure.
3. Create a pipeline parameter that will allow you to change the version of the
   Python interpreter when starting the pipeline manually. Give it a default
   value of 3.11.
4. Create the "Build" stage:

   This stage should contain one job and two steps.

   1. The first step includes building a compressed archive of the directory
      `src/hello_world/azure_functions`. To do so, we must compress all files
      in there using the zip program, but not the root dir itself (i.e. not
      `azure_functions`). There are several ways you can create this zip: one
      could use a bash script, or work with the ArchiveFiles task for example. 
   2. The second step is to publish this zip file as a pipeline artifact. Make
      sure to publish it in the artifacts' directory of the Build. Tip: take a
      look at the system and build environment variables.

## Testing the code

The second stage we introduce is the test stage. For now, we only have a single
test. Different programming languages and frameworks have their preferred tools
for running tests. For Python, Pytest is a popular test runner. To use it, one
runs `pytest` from the root of the code repo. The program will find the tests
by itself. In general there are often libraries or package needed to execute
the pipeline. In this part we will also learn how we can install external
dependencies our program needs (the so-called requirements). There are several
ways to execute the steps, if in doubt: use Google!

Add a new stage to the pipeline. It will need to perform these 3 steps:

1. Instruct the subsequent steps in this job to use the Python version coming
   from the pipeline parameter you made earlier. There's a task you can use for
   this: `UsePythonVersion`.
2. Configure the environment of the agent, by installing the libraries our
   application needs. In the Python world, one could do that by running the
   following shell command: `pip install -r *PATH_TO_REQUIREMENTSFILE*`. This
   command will install all packages needed and defined in a specific file,
   which is conventionally called `requirements.txt`.
3. With all the libraries our application needs installed, we can run the test
   suite. This can done via the command `pytest`.

Make sure that all steps have a clear `displayName`, which is the
human-readable description that you want to associate with these steps and
which will be shown in the user interface..

## Deploy the artifact

Now we have built and tested our code. It is time to deploy! As is often the
case in software development, there are several environments where our artifact
needs to be deployed to: development, testing, quality assurance, production,
...  This project is no different and we are working with a `DEV` and `PRD`
environment. In this part you should define two more stages, to deploy the
artifact to each environment.

There are two steps that should be defined in each stage:

1. Download the artifact you created in the build stage back into the current
   environment (remember, this step might be running on a completely different
   machine than where you built the artifact, which is why you must download it
   first).
2. Deploy the artifact. For this use the following code:

   ```
   - task: AzureFunctionApp@1
     inputs:
       azureSubscription: "service_student$YOURNUMBER$"
       appType: functionAppLinux
       appName: "functionapp-student*the number assigned to you*-*dev or prd depending on the environment*"
       package: *The downloaded artifact". Tip: try to find out where they are downloaded.
   ```

Verify the deployment has succeeded by visiting the URL of the Function App.
The instructor can give you the URL.

## Add pipeline triggers

Currently our pipeline is only confgured to run manually.
This is not what we want from a pipeline that does continuous integration and continuous deployment (CI/CD).

Define a new trigger, so that the pipeline is started when:

* there is a new commit on the main branch and
* the changes of that commit happened in the `/azure_functions` folder

Save this new version of your pipeline and then make a minor change to the code
inside that folder. Verify it has triggered your pipeline.

## Templates & Environments

We have seen in the slides that it is possible to remove some code duplication.
Create a new folder `templates` in the `pipelines` folder. Here define a
template that deploys to an environment.

Use environments: `hello_world_*YOURNAME*_*ENVIRONMENT*`.

Replace the duplicated code in your original pipeline by referencing the
template and supplying the needed parameters.

## Caching

If you inspected the build logs of the pipeline, you may have noticed that it
takes some time to install all those dependencies. What's worse is that happens
with each run! Clearly that's not a very efficient use of the time, since those
dependencies don't change all that often. We can get attempt to optimize that
step by caching the build dependencies, which means they'll be available from
Azure DevOps in the next pipeline run.

1. Cache the requirements file/pip dependencies.
2. Make sure we don't install the dependencies if they were in the cache.

## Add a human approval step

Since we have a working environment for both `DEV` and `PRD` it is a good idea
to add an approval check to the deployment of this environment.

Add a manual approval to your `PRD` environment, the one you reference in your code:

1. Go to the environments tab and find your `PRD` environment.
2. From here go to the "checks settings" and add a manual approval.

[System variable]: https://learn.microsoft.com/en-us/azure/devops/pipelines/build/variables?view=azure-devops&tabs=yaml
