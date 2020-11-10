/**
 * Configure your Gatsby site with this file.
 *
 * See: https://www.gatsbyjs.com/docs/gatsby-config/
 */

module.exports = {
    plugins: [
        `gatsby-plugin-react-helmet`,
        {
            resolve: "gatsby-source-wagtail",
            options: {
                url: "http://localhost:4243/graphql/"
            },
        },
    ],
    proxy: [
        {
            prefix: "/wagtail",
            url: "http://localhost:4243",
        },
        {
            prefix: "/static",
            url: "http://localhost:4243",
        },
        {
            prefix: "/media",
            url: "http://localhost:4243",
        },
    ],
}
