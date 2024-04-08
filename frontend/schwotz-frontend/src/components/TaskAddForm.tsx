"use client";

import { twMerge } from "tailwind-merge";
import { useState } from "react";

export default function TaskAddForm(props: {
	add: (task: Task) => void,
}) {
	return (
		<form
			className={twMerge(
				"flex flex-col space-y-4",
			)}
			onSubmit={async e => {
				e.preventDefault()
				const form = e.target as HTMLFormElement
				const task = {
					name: form.taskname.value,
					assigned: form.assigned.value,
					nextup: new Date(form.nextup.value),
					timedelta: form.timedelta.value,
				} as Task
				console.log(task)
				await props.add(task)
			}}
		>
			<label>
				Name:
				<input type="text" name="taskname" />
			</label>
			<label>
				Beauftragter:
				<input type="text" name="assigned" />
			</label>
			<label>
				Nächster Termin:
				<input type="date" name="nextup" />
			</label>
			<label>
				Häufigkeit:
				<input type="string" name="timedelta" />
			</label>
			<button
				className={twMerge(
					"bg-green-500 hover:bg-green-700 text-white p-2",
				)}
				type="submit"
			>Hinzufügen</button>
		</form>
	)
}