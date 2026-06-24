"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

export default function ProtectedRoute({
    children
}) {
    const router = useRouter();

    useEffect(() => {
        const token = localStorage.getItem("ledgerpro_token");

        if (!token) {
            router.push("/login");
        }
    }, [router]);

    return children;
}
