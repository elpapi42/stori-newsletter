"use client"

import Newsletter from '@/components/newsletter';
import Button from '@/components/button';
import Input from '@/components/input';
import { useState } from 'react';
import { useRouter } from 'next/navigation'
import { useEffect } from 'react';


export default function NewslettersIndex() {
  const [createNewsletterValue, setCreateNewsletterValue] = useState('');
  const [newslettersValue, setNewslettersValue] = useState([]);

  const router = useRouter()

  const postNewsletter = async (title) => {
    try {
      let response = await fetch(process.env.NEXT_PUBLIC_BACKEND_URL + "/newsletter", {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title }),
      });

      response = await response.json();

      console.log(response);

      return response.id;
    } catch (err) {
      console.error(err);
      return null;
    }
  };

  const onCreateNewsletter = async () => {
    let newsletterId = await postNewsletter(createNewsletterValue);

    console.log(newsletterId);

    if (!newsletterId) {
      return;
    };

    router.push("/newsletters/" + newsletterId)
  };

  const getAllNewsLetters = async () => {
    try {
      let response = await fetch(process.env.NEXT_PUBLIC_BACKEND_URL + "/newsletter",
        { method: 'GET' }
      );

      response = await response.json();

      console.log(response);
  
      setNewslettersValue(response);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {getAllNewsLetters();}, []);

  return (
    <div className="w-full container relative mx-auto pt-16 px-56">
      <div className="flex flex-row justify-between">
        <div className="text-3xl">
          Newsletters
        </div>
        <div className="flex flex-row space-x-2">
          <Input placeholder="Title" value={createNewsletterValue} onChange={(e) => setCreateNewsletterValue(e.target.value)}/>
          <Button text="Create Newsletter" onClick={onCreateNewsletter}/>
        </div>
      </div>
      <ul>
        {newslettersValue.map(newsletter => (
          <Newsletter key={newsletter.id} id={newsletter.id} title={newsletter.title}/>
        ))}
      </ul>
    </div>
  )
}
