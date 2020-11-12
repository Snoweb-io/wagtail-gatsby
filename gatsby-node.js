const { createWagtailPages } = require("./plugins/gatsby-source-wagtail/pages");


exports.createPages = ({ graphql, actions }) => {
  return createWagtailPages(
    {
      "cms.TestPage": "templates/test.js",
    },
    graphql,
    actions,
    []
  );
};
