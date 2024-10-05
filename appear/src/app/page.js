import * as React from "react";

// 1. import `NextUIProvider` component
import { NextUIProvider } from "@nextui-org/react";

export default async function Home() {
  let data = await fetch("http://127.0.0.1:8000/smarteq/?format=json");
  let posts = await data.json();
  return (
    <NextUIProvider>
      <ul>
        {posts.user_profiles.map((profile) => (
          <li key={profile.id}>{profile.photo}</li>
        ))}
        {posts.addresses.map((profile) => (
          <li key={profile.id == 1}>{profile.city}</li>
        ))}
      </ul>
    </NextUIProvider>
  );
}
