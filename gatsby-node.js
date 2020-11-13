const { createWagtailPages } = require("./plugins/gatsby-source-wagtail/pages");


exports.createPages = async function ({ graphql, actions }) {
  return createWagtailPages(
    {
      "cms.TestPage": "templates/test.js",
    },
    graphql,
    actions,
    []
  );
};
