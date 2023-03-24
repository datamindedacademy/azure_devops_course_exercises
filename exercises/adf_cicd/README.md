# Exercises ADF CI/CD

## Introduction

In this set of steps you will learn how to set up a CI/CD pipeline for your azure datafactorie.
We will have two factories in two seperate environments, one in the `DEV` pillar and one in the `PRD`.
At the end of the exercise your `PRD` ADF will be linked to the `DEV` ADF trough azure pipelines.

## Linking ADF to GIT

The first step is to link your `DEV` ADF to a new git repository. Each one of you should have been assigned a number,
this number will be present in the name of your data factory.

1. Create a new repository in our azure devops project. Make sure you use a unique name (use your own name in it).
Don't create the README file (we will not need it).
2. Go to your `DEV` ADF and press the *set up code repository button*.
   1. At the second step you should choose the `Repository name`, here you should have the
   option to choose your name.
   2. Choose `main` as your collaboration branch (master is legacy). You might need to create it.
   3. Choose `adf_publish` as your publish branch.
   4. Finish the setup by pressing the *apply* button.

## Creating an ADF pipeline
In this step we will create an ADF pipeline that will also send a request to our function we have
created and deployed in the previous set of exercises.


1. Create a new pipeline.
   1. Give the pipeline a name
   2. Add an `Azure Function` activity
      1. Give the activity a name
      2. Under Settings you can add a linked service.
         1. Make sure to add the `DEV` function app.
         2. As for the correct key, you can go to the function app in the azure portal, 
      go to function keys, under which you will find 2, and you can use the one named *_default*.  
           
         **NOTE**: This is not the ideal way of working. Best practice is to store a custom-made app key in the key vault as a secret.
         This can link trough managed identities to the ADF which is a much cleaner way of working, but for the purpose of this exercise
         we will not add too much boilerplate.

      3. Fill in YOUR unique function name. (If you didn't complete the previous exercise, you can use `hello_world`)
      4. Use the GET or POST method.
      5. As a header you can pass `name` with a value of your choice
      6. The body you can add something of your choice.
      7. Make sure to save everything and do a debug run.
2. Make sure you save your new pipeline by pressing *save all* on the top! Afterwards press the *validate all* button. 
If everything is on order you can publish, by pressing the *publish* button.

## Deploying the pipeline to the PRD Factory
In this step we will try and make sure that the pipeline we created in our `DEV` environment is also present in our `PRD` environment
with the correct parameters.

1. Go to your repository that is linked to your ADF. Now there should be several files in the `main` branch as well as the `adf_publish` branch
2. Go to the adf-publish branch, in there you need to add the two files included in 
the directory this file is located in.
You can go and take a look what happens exactly in the devops-pipeline (`.yml`file), but it consists of:
   1. Stopping all triggers
   2. Deploying
   3. Redeploy the triggers
3. Create a new azure-devops-pipeline that uses the `.yml` file you uploaded. Make sure this is located in the `adf_publish` branch!
There are still 2 variables to be filled in and those are your two ADF names.
Now you can save and run your azure-devops-pipeline for the first time!
4. If you go to your `PRD` data factory you will see this new adf-pipeline. 
However, our activity is still linked to our `DEV` function app, which is not ideal!

5. On the `adf_publish` branch, there should be a file named: `ARMTemplateParametersForFactory.json`.
Try and find it, in there you should see three parameters:
   1. One that represents the factory name
   2. One that represents the function key
   3. One that represents the function app url.
6. In your azure-devops-pipeline you can find where the parameter `factoryName` is overwritten.
Add the other ones there and set them to the correct values regarding your function app in `PRD`.
7. Save the pipeline and check if it succeeds. If it does, go check one last time in your `PRD` ADF
if the reference is correct. You can check this under the *manage* section and the *Linked services* tab.


## Congratulations
If you made it here you have succeeded in creating a best practice 
CI/CD pipeline for ADF's in two different pillars/environments. 
As you noticed this exercise is a simplification and in the real world it is often more complex.
However, the principles stay the same! 

