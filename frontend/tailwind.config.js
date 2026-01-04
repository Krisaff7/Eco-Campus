/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{vue,js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                'eco-green': '#27AE60',
                'eco-blue': '#2980B9',
                'eco-dark': '#2C3E50',
                'eco-light': '#F9F9F9',
            },
        },
    },
    plugins: [],
}