import { redirect } from 'next/navigation';

export default function Home() {
  redirect("/newsletters");

  return (
    <main>
    </main>
  )
}
