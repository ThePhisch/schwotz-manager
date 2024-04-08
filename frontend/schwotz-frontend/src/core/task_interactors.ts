"use server";


export async function task_get_list(): Promise<Task[]> {
	"use server"
	const response = await fetch('http://docker-web-1:8005/t/list');
	const data = await response.json();

	let tasks = []
	for (let t of data) {
		tasks.push({
			id: t.id,
			name: t.name,
			assigned: t.assigned,
			nextup: new Date(t.nextup),
			timedelta: t.timedelta,
		});
	}

	return tasks
}

export async function task_get(task_id: number): Promise<Task> {
	"use server"
	const response = await fetch(`http://docker-web-1:8005/t/${task_id}`);
	const data = await response.json();

	return {
		id: data.id,
		name: data.name,
		assigned: data.assigned,
		nextup: new Date(data.nextup),
		timedelta: data.timedelta,
	}
}

export async function task_complete(task_id: number) {
	"use server"
	const response = await fetch(`http://docker-web-1:8005/t/${task_id}/complete`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
	});
	const data = await response.json();
	console.log(data);
}

export async function task_delete(task_id: number) {
	"use server"
	const response = await fetch(`http://docker-web-1:8005/t/${task_id}`, {
		method: 'DELETE',
		headers: {
			'Content-Type': 'application/json',
		},
	});
	const data = await response.json();
	console.log(data);
}

export async function task_update(task: Task) {
	"use server"
	const response = await fetch(`http://docker-web-1:8005/t/${task.id}`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(task),
	});
	const data = await response.json();
	console.log(data);
}

export async function task_add(task: Task) {
	"use server"
	const response = await fetch('http://docker-web-1:8005/t', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(task),
	});
	const data = await response.json();
	console.log(data);
}