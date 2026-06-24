"use client";

import { useState } from "react";
import AppLayout from "@/components/AppLayout";
import ProtectedRoute from "@/components/ProtectedRoute";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export default function StockLedgerPage() {

    const [productId, setProductId] = useState("");

    const [entries, setEntries] = useState([]);

    const loadLedger = async () => {

        const res = await fetch(
            `${API_URL}/stock/ledger/${productId}`
        );

        const data = await res.json();

        setEntries(data);
    };

    return (
        <ProtectedRoute>
            <AppLayout>

                <h1 className="text-3xl font-bold mb-6 text-black">
                    Stock Ledger
                </h1>

                <div className="bg-white p-6 rounded-xl shadow mb-6 text-black">

                    <div className="flex gap-4">

                        <input
                            placeholder="Product ID"
                            value={productId}
                            onChange={(e) =>
                                setProductId(
                                    e.target.value
                                )
                            }
                            className="border p-3 rounded"
                        />

                        <button
                            onClick={loadLedger}
                            className="bg-blue-600 text-white px-5 rounded"
                        >
                            Search
                        </button>

                    </div>

                </div>

                <div className="bg-white rounded-xl shadow p-6 text-black">

                    <table className="w-full">

                        <thead>

                            <tr>

                                <th>Date</th>
                                <th>Type</th>
                                <th>In</th>
                                <th>Out</th>
                                <th>Rate</th>

                            </tr>

                        </thead>

                        <tbody>

                            {entries.map(
                                (entry, index) => (

                                <tr key={index}>

                                    <td>{entry.date}</td>

                                    <td>
                                        {entry.movement_type}
                                    </td>

                                    <td>
                                        {entry.quantity_in}
                                    </td>

                                    <td>
                                        {entry.quantity_out}
                                    </td>

                                    <td>
                                        {entry.rate}
                                    </td>

                                </tr>

                            ))}

                        </tbody>

                    </table>

                </div>

            </AppLayout>
        </ProtectedRoute>
    );
}