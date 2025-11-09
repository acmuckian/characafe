## Table of Contents
- [Performance](#performance)

- [Browser Compatibility](#browser-compatibility)
- [Responsiveness](#responsiveness)

- [Code Validation](#code-validation)

- [Testing](#testing)
  - [Automated Testing](#automated-testing)
   - [Manual Testing](#manual-testing)
  - [Features Testing](#features-testing)


## Performance

### Google Lighthouse Performance

[Google Lighthouse](https://developers.google.com/web/tools/lighthouse) was used to test the performance of the website.

![screenshot of google lighthouse desktop score]()

The main limitation was file sizes - particularly since this is an image board website since users can upload files which are quite large. In future, attempts will be made to limit 

## Browser Compatibility

| Browser | Responsive |
|---------|------------|
| Chrome  | Yes        |
| Mozilla |    Yes       |
| Safari  |  Yes         |

## Responsiveness 

The website was tested across different browsers. It was also tested on a MacBook Pro version 12.7.6 and an iPhone 8. 

The website was tested on different mobiles and tablets, including by using Google's DevTools:

* Galaxy Note 20 Android 11
* iPad iPad OS 14.7.1 
* iPhone 11 Pro iOS 14.6

## Code Validation 

### HTML 

[HTML W3C Validator](https://validator.w3.org/nu/) was used to validate the HTML files. 

* [Home Page]() - no errors/warnings found 
* [Menu Page]() - some of the images had no errors/warnings to show. 
* [Products Page]() - 
* [Product Detail Page]() - no errors/warnings found
* [Wishlist Page]() - 
* [Checkout Page]() - 
* [Login Page]() - 
* [Sign Up Page]() - 
* [Logout Page]() - 


### Javascript 

[JSHint](https://jshint.com/) was used to check the validity of the javascript on stripe_elements.js 

### CSS 

[Jigsaw CSS](https://jigsaw.w3.org/css-validator/) was used to validate the CSS via a direct upload of the styles.css file. There were no errors and 8 warnings. 

### Python 

[PEP8 CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python code by PEP8 standards.

- 
## Testing 

### Automated Testing 

Automated testing was performed for some of views and forms for both img and contact. Due to time constraints, only six tests were made - these six tests passed with OK. 

### Manual Testing



## Features Testing 
|                         **Home   Page**                         |            |
|:---------------------------------------------------------------:|:----------:|
| **Feature**                                                     | **Status** |
| Clicking   Characafe brings up home page                        | Yes        |
| clicking   contact leads to contact page                        | Yes        |
| clicking   menu leads to menu page                              | Yes        |
| clicking   menu leads to characters page                        | Yes        |
| navbar   shows username when logged in                          | Yes        |
| dropdown   beside avatar shows profile, wishlist and logout     | Yes        |
| click   logout goes to logout page                              | Yes        |
| clicking   profile goes to profile page                         | Yes        |
| clicking   shopping bag icon shows bag page                     | Yes        |
| **carousel  **                                                  |            |
| clicking   right on the carousel shows next slide               | Yes        |
| clicking   right on the carousel shows slide before             | Yes        |
| carousel   moves independently                                  | Yes        |
| **menu  **                                                      |            |
| menu   icons spin when hovered over                             | Yes        |
| **footer**                                                      |            |
| clicking   social media icons open social media page in new tab | Yes        |
| can't   subscribe unless you enter text                         | Yes        |
| can't   subscribe without entering an email address             | Yes        |

| **Shop   Main Page**                                                            |            |
|---------------------------------------------------------------------------------|------------|
| **Feature**                                                                     | **Status** |
| Adding   product to wishlist notifies you it was added                          | Yes        |
| adding   product to bag updates the bag                                         | Yes        |
| adding   product to bag notifies that it was added                              | Yes        |
| adding   product to bag notification shows you a summary of what is in the bag  | Yes        |
| clicking   on product image brings you to product page                          | Yes        |
| clicking   on product title brings you to product page                          | Yes        |
| sorting   price low to high shows lowest priced item first                      | Yes        |
| sorting   name Z-A shows name order Z-A                                         | Yes        |
| sorting   name A-Z shows name order A-Z                                         | Yes        |
| sorting   rating high to low shows product with highest ratings first           | Yes        |

| **Contact   Page**                                                                                          |            |
|-------------------------------------------------------------------------------------------------------------|------------|
| **Feature**                                                                                                 | **Status** |
| inserting   text but not an email address on the contact page prompts for an email   address to be inserted | Yes        |
| contact   submit shows contact modal                                                                        | Yes        |
| cannot   subscribe without inserting email                                                                  | Yes        |
| must be   an email address for subscription                                                                 | Yes        |
| clicking   submit triggers a modal notification for the subscription                                        | Yes        |
| clicking   submit triggers a modal notification for the message being sent                                  | Yes        |
## Bugs 
