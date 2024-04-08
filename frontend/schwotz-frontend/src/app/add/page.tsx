"use server"

import { H1 } from "@/components/H1"
import TaskAddForm from "@/components/TaskAddForm"
import { twMerge } from "tailwind-merge"


export default async function Add() {
	return (
		<main className="p-4">
			<H1>Aufgabe Hinzufügen</H1>
			<TaskAddForm />
		</main>
	)
}