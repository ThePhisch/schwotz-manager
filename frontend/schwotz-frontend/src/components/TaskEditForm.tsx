"use client";

import { twMerge } from "tailwind-merge";

import { task_get } from "@/core/task_interactors";
import { useEffect, useState } from "react";
import TaskForm from "./TaskForm";

export default function TaskEditForm(props: {
	id: number,
}) {


	const [task, setTask] = useState<Task | null>(null)

	useEffect(() => {
		task_get(props.id).then((task) => {
			setTask(task)
		})
	}, [])

	if (task === null) {
		return <p>Lädt...</p>
	}
	return (
		<TaskForm task={task} edit/>
	)
}