const { createWagtailPages } = require("gatsby-source-wagtail/pages.js");

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
