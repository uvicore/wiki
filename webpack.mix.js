const mix = require('laravel-mix');

/*
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your Laravel applications. By default, we are compiling the CSS
 | file for the application as well as bundling up all the JS files.
 |
 */
base = 'jdbill/marketing/http'


mix.js(`${base}/assets/js/app.js`, `${base}/static/js`)
    .postCss(`${base}/assets/css/app.css`, `${base}/static/css`, [
        require("tailwindcss"),
    ])
    .extract(['vue']);


    //.version();

// if (mix.inProduction()) {
//     mix.version();
// }
