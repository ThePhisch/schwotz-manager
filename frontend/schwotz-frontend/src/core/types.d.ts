type Task = {
    id?: number;
    name: string;
    assigned: string;
    timedelta: string; // note that there is no timedelta in typescript
    nextup: Date;
}

type Session = {
    id?: number;
    user_id: number
    token: string;
    expires_at: Date;
    created_at: Date;
    updated_at: Date;
}