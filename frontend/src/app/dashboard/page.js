"use client";

import { useEffect, useState } from "react";
import AppLayout from "@/components/AppLayout";
import ProtectedRoute from "@/components/ProtectedRoute";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export default function DashboardPage() {

    const [stats, setStats] = useState({
        companies: 0,
        ledgers: 0,
        products: 0,
        sales: 0,
    });

    useEffect(() => {

    const fetchData = async () => {

        try {

            const [
                companiesRes,
                ledgersRes,
                productsRes,
                salesRes
            ] = await Promise.all([
                fetch(`${API_URL}/companies/`),
                fetch(`${API_URL}/ledgers/`),
                fetch(`${API_URL}/products/`),
                fetch(`${API_URL}/sales/`)
            ]);

            const companies = await companiesRes.json();
            const ledgers = await ledgersRes.json();
            const products = await productsRes.json();
            const sales = await salesRes.json();

            setStats({
                companies: Array.isArray(companies)
                    ? companies.length
                    : 0,

                ledgers: Array.isArray(ledgers)
                    ? ledgers.length
                    : 0,

                products: Array.isArray(products)
                    ? products.length
                    : 0,

                sales: Array.isArray(sales)
                    ? sales.length
                    : 0,
            });

        } catch (error) {

            console.error(
                "Dashboard Error:",
                error
            );

        }

    };

    fetchData();

}, []);

    return (

        <ProtectedRoute>

            <AppLayout>

                <h1 className="text-3xl font-bold text-black mb-6">
                    Dashboard
                </h1>

                <div className="grid grid-cols-4 gap-5">

                    <div className="bg-white p-6 rounded-xl shadow">
                        <h3 className="text-black">
                            Companies
                        </h3>

                        <p className="text-2xl font-bold text-black">
                            {stats.companies}
                        </p>
                    </div>

                    <div className="bg-white p-6 rounded-xl shadow">
                        <h3 className="text-black">
                            Ledgers
                        </h3>

                        <p className="text-2xl font-bold text-black">
                            {stats.ledgers}
                        </p>
                    </div>

                    <div className="bg-white p-6 rounded-xl shadow">
                        <h3 className="text-black">
                            Products
                        </h3>

                        <p className="text-2xl font-bold text-black">
                            {stats.products}
                        </p>
                    </div>

                    <div className="bg-white p-6 rounded-xl shadow">
                        <h3 className="text-black">
                            Sales
                        </h3>

                        <p className="text-2xl font-bold text-black">
                            {stats.sales}
                        </p>
                    </div>

                </div>

            </AppLayout>

        </ProtectedRoute>
    );
}