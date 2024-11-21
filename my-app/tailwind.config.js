/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      "./src/**/*.{js,jsx,ts,tsx}"
  ],
  theme: {
    extend: {
      backgroundImage: {
        'github-mark': "url('./src/assets/github-mark.svg')",
      }
    },
  },
  plugins: [],
}

