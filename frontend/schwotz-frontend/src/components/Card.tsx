"use client";

import { useState } from "react";

export default function Card() {
    const [pressed, setPressed] = useState(false);
    const handleClick = (e: any) => setPressed(!pressed);

    return (
        <div>
            <button
                className="bg-blue-200"
                onClick={handleClick}
            >
                Hi
            </button>
            <p>{pressed ? "Hello" : "Goodbye"}</p>
        </div>
    )
}