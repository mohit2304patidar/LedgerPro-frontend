"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

const API_URL = process.env.NEXT_PUBLIC_API_URL;

export default function RegisterPage() {

    const router = useRouter();

    const[loading, setLoading] = useState(false);
    const[showPassword, setShowPassword] = useState(false);
    const[showConfirmPassword, setShowConfirmPassword] = useState(false);
    const[formData, setFormData] = useState({
        full_name: "",
        email: "",
        password: "",
        confirmPassword: "",
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value,
        });
    };

    const handleRegister = async (e) => {
        e.preventDefault();

        if(
            !formData.full_name ||
            !formData.email ||
            !formData.password ||
            !formData.confirmPassword
        ) {
            alert("Please fill all fields");

            return;
        }

        if (formData.password !== formData.confirmPassword) {
            alert("Passwords do not match");
            return;
        }

        setLoading(true);

        try {
            const res = await fetch(`${API_URL}/auth/register`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    full_name: formData.full_name,
                    email: formData.email,
                    password: formData.password,
                }),
            });

            const data = await res.json();
            if (!res.ok) {
                alert(data.detail || "Registration Failed");
                setLoading(false);
                return;
            }

            alert("Registration Successful");
            router.push("/login");
        } catch (err) {
            console.log(err);
            alert("Server Connection Error");
        } finally {
            setLoading(false);
        }
    };

    return (

        <div className="min-h-screen flex items-center justify-center bg-linear-to-br from-blue-100 via-white to-indigo-100 p-6">
            
            <div className="w-full max-w-md bg-white rounded-2xl shadow-2xl p-8">

                <div className="text-center mb-8">

                    <h1 className="text-4xl font-bold text-bold text-blue-700">
                        LedgerPro
                    </h1>

                    <p className="text-gray-500 mt-2">
                        Create Your Account
                    </p>
                </div>

                <form
                    onSubmit={handleRegister}
                    className="space-y-5"
                >
                    <div>

                        <label className="block mb-2 font-medium text-gray-700">
                            Full Name
                        </label>

                        <input
                            type="text"
                            name="full_name"
                            value={formData.full_name}
                            onChange={handleChange}
                            placeholder="Enter Full Name"
                            className="w-full border rounded-lg p-3 outline-none focus:ring-blue-500 text-black"
                        />
                    </div>

                    <div>

                        <label className="block mb-2 font-medium text-gray-700">
                            Email Address
                        </label>

                        <input
                            type="email"
                            name="email"
                            value={formData.email}
                            onChange={handleChange}
                            placeholder="Enter Email"
                            className="w-full border rounded-lg p-3 outline-none focus:ring-blue-500 text-black"
                        />        
                    </div>

                    <div>

                        <label className="block mb-2 font-medium text-gray-700">
                            Password
                        </label>

                        <div className="relative">

                            <input
                                type={
                                    showPassword ? "text" : "password"
                                }
                                name = "password"
                                value={formData.password}
                                onChange={handleChange}
                                placeholder="Enter Password"
                                className="w-full border rounded-lg p-3 pr-12 outline-none focus:ring-blue-500 text-black"
                            />

                            <button
                                type="button"
                                onClick={() => setShowPassword(!showPassword)}
                                className="absolte right-3 top-3 text-sm text-blue-600"
                            >
                                {showPassword ? "Hide" : "Show"}
                            </button>
                        </div>
                    </div>

                    <div>

                        <label className="block mb-2 font-medium text-gray-700">
                            confirm Password
                        </label>

                        <div className="relative">

                            <input
                                type={showConfirmPassword ? "text" : "password"}
                                name="confirmPassword"
                                value={formData.confirmPassword}
                                onChange={handleChange}
                                placeholder="Confirm Password"
                                className="w-full border rounded-lg p-3 pr-12 outline-none focus:ring-2 focus:ring-blue-500 text-black"
                            />

                            <button
                                type="button"
                                onClick={() => 
                                    setShowConfirmPassword(
                                        !showConfirmPassword
                                    )
                                }

                                className="absolute right-3 top-3 text-sm text-blue-600"
                            >
                                {showConfirmPassword ? "Hide" : "Show"}
                            </button>
                        </div>
                    </div>

                    <button
                        type="submit"
                        disabled={loading}
                        className="w-full bg-blue-600 hover:bg-blue-700 text-white py-3 rounded-lg font-semibold transition"
                    >
                        { loading ? "Creating Account..." : "Create Account"}
                    </button>

                    <div className="text-center">
                        <p className="text-gray-600">
                            Already Have an Account?

                            <button
                                type="button"
                                onClick={() => router.push("/login")}
                                className="ml-2 text-blue-600 font-semibold hover:underline"
                            >
                                Login
                            </button>
                        </p>
                    </div>
                </form>
            </div>
        </div>
    );
}