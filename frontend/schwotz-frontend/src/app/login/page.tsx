"use client"

import { H1 } from "@/components/H1";
import { useState } from "react";
import { twMerge } from "tailwind-merge";
import { session_get, session_login } from "@/core/session_interactors";
import { Session } from "inspector";

export default function Login() {

  const [message, setMessage] = useState<string>("")
  const [token, setToken] = useState<string | null>(null)

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    const form = e.currentTarget as HTMLFormElement
    session_login(
      form.username.value, form.password.value
    ).then(
      token => {
        setToken(token)  // TODO: remove this later!
        // TODO: store token in session storage
        // TODO: redirect to home page
      }
    ).catch(
      error => {
        console.error(error)
        setMessage("Login failed")
      }
    )
  }

  return (
      <main
        className={twMerge(
          "p-4",
        )}
      >
        <H1>Login</H1>
        <form
          className="flex flex-col w-72"
          onSubmit={handleSubmit}  
        >
          <label>
            Username
            <input type="text" name="username"/>
          </label>
          <label>
            Password
            <input type="text" name="password"/>
          </label>
          <button type="submit" className="bg-blue-500">Login</button>
        </form>
        <p>{token}</p>
        <button
          type="button"
          className="bg-green-500" 
          onClick={(e) => {
            session_get(token ? token : "").then(
              data => setMessage(JSON.stringify(data))
            ).catch(
              error => {
                console.error(error)
                setMessage("Session data retrieval failed")
              }
            )
          }}
        >
          Show session data
        </button>
        <p>{message}</p>
      </main>
  );
}
