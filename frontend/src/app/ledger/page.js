"use client";

import { useState, useEffect, useCallback } from "react";
import AppLayout from "@/components/AppLayout";
import ProtectedRoute from "@/components/ProtectedRoute";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export default function LedgerPage() {

    const [ledgers, setLedgers] = useState([]);

    const [formData, setFormData] = useState({
        name: "",
        group_id: 1,
        ledger_type: "GENERAL",
        opening_balance: 0,
        balance_type: "Dr",
        gst_numbers: "",
        pan_numbers: "",
        mobiles: "",
        email: "",
        address: "",
    });

    useEffect(() => {
        const loadLedgers = async () => {
            try{
                const res = await fetch(`${API_URL}/ledgers/`);
                const data = await res.json();
                setLedgers(data);
            } catch (err) {
                console.log(err);
            }
        };
        loadLedgers();
    }, []);

    
    const createLedger = async () => {

        try {

            const res = await fetch(`${API_URL}/ledgers/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(formData)
            });

            if (res.ok) {

                setFormData({
                    name: "",
                    group_id: 1,
                    ledger_type: "GENERAL",
                    opening_balance: 0,
                    balance_type: "Dr",
                    gst_numbers: "",
                    pan_numbers: "",
                    mobiles: "",
                    email: "",
                    address: "",
                });

                fetchLedgers();
            }

        } catch (err) {
            console.log(err);
        }
    };

    return (
        <ProtectedRoute>
            <AppLayout>

                <h1 className="text-3xl font-bold text-black mb-6">
                    Ledger Management
                </h1>

                <div className="bg-white p-6 rounded-xl shadow mb-6">

                    <div className="grid grid-cols-2 gap-4">

                        <input
                            className="border p-3 rounded text-black"
                            placeholder="Ledger Name"
                            value={formData.name}
                            onChange={(e) =>
                                setFormData({
                                    ...formData,
                                    name: e.target.value
                                })
                            }
                        />

                        <input
                            className="border p-3 rounded text-black"
                            placeholder="Group ID"
                            type="number"
                            value={formData.group_id}
                            onChange={(e) =>
                                setFormData({
                                    ...formData,
                                    group_id: Number(e.target.value)
                                })
                            }
                        />

                        <input
                            className="border p-3 rounded text-black"
                            placeholder="Opening Balance"
                            type="number"
                            value={formData.opening_balance}
                            onChange={(e) =>
                                setFormData({
                                    ...formData,
                                    opening_balance: Number(e.target.value)
                                })
                            }
                        />

                        <select
                            className="border p-3 rounded text-black"
                            value={formData.balance_type}
                            onChange={(e) =>
                                setFormData({
                                    ...formData,
                                    balance_type: e.target.value
                                })
                            }
                        >
                            <option>Dr</option>
                            <option>Cr</option>
                        </select>

                        <input
                            className="border p-3 rounded text-black"
                            placeholder="Mobile"
                            value={formData.mobiles}
                            onChange={(e) =>
                                setFormData({
                                    ...formData,
                                    mobiles: e.target.value
                                })
                            }
                        />

                        <input
                            className="border p-3 rounded text-black"
                            placeholder="Email"
                            value={formData.email}
                            onChange={(e) =>
                                setFormData({
                                    ...formData,
                                    email: e.target.value
                                })
                            }
                        />

                    </div>

                    <button
                        onClick={createLedger}
                        className="mt-4 bg-blue-600 text-white px-5 py-3 rounded"
                    >
                        Create Ledger
                    </button>

                </div>

                <div className="bg-white rounded-xl shadow p-6 text-black">

                    <h2 className="text-xl font-bold text-black mb-4">
                        Ledger List
                    </h2>

                    <table className="w-full">

                        <thead>
                            <tr className="border-b">
                                <th className="text-left p-2">ID</th>
                                <th className="text-left p-2">Name</th>
                                <th className="text-left p-2">Type</th>
                                <th className="text-left p-2">Opening Balance</th>
                            </tr>
                        </thead>

                        <tbody>

                            {ledgers.map((ledger) => (

                                <tr
                                    key={ledger.id}
                                    className="border-b"
                                >
                                    <td className="p-2">{ledger.id}</td>
                                    <td className="p-2">{ledger.name}</td>
                                    <td className="p-2">{ledger.ledger_type}</td>
                                    <td className="p-2">
                                        {ledger.opening_balance}
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