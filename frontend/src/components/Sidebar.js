"use client";
import Link from "next/link";
import { logout } from "@/lib/auth";

export default function Sidebar() {
    return (
        <div className="w-64 bg-white shadow-md min-h-screen p-5">
            <h1 className="text-2xl font-bold text-black mb-8">
                LedgerPro
            </h1>

            <nav className="flex flex-col gap-4">
                <Link href="/dashboard" className="text-black">
                    Dashboard
                </Link>

                <Link href="/company" className="text-black">
                    Company
                </Link>

                <Link href="ledger" className="text-black">
                    Ledgers
                </Link>

                <Link href="/product" className="text-black">
                    Products
                </Link>

                <Link href="stock-summary" className="text-black">
                    Stock Summary
                </Link>

                <Link href="stock-ledger" className="text-black">
                    Stock Ledger
                </Link>

                <Link href="/purchase" className="text-black">
                    Purchase
                </Link>

                <Link href="/sales" className="text-black">
                    Sales
                </Link>

                <Link href="/reports" className="text-black">
                    Reports
                </Link>
            </nav>

            <button onClick={logout} className="mt-8 w-full bg-red-500 hover:bg-red-600 text-white py-2 rounded-lg">Logout</button>
        </div>
    )
}