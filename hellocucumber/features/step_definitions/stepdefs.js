const assert = require('assert');
const { Given, When, Then, Before, After, setDefaultTimeout } = require('@cucumber/cucumber');
const { chromium, WebKit, Firefox, expect } = require('@playwright/test');
const { Page } = require("playwright");

let chrome, webkit, firefox, page;

setDefaultTimeout(30*1000);

Before(async function () {
            chrome = await chromium.launch({ headless: false });
            //webkit = await WebKit.launch();
            //firefox = await Firefox.launch();
            const context = await chrome.newContext();
            page = await context.newPage();
         });

Given('I am on the {string} page', async function (string) {
           // Write code here that turns the phrase above into concrete actions
           await page.goto(string);
         });
When('I enter {string} into the {string} field', async function (string, string2) {
           // Write code here that turns the phrase above into concrete actions
           await page.getByLabel(string2).fill(string);
           //await page.getByPlaceholder("").fill("Hello");
         });
When('I click on {string}', async function (button) {
           // Write code here that turns the phrase above into concrete actions
           await page.getByRole('button', { name: button }).click();
         });
Then('I should see {string} as the application status', async function (expectedText) {
           // Write code here that turns the phrase above into concrete actions
            await expect(page.getByText(expectedText)).toBeVisible();
         });