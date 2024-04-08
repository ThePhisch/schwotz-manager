"use client";

import { twMerge } from "tailwind-merge";
import Card from "./Card";
import { useEffect, useState } from "react";

export default function SortedCards(props: {
	tasklist: () => Promise<Task[]>,
}) {

	const [tasklist, setTasklist] = useState<Task[]>([]);

	useEffect(() => {
		props.tasklist().then((tasklist) => {
			setTasklist(tasklist);
		});
	}, [tasklist])

	return (
		<div className={twMerge("grid grid-cols-1 gap-4")}>
			{tasklist.map((task) => {
				return (
					<Card
						key={task.id}
						task={task}
					/>
				);
			})
			}

		</div>
	);
}