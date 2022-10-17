/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./blog/{static,templates}/**/*.{html,js}"],
  theme: {
    fontFamily: {
      'sans': ['Roboto', 'arial'],
      'serif': ['"Roboto Serif"', '"Times New Roman"'],
      'mono': ['"Roboto Mono"', "monospace"],
      'display': ['Inter', 'Roboto', 'Arial']
    },
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
