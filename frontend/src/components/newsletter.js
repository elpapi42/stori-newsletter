import Link from 'next/link';
import Image from 'next/image';
import React from 'react';

export default function Newsletters({ id, title }) {
  return (
    <Link href={"/newsletters/" + id} className='flex flex-row justify-between my-2 border-2 rounded-lg border-emerald-400 py-2 px-4'>
      <div className='text-xl truncate'>{title}</div>
      <Image
        src="/arrow.svg"
        width={25}
        height={25}
        alt="Picture of the author"
      />
    </Link>
  );
}
