"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { saveToken } from "@/lib/auth";
import { Fascinate } from "next/font/google";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export default function LoginPage() {

    const router = useRouter();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);

    const login = async () => {
        if (!email || !password) {
            alert("Please enter email and password.");
            return;
        }

        setLoading(true);

        try {
            const res = await fetch(`${API_URL}/auth/login`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    email,
                    password,
                }),
            });

            const data = await res.json();
            if (res.ok && data.access_token) {
                saveToken(data.access_token);

                window.location.href = "/dashboard";
            } else {
                alert(data.detail || "invalid Credentials");
            }
        } catch (error) {
            console.error(error);
            alert("Server Connection Error");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen flex items-center jusitfy-center bg-slate-100">

            <div className="bg-white p-8 rounded-xl shadow-xl w-105 text-black">

                <div className="text-center mb-8">

                    <h1 className="text-4xl font-bold text-blue-700">
                        LedgerPro
                    </h1>

                    <p className="text-gray-500 mt-2">
                        Login to Continue
                    </p>

                </div>

                <input
                    type="email"
                    placeholder="Email Address"
                    className="border p-3 w-full mb-4 rounded-lg focus:outline-none focus: ring-blue-500"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />

                <input
                    type="password"
                    placeholder="Password"
                    className="border p-3 w-full mb-5 rounded-lg focus:outline-none focus:ring-blue-500"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />

                <button
                    type="button"
                    onClick={login}
                    disabled={loading}
                    className="bg-blue-600 hover: bg-blue-700 transition text-white w-full p-3 rounded-lg font-semibold"
                >
                    {loading ? "Logging In..." : "Login"}
                </button>

                <div className="mt-6 text-center">
                    <p className="text-gray-600">
                        Dont have an account?

                        <button
                            type="button"
                            onClick={() => router.push("/register")}
                            className="ml-2 text-blue-600 font-semibold hover:underline"
                        >
                            Create Account
                        </button>
                    </p>
                </div>

            </div>
        </div>
    );
}