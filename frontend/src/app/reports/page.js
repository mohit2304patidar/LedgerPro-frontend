"use client";

import { useEffect, useState } from "react";
import AppLayout from "@/components/AppLayout";
import ProtectedRoute from "@/components/ProtectedRoute";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export default function ReportsPage() {

const [report, setReport] = useState({
    totalSales: 0,
    totalPurchases: 0,
    salesCount: 0,
    purchaseCount: 0,
});

const [sales, setSales] = useState([]);
const [purchases, setPurchases] = useState([]);

useEffect(() => {

    const fetchReports = async () => {

        try {

            const [
                salesRes,
                purchasesRes
            ] = await Promise.all([
                fetch(`${API_URL}/sales/`),
                fetch(`${API_URL}/purchases/`)
            ]);

            const salesData =
                await salesRes.json();

            const purchasesData =
                await purchasesRes.json();

            const salesList =
                Array.isArray(salesData)
                    ? salesData
                    : [];

            const purchaseList =
                Array.isArray(purchasesData)
                    ? purchasesData
                    : [];

            setSales(salesList);
            setPurchases(purchaseList);

            const totalSales =
                salesList.reduce(
                    (sum, item) =>
                        sum +
                        (item.total_amount || 0),
                    0
                );

            const totalPurchases =
                purchaseList.reduce(
                    (sum, item) =>
                        sum +
                        (item.total_amount || 0),
                    0
                );

            setReport({
                totalSales,
                totalPurchases,
                salesCount:
                    salesList.length,
                purchaseCount:
                    purchaseList.length,
            });

        } catch (error) {

            console.error(
                "Reports Error:",
                error
            );

        }

    };

    fetchReports();

}, []);

return (

    <ProtectedRoute>

        <AppLayout>

            <h1 className="text-3xl font-bold text-black mb-6">
                Reports Dashboard
            </h1>

            <div className="grid grid-cols-4 gap-5 mb-8">

                <div className="bg-white p-6 rounded-xl shadow">

                    <h3 className="text-gray-500">
                        Total Sales
                    </h3>

                    <p className="text-2xl font-bold text-green-600">
                        ₹{report.totalSales}
                    </p>

                </div>

                <div className="bg-white p-6 rounded-xl shadow">

                    <h3 className="text-gray-500">
                        Total Purchases
                    </h3>

                    <p className="text-2xl font-bold text-blue-600">
                        ₹{report.totalPurchases}
                    </p>

                </div>

                <div className="bg-white p-6 rounded-xl shadow">

                    <h3 className="text-gray-500">
                        Sales Entries
                    </h3>

                    <p className="text-2xl font-bold text-purple-600">
                        {report.salesCount}
                    </p>

                </div>

                <div className="bg-white p-6 rounded-xl shadow">

                    <h3 className="text-gray-500">
                        Purchase Entries
                    </h3>

                    <p className="text-2xl font-bold text-orange-600">
                        {report.purchaseCount}
                    </p>

                </div>

            </div>

            <div className="bg-white rounded-xl shadow p-5">

                <h2 className="text-xl font-semibold text-black mb-4">
                    Recent Sales
                </h2>

                <table className="w-full">

                    <thead>

                        <tr className="border-b">

                            <th className="p-2 text-left text-black">
                                Voucher
                            </th>

                            <th className="p-2 text-left text-black">
                                Date
                            </th>

                            <th className="p-2 text-left text-black">
                                Amount
                            </th>

                        </tr>

                    </thead>

                    <tbody>

                        {sales.map((sale) => (

                            <tr
                                key={sale.id}
                                className="border-b"
                            >

                                <td className="p-2 text-black">
                                    {sale.voucher_no}
                                </td>

                                <td className="p-2 text-black">
                                    {sale.sale_date}
                                </td>

                                <td className="p-2 text-black">
                                    ₹{sale.total_amount}
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