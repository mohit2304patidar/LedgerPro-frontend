"use client";

import { useState } from "react";
import { saveToken } from "@/lib/auth";

const API_URL = "https://ledgerpro-azro.onrender.com";
export default function LoginPage() {

    const [email, setEmail] =
        useState("");

    const [password, setPassword] =
        useState("");

    const login = async() => {
        console.log("LOGIN CLICKED")
        try {
            const res = await fetch(`${API_URL}/auth/login`,
                {
                    method: "POST",
                    headers: {
                        "Content-Type":
                        "application/json"
                    },
                    body: JSON.stringify({
                        email,
                        password
                    })
                }
            );

            const data = await res.json();
            console.log("Login Response: ", data);

            if (res.ok && data.access_token) {
                saveToken(data.access_token);
                console.log("Saved Token: ", localStorage.getItem(
                    "ledgerpro_token"
                ));
                window.location.href = "/dashboard";
            }
            else {
                alert(data.detail || "Invalid Credentials");
            }
        } catch (error) {
            console.error(error);
            alert("Server Connection Error");
        }
    };

    return (

        <div className="min-h-screen flex items-center justify-center bg-slate-100">

            <div className="bg-white p-8 rounded-xl shadow w-[400px] text-black">

                <h1 className="text-3xl font-bold mb-6">
                    LedgerPro Login
                </h1>

                <input
                    type="email"
                    placeholder="Email"
                    className="border p-3 w-full mb-4 rounded"
                    value={email}
                    onChange={(e) =>
                        setEmail(
                            e.target.value
                        )
                    }
                />

                <input
                    type="password"
                    placeholder="Password"
                    className="border p-3 w-full mb-4 rounded"
                    value={password}
                    onChange={(e) =>
                        setPassword(
                            e.target.value
                        )
                    }
                />

                <button type="button" onClick={login} className="bg-blue-600 text-white w-full p-3 rounded">
                    Login
                </button>

            </div>

        </div>
    );
}