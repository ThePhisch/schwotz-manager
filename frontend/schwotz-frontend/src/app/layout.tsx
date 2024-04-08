import type { Metadata } from "next";
import "./globals.css";

import { twMerge } from "tailwind-merge";
import { A } from "@/components/A";

export const metadata: Metadata = {
  title: "Schwotz Manager",
  description: "Our Webapp",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={twMerge(
        )}
      >
      <header
        className={twMerge(
          "h-fit pt-2 pb-1 px-1 border-b",
          "flex flex-row justify-start space-x-4"
        )}
      >
        <A href="/">Alle Aufgaben</A>
        <A href="/add">Neue Aufgabe</A>
      </header>  
        {children}
      </body>
    </html>
  );
}
