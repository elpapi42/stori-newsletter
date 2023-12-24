"use client"

import Button from '@/components/button';
import AudienceInput from '@/components/audienceInput';
import { useState } from 'react';

export default function NewsletterDetail({ params }) {
  const [audience, setAudience] = useState([]);

  return (
    <div className="w-full container relative mx-auto pt-16 px-56">
      <div className="flex flex-row justify-between mb-4">
        <div className="text-3xl">
          OperaGx Launches soon!
        </div>
        <div className="flex flex-row justify-between space-x-2">
          <Button text="Save"/>
          <Button text="Send"/>
        </div>
      </div>

      <AudienceInput onChange={(audience) => setAudience(audience)}/>
    </div>
  )
}
