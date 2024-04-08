"use client";

import { twMerge } from "tailwind-merge";
import React, { useState } from "react";
import { task_complete, task_delete, task_get, task_update } from "@/core/task_interactors";

export default function Card(props: {
	task: Task, 
})  {
	const [task, setTask] = useState<Task>(props.task);
	const [editing, setEditing] = useState<boolean>(false);
	const [newtask, setNewTask] = useState<Task>(props.task);

	return (
		<div
			className={twMerge(
				"p-4 my-4 bg-white shadow-md rounded-md",
			)}
		>
			<div className="flex flex-row items-center">
				<div
					className="grow"
				>
					<h3 className="font-bold">{task.name}</h3>
					<p>Beauftragter: {task.assigned}</p>
					<p>Nächster Termin: {task.nextup.toLocaleDateString('de-DE')}</p>
					<p>Häufigkeit: {task.timedelta}</p>
				</div>
				<div
					className="shrink-0 flex flex-col space-y-1 items-center justify-center"
				>
					<button
						className={twMerge(
							"bg-green-100 hover:bg-green-200 border-green-500 text-green-900",
							"px-4 py-2 border-2 rounded-md w-36"
						)}
						onClick={async e => {
							await task_complete(task.id as number);
							setTask(await task_get(task.id as number));
						}}
					>
						Erledigt!
					</button>
					<button
						className={twMerge(
							"bg-blue-100 hover:bg-blue-200 border-blue-500 text-blue-900",
							"px-4 py-2 border-2 rounded-md w-36"
						)}
						onClick={e => {setEditing(!editing)}}
					>
						Bearbeiten
					</button>
				</div>
			</div>
			<form
				className={twMerge(
					"p-4 my-4 bg-gray-100 shadow-md rounded-md",
					editing ? "flex" : "hidden",
					"flex-col space-y-4"
				)}
				onSubmit={async e => {
					e.preventDefault();
					const form = e.target as HTMLFormElement;
					await task_update(newtask);
					setTask(await task_get(task.id as number));
					setEditing(false);
				
				}}
			>
				<label>
					Neuer Name:
					<input
						type="text"
						name="newname"
						value={newtask.name}
						onChange={e => setNewTask({...newtask, name: e.target.value})}
					/>
				</label>
				<label>
					Neuer Beauftragter:
					<input type="text" name="newassigned" defaultValue={newtask.assigned}/>
				</label>
				<label>
					Neuer Nächster Termin:
					<input
						type="date"
						name="newnextup"
						defaultValue={
							// super hacky way to get the date in the correct format
							newtask.nextup.toLocaleDateString("en-CA")
						}
					/>
				</label>
				<label>
					Neue Häufigkeit:
					<input type="string" name="newtimedelta" defaultValue={newtask.timedelta}/>
				</label>
				<button
					className={twMerge("bg-red-500")}
					onClick={e => {
						task_delete(task.id as number)
						setEditing(false)
					}}
				>
					Aufgabe Löschen	
				</button>
				<button
					className={twMerge("bg-blue-500")}
					onClick={e => {setEditing(false)}}
				>
					Abbrechen
				</button>
				<button
					className={twMerge("bg-green-500")}
				>
					Änderungen Speichern
				</button>
			</form>
		</div>
	)
}