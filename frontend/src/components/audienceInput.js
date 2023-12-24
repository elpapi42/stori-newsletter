import React from 'react';
import Button from '@/components/button';
import Bubble from '@/components/bubble';
import Input from '@/components/input';
import { useState } from 'react';
import { useEffect } from 'react';

const REGEX_EMAIL = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

export default function AudienceInput({ emails, setEmails }) {
  const [inputEmail, setInputEmail] = useState('');

  const onAddEmail = () => {
    if (!REGEX_EMAIL.test(inputEmail)) {return;}

    if (!inputEmail) {return;}

    if (emails.includes(inputEmail)) {return;}

    setEmails([...emails, inputEmail]);

    setInputEmail('');
  }

  return (
    <div className="flex flex-row space-x-2 flex-wrap">
      <div className="mb-2">
        <Input placeholder="Email" value={inputEmail} onChange={(e) => setInputEmail(e.target.value)}/>
      </div>
      <div className="mb-2">
        <Button text="Add" onClick={onAddEmail}/>
      </div>
      {emails.map(email => (
        <div className="mb-2">
          <Bubble key={email} text={email} onClose={() => setEmails(emails.filter(e => e !== email))}/>
        </div>
      ))}
    </div>
  );
}
