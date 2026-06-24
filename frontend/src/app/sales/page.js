"use client";

import { useState, useEffect } from "react";
import AppLayout from "@/components/AppLayout";
import ProtectedRoute from "@/components/ProtectedRoute";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export default function SalesPage() {

    const [sales, setSales] = useState([]);

    const [formData, setFormData] = useState({
        customer_id: 1,
        sale_date: new Date().toISOString().split("T")[0],
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

        const loadSales = async () => {

            try {

                const res = await fetch(
                    `${API_URL}/sales/`
                );

                const data = await res.json();

                setSales(data);

            } catch (error) {
                console.log(error);
            }

        };

        loadSales();

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

    const saveSale = async () => {

        const payload = {
            ...formData,
            total_amount: calculateTotal()
        };

        try {

            const res = await fetch(
                `${API_URL}/sales/`,
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

                alert("Sale Saved");

                window.location.reload();
            }

        } catch (error) {
            console.log(error);
        }
    };

    const downloadInvoice = (saleId) => {
        window.open(`${API_URL}/Invoice/sales/${saleId}`,
            "_blank"
        );
    };

    return (
        <ProtectedRoute>
            <AppLayout>

                <h1 className="text-3xl font-bold text-black mb-6">
                    Sales Voucher
                </h1>

                <div className="bg-white p-6 rounded-xl shadow mb-6 text-black">

                    <div className="grid grid-cols-2 gap-4">

                        <input
                            type="number"
                            placeholder="Customer ID"
                            value={formData.customer_id}
                            onChange={(e) =>
                                setFormData({
                                    ...formData,
                                    customer_id:
                                        Number(
                                            e.target.value
                                        )
                                })
                            }
                            className="border p-3 rounded"
                        />

                        <input
                            type="date"
                            value={formData.sale_date}
                            onChange={(e) =>
                                setFormData({
                                    ...formData,
                                    sale_date:
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
                            Total: {calculateTotal()}
                        </h2>

                    </div>

                    <button
                        onClick={saveSale}
                        className="mt-4 bg-blue-600 text-white px-6 py-3 rounded"
                    >
                        Save Sale
                    </button>

                </div>

                <div className="bg-white rounded-xl shadow p-6 text-black">

                    <h2 className="text-xl font-bold mb-4">
                        Sales History
                    </h2>

                    <table className="w-full">

                        <thead>

                            <tr>
                                <th>ID</th>
                                <th>Voucher</th>
                                <th>Date</th>
                                <th>Total</th>
                                <th>Action</th>
                            </tr>

                        </thead>

                        <tbody>

                            {sales.map((sale) => (

                                <tr key={sale.id}>

                                    <td>{sale.id}</td>
                                    <td>{sale.voucher_no}</td>
                                    <td>{sale.sale_date}</td>
                                    <td>{sale.total_amount}</td>

                                    <td>
                                        <button
                                            onClick={() => downloadInvoice(sale.id)}
                                            className="bg-blue-600 text-white px-3 py-1 rounded"
                                        >
                                            Download PDF
                                        </button>
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