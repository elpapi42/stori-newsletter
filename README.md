# Instructions

1. At the root of the repo, run `sudo chmod +x init.sh`
2. At the root of the repo, run `./init.sh`
3. Run `docker compose up --detach --build`
4. Go to `http://localhost:3000``

## Warning

The email delivery feature is not going to work initially, AWS credentials with permissions to SES are required and not provided in this repo. All the other features are going to work.

If you want the email delivery feature to work, follow the instructions below:

1. Login into you AWS account
2. Go to IAM
3. Create a new user
4. Give the user the following permissions:
    - AmazonSESFullAccess
5. Create the user
6. Create an access key for the user
7. Copy the access key and secret key
8. Paste the access key and secret key into the backend/.env file
9. Go to AWS SES Admin Console
10. Verify the email address you want to send emails from
11. Add the email adress to the backend/.env file
12. Run `docker compose up -d --build` again

If you do not want to follow the steps above, we can test the application during the next interview.

## Potential Improvements

1. Send emails concurrently in SESNewsletterDispatcher
2. The MVP is fragile, the lack of testing might improve this
3. Indexing the scheduled_at field in the DB
4. Better handling of closing connections to the DB
5. Extend the NewsletterRepo with batching capabilities
6. Remove non-structured logging from fastapi
7. Add global error handling and logging for the API
8. Delete Newsletter feature
