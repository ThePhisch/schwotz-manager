import React from "react";
import { twMerge } from "tailwind-merge";

export const A: React.FC<JSX.IntrinsicElements["a"]> = (props) => {
    return (
        <a
            {...props}
            className={twMerge(
                "hover:underline text-blue-700 hover:text-blue-900",
                props.className
            )}
        >
            {props.children}
        </a>
    );
}