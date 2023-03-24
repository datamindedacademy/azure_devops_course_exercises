
## Echo
In these set of small exercises we will become a little more familiar with the concepts of a YAML pipeline.

1. Create a new pipeline and select your own forked repository as a starting point.
2. You can select the starter pipeline for now.
3. Rename the pipeline to `*YOUR_NAME*_echo_pipeline`.
4. Save and Run.
5. Check the output of the pipeline

Let's inspect the pipeline for a second and make some changes to it.

1. Create a parameter with the name `myName` and make sure it is a string.
2. Give it a default value.
3. Pass several possible values to choose from.
4. Alter the first script step, and instead of `echo Hello, world!`, 
write `echo Hello *REFERENCE_YOUR_PARAM*`
5. Save and Run

Until now everything was done in a single stage, in a single job, lets change that!

1. Make sure we have a single stage and 2 separate jobs. 
The steps that were already defined can stay in the same and first job.
2. Let's define the pool, in the jobs itself. 
For the first job we can use the vmImage `ubuntu-latest`.
3. For the second job, you can use the vmImage: `windows-latest`.
4. Let's define a script step in the second job that shows the current path.
   (TIP: just look at the command line command for this, only 3 letters are required)
5. Save and Run.

Suppose that our first job has some output we want to use in our second.
Let's simulate this! 

1. In the first step where its says `echo Hello *REFERENCE_YOUR_PARAM*`, change this line too: `echo "##vso[task.setvariable variable=myOutputVar;isOutput=true]*YOUR_PARAMETER*"`.
On the line below, add `name: producedVar`. This will make sure that the task has an output variable with the name `myOutputVar` and the value: *YOUR_PARAMETER* and that we can reference it through `producedVar`.
2. Let's make sure our second job depends on our first.
3. In our script of the second job, lets now try and reference the variable we set in the first job.
   (If you are stuck, try and google it first!)
4. Save and run

Good job! I think you are ready for the big exercise now!