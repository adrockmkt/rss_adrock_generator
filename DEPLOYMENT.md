

# RSS Ad Rock Generator – Deployment Guide

This document defines the official deployment procedure for the RSS Ad Rock Generator in production.

---

## 1. Production Environment

Server:
- DigitalOcean Droplet
- Ubuntu 22.04 LTS
- Python 3.10
- Nginx

Project directory:

/home/adrock/rss_adrock_generator

Public RSS location:

https://mobiledelivery.com.br/rss/adrock.xml

---

## 2. Initial Setup (First Deployment)

### 2.1 Clone repository

cd /home/adrock
git clone https://github.com/adrockmkt/rss_adrock_generator.git
cd rss_adrock_generator

### 2.2 Create virtual environment

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

---

## 3. Updating Production

When changes are pushed to GitHub:

ssh adrock@147.182.183.10
cd /home/adrock/rss_adrock_generator

git fetch origin
git reset --hard origin/main

source venv/bin/activate
pip install -r requirements.txt

---

## 4. Manual Execution (Testing)

source venv/bin/activate
python main.py

Expected output:

- List of discovered posts
- IndexNow submission status
- RSS successfully generated message

---

## 5. Cron Automation

Production cron (root):

0 7 * * * /home/adrock/rss_adrock_generator/rodar_rss.sh >> /home/adrock/rss_adrock_generator/rss.log 2>&1

This ensures:

- Daily RSS regeneration
- Image updates
- IndexNow incremental submission

To edit:

sudo crontab -e

To verify:

sudo crontab -l

---

## 6. Log Monitoring

RSS execution log:

/home/adrock/rss_adrock_generator/rss.log

View last lines:

tail -n 50 /home/adrock/rss_adrock_generator/rss.log

Clear log if necessary:

> /home/adrock/rss_adrock_generator/rss.log

---

## 7. Rollback Strategy

If a deployment breaks production:

cd /home/adrock/rss_adrock_generator

git log --oneline

git reset --hard <previous_commit_hash>

Then reinstall dependencies if needed:

source venv/bin/activate
pip install -r requirements.txt

---

## 8. Permissions

Ensure the project directory is owned by adrock:

sudo chown -R adrock:adrock /home/adrock/rss_adrock_generator

Nginx must have read access to:

/home/adrock/rss_adrock_generator/rss/
/home/adrock/rss_adrock_generator/rss_images/

---

## 9. Production Checklist

Before confirming deployment:

- git status clean
- requirements.txt updated
- RSS validates at W3C validator
- Images loading correctly
- IndexNow returns 200 or 202
- No "Sem título" entries

---

## 10. Future Hardening

Recommended improvements:

- Add systemd service instead of pure cron
- Add healthcheck endpoint
- Add monitoring alert (email on failure)
- Add Docker deployment option

---

This deployment process is the official operational standard for the RSS Ad Rock Generator project.