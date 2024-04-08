import { twMerge } from "tailwind-merge"
import { H1 } from "@/components/H1"

export default function Edit() {
    return (
        <main className="p-4">
            <H1>Aufgabe Bearbeiten</H1>
            <TaskEditForm />
        </main>
    )
}