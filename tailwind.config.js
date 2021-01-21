base = './jdbill/marketing/http'
assets = `${base}/assets`
views = `${base}/views`

module.exports = {
  purge: [
    `${assets}/**/*.js`,
    `${views}/**/*.j2`,
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
