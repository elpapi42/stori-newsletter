import Link from 'next/link';
import Image from 'next/image';
import React from 'react';

export default function Input({ placeholder, value, onChange }) {
  return (
    <input 
      type="text"
      className="border-2 rounded-lg border-emerald-400 py-2 px-4 outline-none w-full"
      placeholder={placeholder}
      value={value}
      onChange={onChange}
    />
  );
}
