"use client";

import { useEffect, useState } from "react";
import AppLayout from "@/components/AppLayout";
import ProtectedRoute from "@/components/ProtectedRoute";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export default function StockSummaryPage() {

    const [stocks, setStocks] = useState([]);

    useEffect(() => {

        const loadStock = async () => {

            const res = await fetch(
                `${API_URL}/stock/summary`
            );

            const data = await res.json();

            console.log(data);

            setStocks(data);
        };

        loadStock();

    }, []);

    return (
        <ProtectedRoute>
            <AppLayout>

                <h1 className="text-3xl font-bold mb-6 text-black">
                    Stock Summary
                </h1>

                <div className="bg-white rounded-xl shadow p-6 text-black">

                    <table className="w-full">

                        <thead>

                            <tr className="border-b">

                                <th className="p-3">Product</th>
                                <th className="p-3">Opening</th>
                                <th className="p-3">Purchase</th>
                                <th className="p-3">Sales</th>
                                <th className="p-3">Current</th>

                            </tr>

                        </thead>

                        <tbody>

                            {stocks.map((item) => (

                                <tr
                                    key={item.product_id}
                                    className="border-b"
                                >

                                    <td className="p-3">
                                        {item.product_name}
                                    </td>

                                    <td className="p-3">
                                        {item.opening_stock}
                                    </td>

                                    <td className="p-3">
                                        {item.purchase_qty}
                                    </td>

                                    <td className="p-3">
                                        {item.sale_qty}
                                    </td>

                                    <td className="p-3 font-bold">
                                        {item.current_stock}
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