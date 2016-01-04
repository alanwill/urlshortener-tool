## urlshortener-tool

This app will shorten a long URL using the [Goo.gl](http://goo.gl) service. It requires an OAuth token in order to associate its requests with your Google account so that you can log into goo.gl and view the URL analytics.

### prerequisites & installation

0. A Google account
1. Install the Google Python library
    ```
    pip install --upgrade google-api-python-client`
    ```
2. Rename `client_secrets_sample.json` to `client_secrets.json`
3. Go to the [Google Developer Console](https://console.developers.google.com/apis) and enable the URL Shortener API
4. Create [OAuth2 client credentials](https://console.developers.google.com/apis/credentials) for the app. For *Application Type* choose **Other**.
5. Now that you have a client ID and secret, populate the `client_secrets.json` from step 1 with those values. The other 3 keys can be left as is.

That should be it, go ahead and run shorten-url.py and happy URL shortening.

*During the first run you'll be prompted authorize the app, just follow the instructions as it should be pretty self explanatory.
