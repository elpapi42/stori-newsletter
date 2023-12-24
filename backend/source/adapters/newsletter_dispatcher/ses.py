import os
import asyncio
from dataclasses import dataclass

import marko
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

from source.ports.newsletter_dispatcher import NewsletterDispatcher
from source.ports.file_storage import FileStorage
from source.domain.newsletter import Newsletter
from source.infrastructure.aws import ses_client


SENDER = "whitman-2@hotmail.com"


@dataclass
class SESNewsletterDispatcher(NewsletterDispatcher):
    ses_client = ses_client
    file_storage: FileStorage

    async def dispatch(self, newsletter: Newsletter) -> None:
        msg = MIMEMultipart('mixed')

        msg['Subject'] = newsletter.title
        msg['From'] = SENDER

        msg_body = MIMEMultipart('alternative')

        htmlpart = MIMEText(marko.convert(newsletter.body).encode(), 'html', "utf-8")
        msg_body.attach(htmlpart)

        msg.attach(msg_body)

        if newsletter.file_uri:
            # Load attachment to memory
            file = await self.file_storage.get_by_uri(newsletter.file_uri)
            internal_file_name = os.path.basename(newsletter.file_uri)

            msg_att = MIMEApplication(file.read())
            msg_att.add_header('Content-ID', internal_file_name)
            msg_att.add_header('Content-Disposition', 'attachment', filename=internal_file_name)

            embeded_image = MIMEMultipart('alternative')
            embeded_image.attach(MIMEText(f'<html><body><img src="cid:{internal_file_name}"></body></html>', 'html', "utf-8"))

            msg.attach(msg_att)
            msg.attach(embeded_image)

        for email in newsletter.audience:
            msg['To'] = email.value

            try:
                self.ses_client.send_raw_email(
                    Source=SENDER,
                    Destinations=[email.value],
                    RawMessage={'Data':msg.as_string()}
                )
            except ClientError as e:
                print(e.response['Error']['Message'])

            # My aws account is in sandbox mode,
            # so I can only send emails to verified emails and 1 per second at most.
            # Real world scenario, I would concurrently execute the send_raw_email using aioboto3 library
            await asyncio.sleep(1)
