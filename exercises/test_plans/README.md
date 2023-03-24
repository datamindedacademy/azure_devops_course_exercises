# Hands On Azure Test Plans


## Introduction
As in every project testing is so important. In these hands on we will take 
a small glimpse of what is possible with azure test plans.

## Creating a test case

1. Go to your board and find the issue “$NAME$ Hands on: Test Plans”
2. Create a new test for this issue 
3. The goal of this test is to see the working of the azure function without giving a name, and thus an anonymous API call so to say. and it can be seen as an end-to-end test. 
   1. Give it a good title 
   2. Fill in the description 
   3. Assign it to yourself 
   4. Check the status on design 
   5. Create two steps 
      1. The actual API call (use the world url)
      2. The verification step
4. Also link the epic you created (use the link Tests for the wanted result).
5. Check the iteration ,and select your correct sprint

## Sharing Parameters

1. Create another test case where the goal: “also do an API call but this time with a param given (a name).”
2. Make sure this time you add a sharable param named URL (add your name as well, might get confusing otherwise)
3. Use this param in your previous test case as well.
4. Make the complete step that uses this param a sharable step
5. Insert the step in the other test case as well.

## Running the tests

1. Go to the test plans view
2. Find your correct test plan (linked to the issue)
3. Create a graph that show you the outcome of both tests created.
4. Run the tests as a web application.
5. Do the actual testing, go to the URLS provided by the instructors
6. Check the graph again and see how you did.


## Creating automated tests

In this exercise we will export our test results to test plans.
We have already built a YAML pipeline that has a testing stage.
The goal is to expand this stage such that we export our test results to Azure test plans.
For this to happen 2 changes are required.
TIP: How to do this can be found in the microsoft documentation.

1. Adapt script step where with the command: `pytest $(functionsDirectory)`.
This step should export an xml file now for the coverage as well as the test result.
2. Another task should be added where the xml file and test results are exported.


Rerun the pipeline and check the results in the `Runs` view of the test plans.


