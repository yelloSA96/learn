// These need to be installed through npm and possibly through dev only
const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const UglifyJsPlugin = require("uglifyjs-webpack-plugin");

module.exports = {
    // Here are the entry points (aka different files)
    entry: './src/index.js',
    output: {
        // Approach to how we output the files E.g. multiple Entrypoints or vendor approach for the compressed files 
        filename: "main.js",
        path: path.resolve(__dirname,"dist")
    },  
    optimization: {
        // Different types of minifying plugin approaches
        minimizer: [new UglifyJsPlugin()]
    },
    // Different plugins that can be extended from this webpack minimum
    plugins: [
        // HTML Webpack Plugin allows your to create your HTML and Javascript files where it connects them for you
        new HtmlWebpackPlugin(),
    ],
    // Can be used to automatically re-compile the files 
    devServer: {
        contentBase: path.join(__dirname, "dist"),
        port: 9000
    },
    module: {
        rules: [
            {
                // This is how we load different type of prepared babel environements
                test: /\.js$/,
                exclude: /(node_modules)/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env', '@babel/preset-react']
                    }
                }
            },
            {
                // This is processing the styles and minifying it 
                test: /\.css$/,
                use: [
                    {loader: 'style-loader'},
                    {loader: 'css-loader'}
                ]
            },
            {
                // This is how they process images for production through the url-loader(minimises speed )
                test: /\.(png|jpg)$/,
                use: [
                    {loader: 'url-loader'}
                ]
            }

        ]
    }
}