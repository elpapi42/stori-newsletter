import Image from 'next/image';
import React from 'react';

export default function Bubble({ text, onClose }) {
  return (
    <button
      type="button"
      className="flex flex-row border-2 rounded-full items-center space-x-2 border-emerald-400 bg-emerald-400 py-2 px-4 outline-none active:border-emerald-800 active:bg-emerald-400"
      onClick={onClose}
    >
      <div>
        {text}
      </div>
      <Image
        src="/cross.svg"
        width={15}
        height={15}
        alt="Picture of the author"
      />
    </button>
  );
}
