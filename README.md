# Intelligent Test Automation Framework

## Description
A modular, BDD-style test automation framework using Cucumber for business-readable test cases and Playwright for execution.

An LLM is also integrated to auto-generate `.feature` files from natural language. In addition, Pega is connected by plugin to extract case type flow and generate base Gherkin templates.


## Generating Features With Natural Language
**Single-time setup:**

First create the dotenv file with your secret openai API key. The LLM will not work without this.

The file must be in the main folder. Example path: `/.env`

Make sure the file is in the format:

```
OPENAI_API_KEY=[your key here]
```

**Every time you run:**

Run the `generate.py` file. Follow the prompts to input your feature specifications in natural language. Your generated .feature file should be in `hellocucumber/features/` with gherkin syntax.


## Generating Tests With Pega Integration
UNIMPLEMENTED


## Testing with Cucumber-Playwright Integration
All features and step definitions are inside the `/hellocucumber` folder. 

All tests should be run from this folder.


### Make Tests
After generating your features, use `/hellocucumber/features/step_definitions/stepdefs.js`


Select which browser to run your tests on by launching, creating a new context, then a new page.


This is the page object, and all actions performed are using this page object.


Before you can test, you must implement steps that do not follow the existing common steps.


The fastest way to see which steps still need to be created is to run:

`npm test`

The output should include undefined steps and code snippets.

Example:
```
? Given today is Sunday
       Undefined. Implement with the following snippet:

         Given('today is Sunday', function () {
           // Write code here that turns the phrase above into concrete actions
           return 'pending';
         });
```
Use the code snippet inside stepdefs.js and implement your test.

To implement each step, use [Playwright](https://playwright.dev/docs/writing-tests).

Once all steps are implemented, you can run your tests.


### Run Tests

To run cucumber-js, type: `npm test`

By default, every .feature file in `/hellocucumber/features` is run.


### Reporting
Each test automatically generates a command-line output, an html output and a json output.

Generated reports are inside `/hellocucumber/reports`

For reference on detailed step results, visit [step results page.](https://cucumber.io/docs/cucumber/api#step-results)


## Dependencies
**You must install the following dependencies:**
Languages/Runtime env:
- Javascript/Typescript
- Python
- Node.js + npm
Packages/Libraries:
- Cucumber (@cucumber/cucumber on npm) - [Installation Page](https://cucumber.io/docs/installation/)
- Playwright (npm) - [Installation Page](https://playwright.dev/docs/intro)
- openai (python)