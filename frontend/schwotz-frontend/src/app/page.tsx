"use server"
import Card from "@/components/Card";


export default async function Home() {

  async function task_get_list(): Promise<Task[]> {
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

  return (
    <main className="p-4">
      <h1 className="text-3xl font-bold">Welcome to Schwotz Manager</h1>
      {await task_get_list().then(
        tasks => tasks.map(
          task => 
          <div
            key={task.id}
            className="p-4 my-4 bg-white shadow-md rounded-md"
          >
            <h3 className="font-bold">{task.name}</h3>
            <p>Beauftragter: {task.assigned}</p>
          </div>
      ))}
    </main>
  );
}
