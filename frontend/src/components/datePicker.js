import React from 'react';

export default function DatePicker({ date, setDate }) {
  const onChangeDate = (date) => {
    setDate(date);
  }

  return (
    <div className="flex flex-row items-center">
      <div className='flex flex-row border-2 rounded-l-lg border-emerald-400 border-r-white h-full items-center px-4'>
        Schedule
      </div>

      <input 
        type="datetime-local" 
        className='border-2 rounded-r-lg border-emerald-400 py-2 px-4 h-14 outline-none w-full'
        value={date}
        onChange={(e) => onChangeDate(e.target.value)}
      />
    </div>
  );
}
