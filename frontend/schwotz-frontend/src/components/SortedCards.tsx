"use client";

import { twMerge } from "tailwind-merge";
import Card from "./Card";
import { useEffect, useState } from "react";

export default function SortedCards(props: {
	tasklist: () => Promise<Task[]>,
}) {

	const [tasklist, setTasklist] = useState<Task[]>([]);

	useEffect(() => {
		// unpack promise and sort by nextup (i.e. date)
		props.tasklist().then((tasklist) => {
			setTasklist(
				tasklist.sort(
					(a, b) => a.nextup > b.nextup ? 1 : -1
				)
			);
		});
	}, [tasklist])

	return (
	<div className={twMerge("grid grid-cols-1 gap-2")}>
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