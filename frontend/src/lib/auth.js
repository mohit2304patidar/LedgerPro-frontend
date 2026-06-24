export const saveToken = (token) => {
    localStorage.setItem(
        "ledgerpro_token",
        token
    );
};

export const getToken = () => {
    return localStorage.getItem(
        "ledgerpro_token"
    );
};

export const logout = () => {
    localStorage.removeItem(
        "ledgerpro_token"
    );

    window.location.href = "/login";
};

export const isAuthenticated = () => {
    return !!localStorage.getItem(
        "ledgerpro_token"
    );
};