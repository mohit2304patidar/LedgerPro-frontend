"use client";
import Sidebar from "./Sidebar";
import Navbar from "./Navbar";
import KeyboardShortcuts from "@/components/KeyboardShortcuts";
export default function AppLayout({ children }) {
    return (
        <div className="flex bg-slate-100">
            <KeyboardShortcuts />
            <Sidebar />

            <div className="flex-1">
                <Navbar />
                <div className="p-6">
                    {children}
                </div>
            </div>
        </div>
    );
}