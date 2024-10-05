"use client";
import { Tabs, Tab, Card, CardBody, CardHeader } from "@nextui-org/react";
import Details from "./components/details";

export default function Profile() {
  let tabs = [
    {
      id: "photos",
      label: "Photos",
      content:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    },
    {
      id: "documents",
      label: "Documents",
      link: "https://firebasestorage.googleapis.com/v0/b/mercury-5b809.appspot.com/o/Sample%2FBhavesh_Resume_FSD.pdf?alt=media&token=e5af0e2b-8b3b-4562-b7fc-abab4b14dd90",
    },
    {
      id: "music",
      label: "Music",
      content:
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
    },
    {
      id: "videos",
      label: "Videos",
      content:
        "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    },
  ];

  return (
    <main>
      <div>
        <div className="flex justify-center w-auto min-h-40 bg-gradient-to-r from-indigo-500 from-10% via-sky-500 via-30% to-rose-500 to-90%">
          <div className="w-2/3 p-7 bg-white min-h-64 translate-y-24 rounded-2xl shadow-2xl">
            <Details/>
          </div>
        </div>
      </div>
      <div className="grid grid-cols-6 gap-2 mt-40">
        <div></div>
        <div className="col-span-4">
          <div className="flex w-full flex-col">
            <Tabs aria-label="Dynamic tabs" items={tabs}>
              {(item) => (
                <Tab key={item.id} title={item.label}>
                  <Card>
                    <CardBody>
                      {item.content}
                      {item.link}
                    </CardBody>
                  </Card>
                </Tab>
              )}
            </Tabs>
          </div>
        </div>
        <div></div>
      </div>
    </main>
  );
}
