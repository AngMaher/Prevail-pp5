# Testing

Return back to the [README.md](README.md) file.

Throughout the development of this project, I've carried out numerous tests to ensure that the site works well. In this section you will find documentation of all tests carried out throughout the site.

## Code Validation

I have validated all of my code using the recommended tools for each language.

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot]() | Pass: No Errors |
| All Products  | ![screenshot]() | Pass: No Errors |
| Product Detail | ![screenshot]() | Pass: No Errors |
| How it works  | ![screenshot]() | Pass: No Errors |
| Success Stories | ![screenshot]() | Pass: No Errors |
| Story Detail| ![screenshot]() | Pass: No Errors |
| Sign Up | ![screenshot]() | Pass: No Errors |
| Sign In | ![screenshot]() | Pass: No Errors |
| Log Out | ![screenshot]() | Pass: No Errors |
| Basket | ![screenshot]() | Pass: No Errors |
| Checkout | ![screenshot]() | () |
| Checkout Success | ![screenshot]() | Pass: No Errors |
| Profile | ![screenshot]() | Pass: No Errors |
| Add Product | ![screenshot]() | Pass: No Errors |
| Edit Product | ![screenshot]() | Pass: No Errors |
| Delete Product | ![screenshot]() | Pass: No Errors |
| List Categories  | ![screenshot]() | Pass: No Errors |
| Add Category | ![screenshot]() | Pass: No Errors |
| Edit Category | ![screenshot]() | Pass: No Errors |
| Delete Category | ![screenshot]() | Pass: No Errors |
| Add Success Story | ![screenshot]() | Pass: No Errors |
| Edit Success Story | ![screenshot]() | |
| Delete Success Story | ![screenshot]() | Pass: No Errors |
| Classes | ![screenshot]() | Pass: No Errors |
| Class Detail | ![screenshot]() | Pass: No Errors |
| Add Class | ![screenshot]() | Pass: No Errors |
| Edit Class | ![screenshot]() | Pass: No Errors |
| Delete Class | ![screenshot]() | Pass: No Errors |
| Membership | ![screenshot]() | Pass: No Errors |
| Membership form | ![screenshot]() | Pass: No Errors |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| style.css | ![screenshot]() | Pass: No Errors |
| checkout.css | ![screenshot]() | Pass: No Errors |
| profile.css | ![screenshot]() | Pass: No Errors |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| konami-code.js | ![screenshot]() | Pass: No Errors |
| countryfields.js | ![screenshot]() | Pass: No Errors |
| add_post.html (postloadjs) | ![screenshot]() | Pass: No Errors |
| edit_post.html (postloadjs) | ![screenshot]() | Pass: No Errors |
| add_product.html (postloadjs) | ![screenshot]() | Pass: No Errors |
| edit_product.html (postloadjs) | ![screenshot]() | Pass: No Errors |
| products.html (postloadjs) | ![screenshot]() | Pass: No Errors |
| basket.html (postloadjs) | ![screenshot]() | Pass: No Errors |
| quantity_input_script.html (script) | ![screenshot]() | Pass: No Errors |
| stripe_elements.js | ![screenshot]() | Undefined Stripe variable |

### Python

I have used the recommended [CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | Screenshot | Notes |
| --- | --- |
| Basket contexts.py  ![screenshot]() | Pass: No Errors |
| Basket urls.py | ![screenshot]() | Pass: No Errors |
| Basket views.py | ![screenshot]() | Pass: No Errors |
| Blog admin.py |  ![screenshot]() | Pass: No Errors |
| Blog forms.py | ![screenshot]() | Pass: No Errors |
| Blog models.py | ![screenshot]() | Pass: No Errors |
| Blog urls.py | ![screenshot]() | Pass: No Errors |
| Blog views.py | ![screenshot]() | Pass: No Errors |
| Checkout admin.py | ![screenshot]() | Pass: No Errors |
| Checkout forms.py |  ![screenshot]() | Pass: No Errors |
| Checkout models.py | ![screenshot]() | Pass: No Errors |
| Checkout signals.py | ![screenshot]() | Pass: No Errors |
| Checkout urls.py | ![screenshot]() | Pass: No Errors |
| Checkout views.py | ![screenshot]() | Pass: No Errors |
| Checkout webhook_handler.py | ![screenshot]() | Pass: No Errors |
| Checkout webhooks.py | ![screenshot]() | Pass: No Errors |
| Contact admin.py | ![screenshot]() | Pass: No Errors |
| Contact forms.py | ![screenshot]() | Pass: No Errors |
| Contact models.py | ![screenshot]() | Pass: No Errors |
| Contact urls.py | ![screenshot]() | Pass: No Errors |


## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot]() | Works as expected |
| Firefox | ![screenshot]() | Works as expected |
| Edge | ![screenshot]() | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/testing/responsive-mobile.png) ![screenshot](documentation/testing/responsive-mobile-menu.png) ![screenshot](documentation/testing/responsive-mobile-products.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/testing/responsive-tablet.png) ![screenshot](documentation/testing/responsive-tablet-menu.png) ![screenshot](documentation/testing/responsive-tablet-products.png) | Works as expected |
| Laptop | ![screenshot](documentation/testing/responsive-laptop.png) ![screenshot](documentation/testing/responsive-laptop-products.png) | Works as expected |
| Desktop | ![screenshot](documentation/testing/responsive-desktop.png) ![screenshot](documentation/testing/responsive-desktop-products.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Desktop | ![screenshot]() | No major warnings |
| Home | Mobile | ![screenshot]() | Some minor warnings |
| All Products | Desktop | ![screenshot](documentation/testing/lighthouse-all-products-desktop.png) | Some minor warnings |
| All Products | Mobile | ![screenshot](documentation/testing/lighthouse-all-products-mobile.png) | Some minor warnings |
| Individual Product | Desktop | ![screenshot](documentation/testing/lighthouse-product-desktop.png) | No major warnings |
| Individual Product | Mobile | ![screenshot](documentation/testing/lighthouse-product-mobile.png) | Some minor warnings |
| Contact | Desktop | ![screenshot](documentation/testing/lighthouse-contact-desktop.png) | No major warnings |
| Contact | Mobile | ![screenshot](documentation/testing/lighthouse-contact-mobile.png) | Some minor warnings |
| Blog | Desktop | ![screenshot](documentation/testing/lighthouse-blog-desktop.png) | No major warnings |
| Blog | Mobile | ![screenshot](documentation/testing/lighthouse-blog-mobile.png) | Some minor warnings |
| Blog Post | Desktop | ![screenshot](documentation/testing/lighthouse-blog-post-desktop.png) | No major warnings |
| Blog Post | Mobile | ![screenshot](documentation/testing/lighthouse-blog-post-mobile.png) | Some minor warnings |
| Sign Up | Desktop | ![screenshot](documentation/testing/lighthouse-signup-desktop.png) | No major warnings |
| Sign Up | Mobile | ![screenshot](documentation/testing/lighthouse-signup-mobile.png) | Some minor warnings |
| Sign In | Desktop | ![screenshot](documentation/testing/lighthouse-login-desktop.png) | No major warnings |
| Sign In | Mobile | ![screenshot](documentation/testing/lighthouse-login-mobile.png) | Some minor warnings |
| Password Reset | Desktop | ![screenshot](documentation/testing/lighthouse-password-reset-desktop.png) | No major warnings |
| Password Reset | Mobile | ![screenshot](documentation/testing/lighthouse-password-reset-mobile.png) | Some minor warnings |
| Search | Desktop | ![screenshot](documentation/testing/lighthouse-search-desktop.png) | No major warnings |
| Search | Mobile | ![screenshot](documentation/testing/lighthouse-search-mobile.png) | Some minor warnings |
| Log Out | Desktop | ![screenshot](documentation/testing/lighthouse-logout-desktop.png) | No major warnings |
| Log Out | Mobile | ![screenshot](documentation/testing/lighthouse-logout-mobile.png) | Some minor warnings |
| Basket | Desktop | ![screenshot](documentation/testing/lighthouse-basket-desktop.png) | No major warnings |
| Basket | Mobile | ![screenshot](documentation/testing/lighthouse-basket-mobile.png) | Some minor warnings |
| Checkout | Desktop | ![screenshot](documentation/testing/lighthouse-checkout-desktop.png) | No major warnings |
| Checkout | Mobile | ![screenshot](documentation/testing/lighthouse-checkout-mobile.png) | Some minor warnings |
| Checkout Success | Desktop | ![screenshot](documentation/testing/lighthouse-checkout-success-desktop.png) | Some minor warnings |
| Checkout Success | Mobile | ![screenshot](documentation/testing/lighthouse-checkout-success-mobile.png) | Some minor warnings |
| Profile | Desktop | ![screenshot](documentation/testing/lighthouse-profile-desktop.png) | No major warnings |
| Profile | Mobile | ![screenshot](documentation/testing/lighthouse-profile-mobile.png) | Some minor warnings |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| **Home Page** | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Shop Now button | Redirection to All Products page | Pass | |
| | Enter Konami code correctly on keyboard | Sound plays and modal pops up giving discount code | Pass | |
| | Enter Konami code incorrectly on keyboard | Nothing | Pass | |
| **All Products Page** | | | | |
| | Click on All Products link in navbar | Redirection to All Products page | Pass | |
| | Click on All Products By Price link in navbar | Redirection to All Products page | Pass | Products sorted by price low to high |
| | Click on All Products By Platform link in navbar | Redirection to All Products page | Pass | Products sorted by platform with platform sorted A-Z |
| | Click on All Products By Release Year link in navbar | Redirection to All Products page | Pass | Products sorted by release year old - new |
| | Click on Games By Nintendo link in navbar | Redirection to All Products page | Pass | Products filtered to Games on Nintendo consoles |
| | Click on Games By Sega link in navbar | Redirection to All Products page | Pass | Products filtered to Games on Sega consoles |
| | Click on Games By Sony link in navbar | Redirection to All Products page | Pass | Products filtered to Games on Sony consoles |
| | Click on Consoles By Nintendo link in navbar | Redirection to All Products page | Pass | Products filtered to Nintendo consoles |
| | Click on Consoles By Sega link in navbar | Redirection to All Products page | Pass | Products filtered to Sega consoles |
| | Click on Consoles By Sony link in navbar | Redirection to All Products page | Pass | Products filtered to Sony consoles |
| | Click on Price (low to high) in Sort by... dropdown | Redirection to All Products page | Pass | Products sorted by price low to high |
| | Click on Price (high to low) in Sort by... dropdown | Redirection to All Products page | Pass | Products sorted by price high to low |
| | Click on Name (A-Z) in Sort by... dropdown | Redirection to All Products page | Pass | Products sorted alphabetically A-Z |
| | Click on Name (Z-A) in Sort by... dropdown | Redirection to All Products page | Pass | Products sorted alphabetically Z-A |
| | Click on Year (oldest to newest) in Sort by... dropdown | Redirection to All Products page | Pass | Products sorted by release year old to new |
| | Click on Year (newest to oldest) in Sort by... dropdown | Redirection to All Products page | Pass | Products sorted by release year new to old |
| | Click on Platform (A-Z) in Sort by... dropdown | Redirection to All Products page | Pass | Products sorted by platform A-Z |
| | Click on Platform (Z-A) in Sort by... dropdown | Redirection to All Products page | Pass | Products sorted by platform Z-A |
| | Click on Product card image | Redirection to Product Detail page for that product | Pass | |
| | Click on Product card name | Redirection to Product Detail page for that product | Pass | |
| | Click on Add to basket button | Product added to basket | Pass | Single quantity added to basket |
| | Click on disabled Add to basket button | Nothing | Pass | |
| | Click on edit product button | Redirection to Edit Product page for that product | Pass | Button only appears if logged in user is an admin |
| | Click on delete product button | Redirection to Delete Product confirmation page for that product | Pass | Button only appears if logged in user is an admin |
| **Product Detail Page** | | | | |
| | Click on Product image or name in all products page | Redirection to Product Detail page | Pass | |
| | Click on Keep Shopping button | Redirection to All Products page | Pass | |
| | Click + button on quantity selector form | Quantity number increases if number + 1 is less than or equal to product's stock | Pass | |
| | Click - button on quantity selector form | Quantity number decreases if current quantity is greater than one | Pass | |
| | Click + button on quantity selector form if quantity is at the product's stock | Nothing | Pass | |
| | Manually enter number greater than product stock in quantity selector form | Error message appears letting the user know what the product's stock is | Pass | |
| | Click Add To Basket button | Product is added to basket and quantity is set to the user's choice | Pass | |
| | Click Add To Basket button when user already has the product in their basket | Quantity selected is added to the existing quantity in the user's basket for the product | Pass | Only applicable if quantity being added plus existing quantity remains less than or equal to product's stock |
| | Click Add To Basket button when user already has the product in their basket and quantity selected plus existing quantity is greater than product's stock | Message appears informing user that they're trying to add more quantity than the product has in stock and nothing is added | Pass | |
| | Click on edit product button | Redirection to Edit Product page for that product | Pass | Button only appears if logged in user is an admin |
| | Click on delete product button | Redirection to Delete Product confirmation page for that product | Pass | Button only appears if logged in user is an admin |
| **Search** | | | | |
| | Enter word into search bar that appears in at least one product's name or description | Redirection to Products page | Pass | Products filtered to only show products containing search term |
| | Enter word into search bar that doesn't appear in any product's name or description | Redirection to Products page | Pass | Products page is empty and shows user that 0 products were returned |
| | Enter nothing into search bar | Redirection to Products page | Pass | Error message shows and lets user know they entered nothing into the search bar and all products are displayed |
| **Contact Page** | | | | |
| | Click on Contact Us link in footer | Redirection to Contact Us page | Pass | |
| | Enter name | Form will only submit if all fields are filled | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message | Form will only submit if all fields are filled | Pass | |
| | Click Send with missing fields | Message lets user know all fields are required | Pass | |
| | Click Send with all valid fields | User is sent email confirming their message has been received and new ticket is created in open tickets page for admin | Pass | |
| **Blog Page** | | | | |
| | Click on the Blog link in nav menu | Redirection to Blog page | Pass | |
| | Click on the Blog link in footer | Redirection to Blog page | Pass | |
| | Click on Blog post | Redirection to Blog Post page | Pass | |
| | Click on edit blog button | Redirection to Edit Blog page for that post | Pass | Button only appears if logged in user is an admin |
| | Click on delete blog button | Redirection to Delete Blog confirmation page for that post | Pass | Button only appears if logged in user is an admin |
| **Blog Post** | | | | |
| | Click on Blog post on blog page | Redirection to Blog Post page | Pass | |
| | Click hollow heart icon | Alert pops up confirming post has been liked, heart icon turns solid red and like count increases by 1 | Pass | Only if user is logged in, nothing happens if logged out |
| | Click filled in heart icon | Alert pops up confirming post has been unliked, heart icon turns hollow and like count decreases by 1 | Pass | |
| | Click Submit button under comment form | Comment added to post | Pass | Comment only added if field is filled |
| | Click Submit button under empty comment form | Message appears for user informing them they need to fill the body field | Pass | |
| | Click on edit blog button | Redirection to Edit Blog page for that post | Pass | Button only appears if logged in user is an admin |
| | Click on delete blog button | Redirection to Delete Blog confirmation page for that post | Pass | Button only appears if logged in user is an admin |
| **Sign Up Page** | | | | |
| | Click on Register button under account on nav menu | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click Sign Up button on sign up page | Sends confirmation email and lets user know to check their email | Pass | |
| | Click link in confirmation email | Redirects user to sign in page | Pass | |
| **Sign In Page** | | | | |
| | Click on the Login button under account on nav menu | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button on login page | Redirects user to homepage | Pass | |
| | Click Forgot Password | Redirects user to password reset page | Pass | |
| | Sign in before confirming account | Redirects to message reminding user to confirm email address | Pass | |
| **Password Reset Page** | | | | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Click Reset Password button | Sends email with instructions to reset password | Pass | |
| **Log Out Page** | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| **User Profile Page** | | | | |
| | Click on the My Profile link under account on nav menu | Redirection to User profile page page | Pass | Only shows for logged in users |
| | Click Update Information button | Saves form contents to be default information for user | Pass | Default information is cleared if form is submitted while blank |
| | Click Order Number for previous order in Order History | Redirects user to order confirmation page for that order | Pass | |
| | Brute forcing the URL to profile if not logged in | User given an error | Pass | Redirects user to error page |
| **Basket** | | | | |
| | Click Basket icon in main nav | Redirects user to basket page | Pass | Shows back to shop button if basket is empty |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| | Click + button on quantity selector form | Quantity number increases if number + 1 is less than or equal to product's stock | Pass | |
| | Click - button on quantity selector form | Quantity number decreases if current quantity is greater than one | Pass | |
| | Click + button on quantity selector form if quantity is at the product's stock | Nothing | Pass | |
| | Click update button under quantity selector form | Updated quantity of product in basket to number in quantity select form | Pass | |
| | Click remove button under quantity selector form | Removes product from basket completely | Pass | |
| | Manually enter number greater than product stock in quantity selector form | Error message appears letting the user know what the product's stock is | Pass | |
| | Click on discount apply button with empty discount field | Message appears letting user know the field can't be blank | Pass | |
| | Click on discount apply button with invalid code in the discount field | Error message shows letting user know the code entered doesn't exist | Pass | |
| | Click on discount apply button with valid code in the discount field | Alert message shows letting user know the discount has been added | Pass | |
| | Discount code added successfully | Percentage gets taken off the basket total, discount form is replaced with discount amount | Pass | |
| | Click on trash icon next to discount amount | Discount removed and discount code form reappears in place of discount amount | Pass | |
| | Remove item from basket that brings total to below €50 | Delivery goes from FREE to 10% of the total cost of the basket contents | Pass | |
| | Click on Keep Shopping button | Redirection to All Products page | Pass | |
| | Click on Secure Checkout button | Redirection to checkout page | Pass | |
| **Checkout** | | | | |
| | Click on Secure Checkout button in basket | Redirection to checkout page | Pass | |
| | Click Complete Order button without all required fields filled out | Message letting user know that required fields need to be filled out | Pass | |
| | Click Save delivery information to profile button | User's default information will be set to whatever is filled in at the checkout on order completion | Pass | Only visible to logged in users |
| | Click on Create an account link | Redirection to sign up page | Pass | Only visible to logged out users |
| | Click on login link | Redirection to sign in page | Pass | Only visible to logged out users |
| | Click Complete Order button without card details filled out | Message letting user know that their card number is incomplete | Pass | |
| | Click Complete Order button with all details filled out | Loading spinner appears and order is processed | Pass | |
| | Order completed | Order confirmation email is sent to the user and redirection to checkout success page | Pass | |
| **Checkout Success Page** | | | | |
| | Order completed | Redirection to checkout success page | Pass | |
| | Click Checkout latest deals button | Redirects user to all products page | Pass | Only visible if user comes to this page straight from order completion |
| | Click Back to profile button button | Redirects user to their profile | Pass | Only visible if user comes to this page from the order history list on their profile |
| **Add Product Page** | | | | |
| | Click Add New Product link from Admin dropdown | Redirects admin to add product page | Pass | User can only see this if they're logged in as an admin |
| | Click Cancel button | Redirects admin to all products page | Pass | |
| | Click Add Product button with form filled correctly | Creates a new product on the site using the information provided | Pass | |
| | Click Add Product button with form filled incorrectly | Message appears letting the admin know to fill in the required form fields | Pass | |
| | Set product's stock to be less than 1 | Product will be created but appear on the site as sold out with add to basket button disabled | Pass | |
| | Click Add Product button with no image set | Product will be created but will be displayed with default product image | Pass | |
| | Brute forcing the URL to add a new product if not an admin | User given an error | Pass | Redirects user to error page |
| **Edit Product Page** | | | | |
| | Click edit icon on product | Redirects user to Edit Product page | Pass | User must be an admin to see icon and access this page |
| | Click Cancel button | Redirects admin to all products page | Pass | |
| | Click Update Product button with form filled correctly | Updates product with information provided | Pass | |
| | Click Update Product button with form filled incorrectly | Message appears letting the admin know to fill in the required form fields | Pass | |
| | Set product's stock to be less than 1 | Product will be updated but appear on the site as sold out with add to basket button disabled | Pass | |
| | Click Update Product button with no image set | Product will be updated but will be displayed with default product image | Pass | |
| | Brute forcing the URL to edit a product if not an admin | User given an error | Pass | Redirects user to error page |
| **Delete Product Page** | | | | |
| | Click delete icon on product | Redirects user to Edit Product page | Pass | User must be an admin to see icon and access this page |
| | Click Cancel button | Redirects admin to product detail page for selected product | Pass | |
| | Click Delete Product button | Product will be completely deleted from the site | Pass | |
| | Brute forcing the URL to delete a product if not an admin | User given an error | Pass | Redirects user to error page |
| **Add Blog Page** | | | | |
| | Click Add New Blog Post link from Admin dropdown | Redirects admin to add blog page | Pass | User can only see this if they're logged in as an admin |
| | Click Cancel button | Redirects admin to blog | Pass | |
| | Click Add Post button with form filled correctly | Creates a new blog post on the site using the information provided | Pass | |
| | Click Add Post button with form filled incorrectly | Message appears letting the admin know to fill in the required form fields | Pass | |
| | Click Add Post button with no image set | Blog post will be created but will be displayed with default blog post image | Pass | |
| | Brute forcing the URL to add a new blog post if not an admin | User given an error | Pass | Redirects user to error page |
| **Edit Blog Page** | | | | |
| | Click edit icon on blog post | Redirects user to Edit Blog Post page | Pass | User must be an admin to see icon and access this page |
| | Click Cancel button | Redirects admin to blog | Pass | |
| | Click Update Post button with form filled correctly | Updates blog post with information provided | Pass | |
| | Click Update Post button with form filled incorrectly | Message appears letting the admin know to fill in the required form fields | Pass | |
| | Click Update Post button with no image set | Blog post will be updated but will be displayed with default blog post image | Pass | |
| | Brute forcing the URL to edit a blog post if not an admin | User given an error | Pass | Redirects user to error page |
| **Delete Blog Page** | | | | |
| | Click delete icon on blog post | Redirects user to Delete Blog post page | Pass | User must be an admin to see icon and access this page |
| | Click Cancel button | Redirects admin to blog | Pass | |
| | Click Delete Post button | Blog post will be completely deleted from the site | Pass | |
| | Brute forcing the URL to delete a blog post if not an admin | User given an error | Pass | Redirects user to error page |
| **Open Tickets Page** | | | | |
| | Click View Open Tickets link from Admin dropdown | Redirects admin to open tickets | Pass | User can only see this if they're logged in as an admin |
| | Click Close Ticket button on ticket | Marks ticket as seen and removes it from list of open tickets | Pass | If last open ticket is closed the page will contain just a header saying No Open Tickets |
| | Brute forcing the URL to access open ticket page if not an admin | User given an error | Pass | Redirects user to error page |
| **Footer** | | | | |
| | Click Blog link in footer | Redirects user to blog page | Pass | |
| | Click Contact Us link in footer | Redirects user to contact page | Pass | |
| | Click social media icons in footer | Opens social media site clicked in a new tab | Pass | |
| | Click on Games By Nintendo link in footer | Redirection to All Products page | Pass | Products filtered to Games on Nintendo consoles |
| | Click on Games By Sega link in footer | Redirection to All Products page | Pass | Products filtered to Games on Sega consoles |
| | Click on Games By Sony link in footer | Redirection to All Products page | Pass | Products filtered to Games on Sony consoles |
| | Click on Consoles By Nintendo link in footer | Redirection to All Products page | Pass | Products filtered to Nintendo consoles |
| | Click on Consoles By Sega link in footer | Redirection to All Products page | Pass | Products filtered to Sega consoles |
| | Click on Consoles By Sony link in footer | Redirection to All Products page | Pass | Products filtered to Sony consoles |
| | Click on Subscribe button on blank newsletter form | Error message appears telling user to try again | Pass | |
| | Click on Subscribe button on filled newsletter form | Alert message lets user know they have signed up for the mailing list and welcome email is sent to address provided | Pass | |
| | Try to subscribe to newsletter with already subscribed email address | Error message appears telling user to check the form or make sure they're not already subscribed | Pass | |

## User Story Testing

The following are user stories I've implemented with screenshots to prove.

| User Story | Screenshot |
| --- | --- |
| As a first-time site visitor I want to be able to clearly see what the site's purpose is so that I can decide whether or not to continue browsing it. | ![screenshot](documentation/testing/homepage.png) |
| As a user I want to be able to easily navigate the website so that I can find the content I'm looking for. | ![screenshot](documentation/testing/main-nav.png) ![screenshot](documentation/testing/main-nav-dropdown.png) |
| As a site user I want to be able to search the website so that I can find specific products and see if the site has them in stock. | ![screenshot](documentation/testing/search-bar.png) ![screenshot](documentation/testing/search-results.png) ![screenshot](documentation/testing/search.png) |
| As a site user I want to be able to contact the site owners so that I can request further information about the site or lodge a complaint. | ![screenshot](documentation/testing/contact-page.png) ![screenshot](documentation/testing/contact-form.png) |
| As a site user I want to be able to see a list of all site products so that I can browse what the site has to offer. | ![screenshot](documentation/testing/all-products.png) |
| As a site user I want to be able to see the prices of products clearly so that I can make a decision whether or not to purchase. | ![screenshot](documentation/testing/product-card.png) |
| As a site user I want to be able to view a product on its own individual page so that I can see more information about the product. | ![screenshot](documentation/testing/product-detail.png) |
| As a site user I want to be able to sort products by category (game/console or games by console) so that I can find specific products related to the category I select. | ![screenshot](documentation/testing/product-filtering-menu.png) ![screenshot](documentation/testing/product-filtering-detail.png) |
| As a site user I want to be able to add products to my shopping basket so that I can proceed to the checkout and purchase them. | ![screenshot](documentation/testing/add-to-basket.png) |
| As a site user I want to be able to see a running total of the items in my basket so that I can manage my spending and know what to expect at the checkout. | ![screenshot](documentation/testing/add-to-basket-message.png) |
| As a site user I want to be able to checkout with a card payment so that I can place an order for the items in my basket. | ![screenshot](documentation/testing/checkout.png) |
| As a site user I want to be able to receive an order confirmation email after I purchase from the shop so that I can have a record of what I've purchased in my email inbox. | ![screenshot](documentation/testing/order-confirmation-email.png) |
| As a site user I want to be able to apply discount codes in the checkout so that I can receive a discount on my purchase. | ![screenshot](documentation/testing/discount-form.png) ![screenshot](documentation/testing/discount-added.png) |
| As a site user I want to be able to create an account on the site so that I can save my billing and shipping details and see a history of my purchases on my account. | ![screenshot](documentation/testing/sign-up.png) |
| As a registered user I want to be able to edit the details saved to my account so that I can keep my details up to date. | ![screenshot](documentation/testing/profile.png) ![screenshot](documentation/testing/default-delivery-form.png) |
| As a site user I want to be able to view blog posts on the website so that I can read any posts I feel are relevant to me. | ![screenshot](documentation/testing/blog.png) ![screenshot](documentation/testing/blog-post.png) |
| As a site admin I want to be able to create blog posts from the front end so that I can share information with site visitors. | ![screenshot](documentation/testing/add-blog.png) |
| As a site admin I want to be able to edit existing blog posts so that I can ensure that posts are up to date and relevant without having to create them from scratch in case of error. | ![screenshot](documentation/testing/edit-blog.png) |
| As a site admin I want to be able to delete existing blog posts so that I can remove any unwanted posts from the site. | ![screenshot](documentation/testing/delete-blog.png) |
| As a site admin I want to be able to create new products from the front end so that I can easily add new products to the site. | ![screenshot](documentation/testing/add-product.png) |
| As a site admin I want to be able to edit existing products so that I can ensure that all product listings are up to date and accurate. | ![screenshot](documentation/testing/edit-product.png) |
| As a site admin I want to be able to delete products from the site so that I can remove any products that are no longer being supplied by the site. | ![screenshot](documentation/testing/delete-product.png) |
| As a site admin I want to be able to set the stock for each product so that I can manage how many units of each product the site can sell. | ![screenshot](documentation/testing/stock-green.png) ![screenshot](documentation/testing/stock-yellow.png) ![screenshot](documentation/testing/stock-sold-out.png) |
| As a site admin I want to be able to see a list of open tickets so that I can manage contact form inquiries. | ![screenshot](documentation/testing/open-tickets-1.png) ![screenshot](documentation/testing/single-open-ticket.png) ![screenshot](documentation/testing/no-open-tickets.png) |
| As a site user I want to be able to sign up for the site's mailing list so that I can receive offers and news in my inbox. | ![screenshot](documentation/testing/newsletter-form.png) ![screenshot](documentation/testing/newsletter-alert.png) ![screenshot](documentation/testing/newsletter-email.png) |
| As a site user I want to be able to enter the Konami code (Up Up Down Down Left Right Left Right B A) on my keyboard so that I can experience an easter egg. | ![screenshot](documentation/testing/konami-code-easter-egg.png) ![screenshot](documentation/testing/konami-code-modal.png) |
| As a site admin I want to be able to set appropriate keywords on site pages so that I can increase the chances potential customers will find the site when searching to purchase records on Google. | ![screenshot](documentation/testing/seo-keywords.png) |
| As a site admin I want to be able to share the business on Facebook so that I can reach and market to a larger audience. | ![screenshot](documentation/facebook-mockup.png) |

The following are user stories I wasn't able to implement and have labeled as Wont Have in my MoSCoW prioritization

| User Story | Screenshot |
| --- | --- |
|  | N/A |



## Bugs

## Unfixed Bugs
