# Instamojo Old API

Assists you to programmatically create, edit and delete products on Instamojo.

**Note**: If you're using this wrapper with our sandbox environment `https://test.instamojo.com/` then you should pass `'https://test.instamojo.com/api/1.1/'` as third argument to the `Instamojo` class while initializing it. API key and Auth token for the same can be obtained from https://test.instamojo.com/developers/ (Details: [Test Or Sandbox Account](https://instamojo.zendesk.com/hc/en-us/articles/208485675-Test-or-Sandbox-Account)).

    api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/');

## Usage

    from instamojo_wrapper import Instamojo
    api = Instamojo(api_key=API_KEY,
                    auth_token=AUTH_TOKEN)

    # Get a list of all products that you have created and display their slugs.
    response = api.links_list()
    for link in response['links']:
        print link['slug']

    # Create a new product
    response = api.link_create(title='Hello, world!',
                               description='Well, hello again.',
                               base_price=0)

    # Display the URL of the newly created product
    print response['link']

This will give you JSON object containing details of the product that was just created.

## Payments API and Webhook/Redirect

    from instamojo_wrapper import Instamojo
    api = Instamojo(api_key, token_auth)
    payment = api.payment_detail(payment_id='PAYMENT ID YOU GOT FROM WEBHOOK OR REDIRECT')

This will return a Payment object with details of the transaction.

You have these functions to interact with the API:
 * `debug()`
 * `auth(username, password)`
 * `links_list()` => list of products
 * `link_detail(slug)` => Product
 * `link_create(title, description, base_price)` => Product
 * `link_edit(slug)` => Product
 * `link_delete(slug)` => No Data
 * `payments_list()` => List of Payments
 * `payment_detail(payment_id)` => Payment

## Product Creation Parameters

### Required

  * `title` - Title of the Product, be concise.
  * `description` - Describe what your customers will get, you can add terms and conditions and any other relevant information here. Markdown is supported, popular media URLs like Youtube, Flickr are auto-embedded.
  * `base_price` - Price of the product. This may be 0, if you want to offer it for free.

### File and Cover Image
  * `file_upload` - Full path to the file you want to sell. This file will be available only after successful payment.
  * `cover_image` - Full path to the IMAGE you want to upload as a cover image.

### Quantity
  * `quantity` - Set to 0 for unlimited sales. If you set it to say 10, a total of 10 sales will be allowed after which the product will be made unavailable.

### Post Purchase Note
  * `note` - A post-purchase note, will only displayed after successful payment. Will also be included in the ticket/ receipt that is sent as attachment to the email sent to buyer. This will not be shown if the payment fails.

### Event
  * `start_date` - Date-time when the event is beginning. Format: `YYYY-MM-DD HH:mm`
  * `end_date` - Date-time when the event is ending. Format: `YYYY-MM-DD HH:mm`
  * `venue` - Address of the place where the event will be held.
  * `timezone` - Timezone of the venue. Example: Asia/Kolkata

### Redirects and Webhooks
  * `redirect_url` - This can be a Thank-You page on your website. Buyers will be redirected to this page after successful payment.
  * `webhook_url` - Set this to a URL that can accept POST requests made by Instamojo server after successful payment.
  * `enable_pwyw` - set this to True, if you want to enable Pay What You Want. Default is False.
  * `enable_sign` - set this to True, if you want to enable Link Signing. Default is False. For more information regarding this check: https://support.instamojo.com/hc/en-us/articles/208542675-How-do-I-ensure-that-the-link-is-tamper-proof-

---

## [Request a Payment](RAP.md)

---

## [Refunds](REFUNDS.md)

---

Further documentation is available at https://www.instamojo.com/developers/
