# Mailtrap Bulk Email Sender

A small Python script that sends an HTML email broadcast to a list of customer email addresses using the Mailtrap Email API.

## How it works

The script reads:

- an HTML email body from `template.html`
- a plain-text fallback body from `plaintext.txt`
- a list of recipient addresses (one per line) from `emails.txt`

It then sends one individual email per recipient through Mailtrap's API and logs the result of each send to a timestamped file in `logs/`.

## Requirements

- Python 3.8 or newer
- A Mailtrap account with a verified sending domain
- Packages:

```bash
pip install mailtrap python-dotenv
```

## Setup

1. Copy each `.example` file to its real counterpart:

```bash
cp emails.txt.example emails.txt
cp plaintext.txt.example plaintext.txt
cp template.html.example template.html
cp .env.example .env
```

2. Fill in your real data:

- `emails.txt`: your actual customer email list, one address per line
- `plaintext.txt`: the plain-text version of your email body
- `template.html`: the HTML version of your email body
- `.env`: your Mailtrap credentials and sender details (see below)

3. Install dependencies:

```bash
pip install -r requirements.txt
```

or manually:

```bash
pip install mailtrap python-dotenv
```

## Environment variables (.env)

| Variable             | Description                                                      |
| -------------------- | ---------------------------------------------------------------- |
| `MAILTRAP_API_TOKEN` | Your Mailtrap API token, found under Settings, API Tokens        |
| `FROM_EMAIL`         | Sender address. Must be on a domain verified in Mailtrap         |
| `FROM_NAME`          | Display name shown to recipients, for example "Pastry By Tasnim" |
| `MAIL_SUBJECT`       | Subject line for the broadcast                                   |

Example `.env`:

```env
MAILTRAP_API_TOKEN="API_TOKEN_HERE"
FROM_EMAIL="noreply@permitteddomain.com"
FROM_NAME="Display Name on Email"
MAIL_SUBJECT="Mail Subject Here"
```

Never commit your real `.env` file. Only `.env.example`, with placeholder values, should be pushed to GitHub.

## Usage

Once `.env`, `emails.txt`, `plaintext.txt`, and `template.html` are filled in, run:

```bash
python sendmail.py
```

Progress and results are written to a new timestamped file under `logs/`, for example:

```
logs/send_log_2026-07-21_14-32-08.txt
```

Each line in the log shows either:

- ✅: `email@example.com -> <response>`, sent successfully
- ❌: `email@example.com -> <error>`, with the error message

## Project structure

```
.
├── emails.txt              (gitignored, real recipient list)
├── emails.txt.example      (sample format for reference)
├── logs/                   (gitignored, generated send logs)
├── plaintext.txt           (gitignored, real plain-text email body)
├── plaintext.txt.example   (sample plain-text body)
├── sendmail.py             (main script)
├── template.html           (gitignored, real HTML email body)
└── template.html.example   (sample HTML template)
```

## Notes on sending limits

Mailtrap's free tier allows 150 emails per day and 4,000 per month. If your recipient list grows beyond that, split `emails.txt` across multiple days or upgrade your Mailtrap plan. Sends beyond the daily cap will fail and be logged as failed until the limit resets.

## Security

Add a `.gitignore` with at least:

```
.env
emails.txt
plaintext.txt
template.html
logs/
```

This keeps your API token, customer email list, and real email content out of version control. Only the `.example` placeholder files and the script itself should be public.
