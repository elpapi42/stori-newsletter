"use client"

import "@uiw/react-md-editor/markdown-editor.css";
import "@uiw/react-markdown-preview/markdown.css";
import dynamic from "next/dynamic";
import Link from 'next/link';
import Image from 'next/image';
import Button from '@/components/button';
import AudienceInput from '@/components/audienceInput';
import Input from '@/components/input';
import { useState } from 'react';
import { useEffect } from 'react';
import { FilePicker } from 'evergreen-ui'

const MDEditor = dynamic(
  () => import("@uiw/react-md-editor"),
  { ssr: false }
);

export default function NewsletterDetail({ params }) {
  const [title, setTitle] = useState('');
  const [audience, setAudience] = useState([]);
  const [body, setBody] = useState('');
  const [file, setFile] = useState(null);

  const getNewsLetter = async () => {
    try {
      let response = await fetch(process.env.NEXT_PUBLIC_BACKEND_URL + "/newsletter/" + params.id,
        { method: 'GET' }
      );

      response = await response.json();

      console.log(response);
  
      setTitle(response.title);
      setAudience(response.audience);
      setBody(response.body);
      setFile({name: response.file_name});
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {getNewsLetter();}, []);

  const onSaveNewsLetter = async () => {
    try {
      console.log(file);

      await fetch(process.env.NEXT_PUBLIC_BACKEND_URL + "/newsletter/" + params.id, { 
        method: 'PATCH' ,
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 
          title: title, 
          audience: audience, 
          body: body,
          file_name: file ? file.name : null
        }),
      });

      if (file) {
        const formData = new FormData();
        formData.append('file', file);
        await fetch(process.env.NEXT_PUBLIC_BACKEND_URL + "/newsletter/" + params.id + "/file", { 
          method: 'POST' ,
          body: formData
        });
      }
    } catch (err) {
      console.error(err);
    }
  };

  const onSendNewsLetter = async () => {
    try {
      await fetch(process.env.NEXT_PUBLIC_BACKEND_URL + "/newsletter/" + params.id + "/send", { 
        method: 'POST' ,
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        }
      });
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="w-full container relative mx-auto pt-16 px-56">
      <div className="flex flex-row justify-between mb-4 space-x-8">
        <div className="w-full flex flex-row space-x-2">
          <Link href={"/newsletters"} className='flex flex-row items-center border-2 rounded-lg border-emerald-400 py-2 px-4'>
            <Image
              src="/back.svg"
              width={25}
              height={25}
              alt="Picture of the author"
            />
          </Link>
          <Input placeholder="Title" value={title} onChange={(e) => setTitle(e.target.value)} className="w-full"/>
        </div>
        <div className="flex flex-row justify-between space-x-2">
          <Button text="Save" onClick={onSaveNewsLetter}/>
          <Button text="Send" onClick={onSendNewsLetter}/>
        </div>
      </div>

      <AudienceInput emails={audience} setEmails={setAudience}/>
      <MDEditor value={body} onChange={setBody} height={500}/>

      <FilePicker
        width={400}
        height={40}
        placeholder={file ? file.name : "Select your Newsletter image (Optional)"}
        accept=".png,.jpeg"
        className="border-2 rounded-lg border-emerald-400 py-2 px-4 w-1/2 mt-4"
        onChange={files => setFile(files[0])}
      />
    </div>
  )
}
