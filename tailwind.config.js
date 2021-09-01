base = './mreschke/wiki/http'
assets = `${base}/assets`
views = `${base}/views`

module.exports = {
  purge: [
    `${assets}/**/*.js`,
    `${assets}/**/*.vue`,
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
