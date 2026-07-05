"use client";

import { useState, useEffect, useCallback } from "react";
import AppLayout from "@/components/AppLayout";
import ProtectedRoute from "@/components/ProtectedRoute";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export default function LedgerPage() {
    const [ledgers, setLedgers] = useState([]);
    const [loading, setLoading] = useState(false);

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

    useEffect (() => {
        const loadLedgers = async () => {
            try {
                const res = await fetch(`${API_URL}/ledgers/`);

                if (!res.ok) {
                    throw new Error("Failed to load ledgers");
                }

                const data = await res.json();
                setLedgers(data);
            } catch (err) {
                console.log(err);
            }
        };

        loadLedgers();
    }, []);

    const createLedger = async () => {
        if (!formData.name.trim()) {
            alert("Ledger Name is required");
            return;
        }

        setLoading(true);

        try {
            const res = await fetch(`${API_URL}/ledgers/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(formData),
            });

            const data = await res.json();
            if (!res.ok) {
                alert(data.detail || "Ledger creation failed");
                return;
            }

            alert("Ledger Created Successfully");

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

            // Reload Ledger List

            const LedgerRes = await fetch(`${API_URL}/ledgers/`);
            const ledgerData = await LedgerRes.json();

            setLedgers(ledgerData);
        } catch (err) {
            console.log(err);
            alert("Server Connection Error");
        } finally {
            setLoading(false);
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
                            onChange={(e) => setFormData({
                                ...formData,
                                name: e.target.value,
                                })
                            }
                        />

                        <input
                            className="border p-3 rounded text-black"
                            placeholder="Group ID"
                            type="number"
                            value={formData.group_id}
                            onChange={(e) => setFormData({
                                ...formData,
                                group_id: Number(e.target.value),
                                })
                            }
                        />

                        <select 
                            className="border p-3 rounded text-black"
                            value={formData.ledger_type}
                            onChange={(e) => 
                                setFormData({
                                    ...formData,
                                    ledger_type: e.target.value,
                                })
                            }
                        >
                            <option vlaue="GENERAL">GENERAL</option>
                            <option vlaue="CUSTOMER">CUSTOMER</option>
                            <option vlaue="SUPPLIER">SUPPLIER</option>
                            <option vlaue="BANK">BANK</option>
                            <option vlaue="CASH">CASH</option>
                        </select>

                        <input
                            className="border p-3 rounded text-black"
                            placeholder="Opening Balance"
                            type="number"
                            value={formData.opening_balance}
                            onChange={(e) => 
                                setFormData({
                                    ...formData,
                                    opening_balance: Number(e.target.value),
                                    })
                                }
                        />

                        <select
                            className="border p-3 rounded text-black"
                            value={formData.balance_type}
                            onChange={(e) => setFormData({
                                ...formData,
                                balance_type: e.target.value,
                                })
                            }
                        >
                            <option value="Dr">Dr</option>
                            <option value="Cr">Cr</option>
                        </select>

                        <input
                            className="border p-3 rounded text-black"
                            placeholder="GST Number"
                            value={formData.gst_numbers}
                            onChange={(e) => setFormData({
                                ...formData,
                                gst_numbers: e.target.value,
                                })
                            }
                        />

                        <input
                            className="border p-3 rounded text-black"
                            placeholder="PAN Number"
                            value={formData.pan_numbers}
                            onChange={(e) => setFormData({
                                ...formData,
                                pan_numbers: e.target.vlaue,
                                })
                            }
                        />

                        <input
                            className="border p-3 rounded text-black"
                            placeholder="Mobile"
                            value={formData.mobiles}
                            onChange={(e) => setFormData({
                                ...formData,
                                mobiles: e.target.value,
                                })
                            }
                        />

                        <input 
                            className="border p-3 rounded text-black"
                            placeholder="Email"
                            value={formData.email}
                            onChange={(e) => setFormData({
                                ...formData,
                                email: e.target.value,
                                })
                            }
                        />

                        <textarea
                            className="border p-3 rounded text-black col-span-2"
                            placeholder="Address"
                            value={(e) => setFormData({
                                ...formData,
                                address: e.target.value,
                                })
                            }
                        />

                        <div className="col-span-2">

                            <button
                                onClick={createLedger}
                                disabled={loading}
                                className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg"
                            >
                                {loading ? "Creating..." : "Create Ledger"}
                            </button>

                        </div>
                    </div>
                </div>

                <div className="bg-white rounded-xl shadow p-6">

                    <h2 className="text-xl font-bold text-black mb-4">
                        Ledger List
                    </h2>

                    <table className="w-full border-collapse">
                        <thead>
                            <tr className="bg-gray-100 border">

                                <th className="p-3 border">ID</th>
                                <th className="p-3 border">Name</th>
                                <th className="p-3 border">Group</th>
                                <th className="p-3 border">Type</th>
                                <th className="p-3 border">Opening</th>
                                <th className="p-3 border">Balance</th>
                                <th className="p-3 border">Mobile</th>
                                <th className="p-3 border"> Email</th>
                            
                            </tr>

                        </thead>

                        <tbody>

                            {ledgers.length === 0 ? (

                                <tr>

                                    <td
                                        colSpan="8"
                                        className="text-center p-5 text-gray-500"
                                    >
                                        No Ledger Found
                                    </td>
                                </tr>
                            ) : (
                                ledgers.map((ledger) => (
                                    <tr 
                                        key={ledger.id}
                                        className="border hover:bg-gray-50"
                                    >

                                        <td className="p-3 border">
                                            {ledger.id}
                                        </td>

                                        <td className="p-3 border">
                                            {ledger.name}
                                        </td>

                                        <td className="p-3 border">
                                            {ledger.group_id}
                                        </td>

                                        <td className="p-3 border">
                                            {ledger.ledger_type}
                                        </td>

                                        <td className="p-3 border">
                                            {ledger.opening_balance}
                                        </td>

                                        <td className="p-3 border">
                                            {ledger.balance_type}
                                        </td>

                                        <td className="p-3 border">
                                            {ledger.mobiles}
                                        </td>

                                        <td className="p-3 border">
                                            {ledger.email}
                                        </td>
                                    </tr>
                                ))
                            )}
                        </tbody>
                    </table>
                </div>
            </AppLayout>
        </ProtectedRoute>
    );
}