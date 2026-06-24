"use client";

import { useEffect, useState } from "react";
import AppLayout from "@/components/AppLayout";
import ProtectedRoute from "@/components/ProtectedRoute";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export default function ProductPage() {

    const [products, setProducts] = useState([]);

    const [formData, setFormData] = useState({
        name: "",
        sku: "",
        category_id: 1,
        unit_id: 1,
        hsn_code: "",
        gst_rate: 0,
        purchase_rate: 0,
        sale_rate: 0,
        opening_stock: 0
    });

    useEffect(() => {

        const loadProducts = async () => {

            try {

                const res = await fetch(
                    `${API_URL}/products/`
                );

                const data = await res.json();

                setProducts(data);

            } catch (error) {
                console.log(error);
            }

        };

        loadProducts();

    }, []);

    const handleChange = (e) => {

        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });

    };

    const createProduct = async () => {

        try {

            const res = await fetch(
                `${API_URL}/products/`,
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(formData)
                }
            );

            if (res.ok) {

                alert("Product Created");

                window.location.reload();
            }

        } catch (error) {
            console.log(error);
        }
    };

    return (
        <ProtectedRoute>
            <AppLayout>

                <h1 className="text-3xl font-bold text-black mb-6">
                    Product Master
                </h1>

                <div className="bg-white p-6 rounded-xl shadow mb-8">

                    <div className="grid grid-cols-2 gap-4">

                        <input
                            name="name"
                            placeholder="Product Name"
                            onChange={handleChange}
                            className="border p-3 rounded text-black"
                        />

                        <input
                            name="sku"
                            placeholder="SKU"
                            onChange={handleChange}
                            className="border p-3 rounded text-black"
                        />

                        <input
                            name="hsn_code"
                            placeholder="HSN Code"
                            onChange={handleChange}
                            className="border p-3 rounded text-black"
                        />

                        <input
                            name="gst_rate"
                            placeholder="GST Rate"
                            onChange={handleChange}
                            className="border p-3 rounded text-black"
                        />

                        <input
                            name="purchase_rate"
                            placeholder="Purchase Rate"
                            onChange={handleChange}
                            className="border p-3 rounded text-black"
                        />

                        <input
                            name="sale_rate"
                            placeholder="Sale Rate"
                            onChange={handleChange}
                            className="border p-3 rounded text-black"
                        />

                        <input
                            name="opening_stock"
                            placeholder="Opening Stock"
                            onChange={handleChange}
                            className="border p-3 rounded text-black"
                        />

                    </div>

                    <button
                        onClick={createProduct}
                        className="mt-5 bg-blue-600 text-white px-6 py-3 rounded"
                    >
                        Create Product
                    </button>

                </div>

                <div className="bg-white rounded-xl shadow p-6 text-black">

                    <table className="w-full">

                        <thead>

                            <tr className="border-b">

                                <th className="text-left p-3">ID</th>
                                <th className="text-left p-3">Name</th>
                                <th className="text-left p-3">SKU</th>
                                <th className="text-left p-3">Purchase</th>
                                <th className="text-left p-3">Sale</th>
                                <th className="text-left p-3">Stock</th>

                            </tr>

                        </thead>

                        <tbody>

                            {products.map((item) => (

                                <tr
                                    key={item.id}
                                    className="border-b"
                                >

                                    <td className="p-3">{item.id}</td>
                                    <td className="p-3">{item.name}</td>
                                    <td className="p-3">{item.sku}</td>
                                    <td className="p-3">{item.purchase_rate}</td>
                                    <td className="p-3">{item.sale_rate}</td>
                                    <td className="p-3">{item.opening_stock}</td>

                                </tr>

                            ))}

                        </tbody>

                    </table>

                </div>

            </AppLayout>
        </ProtectedRoute>
    );
}