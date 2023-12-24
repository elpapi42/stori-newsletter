from dataclasses import dataclass

from botocore.exceptions import ClientError

from source.ports.newsletter_dispatcher import NewsletterDispatcher
from source.domain.newsletter import Newsletter
from source.infrastructure.aws import ses_client


SENDER = "whitman-2@hotmail.com"


@dataclass
class SESNewsletterDispatcher(NewsletterDispatcher):
    ses_client = ses_client

    async def dispatch(self, newsletter: Newsletter) -> None:
        try:
            response = self.ses_client.send_email(
                Destination={'ToAddresses': [email.value for email in newsletter.audience]},
                Message={
                    'Body': {
                        'Html': {'Charset': "UTF-8", 'Data': ""},
                        'Text': {'Charset': "UTF-8", 'Data': newsletter.body},
                    },
                    'Subject': {'Charset': "UTF-8", 'Data': newsletter.title},
                },
                Source=SENDER,
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
