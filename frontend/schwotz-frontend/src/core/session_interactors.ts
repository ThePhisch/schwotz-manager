"use server";

export async function session_login(username: string, password: string): Promise<string> {
    const response = await fetch('http://docker-web-1:8005/s', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(
            { "username": username, "password": password }
        ),
    });
    
    if (!response.ok) {
        throw new Error('Login failed');
    }

    const data = await response.json();

    return data.token;
}

export async function session_logout(token: string): Promise<string> {
    // not implemented error
    throw new Error('Not implemented');
}

export async function session_get(token: string): Promise<Session> {
    const response = await fetch(`http://docker-web-1:8005/s/${token}`, {
        headers: {
            'Content-Type': 'application/json',
        },
        method: 'GET',
    });

    const data = await response.json();

    return {
        id: data.id,
        user_id: data.user_id,
        token: data.token,
        expires_at: new Date(data.expires_at),
        created_at: new Date(data.created_at),
        updated_at: new Date(data.updated_at),
    }
}