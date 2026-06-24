"use client";

import { useState, useEffect } from "react";

export default function Navbar() {

const [showShortcuts, setShowShortcuts] =
    useState(false);

useEffect(() => {

    const handleEsc = (e) => {

        if (e.key === "Escape") {
            setShowShortcuts(false);
        }

    };

    window.addEventListener(
        "keydown",
        handleEsc
    );

    return () => {

        window.removeEventListener(
            "keydown",
            handleEsc
        );

    };

}, []);

return (

    <>

        <div
            className="
                bg-white
                shadow-sm
                h-16
                flex
                items-center
                justify-between
                px-6
            "
        >

            <h2
                className="
                    text-xl
                    font-semibold
                    text-black
                "
            >
                Dashboard
            </h2>

            <div
                className="
                    flex
                    items-center
                    gap-4
                "
            >

                <button
                    onClick={() =>
                        setShowShortcuts(true)
                    }
                    className="
                        bg-blue-600
                        hover:bg-blue-700
                        text-white
                        px-4
                        py-2
                        rounded-lg
                        transition
                    "
                >
                    ⌨ Shortcuts
                </button>

                

            </div>

        </div>

        {showShortcuts && (

            <div
                onClick={() =>
                    setShowShortcuts(false)
                }
                className="
                    fixed
                    inset-0
                    bg-black/50
                    flex
                    items-center
                    justify-center
                    z-50
                "
            >

                <div
                    onClick={(e) =>
                        e.stopPropagation()
                    }
                    className="
                        bg-white
                        rounded-xl
                        shadow-2xl
                        p-6
                        w-full
                        max-w-2xl
                        max-h-[80vh]
                        overflow-y-auto
                    "
                >

                    <div
                        className="
                            flex
                            justify-between
                            items-center
                            mb-6
                        "
                    >

                        <div>

                            <h2
                                className="
                                    text-2xl
                                    font-bold
                                    text-blue-700
                                "
                            >
                                LedgerPro Keyboard Guide
                            </h2>

                            <p
                                className="
                                    text-sm
                                    text-gray-500
                                "
                            >
                                TallyPrime Inspired Navigation
                            </p>

                        </div>

                        <button
                            onClick={() =>
                                setShowShortcuts(false)
                            }
                            className="
                                text-red-500
                                text-2xl
                                font-bold
                            "
                        >
                            ✕
                        </button>

                    </div>

                    <table
                        className="
                            w-full
                            text-black
                        "
                    >

                        <thead>

                            <tr
                                className="
                                    border-b
                                    bg-gray-100
                                "
                            >

                                <th
                                    className="
                                        text-left
                                        p-3
                                    "
                                >
                                    Shortcut
                                </th>

                                <th
                                    className="
                                        text-left
                                        p-3
                                    "
                                >
                                    Action
                                </th>

                            </tr>

                        </thead>

                        <tbody>

                            <tr><td className="p-3 font-semibold">F2</td><td>Company</td></tr>
                            <tr><td className="p-3 font-semibold">F3</td><td>Ledger</td></tr>
                            <tr><td className="p-3 font-semibold">F4</td><td>Product</td></tr>
                            <tr><td className="p-3 font-semibold">F5</td><td>Purchase</td></tr>
                            <tr><td className="p-3 font-semibold">F6</td><td>Sales</td></tr>
                            <tr><td className="p-3 font-semibold">F7</td><td>Reports</td></tr>
                            <tr><td className="p-3 font-semibold">F8</td><td>Stock Summary</td></tr>
                            <tr><td className="p-3 font-semibold">F9</td><td>Stock Ledger</td></tr>
                            <tr><td className="p-3 font-semibold">F10</td><td>Dashboard</td></tr>
                            <tr><td className="p-3 font-semibold">F12</td><td>Logout</td></tr>

                            <tr className="border-t">
                                <td className="p-3 font-semibold">
                                    Ctrl + N
                                </td>
                                <td>
                                    New Company
                                </td>
                            </tr>

                            <tr>
                                <td className="p-3 font-semibold">
                                    Ctrl + L
                                </td>
                                <td>
                                    New Ledger
                                </td>
                            </tr>

                            <tr>
                                <td className="p-3 font-semibold">
                                    Ctrl + P
                                </td>
                                <td>
                                    New Product
                                </td>
                            </tr>

                            <tr>
                                <td className="p-3 font-semibold">
                                    Ctrl + F
                                </td>
                                <td>
                                    Search
                                </td>
                            </tr>

                            <tr>
                                <td className="p-3 font-semibold">
                                    Ctrl + S
                                </td>
                                <td>
                                    Save
                                </td>
                            </tr>

                            <tr className="border-t">
                                <td className="p-3 font-semibold">
                                    Esc
                                </td>
                                <td>
                                    Close Popup
                                </td>
                            </tr>

                        </tbody>

                    </table>

                </div>

            </div>

        )}

    </>

);

}