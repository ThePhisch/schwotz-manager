"use client";

import { twMerge } from "tailwind-merge";

import { task_update, task_add } from "@/core/task_interactors";

export default function TaskForm(props: {
	edit: boolean, // else create
	task?: Task,
}) {

	const task_interactor = props.edit ? task_update : task_add

	return (
		<form
			className={twMerge(
				"p-4",
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
				await task_interactor(task)
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