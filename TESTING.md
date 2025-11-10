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
* [Menu Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcharacafe-1eb4a9dff267.herokuapp.com%2Fmenu) - no errors found
* [Products Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcharacafe-1eb4a9dff267.herokuapp.com%2Fproducts) - no errors found
* [Product Detail Page]() - no errors/warnings found
* [Wishlist Page]() - 
* [Checkout Page]() - 
* [Profile Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcharacafe-1eb4a9dff267.herokuapp.com%2Fprofiles%2F) - one info on input tag, no errors 
* [Contact Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcharacafe-1eb4a9dff267.herokuapp.com%2Fcontact%2F) - errors related to crispy forms formulation and it couldn't be avoided with time constraints 
* [Login Page]() - 
* [Sign Up Page]() - 
* [Logout Page]() - 


### Javascript 

[JSHint](https://jshint.com/) was used to check the validity of the javascript on stripe_elements.js 

### CSS 

[Jigsaw CSS](https://jigsaw.w3.org/css-validator/) was used to validate the CSS via a direct upload of the styles.css file. There were no errors and 8 warnings. 

### Python 

[PEP8 CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python code by PEP8 standards.

**Checkout**

- _admin.py_ - no errors found
- _forms.py_ - no errors found
- _models.py - no errors found 
- _signals.py_ - no errors found 
- _views.py_ - 

**Products** 

- _admin.py_ - no errors found
- _forms.py_ - no errors found 
- _models.py_ - no errors found
- _views.py_ - no errors found 

**Bag**

- 


**Home**

- _models.py_ - no errors found 
- _views.py_ - no errors found 

**Contact** 

- _forms.py_ - no errors found
- _models.py_ - no errors found 
- _views.py_ - no errors found 
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

| **Products   Detail Page**                                              |            |
|--------------------------------------------------------------------------|------------|
| **Feature**                                                              | **Status** |
| Cannot add quantity below 0                                              | Yes        |
| Clicking   keep shopping returns to shop main page                       | Yes        |
| Clicking add to bag adds item to bag                                     | Yes        |
| Clicking add to bag shows toast                                          | Yes        |
| "You   might also like" shows items with that character in it            | Yes        |
| A visitor can add a comment                                              | Yes        |
| A   visitor can edit or delete their comment                             | Yes        |
| Clicking   on a related product image brings user to product's home page | Yes        |
| Unable   to add to bag for unavailable products                          | Yes        |
| Adding   to wishlist notifies you it was added to wishlist               | Yes        |

| **Checkout   Page**                                                                                              |            |
|------------------------------------------------------------------------------------------------------------------|------------|
| **Feature**                                                                                                      | **Status** |
| cannot   complete order without putting in name, email, phone no., street address,   town/city, county, country  | Yes        |
| cannot   complete order without card details                                                                     | Yes        |
| cannot   put in an invalid card number                                                                           | Yes        |
| told   correct amount charged                                                                                    | Yes        |
| side   column shows my orders, the product, name, quantity, sub-total and the total                              | Yes        |
| successful   details completion triggers loading overlay and checkout success page                               | Yes        |
| **Checkout   Success Page **                                                                                     |            |
| toast   shows my order no and that confirmation email sent                                                       | Yes        |
| order   shows my delivery information as I inserted it                                                           | Yes        |
| billing   info shows the amount, delivery fee, grand total                                                       | Yes        |
| clicking   rest of range button brings to product page                                                           | Yes        |

## Bugs 
