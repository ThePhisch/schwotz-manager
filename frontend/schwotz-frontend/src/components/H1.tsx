import { twMerge } from "tailwind-merge"

export const H1: React.FC<JSX.IntrinsicElements["h1"]> = (props) => {
	return (
		<h1
			{...props}
			className={twMerge(
				"text-3xl font-bold",
				props.className
			)}
		>
			{props.children}
		</h1>
	)
}