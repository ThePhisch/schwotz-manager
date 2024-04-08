"use server"

import { H1 } from "@/components/H1"
import TaskForm from "@/components/TaskForm"
import { twMerge } from "tailwind-merge"


export default async function Add() {
	return (
		<main className="p-4">
			<H1>Aufgabe Hinzufügen</H1>
			<TaskForm edit={false} />
		</main>
	)
}