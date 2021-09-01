const { extract } = require('laravel-mix');
let mix = require('laravel-mix');

/*
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your Uvicore applications. By default, we are compiling the CSS
 | file for the application as well as bundling up all the JS files.
 |
 */

// https://laravel-mix.com/docs/6.0/vue
// https://dev.to/heynolnor/creating-a-project-template-using-laravel-vue-3-and-tailwind-part-1-2518


base = 'mreschke/wiki/http'

mix.options({
    publicPath: `${base}/public`,
    hmrOptions: {
        host: 'localhost',
        port: 5001
    }
})


mix.js(`${base}/assets/js/app.js`, `${base}/public/assets/wiki/js`)
    .postCss(`${base}/assets/css/app.css`, `${base}/public/assets/wiki/css`, [
        require("tailwindcss"),
    ])
    .extract(['@vue'])
    //.vue({ version: 3 })
    .vue()



//mix.js(`${base}/assets/js/app.js`, `${base}/public/assets/wiki/js`).vue();

// mix.postCss(`${base}/assets/css/app.css`, `${base}/public/assets/wiki/css`, [
//     require("tailwindcss"),
// ]);




    //.version();

// if (mix.inProduction()) {
//     mix.version();
// }
