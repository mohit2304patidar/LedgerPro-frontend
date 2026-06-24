"use client";

import { logout } from "@/lib/auth";
import { useRouter } from "next/navigation";
import { useEffect } from "react";

export default function KeyboardShortcuts() {

    const router = useRouter();

    useEffect(() => {

        const handleKeyDown = (e) => {

    switch (true) {

        case e.key === "F2":
            e.preventDefault();
            router.push("/company");
            break;

        case e.key === "F3":
            e.preventDefault();
            router.push("/ledger");
            break;

        case e.key === "F4":
            e.preventDefault();
            router.push("/product");
            break;

        case e.key === "F5":
            e.preventDefault();
            router.push("/purchase");
            break;

        case e.key === "F6":
            e.preventDefault();
            router.push("/sales");
            break;

        case e.key === "F7":
            e.preventDefault();
            router.push("/reports");
            break;

        case e.key === "F8":
            e.preventDefault();
            router.push("/stock-summary");
            break;

        case e.key === "F9":
            e.preventDefault();
            router.push("/stock-ledger");
            break;

        case e.key === "F10":
            e.preventDefault();
            router.push("/dashboard");
            break;

        case e.key === "F12":
            e.preventDefault();

            if (
                confirm(
                    "Are you sure you want to logout?"
                )
            ) {
                logout();
            }

            break;

        case e.ctrlKey && e.key.toLowerCase() === "n":

            e.preventDefault();
            router.push("/company");
            break;

        case e.ctrlKey && e.key.toLowerCase() === "l":

            e.preventDefault();
            router.push("/ledger");
            break;

        case e.ctrlKey && e.key.toLowerCase() === "p":

            e.preventDefault();
            router.push("/product");
            break;

        case e.ctrlKey && e.key.toLowerCase() === "f":

            e.preventDefault();

            alert(
                "Search feature coming soon"
            );

            break;

        case e.ctrlKey && e.key.toLowerCase() === "s":

            e.preventDefault();

            alert(
                "Save shortcut activated"
            );

            break;

        case e.key === "Escape":

            e.preventDefault();
            router.push("/dashboard");
            break;

        default:
            break;
        }
    };

        window.addEventListener(
            "keydown",
            handleKeyDown
        );

        return () => {
            window.removeEventListener(
                "keydown",
                handleKeyDown
            );
        };

    }, [router]);

    return null;
}