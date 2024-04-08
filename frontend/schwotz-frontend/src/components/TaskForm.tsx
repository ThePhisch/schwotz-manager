"use client";

import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import { twMerge } from "tailwind-merge";

import { task_add, task_delete, task_update } from "@/core/task_interactors";

export default function TaskForm(props: {
	task: Task,
	edit?: boolean // else create
}) {
	const router = useRouter()
	const [task, setTask] = useState<Task>(props.task)
	useEffect(() => {
		setTask(props.task)
	}, [props.task])
	
	const task_func = props.edit ? task_update : task_add

	return (
		<form
			className={twMerge(
				"p-4",
				"grid grid-cols-1 space-y-2"
			)}
			onSubmit={e => {
				e.preventDefault()
			}}
		>

			<label>
				Name:
				<input type="text" name="taskname" value={task.name} onChange={e => setTask({ ...task, name: e.target.value })} />
			</label>
			<label>
				Beauftragter:
				<input type="text" name="assigned" value={task.assigned} onChange={e => setTask({ ...task, assigned: e.target.value })} />
			</label>
			<label>
				Nächster Termin:
				<input
					type="date"
					name="nextup"
					value={task.nextup.toLocaleDateString("en-CA")}
					onChange={e => setTask({ ...task, nextup: new Date(e.target.value) })}
				/>
			</label>
			<label>
				Häufigkeit:
				<input type="string" name="timedelta" value={task.timedelta} />
			</label>
			<button
				className={twMerge(
					"bg-green-500 hover:bg-green-700 text-white p-2",
				)}
				type="submit"
				onClick={async e => {
					e.preventDefault()
					await task_func(task)
					router.push("/")
				}}
			>
				Speichern
			</button>
			<button
				className={twMerge(
					"bg-blue-500 hover:bg-blue-700 text-white p-2",
				)}
				onClick={e => {
					e.preventDefault()
					router.push("/")
				}}
			>
				Abbrechen
			</button>
			<button
				className={twMerge(
					"bg-red-500 hover:bg-red-700 text-white p-2",
					props.edit ? "" : "hidden"
				)}
				onClick={async e => {
					e.preventDefault()
					await task_delete(task.id as number)
					router.push("/")
				}}
			>
				Löschen
			</button>
		</form>
	)
}