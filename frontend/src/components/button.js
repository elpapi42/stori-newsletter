import Link from 'next/link';
import Image from 'next/image';
import React from 'react';

export default function Button({ text, onClick }) {
  return (
    <button
      type="button"
      className="border-2 rounded-lg border-emerald-400 py-2 px-4 outline-none active:border-emerald-800 active:bg-emerald-400"
      onClick={onClick}
    >
      {text}
    </button>
  );
}
