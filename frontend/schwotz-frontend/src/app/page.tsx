"use server"

import { twMerge } from "tailwind-merge";

import Card from "@/components/Card";
import { H1 } from "@/components/H1";
import SortedCards from "@/components/SortedCards";
import { task_get_list } from "@/core/task_interactors";


export default async function Home() {


  return (
      <main
        className={twMerge(
          "p-4",
        )}
      >
        <H1>Unsere Aufgaben</H1>
        <SortedCards tasklist={task_get_list} />
      </main>
  );
}
