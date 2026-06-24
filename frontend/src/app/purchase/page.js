"use client";

import { useState, useEffect } from "react";
import AppLayout from "@/components/AppLayout";
import ProtectedRoute from "@/components/ProtectedRoute";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export default function PurchasePage() {

    const [purchases, setPurchases] = useState([]);

    const [formData, setFormData] = useState({
        supplier_id: 1,
        purchase_date: new Date().toISOString().split("T")[0],
        gst_rate: 18,
        intra_state: true,
        total_amount: 0,
        items: [
            {
                product_id: "",
                quantity: "",
                rate: ""
            }
        ]
    });

    useEffect(() => {

        const loadPurchases = async () => {

            const res = await fetch(
                `${API_URL}/purchases/`
            );

            const data = await res.json();

            setPurchases(data);
        };

        loadPurchases();

    }, []);

    const handleItemChange = (
        index,
        field,
        value
    ) => {

        const updatedItems = [...formData.items];

        updatedItems[index][field] = value;

        setFormData({
            ...formData,
            items: updatedItems
        });
    };

    const addItem = () => {

        setFormData({
            ...formData,
            items: [
                ...formData.items,
                {
                    product_id: "",
                    quantity: "",
                    rate: ""
                }
            ]
        });
    };

    const calculateTotal = () => {

        let total = 0;

        formData.items.forEach(item => {

            total +=
                Number(item.quantity || 0)
                *
                Number(item.rate || 0);

        });

        return total;
    };

    const savePurchase = async () => {

        const payload = {
            ...formData,
            total_amount: calculateTotal()
        };

        const res = await fetch(
            `${API_URL}/purchases/`,
            {
                method: "POST",
                headers: {
                    "Content-Type":
                        "application/json"
                },
                body: JSON.stringify(payload)
            }
        );

        if (res.ok) {

            alert("Purchase Saved");

            window.location.reload();
        }
    };

    return (
        <ProtectedRoute>
            <AppLayout>

                <h1 className="text-3xl font-bold text-black mb-6">
                    Purchase Voucher
                </h1>

                <div className="bg-white p-6 rounded-xl shadow mb-6 text-black">

                    <div className="grid grid-cols-2 gap-4">

                        <input
                            type="number"
                            placeholder="Supplier ID"
                            value={formData.supplier_id}
                            onChange={(e) =>
                                setFormData({
                                    ...formData,
                                    supplier_id:
                                        Number(
                                            e.target.value
                                        )
                                })
                            }
                            className="border p-3 rounded"
                        />

                        <input
                            type="date"
                            value={formData.purchase_date}
                            onChange={(e) =>
                                setFormData({
                                    ...formData,
                                    purchase_date:
                                        e.target.value
                                })
                            }
                            className="border p-3 rounded"
                        />

                    </div>

                    <div className="mt-6">

                        {formData.items.map(
                            (item, index) => (

                            <div
                                key={index}
                                className="grid grid-cols-3 gap-4 mb-3"
                            >

                                <input
                                    placeholder="Product ID"
                                    className="border p-3 rounded"
                                    value={item.product_id}
                                    onChange={(e) =>
                                        handleItemChange(
                                            index,
                                            "product_id",
                                            Number(
                                                e.target.value
                                            )
                                        )
                                    }
                                />

                                <input
                                    placeholder="Quantity"
                                    className="border p-3 rounded"
                                    value={item.quantity}
                                    onChange={(e) =>
                                        handleItemChange(
                                            index,
                                            "quantity",
                                            Number(
                                                e.target.value
                                            )
                                        )
                                    }
                                />

                                <input
                                    placeholder="Rate"
                                    className="border p-3 rounded"
                                    value={item.rate}
                                    onChange={(e) =>
                                        handleItemChange(
                                            index,
                                            "rate",
                                            Number(
                                                e.target.value
                                            )
                                        )
                                    }
                                />

                            </div>

                        ))}

                        <button
                            onClick={addItem}
                            className="bg-slate-200 px-4 py-2 rounded"
                        >
                            Add Item
                        </button>

                    </div>

                    <div className="mt-6">

                        <h2 className="text-xl font-bold">

                            Total:
                            {" "}
                            {calculateTotal()}

                        </h2>

                    </div>

                    <button
                        onClick={savePurchase}
                        className="mt-4 bg-blue-600 text-white px-6 py-3 rounded"
                    >
                        Save Purchase
                    </button>

                </div>

                <div className="bg-white rounded-xl shadow p-6 text-black">

                    <h2 className="text-xl font-bold mb-4">
                        Purchase History
                    </h2>

                    <table className="w-full">

                        <thead>

                            <tr>

                                <th>ID</th>
                                <th>Voucher</th>
                                <th>Date</th>
                                <th>Total</th>

                            </tr>

                        </thead>

                        <tbody>

                            {purchases.map((p) => (

                                <tr key={p.id}>

                                    <td>{p.id}</td>
                                    <td>{p.voucher_no}</td>
                                    <td>{p.purchase_date}</td>
                                    <td>{p.total_amount}</td>

                                </tr>

                            ))}

                        </tbody>

                    </table>

                </div>

            </AppLayout>
        </ProtectedRoute>
    );
}