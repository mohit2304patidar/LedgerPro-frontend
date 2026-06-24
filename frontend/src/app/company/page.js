"use client";

import { useState, useEffect } from "react";
import ProtectedRoute from "@/components/ProtectedRoute";
import AppLayout from "@/components/AppLayout";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export default function CompanyPage() {

    const [companies, setCompanies] = useState([]);

    const [formData, setFormData] = useState({
        company_name: "",
        owner_name: "",
        email: "",
        phone: "",
        address: "",
        state: "",
        country: "India",
        financial_year: "2026-2027"
    });
    useEffect(() => {
        const loadCompanies = async () => {
            try {
                const res = await fetch(`${API_URL}/companies/`);
                const data = await res.json();
                setCompanies(data);
            } catch (error) {
                console.log(error);
            }
        };
        loadCompanies();
    }, []);
    
    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const createCompany = async (e) => {
        e.preventDefault();

        try {
            const res = await fetch(`${API_URL}/companies/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(formData)
            });

            if (res.ok) {
                alert("Company Created");

                setFormData({
                    company_name: "",
                    owner_name: "",
                    email: "",
                    phone: "",
                    address: "",
                    state: "",
                    country: "India",
                    financial_year: "2026-2027"
                });

                fetchCompanies();
            }
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <ProtectedRoute>
            <AppLayout>
                <div className="p-8 bg-slate-100 min-h-screen">

                    <h1 className="text-3xl font-bold text-black mb-6">
                        Company Management
                    </h1>

                    <form
                        onSubmit={createCompany}
                        className="bg-white p-6 rounded-xl shadow mb-8"
                    >

                        <div className="grid grid-cols-2 gap-4">

                            <input
                                name="company_name"
                                placeholder="Company Name"
                                value={formData.company_name}
                                onChange={handleChange}
                                className="border p-3 rounded text-black"
                            />

                            <input
                                name="owner_name"
                                placeholder="Owner Name"
                                value={formData.owner_name}
                                onChange={handleChange}
                                className="border p-3 rounded text-black"
                            />

                            <input
                                name="email"
                                placeholder="Email"
                                value={formData.email}
                                onChange={handleChange}
                                className="border p-3 rounded text-black"
                            />

                            <input
                                name="phone"
                                placeholder="Phone"
                                value={formData.phone}
                                onChange={handleChange}
                                className="border p-3 rounded text-black"
                            />

                            <input
                                name="state"
                                placeholder="State"
                                value={formData.state}
                                onChange={handleChange}
                                className="border p-3 rounded text-black"
                            />

                            <input
                                name="financial_year"
                                placeholder="Financial Year"
                                value={formData.financial_year}
                                onChange={handleChange}
                                className="border p-3 rounded text-black"
                            />

                        </div>

                        <textarea
                            name="address"
                            placeholder="Address"
                            value={formData.address}
                            onChange={handleChange}
                            className="border p-3 rounded text-black w-full mt-4"
                            rows="3"
                        />

                        <button
                            type="submit"
                            className="mt-4 bg-blue-600 text-white px-6 py-3 rounded"
                        >
                            Create Company
                        </button>

                    </form>

                    <div className="bg-white rounded-xl shadow p-6">

                        <h2 className="text-2xl font-bold text-black mb-4">
                            Companies
                        </h2>

                        <table className="w-full">

                            <thead>
                                <tr className="border-b">
                                    <th className="text-left p-2 text-black">
                                        Company
                                    </th>
                                    <th className="text-left p-2 text-black">
                                        Owner
                                    </th>
                                    <th className="text-left p-2 text-black">
                                        Email
                                    </th>
                                    <th className="text-left p-2 text-black">
                                        Phone
                                    </th>
                                </tr>
                            </thead>

                            <tbody>

                                {companies.map((company) => (
                                    <tr
                                        key={company.id}
                                        className="border-b"
                                    >
                                        <td className="p-2 text-black">
                                            {company.company_name}
                                        </td>

                                        <td className="p-2 text-black">
                                            {company.owner_name}
                                        </td>

                                        <td className="p-2 text-black">
                                            {company.email}
                                        </td>

                                        <td className="p-2 text-black">
                                            {company.phone}
                                        </td>
                                    </tr>
                                ))}

                            </tbody>

                        </table>

                    </div>

                </div>
            </AppLayout>
        </ProtectedRoute>
    );
}