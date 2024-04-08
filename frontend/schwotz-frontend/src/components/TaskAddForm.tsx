"use client";

import { twMerge } from "tailwind-merge";
import { useState } from "react";
import TaskForm from "./TaskForm";

export default function TaskAddForm() {
	
	const [task, setTask] = useState<Task>({
		name: "",
		assigned: "",
		nextup: new Date(),
		timedelta: "P1W",
	});

	return (
		<TaskForm task={task} />
	)
}