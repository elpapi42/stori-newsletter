"use client"

import { useSearchParams } from 'next/navigation'
import { useEffect } from 'react';


export default function Unsubscribe() {
  const searchParams = useSearchParams()

  const unsubscribeEmailAddress = async () => {
    try {
      await fetch(process.env.NEXT_PUBLIC_BACKEND_URL + "/unsubscribed-email-address", { 
        method: 'POST',
        body: JSON.stringify({ email: searchParams.get('email') }),
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
      });
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {unsubscribeEmailAddress();}, []);

  return (
    <div></div>
  )
}
