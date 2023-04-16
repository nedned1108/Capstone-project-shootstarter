const puppeteer = require('puppeteer');
const fs = require('fs').promises;

const reactCrawler = async (url) => {
  // Launch a new browser
  const browser = await puppeteer.launch();
  // Open a new page
  const page = await browser.newPage();
  // Go to the url
  await page.goto(url, {
    // Wait until the page is fully loaded
    waitUntil: 'networkidle2',
  });
  // Get the html of the page
  const html = await page.content();
  // Save the html to a file
  await browser.close();
  return html;
}
