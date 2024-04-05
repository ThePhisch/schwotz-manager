type Task = {
    id?: number;
    name: string;
    assigned: string;
    timedelta: string; // note that there is no timedelta in typescript
    nextup: Date;
}