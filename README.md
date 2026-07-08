# eCommerce — Checkout Flow - Selenium POM Framework

End-to-end Selenium test (Page Object Model, Pytest, Allure) covering:

Home → hover **Store** → **iPad** → scroll to **iPad Accessories** → **Smart Folio for iPad** tile →
select color **White** → **Add to Bag** → assert item + price on the bag page → **Checkout** →
assert the Sign In / Guest Checkout options are shown.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
# Headed, Chrome (default)
pytest

# Headless, Firefox
pytest --browser=firefox --headless
```

## Allure report

```bash
allure serve allure-results
```

(Requires the [Allure commandline](https://allurereport.org/docs/gettingstarted-installation/) — `npm install -g allure-commandline` or `brew install allure`.)

## CI

`.github/workflows/tests.yml` runs the suite on `ubuntu-latest` across a Chrome + Firefox matrix on every push/PR to `main`, and uploads the raw Allure results and generated HTML report as downloadable workflow artifacts.
