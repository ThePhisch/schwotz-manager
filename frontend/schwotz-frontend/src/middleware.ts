import { NextRequest, NextResponse } from "next/server";

export default function middleware(request: NextRequest) {

    // if url is not for /login, redirect to /login
    if (request.nextUrl.pathname !== "/login") {
        return NextResponse.redirect(new URL("/login", request.url));
    }

    return NextResponse.next()
}

export const config = {
    // filter out requests to /api, /_next/static, /_next/image, and favicon.ico
    // this also means that the middleware will not ruin tailwind styles
    matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)']
};