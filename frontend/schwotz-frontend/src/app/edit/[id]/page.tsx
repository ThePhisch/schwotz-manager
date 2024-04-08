"use server"

import { twMerge } from "tailwind-merge"
import { H1 } from "@/components/H1"
import Card from "@/components/Card"
import { task_get } from "@/core/task_interactors"
import TaskEditForm from "@/components/TaskEditForm"
import { Suspense } from "react"


export default async function Edit({ params }: { params: { id: number } }) {
    return (
        <main className="p-4">
            <H1>Aufgabe Bearbeiten</H1>
            <TaskEditForm id={params.id} />
        </main>
    )
}